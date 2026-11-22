// Verify public deployment bytes without cookies or authentication.
// Usage: node scripts/check_pages.cjs BASE_URL OUTPUT_JSON [relative files...]
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '..');
const base = new URL(process.argv[2]);
const printOnly = process.argv[3] === '-';
const output = printOnly ? null : path.resolve(root, process.argv[3] || 'reports/checks/pages-http-latest.json');
if (base.protocol !== 'https:' || !base.pathname.endsWith('/')) throw Error('Use an HTTPS site root ending in /');
if (output && !output.startsWith(root + path.sep)) throw Error('Report must stay inside HW10');
if (output && fs.existsSync(output)) throw Error('Use a new report name to preserve earlier evidence');
const manifest = JSON.parse(fs.readFileSync(path.join(root, 'reports/build-manifest.json'), 'utf8'));
const supplied = process.argv.slice(4);
const defaults = ['index.html', 'slides/index.html', ...manifest.reader_pages,
  'assets/slides.css', 'assets/slides.js', 'assets/reader.css', 'reports/checks/figures/index.html',
  ...fs.readdirSync(path.join(root, 'assets/diagrams')).filter(f => f.endsWith('.svg')).map(f => 'assets/diagrams/' + f)];
const files = [...new Set(supplied.length ? supplied : defaults)];
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const started = new Date().toISOString();
const checks = [];
async function verify(file, method = 'GET') {
  const local = path.resolve(root, file);
  if (!local.startsWith(root + path.sep)) throw Error('Invalid local path');
  const url = new URL(file, base).href;
  try {
    const res = await fetch(url, {method, redirect:'error', signal:AbortSignal.timeout(20000), headers:{'Cache-Control':'no-cache'}});
    const item = {file, url, method, status:res.status, content_type:res.headers.get('content-type')};
    if (method === 'GET') {
      const bytes = Buffer.from(await res.arrayBuffer());
      item.remote_sha256 = hash(bytes);
      item.local_sha256 = hash(fs.readFileSync(local));
      item.bytes = bytes.length;
      item.passed = res.status === 200 && item.remote_sha256 === item.local_sha256;
    } else {
      item.passed = res.status === 200;
    }
    checks.push(item);
  } catch (error) { checks.push({file, url, method, passed:false, error:error.message}); }
}
(async () => {
  // Keep requests bounded; this is an availability and integrity check, not a load test.
  for (let i = 0; i < files.length; i += 6) await Promise.all(files.slice(i, i + 6).map(f => verify(f)));
  if (!supplied.length) for (const id of ['S01','S02','S03','S04','S05','S06']) {
    await verify(`raw/${id}/original.${['S01','S02','S03'].includes(id)?'pdf':'html'}`, 'HEAD');
  }
  const failures = checks.filter(c => !c.passed);
  const report = {started_at:started, checked_at:new Date().toISOString(), base:base.href,
    mode:'Public HTTPS requests without authentication; GET compares SHA-256 with local bytes; HEAD checks source availability',
    checks, failures, passed:failures.length === 0};
  if (output) {
    fs.mkdirSync(path.dirname(output), {recursive:true});
    fs.writeFileSync(output, JSON.stringify(report, null, 2));
  }
  console.log(JSON.stringify({checked_at:report.checked_at, checks:checks.length, failures, output:output ? path.relative(root,output) : 'stdout only'}));
  if (failures.length) process.exitCode = 1;
})();
