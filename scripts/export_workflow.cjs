// Export the approved Mermaid graph using a local renderer and installed Chrome.
// Run npm install, or use the verified Mermaid archive in the ignored local cache.
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const crypto = require('node:crypto');
const { dependency, browserOptions } = require('./runtime.cjs');
const { chromium } = dependency('playwright');
const sharp = dependency('sharp');
const root = path.resolve(__dirname, '..');
const sourcePath = 'assets/workflow/hw10-graph.mmd';
const source = fs.readFileSync(path.join(root, sourcePath), 'utf8');
let dist;
try { dist=path.dirname(require.resolve('mermaid')); }
catch { dist=path.join(root, '.cache/mermaid-12.3.0/package/dist'); }
if (!fs.existsSync(path.join(dist,'mermaid.esm.min.mjs'))) throw Error('Mermaid renderer missing; run npm install.');
const expectedNodes = [...source.matchAll(/^\s*([A-Z][A-Z0-9]*)[\[{]/gm)].map(m => m[1]);
const expectedEdges = [...source.matchAll(/^\s*[A-Z][A-Z0-9]*\s+(?:-->|--\s+".*?"\s+-->)/gm)].length;
const output = path.join(root, 'assets/workflow');
const reportName = process.argv[2] || 'graph-export-'+new Date().toISOString().replace(/[:.]/g,'-')+'.json';
if (!/^[a-zA-Z0-9._-]+\.json$/.test(reportName)) throw Error('Use a simple JSON report filename.');
const reportPath = path.join(root, 'reports/checks', reportName);
if (fs.existsSync(reportPath)) throw Error('Use a new report filename to preserve earlier checks.');
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const mime = { '.js':'text/javascript', '.mjs':'text/javascript', '.css':'text/css', '.wasm':'application/wasm' };
const server = http.createServer((req,res) => {
  const name = decodeURIComponent(new URL(req.url,'http://localhost').pathname);
  if (name === '/') {
    res.setHeader('Content-Type','text/html; charset=utf-8');
    res.end('<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><style>body{margin:0;background:white;font-family:"Microsoft JhengHei",sans-serif;color:#17343c}#poster{width:max-content;padding:40px;box-sizing:content-box;background:white}header{padding:4px 0 28px}h1{font-size:34px;font-weight:700;line-height:1.5;margin:0 0 9px}.legend{font-size:20px;line-height:1.5;color:#435f63}svg{display:block;max-width:none!important}footer{font-size:19px;line-height:1.5;margin-top:22px;color:#435f63}</style><div id="poster"><header><h1>排球 LLM Wiki｜完整 graph 流程</h1><div class="legend">知識庫 → 教學簡報 → 公開發布　｜　黃色：人工確認　橘色：實作後新增 J0</div></header><main id="chart"></main><footer>每份來源重複 ingest 與 lint；檢查失敗回到對應節點，修正後只複查受影響範圍。</footer></div></html>');
    return;
  }
  const file = path.resolve(dist,'.'+name);
  if (!file.startsWith(dist+path.sep) || !fs.existsSync(file) || !fs.statSync(file).isFile()) {res.writeHead(404).end();return;}
  res.setHeader('Content-Type',mime[path.extname(file)]||'application/octet-stream');
  fs.createReadStream(file).pipe(res);
});
(async () => {
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  let browser;
  try {
    browser = await chromium.launch(browserOptions());
    const page = await browser.newPage({viewport:{width:1600,height:1000},deviceScaleFactor:2});
    const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    const base='http://127.0.0.1:'+server.address().port;
    await page.goto(base);
    await page.evaluate(async ({source,base}) => {
      await document.fonts.ready;
      const {default:mermaid}=await import(base+'/mermaid.esm.min.mjs');
      mermaid.initialize({startOnLoad:false,layout:'dagre',look:'classic',theme:'base',fontFamily:'Microsoft JhengHei, sans-serif',markdownAutoWrap:false,htmlLabels:true,
        themeVariables:{fontFamily:'Microsoft JhengHei, sans-serif',fontSize:'21px',primaryColor:'#eaf3ef',primaryTextColor:'#17343c',primaryBorderColor:'#42796c',secondaryColor:'#fff9e8',tertiaryColor:'#f6f9f8',lineColor:'#587570',textColor:'#17343c',clusterBkg:'#f7f9f8',clusterBorder:'#c2d2cc',edgeLabelBackground:'#ffffff'},
        flowchart:{useMaxWidth:false,nodeSpacing:42,rankSpacing:36,diagramPadding:24,curve:'linear',wrappingWidth:420,subGraphTitleMargin:{top:15,bottom:25}},
        elk:{mergeEdges:false,nodePlacementStrategy:'NETWORK_SIMPLEX'}});
      const {svg}=await mermaid.render('hw10-workflow',source);
      document.getElementById('chart').innerHTML=svg;
    },{source,base});
    const dimensions=await page.locator('#chart svg').evaluate(el=>{
      const b=el.viewBox.baseVal;
      el.setAttribute('width',Math.ceil(b.width));el.setAttribute('height',Math.ceil(b.height));
      return {width:Math.ceil(b.width),height:Math.ceil(b.height)};
    });
    await page.setViewportSize({width:dimensions.width+80,height:1000});
    const validation=await page.locator('#chart svg').evaluate(svg=>{
      const bounds=svg.getBoundingClientRect();
      const nodes=[...svg.querySelectorAll('g.node')].map(n=>(n.getAttribute('data-id')||n.id).replace(/^.*?flowchart-/,'').replace(/-\d+$/,''));
      const labels=[...svg.querySelectorAll('.nodeLabel,.edgeLabel,.cluster-label')].map(n=>({text:n.textContent.trim(),r:n.getBoundingClientRect()}));
      return {nodes,edges:svg.querySelectorAll('path.flowchart-link').length,labelsOutside:labels.filter(n=>n.text && n.r.width>0 && n.r.height>0 && (n.r.left<bounds.left-2||n.r.top<bounds.top-2||n.r.right>bounds.right+2||n.r.bottom>bounds.bottom+2)).map(n=>n.text),font:document.fonts.check('21px "Microsoft JhengHei"')};
    });
    const missing=expectedNodes.filter(n=>!validation.nodes.includes(n));
    if (missing.length || validation.edges!==expectedEdges || validation.labelsOutside.length || errors.length) throw Error(JSON.stringify({missing,expectedEdges,validation,errors}));
    const svg=await page.locator('#chart svg').evaluate(el=>el.outerHTML);
    fs.writeFileSync(path.join(output,'hw10-graph.svg'),svg);
    const png=path.join(output,'hw10-graph.png');
    await page.locator('#poster').screenshot({path:png,type:'png',animations:'disabled'});
    const metadata=await sharp(png).metadata();
    const report={checked_at:new Date().toISOString(),source:sourcePath,source_sha256:sha(Buffer.from(source)),renderer:'mermaid 12.3.0 / Dagre / installed Chrome',browser:await browser.version(),nodes:validation.nodes.length,edges:validation.edges,all_source_nodes_and_edges_present:true,labels_outside_canvas:validation.labelsOutside,script_errors:errors,output:'assets/workflow/hw10-graph.png',width:metadata.width,height:metadata.height,bytes:fs.statSync(png).size,png_sha256:sha(fs.readFileSync(png)),visual_review:'pending'};
    fs.writeFileSync(reportPath,JSON.stringify(report,null,2));
    console.log(JSON.stringify(report));
    // Review crops are temporary and excluded from Git by the existing .cache rule.
    for(let i=0;i<3;i++) {
      const top=Math.round((metadata.height-1800)*i/2);
      await sharp(png).extract({left:0,top,width:metadata.width,height:Math.min(1800,metadata.height)}).resize({width:1800,withoutEnlargement:true}).toFile(path.join(root,`.cache/graph-review-${i+1}.png`));
    }
  } finally {
    if(browser)await browser.close();
    await new Promise(resolve=>server.close(resolve));
  }
})().catch(e=>{console.error(e.stack||e.message);process.exitCode=1;});
