# 4+4 pilot collection policy

Status: baseline accepted/frozen; weekly workflow awaiting explicit schedule time
Effective date: 2026-08-31

The eight approved companies are Unitree, Spirit AI, X Square, Noetix, Figure, Agility
Robotics, Apptronik, and Physical Intelligence. The 2026-08-31 human decision enabled collection
and approved exactly these eight source/company/board tuples for one initial full-board snapshot.
The machine-readable policy is `configs/pilot_collection.yaml`. Baseline review is complete.
Weekly collection remains machine-disabled only until an explicit weekday and local time are
recorded; the scheduler may not invent either value.

## Validation gate

1. An official, public recruitment source that does not require login may enter pilot validation.
2. Inspect exactly 5–10 postings before any source can be considered for formal collection.
3. Record stable ID, title, location, department/team, posting date, full JD, requirements,
   closed/reposted behavior, duplicate risk, and field missingness. Missing fields remain explicit;
   they are not inferred from nearby text or another platform.
4. A source may be labeled `READY_FOR_COLLECTION` after bounded validation. Formal collection
   requires separate human approval of the global gate and exact source tuple.
5. `MANUAL_ONLY` means useful public evidence exists but does not support a repeatable job-level
   feed. `BLOCKED/INACCESSIBLE` describes the access attempt, not the company's hiring state.

## Login and protected-source gate

Sources that require login—or whose access state cannot establish login-free retrieval because a
signed, encrypted, CSRF-bound, CAPTCHA-protected, or otherwise restricted runtime intervenes—must
be labeled `LOGIN_REVIEW_REQUIRED` and receive a review record in
`data/login_source_review.yaml`. The review records include company, URL, reason for review,
expected incremental fields, public official alternatives, access protections, recommendation,
and a human decision.

No credentials, authenticated session, or protected runtime may be used while `human_decision` is
`PENDING`. Human approval is necessary but not sufficient: collection must still be technically
possible without bypassing CAPTCHA, signatures, encryption, login protection, rate limits, or
other access controls. The project never asks a human to solve a CAPTCHA for unattended access.

A visible “login” navigation item does not itself make a public job list login-required. Record
whether job lists and detail pages are actually readable without authentication. VPN-dependent
TLS or routing failures are access-environment observations and must be retested without being
misclassified as an authentication gate.

## Measurement guardrails

- Retrieval failure is `UNKNOWN_NOT_ZERO_HIRING`; it can never be coded as zero hiring.
- Board totals are current requisition records, not vacancies, hires, employment, or headcount.
- Removal is a page-state change until closure semantics are directly observed. Reappearance may
  be a repost, reopening, duplicate, or source redesign.
- A validation sample is a field-feasibility check, not a representative job sample.
- The frozen baseline is t0. Only later successful, complete, comparable snapshots may generate
  lifecycle comparisons; failed or partial attempts cannot generate removals.
- No China–US inference or batch taxonomy coding is permitted in this phase.
- Preserve exact retrieval time and raw IDs in future approved snapshots; do not overwrite prior
  observations.

## Pipeline enforcement

The `collect --execute` path loads `configs/pilot_collection.yaml` and rejects execution unless:
global collection is enabled, the company is pilot approved, the status is
`READY_FOR_COLLECTION`, the source has separate human collection approval, and the platform and
board exactly match the approved config. Dry runs remain network-free.

The first-snapshot orchestrator refuses an existing run directory unless `--resume` is used.
Resume mode skips every source already marked successful, so recovery from a partial run cannot
silently create a second observation for those sources. Failed sources remain
`UNKNOWN_NOT_ZERO_HIRING` and are never written as empty snapshots.
