const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const {chromium}=require('C:/Users/bestl/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve(__dirname,'..');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 const page=await browser.newPage({viewport:{width:1365,height:1000}});const errors=[],results=[];
 page.on('pageerror',e=>errors.push(String(e)));
 for(const file of fs.readdirSync(path.join(root,'query')).filter(s=>s.endsWith('.html'))){
  await page.goto(pathToFileURL(path.join(root,'query',file)).href,{waitUntil:'load'});
  const checks=await page.evaluate(()=>{
   const problems=[],samples=[];
   const codes=[lab.value,...['SK_PYTHON','SK_CPP','SK_LINUX','TC_EVALUATION','SK_SAFETY_OPERATIONS'].filter(c=>data.labels.some(a=>a[0]===c)),data.labels.at(-1)[0]];
   for(const t of ['ALL',task.options[1].value])for(const code of [...new Set(codes)])for(const c of ['GENERAL|UNCONDITIONAL','PREFERRED|UNCONDITIONAL','DUTY_OWN_USE|UNCONDITIONAL','GENERAL|CHOICE']){
    task.value=t;lab.value=code;ctx.value=c;update();
    const [m,b]=c.split('|'),a=data.aggregates.find(a=>a[0]===t&&a[1]===code&&a[2]===m&&a[3]===b);
    if(!a){problems.push('missing aggregate '+t+' '+code+' '+c);continue;}
    const rr=[...document.querySelectorAll('#points tr')];
    const sum=i=>rr.reduce((s,r)=>s+Number(r.cells[i].textContent),0);
    if(sum(1)!==Number(a[4])||sum(2)!==Number(a[5])||sum(6)!==Number(a[6]))problems.push('visible totals differ '+t+' '+code+' '+c);
    if(document.getElementById('summary').textContent.includes('undefined')||document.getElementById('points').innerHTML.includes('NaN'))problems.push('undefined or NaN');
    if(rr.some(r=>r.cells.length!==9))problems.push('column count');
    for(const r of rr){const n=Number(r.cells[6].textContent),p=Number(r.cells[1].textContent),v=r.cells[7].textContent;if(n&&v!==(100*p/n).toFixed(2)+'%')problems.push('visible rate');if(!n&&v!=='不汇总')problems.push('zero denominator not missing');}
    samples.push({task:t,code,context:c,companies:rr.length});
   }
   task.value='ALL';lab.value=data.labels.some(a=>a[0]==='SK_PYTHON')?'SK_PYTHON':data.labels[0][0];ctx.value='GENERAL|UNCONDITIONAL';update();
   if(document.documentElement.scrollWidth>innerWidth+2)problems.push('horizontal overflow');
   return {problems,samples};
  });
  results.push({file,...checks});console.log(file,checks.samples.length,checks.problems.length);
  if(['RF_ML_AI_ENGINEERING.html','RF_INDUSTRIAL_EXPERIENCE_DESIGN.html'].includes(file))await page.screenshot({path:path.join(root,'verification',file+'.png'),fullPage:false});
 }
 await browser.close();const report={status:errors.length||results.some(r=>r.problems.length)?'FAIL':'PASS',browser:'Installed Chrome via bundled Playwright, headless',pages:results.length,states:results.reduce((n,r)=>n+r.samples.length,0),errors,results};
 fs.writeFileSync(path.join(root,'verification','query_browser.json'),JSON.stringify(report,null,2));if(report.status==='FAIL')process.exitCode=1;
})();
