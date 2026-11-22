// Resolve ordinary npm installations first, with the original authoring runtime
// retained as a fallback. The generated site never loads these packages.
const path=require('node:path'),fs=require('node:fs');

function dependency(name){
  if(process.env.HW10_NODE_MODULES)return require(path.join(process.env.HW10_NODE_MODULES,name));
  try{return require(name);}catch(error){
    if(error.code!=='MODULE_NOT_FOUND')throw error;
    const bundled=path.resolve(path.dirname(process.execPath),'..','node_modules',name);
    if(fs.existsSync(bundled))return require(bundled);
    throw new Error(`Missing ${name}. Run npm install in HW10, or set HW10_NODE_MODULES.`);
  }
}

function browserOptions(){
  const explicit=process.env.HW10_BROWSER_EXECUTABLE;
  if(explicit){if(!fs.existsSync(explicit))throw new Error('HW10_BROWSER_EXECUTABLE does not exist');return {headless:true,executablePath:explicit};}
  const candidates=process.platform==='win32'
    ? ['C:/Program Files/Google/Chrome/Application/chrome.exe','C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe']
    : process.platform==='darwin' ? ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome']
    : ['/usr/bin/google-chrome','/usr/bin/chromium','/usr/bin/chromium-browser'];
  const installed=candidates.find(p=>fs.existsSync(p));
  // With no system browser, use the browser installed by npx playwright install chromium.
  return installed?{headless:true,executablePath:installed}:{headless:true};
}

module.exports={dependency,browserOptions};
