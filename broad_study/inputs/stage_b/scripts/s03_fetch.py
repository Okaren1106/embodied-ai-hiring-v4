"""Stage B / network fetch + evidence snapshot harness.

Every Stage B web retrieval goes through this module so that the search log,
the saved snapshot and its hash are produced together and cannot drift apart.

Usage:
    python s03_fetch.py --url URL --id SNAPID --company CN_XSQUARE --question "..." [--lang zh]
    python s03_fetch.py --batch work/fetch_batch.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import RUN, SNAP, WORK, append_jsonl, write_json  # noqa: E402

CURL = r"C:\Windows\system32\curl.exe"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36")
SEARCH_LOG = os.path.join(RUN, "search_log.jsonl")
SNAP_INDEX = os.path.join(WORK, "snapshot_index.json")


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def load_index() -> dict:
    if os.path.exists(SNAP_INDEX):
        with open(SNAP_INDEX, "r", encoding="utf-8") as fh:
            return json.load(fh)
    return {"snapshots": {}}


def save_index(idx: dict) -> None:
    write_json(SNAP_INDEX, idx)


def fetch(url: str, timeout: int = 40, cookie_jar: str | None = None, warmup: bool = False) -> dict:
    """Retrieve a URL with curl. Returns status, headers and body text; never raises.

    cookie_jar + warmup: some sites (Moka job boards) 302 to themselves until a
    session cookie is set, so the jar is primed with one throwaway request first.
    """
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".bin")
    tmp.close()
    hdr = tempfile.NamedTemporaryFile(delete=False, suffix=".hdr")
    hdr.close()
    cmd = [
        # --ssl-no-revoke: this host's Windows schannel cannot reach the CRL/OCSP
        # responder, which aborts otherwise valid TLS handshakes (CRYPT_E_REVOCATION_OFFLINE).
        CURL, "-sS", "-L", "--ssl-no-revoke", "--max-time", str(timeout), "--compressed",
        "-A", UA,
        "-H", "Accept-Language: zh-CN,zh;q=0.9,en;q=0.8",
        "-D", hdr.name,
        "-o", tmp.name,
        "-w", "%{http_code}\t%{content_type}\t%{size_download}\t%{time_total}\t%{url_effective}",
        url,
    ]
    if cookie_jar:
        cmd[1:1] = ["-c", cookie_jar, "-b", cookie_jar]
    started = utc_now()
    try:
        if cookie_jar and warmup:
            subprocess.run([CURL, "-sS", "-c", cookie_jar, "-o", os.devnull,
                            "--ssl-no-revoke", "--max-time", str(timeout), "-A", UA, url],
                           capture_output=True, timeout=timeout + 20)
        # binary capture: curl writes stderr in the console code page on Windows,
        # so decoding must not be delegated to subprocess text mode.
        proc = subprocess.run(cmd, capture_output=True, timeout=timeout + 20)
        stdout_text = _decode_tool(proc.stdout)
        stderr_text = _decode_tool(proc.stderr)
        meta_line = stdout_text.strip().splitlines()[-1] if stdout_text.strip() else ""
        parts = meta_line.split("\t") if meta_line else []
        with open(tmp.name, "rb") as fh:
            raw = fh.read()
        with open(hdr.name, "r", encoding="utf-8", errors="replace") as fh:
            headers = fh.read()
        out = {
            "requested_url": url,
            "effective_url": parts[4] if len(parts) > 4 else url,
            "http_code": int(parts[0]) if parts and parts[0].isdigit() else None,
            "content_type": parts[1] if len(parts) > 1 else "",
            "bytes": int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else len(raw),
            "curl_time_s": float(parts[3]) if len(parts) > 3 and _is_float(parts[3]) else None,
            "stderr": stderr_text.strip()[:2000],
            "headers": headers[:8000],
            "raw": raw,
            "started_utc": started,
            "finished_utc": utc_now(),
        }
    except subprocess.TimeoutExpired:
        out = {"requested_url": url, "http_code": None, "content_type": "", "bytes": 0,
               "stderr": "TIMEOUT", "headers": "", "raw": b"", "effective_url": url,
               "started_utc": started, "finished_utc": utc_now(), "curl_time_s": timeout}
    except Exception as exc:  # pragma: no cover - defensive
        out = {"requested_url": url, "http_code": None, "content_type": "", "bytes": 0,
               "stderr": f"EXC {type(exc).__name__}: {exc}", "headers": "", "raw": b"",
               "effective_url": url, "started_utc": started, "finished_utc": utc_now(),
               "curl_time_s": None}
    finally:
        for p in (tmp.name, hdr.name):
            try:
                os.unlink(p)
            except OSError:
                pass
    return out


def _is_float(v: str) -> bool:
    try:
        float(v)
        return True
    except ValueError:
        return False


def _decode_tool(raw: bytes) -> str:
    """Decode curl stdout/stderr bytes that are not guaranteed to be UTF-8."""
    if not raw:
        return ""
    for enc in ("utf-8", "gb18030", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def decode(raw: bytes, content_type: str) -> tuple[str, str]:
    """Return (text, encoding_used). utf-8 -> gb18030 -> latin-1 fallback."""
    if not raw:
        return "", "none"
    m = re.search(r"charset=([\w\-]+)", content_type or "", re.I)
    declared = m.group(1).lower() if m else None
    for enc in [declared, "utf-8", "gb18030", "big5", "latin-1"]:
        if not enc:
            continue
        try:
            return raw.decode(enc), enc
        except (UnicodeDecodeError, LookupError):
            continue
    return raw.decode("utf-8", errors="replace"), "utf-8-replace"


TAG_RE = re.compile(r"<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>|<noscript\b[^>]*>.*?</noscript>",
                    re.I | re.S)
BLOCK_RE = re.compile(r"</(p|div|section|article|li|h[1-6]|tr|br)\s*>|<br\s*/?>", re.I)


def html_to_text(html: str) -> str:
    t = TAG_RE.sub(" ", html)
    t = re.sub(r"<head\b[^>]*>.*?</head>", " ", t, flags=re.I | re.S)
    t = BLOCK_RE.sub("\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    import html as _html
    t = _html.unescape(t)
    t = re.sub(r"[ \t\u00a0]+", " ", t)
    t = re.sub(r"\n\s*\n\s*\n+", "\n\n", t)
    return t.strip()


def pdf_to_text(raw: bytes) -> str:
    """Extract text from a PDF snapshot. Missing extractors leave a hashable placeholder."""
    try:
        import pypdf  # type: ignore
        reader = pypdf.PdfReader(__import__("io").BytesIO(raw))
        parts = []
        for page in reader.pages:
            parts.append(page.extract_text() or "")
        text = "\n".join(parts).strip()
        if text:
            return text
    except Exception:
        pass
    return f"[PDF snapshot {len(raw)} bytes; text extraction unavailable]"


def extract_meta(html: str) -> dict:
    def meta(name: str) -> str:
        pats = [
            rf'<meta[^>]+property=["\']{name}["\'][^>]+content=["\']([^"\']*)',
            rf'<meta[^>]+name=["\']{name}["\'][^>]+content=["\']([^"\']*)',
            rf'<meta[^>]+content=["\']([^"\']*)["\'][^>]+property=["\']{name}["\']',
            rf'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']{name}["\']',
        ]
        for p in pats:
            m = re.search(p, html, re.I)
            if m:
                return m.group(1).strip()
        return ""

    title = ""
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    if m:
        title = html_to_text(m.group(1))
    ld = []
    for m in re.finditer(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.I | re.S):
        raw = m.group(1).strip()
        try:
            data = json.loads(raw)
            ld.append(data)
        except Exception:
            ld.append({"_unparsed": raw[:500]})
    return {
        "title": title,
        "og_title": meta("og:title"),
        "og_site_name": meta("og:site_name"),
        "published": meta("article:published_time") or meta("datePublished") or meta("publishdate") or meta("pubdate"),
        "modified": meta("article:modified_time") or meta("lastmod"),
        "description": meta("description") or meta("og:description"),
        "jsonld": ld[:6],
    }


def snapshot(url: str, snap_id: str, company: str, question: str, note: str = "",
             keep_raw: bool = True, cookie_jar: str | None = None, warmup: bool = False,
             timeout: int = 40) -> dict:
    idx = load_index()
    res = fetch(url, timeout=timeout, cookie_jar=cookie_jar, warmup=warmup)
    is_pdf = (res["raw"][:4] == b"%PDF") or "pdf" in (res["content_type"] or "").lower()
    text, enc = decode(res["raw"], res["content_type"])
    meta = {}
    if is_pdf:
        body_text = pdf_to_text(res["raw"])
        enc = "pdf"
    else:
        meta = extract_meta(text) if "html" in (res["content_type"] or "").lower() or "<html" in text[:2000].lower() else {}
        body_text = html_to_text(text) if (meta or "<html" in text[:2000].lower()) else text

    os.makedirs(SNAP, exist_ok=True)
    rel_base = os.path.join("evidence_snapshots", f"{company}__{snap_id}")
    abs_base = os.path.join(RUN, rel_base)
    raw_sha = hashlib.sha256(res["raw"]).hexdigest()
    body_sha = hashlib.sha256(body_text.encode("utf-8")).hexdigest()
    if keep_raw:
        raw_ext = ".pdf" if is_pdf else ".html"
        with open(abs_base + raw_ext, "wb") as fh:
            fh.write(res["raw"])
    with open(abs_base + ".txt", "w", encoding="utf-8") as fh:
        fh.write(body_text)

    status = "OK" if (res["http_code"] or 0) == 200 else (
        "HTTP_ERROR" if res["http_code"] else "TIMEOUT"
    )
    if res["http_code"] is None and "TIMEOUT" in (res["stderr"] or ""):
        status = "TIMEOUT"
    elif res["http_code"] is None:
        status = "BLOCKED"

    rec = {
        "snapshot_id": snap_id,
        "company_id": company,
        "question": question,
        "requested_url": url,
        "effective_url": res["effective_url"],
        "http_code": res["http_code"],
        "access_status": status,
        "content_type": res["content_type"],
        "bytes": res["bytes"],
        "body_text_chars": len(body_text),
        "raw_sha256": raw_sha,
        "body_text_sha256": body_sha,
        "snapshot_text_path": rel_base + ".txt",
        "snapshot_raw_path": (rel_base + (".pdf" if is_pdf else ".html")) if keep_raw else "",
        "encoding_used": enc,
        "title": meta.get("title", "") if meta else "",
        "published_meta": meta.get("published", "") if meta else "",
        "modified_meta": meta.get("modified", "") if meta else "",
        "og_site_name": meta.get("og_site_name", "") if meta else "",
        "retrieved_at_utc": res["finished_utc"],
        "note": note,
        "error": res["stderr"][:500],
    }
    idx["snapshots"][snap_id] = rec
    save_index(idx)
    append_jsonl(SEARCH_LOG, {
        "ts_utc": res["finished_utc"],
        "action": "FETCH",
        "company_id": company,
        "question": question,
        "url": url,
        "http_code": res["http_code"],
        "access_status": status,
        "snapshot_id": snap_id,
        "result": "retrieved" if status == "OK" else f"failed: {status}",
        "note": note,
    })
    return rec


def log_search(company: str, question: str, query: str, tool: str, outcome: str,
               urls_checked: list[str] | None = None, note: str = "") -> None:
    append_jsonl(SEARCH_LOG, {
        "ts_utc": utc_now(),
        "action": "SEARCH",
        "company_id": company,
        "question": question,
        "tool": tool,
        "query": query,
        "urls_checked": urls_checked or [],
        "result": outcome,
        "note": note,
    })


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url")
    ap.add_argument("--id")
    ap.add_argument("--company", default="GENERAL")
    ap.add_argument("--question", default="")
    ap.add_argument("--note", default="")
    ap.add_argument("--batch")
    args = ap.parse_args()
    if args.batch:
        with open(args.batch, "r", encoding="utf-8") as fh:
            items = json.load(fh)
        results = []
        for it in items:
            jar = None
            if it.get("cookie_jar"):
                jar = os.path.join(WORK, "cookies", it["cookie_jar"] + ".txt")
                os.makedirs(os.path.dirname(jar), exist_ok=True)
            r = snapshot(it["url"], it["id"], it.get("company", "GENERAL"),
                         it.get("question", ""), it.get("note", ""),
                         cookie_jar=jar, warmup=bool(it.get("warmup")),
                         timeout=int(it.get("timeout", 40)))
            results.append({k: r[k] for k in ("snapshot_id", "http_code", "access_status",
                                              "bytes", "body_text_chars", "title", "effective_url")})
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0
    if not args.url or not args.id:
        ap.error("--url and --id are required without --batch")
    r = snapshot(args.url, args.id, args.company, args.question, args.note)
    print(json.dumps({k: r[k] for k in ("snapshot_id", "requested_url", "effective_url", "http_code",
                                        "access_status", "bytes", "body_text_chars", "title",
                                        "published_meta", "raw_sha256", "snapshot_text_path")},
                     ensure_ascii=False, indent=2))
    return 0 if r["access_status"] == "OK" else 1


if __name__ == "__main__":
    raise SystemExit(main())
