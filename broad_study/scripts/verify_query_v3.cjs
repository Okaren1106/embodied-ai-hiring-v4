const fs = require('fs'), path = require('path'), vm = require('vm'), assert = require('assert');
const root=path.resolve(__dirname,'..'), checks=[];
function execute(file) {
 const html=fs.readFileSync(file,'utf8'), elements={};
 const get=id=>elements[id]||(elements[id]={
  value:'',textContent:'',_html:'',
  set innerHTML(v){this._html=v;const m=v.match(/<option value="([^"]*)"/);if(m)this.value=m[1];},
  get innerHTML(){return this._html;}
 });
 for(const m of html.matchAll(/<select id="([^"]+)"[^>]*>([\s\S]*?)<\/select>/g)) get(m[1]).innerHTML=m[2];
 const context=vm.createContext({document:{getElementById:get}});
 for(const m of html.matchAll(/<script>([\s\S]*?)<\/script>/g))vm.runInContext(m[1],context,{timeout:10000});
 return {html,get,run:s=>vm.runInContext(s,context,{timeout:10000})};
}
for(const name of fs.readdirSync(path.join(root,'query')).filter(x=>x.endsWith('.html'))) {
 const x=execute(path.join(root,'query',name));
 assert(x.get('summary').textContent.includes('当前组'),name);
 assert(x.get('points').innerHTML.includes('<tr>'),name);
 const tasks=[...x.get('task').innerHTML.matchAll(/<option value="([^"]+)"/g)].map(y=>y[1]);
 x.get('task').value=tasks[1]; x.run('update()');
 assert(x.get('summary').textContent.includes('当前组'),name+' task');
 x.get('ctx').value='PREFERRED|UNCONDITIONAL';x.run('update()');
 assert(!x.get('summary').textContent.includes('undefined'),name+' context');
 checks.push({page:name,initial:true,task_switch:true,context_switch:true});
}
assert.equal(checks.length,17);
const t=execute(path.join(root,'two_layers.html'));
for(const [task,n] of [['ROBOT_MODEL',105],['ROBOT_RUNTIME',87],['BOARD_CIRCUIT',56]]) {
 t.get('task').value=task;t.run('labels()');
 assert(t.get('summary').textContent.includes(' '+n+' '),task);
 assert(t.get('body').innerHTML.includes('<tr>'),task);
 const first=t.get('body').innerHTML.match(/<tr>(.*?)<\/tr>/)[1];
 assert.equal([...first.matchAll(/<td>/g)].length,10);
 assert(!first.includes('undefined'));
}
const files=[path.join(root,'index.html'),path.join(root,'two_layers.html'),...checks.map(x=>path.join(root,'query',x.page))];
let links=0;
for(const file of files)for(const m of fs.readFileSync(file,'utf8').matchAll(/href="([^"]+)"/g)) {
 if(/^(https?:|#)/.test(m[1]))continue;
 assert(fs.existsSync(path.resolve(path.dirname(file),m[1])),m[1]);links++;
}
const receipt={status:'PASS',method:'Node VM executed embedded JavaScript using a minimal DOM with native select initial-value behavior; not a browser visual inspection',function_pages:17,two_layer_tasks:3,table_columns:10,local_links_checked:links,checks};
fs.writeFileSync(path.join(root,'verification/query_v3.json'),JSON.stringify(receipt,null,2));
console.log(JSON.stringify({status:receipt.status,pages:17,tasks:3,links}));
