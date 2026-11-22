const fs=require('node:fs'),path=require('node:path'),{pathToFileURL,fileURLToPath}=require('node:url');
const {dependency,browserOptions}=require('./runtime.cjs');
const {chromium}=dependency('playwright');const {marked}=dependency('marked');
const root=path.resolve(__dirname,'..'),phase=process.argv[2]||('run-'+new Date().toISOString().replace(/[:.]/g,'-')),dir=path.join(root,'reports/checks/html-2026-11-22',phase);fs.mkdirSync(dir,{recursive:true});
const checks=[],errors=[],consoleErrors=[],requests=[];const check=(name,ok,detail)=>checks.push({name,passed:!!ok,detail});
const url=pathToFileURL(path.join(root,'slides/index.html')).href;const manifest=JSON.parse(fs.readFileSync(path.join(root,'reports/build-manifest.json')));
const diagrams=JSON.parse(fs.readFileSync(path.join(root,'assets/diagram-manifest.json')));
const filename=p=>path.join(dir,p);
(async()=>{
const browser=await chromium.launch(browserOptions());
const context=await browser.newContext({viewport:{width:1440,height:1000},deviceScaleFactor:1});const page=await context.newPage();
context.setDefaultTimeout(8000);page.setDefaultTimeout(8000);
page.on('pageerror',e=>consoleErrors.push(e.message));page.on('request',r=>{if(/^https?:/.test(r.url()))requests.push(r.url());});
let visit=0;
async function jump(n){await page.goto(url+'?check='+ ++visit +'#'+manifest.main[n-1].id);await page.locator('.slide:visible').waitFor();}
const visible=async()=>+(await page.locator('.slide:visible').getAttribute('data-page'));
try{
await jump(1);check('exactly_18_slides',await page.locator('.slide').count()===18,await page.locator('.slide').count());
check('first_page_previous_disabled',await page.locator('#prev').isDisabled(),true);
await page.locator('#help-button').click();check('help_dialog_opens',await page.locator('#help-dialog').evaluate(e=>e.open),true);await page.locator('#help-dialog [data-close]').click();
await page.locator('#fullscreen').click();check('fullscreen_enters',await page.evaluate(()=>!!document.fullscreenElement),true);await page.locator('#fullscreen').click();check('fullscreen_exits',await page.evaluate(()=>!document.fullscreenElement),true);
await page.locator('#next').click();check('next_button',await visible()===2,await visible());
await page.keyboard.press('ArrowRight');check('keyboard_after_next_click',await visible()===3,await visible());
await jump(4);await page.locator('.slide:visible [data-step="1"]').click();await page.locator('.slide:visible [data-step="1"]').click();check('score_diagram_26_24',await page.locator('.slide:visible output').innerText()==='26：24 · 3/3',await page.locator('.slide:visible output').innerText());
check('diagram_last_step_disabled',await page.locator('.slide:visible [data-step="1"]').isDisabled(),true);
await page.locator('#open-menu').click();check('menu_opens',await page.locator('#menu-dialog').evaluate(e=>e.open),true);await page.locator('[data-go="10"]').click();check('menu_goes_to_11',await visible()===11,await visible());
await page.locator('.slide:visible .zoom-diagram').click();check('zoom_opens',await page.locator('#zoom-dialog').evaluate(e=>e.open),true);await page.keyboard.press('Escape');check('escape_closes_zoom',!await page.locator('#zoom-dialog').evaluate(e=>e.open),true);
await page.locator('.slide:visible h2').focus();await page.keyboard.press('End');check('end_to_18',await visible()===18,await visible());await page.keyboard.press('Home');check('home_to_1',await visible()===1,await visible());await page.keyboard.press('PageDown');check('page_down',await visible()===2,await visible());await page.keyboard.press('PageUp');check('page_up',await visible()===1,await visible());
await jump(8);await page.locator('.slide:visible .supplement summary').focus();await page.keyboard.press('Enter');check('keyboard_expands_supplement',await page.locator('.slide:visible .supplement').evaluate(e=>e.open),true);check('libero_complete_supplement',(await page.locator('.slide:visible .supplement').innerText()).includes('高手手指傳球'),true);await page.screenshot({path:filename('08-expanded.png'),fullPage:true});
const [popup]=await Promise.all([context.waitForEvent('page'),page.locator('.slide:visible .claim-ref').first().click()]);await popup.waitForLoadState();check('claim_link_to_reader',popup.url().includes('slide-sources.html#C08.1')&&await popup.locator('#C08\\.1').count()===1,popup.url());await popup.close();
const wikiHref=await page.locator('.slide:visible .slide-footer a').first().getAttribute('href');const wiki=await context.newPage();await wiki.goto(new URL(wikiHref,url).href);check('wiki_reader_opens',(await wiki.locator('h1').innerText()).includes('自由球員'),wiki.url());const source=wiki.locator('a[href*="s01-fivb-rules"]').first();await source.click();check('wiki_to_original_source',await wiki.locator('a[href*="raw/S01/original.pdf"]').count()>0,wiki.url());await wiki.close();
await jump(16);for(let i=0;i<9;i++)await page.locator('.slide:visible [data-step="1"]').click();check('rally_final_step',(await page.locator('.slide:visible output').innerText()).includes('B 輪轉、取得發球權'),await page.locator('.slide:visible output').innerText());await page.screenshot({path:filename('16-final-state.png'),fullPage:false});
await jump(17);await page.locator('[data-question="Q1"] [data-answer="A"]').click();check('quiz_wrong_explained',await page.locator('[data-question="Q1"] .incorrect').count()===1&&await page.locator('[data-question="Q1"] .quiz-result').isVisible(),true);await page.locator('[data-question="Q2"] [data-answer="A"]').focus();await page.keyboard.press('Enter');check('quiz_keyboard_and_no_slide_change',await visible()===17&&await page.locator('[data-question="Q2"] .correct').count()===1,true);await page.locator('[data-reveal="Q3"]').click();check('quiz_reveal_reason',(await page.locator('[data-question="Q3"] .quiz-result').innerText()).includes('攔網觸球不占三擊'),true);await page.screenshot({path:filename('17-answers.png'),fullPage:true});
for(const q of manifest.main[16].main_markdown.matchAll(/\*\*(Q[1-3])｜([^*]+)\*\*[^\n]*\n\n- A．([^\n]+)\n- B．([^\n]+)/g)){
 const section=page.locator(`[data-question="${q[1]}"]`),actual=await section.locator('h3').evaluate(el=>{const c=el.cloneNode(true);c.querySelectorAll('.claim-ref').forEach(a=>a.remove());return c.textContent.replace(/\s+/g,'');});
 check(`quiz_${q[1]}_approved_question`,actual===(q[1]+q[2]).replace(/\s+/g,''),actual);
 for(let [i,key]of [[3,'A'],[4,'B']])check(`quiz_${q[1]}_option_${key}`,(await section.locator(`[data-answer="${key}"]`).innerText())===key+'．'+q[i],q[i]);
}
check('quiz_no_literal_markdown',(await page.locator('.slide:visible .main-copy').innerText()).includes('**')===false,true);
await context.setOffline(true);await jump(1);check('file_reading_offline',await page.locator('.slide:visible .diagram img').evaluate(i=>i.complete&&i.naturalWidth>0),true);await context.setOffline(false);
// Read the actual HTML render against the approved text, excluding citation labels.
for(let n=1;n<=18;n++){
 await jump(n);await page.locator('.slide:visible img').evaluate(i=>i.decode());
 if(n===17)check('quiz_answers_initially_hidden',await page.locator('.quiz-result:visible').count()===0,true);
 const layout=await page.evaluate(()=>{const s=document.querySelector('.slide:not([hidden])'),m=s.querySelector('.slide-main').getBoundingClientRect();return {page:+s.dataset.page,docWidth:document.documentElement.scrollWidth,width:innerWidth,mainBottom:m.bottom,navTop:document.querySelector('.deck-nav').getBoundingClientRect().top};});
 check(`desktop_${n}_no_horizontal_overflow`,layout.docWidth<=layout.width+1,layout);
 check(`desktop_${n}_main_clear_of_nav`,layout.mainBottom<=layout.navTop+1,layout);
 if(n!==17){for(const [selector,key]of [['.main-copy','main_markdown'],['.supplement .details-body','supplement_markdown']]){const expectedHTML=marked.parse(manifest.main[n-1][key].replace(/〔[^〕]+〕/g,''));const equal=await page.locator('.slide:visible '+selector).evaluate((el,html)=>{const doc=new DOMParser().parseFromString(html,'text/html');const clone=el.cloneNode(true);clone.querySelectorAll('.claim-ref').forEach(x=>x.remove());const norm=t=>t.replace(/\s+/g,'');return {same:norm(clone.textContent)===norm(doc.body.textContent),expected:norm(doc.body.textContent).length,actual:norm(clone.textContent).length};},expectedHTML);check(`${n}_${key}_preserved`,equal.same,equal);}}
 await page.screenshot({path:filename(`${String(n).padStart(2,'0')}-desktop.png`),fullPage:false});
}
await page.setViewportSize({width:390,height:844});
for(let n=1;n<=18;n++){await jump(n);const dims=await page.evaluate(()=>({w:innerWidth,doc:document.documentElement.scrollWidth}));check(`mobile_${n}_no_horizontal_overflow`,dims.doc<=dims.w+1,dims);if([3,7,8,11,16,17].includes(n))await page.screenshot({path:filename(`${String(n).padStart(2,'0')}-mobile.png`),fullPage:true});}
await jump(11);await page.locator('.slide:visible .zoom-diagram').click();const zoom=await page.locator('.zoom-scroll').evaluate(e=>({scroll:e.scrollWidth,client:e.clientWidth,page:document.documentElement.scrollWidth}));check('mobile_zoom_scroll_contained',zoom.scroll>zoom.client&&zoom.page<=390,zoom);await page.keyboard.press('Escape');
await page.locator('.slide:visible .supplement summary').click();await page.locator('.slide:visible .slide-footer').scrollIntoViewIfNeeded();check('mobile_footer_reachable',await page.locator('.slide:visible .slide-footer').isVisible(),true);
await page.setViewportSize({width:1024,height:768});for(let n=1;n<=18;n++){await jump(n);const b=await page.locator('.slide:visible .slide-main').boundingBox();const nav=await page.locator('.deck-nav').boundingBox();check(`compact_${n}_main_height`,b.y+b.height<=nav.y+1,{bottom:b.y+b.height,navTop:nav.y});if([7,17].includes(n))await page.screenshot({path:filename(`${String(n).padStart(2,'0')}-compact.png`),fullPage:false});}
await jump(17);for(let q of ['Q1','Q2','Q3'])await page.locator(`[data-reveal="${q}"]`).click();await page.locator('.slide:visible .slide-footer').scrollIntoViewIfNeeded();const quizFooter=await page.locator('.slide:visible .slide-footer').boundingBox(),quizNav=await page.locator('.deck-nav').boundingBox();check('compact_expanded_quiz_can_scroll_clear_of_nav',quizFooter.y+quizFooter.height<=quizNav.y,{footer:quizFooter,nav:quizNav});
// Inspect SVG text geometry in the browser, including every step state.
const svgp=await context.newPage();for(let d of diagrams){for(let s of d.states){const f=path.resolve(root,'slides',s.file);await svgp.goto(pathToFileURL(f).href);const outside=await svgp.evaluate(()=>[...document.querySelectorAll('text')].map(e=>{const b=e.getBBox();return {text:e.textContent,x:b.x,y:b.y,r:b.x+b.width,b:b.y+b.height};}).filter(b=>b.x<0||b.y<0||b.r>761||b.b>481));check(`svg_bounds_${path.basename(f)}`,outside.length===0,outside);}}await svgp.close();
// Validate actual generated local links and referenced resources without network requests.
let missing=[];const generated=['slides/index.html',...manifest.reader_pages];for(let f of generated){let html=fs.readFileSync(path.join(root,f),'utf8');for(let match of html.matchAll(/(?:href|src)="([^"]+)"/g)){let u=match[1].replaceAll('&amp;','&');if(/^(https?:|mailto:|data:|#)/.test(u))continue;let [p,hash]=u.split('#');let resolved=path.resolve(root,path.dirname(f),decodeURIComponent(p));if(!fs.existsSync(resolved))missing.push({from:f,target:u});else if(hash&&resolved.endsWith('.html')&&!hash.startsWith('page=')){let target=fs.readFileSync(resolved,'utf8');if(!target.includes(`id="${decodeURIComponent(hash)}"`))missing.push({from:f,target:u,reason:'missing anchor'});}}}check('generated_links_and_resources',!missing.length,{pages:generated.length,missing});
const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:1024,height:768}});const np=await nojs.newPage();await np.goto(url);check('no_js_all_18_pages',await np.locator('.slide:visible').count()===18,await np.locator('.slide:visible').count());await nojs.close();
check('no_runtime_errors',consoleErrors.length===0,consoleErrors);check('no_remote_core_requests',requests.length===0,requests);
}catch(e){errors.push(e.stack||e.message);}
const result={checked_at:new Date().toISOString(),browser:await browser.version(),mode:'real headless Chromium via installed Chrome; file:// URLs',phase,checks,failures:checks.filter(c=>!c.passed),errors,screenshot_directory:path.relative(root,dir).replaceAll('\\','/'),screenshots:fs.readdirSync(dir).filter(f=>f.endsWith('.png'))};
fs.writeFileSync(filename('browser-results.json'),JSON.stringify(result,null,2));console.log(JSON.stringify({phase,checks:checks.length,failures:result.failures,errors,screenshots:result.screenshots.length}));await browser.close();if(result.failures.length||errors.length)process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1;});
