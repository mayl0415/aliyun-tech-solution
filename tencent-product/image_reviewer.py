#!/usr/bin/env python3
"""
图片审核工具 - 浏览 Markdown 文件中的图片，标记保留或删除
用法: uv run python tencent-product/image_reviewer.py [port]
"""

import json
import re
import sys
import urllib.request
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import List, Dict

BASE_DIR = Path(__file__).parent

# ============================================================
# Core Functions
# ============================================================

def get_directories() -> List[Dict]:
    dirs = []
    for name in ['products', 'solutions']:
        d = BASE_DIR / name
        if d.exists():
            count = len(list(d.rglob('*.md')))
            dirs.append({'name': name, 'count': count})
    return dirs


def get_md_files(directory: str) -> List[Dict]:
    dir_path = BASE_DIR / directory
    if not dir_path.exists():
        return []
    files = []
    for md in sorted(dir_path.rglob('*.md')):
        with open(md, 'r', encoding='utf-8') as f:
            content = f.read()
        img_count = len(re.findall(r'!\[[^\]]*\]\(https?://[^)]+\)', content))
        files.append({
            'path': str(md.relative_to(BASE_DIR)),
            'name': md.stem,
            'category': md.parent.name if md.parent != dir_path else '',
            'image_count': img_count,
        })
    return files


def extract_images(filepath: str) -> List[Dict]:
    full_path = BASE_DIR / filepath
    if not full_path.exists():
        return []
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    images = []
    for match in re.finditer(r'!\[([^\]]*)\]\((https?://[^)]+)\)', content):
        images.append({'alt': match.group(1), 'url': match.group(2)})
    return images


def get_image_ext(url: str) -> str:
    path = urllib.parse.urlparse(url).path
    ext = Path(path).suffix.lower()
    return ext if ext in ['.png', '.jpg', '.jpeg', '.svg', '.webp'] else '.png'


def execute_review(filepath: str, keep_urls: List[str], delete_urls: List[str]) -> Dict:
    full_path = BASE_DIR / filepath
    md_stem = full_path.stem
    md_dir = full_path.parent

    saved = []
    errors = []
    url_to_local = {}

    for i, url in enumerate(keep_urls, 1):
        ext = get_image_ext(url)
        local_name = f"{md_stem}_{i}{ext}"
        local_path = md_dir / local_name
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Referer': 'https://cloud.tencent.com/',
            })
            with urllib.request.urlopen(req, timeout=20) as resp:
                with open(local_path, 'wb') as f:
                    f.write(resp.read())
            url_to_local[url] = local_name
            saved.append(local_name)
        except Exception as e:
            errors.append(f"{url}: {e}")

    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for url, local_name in url_to_local.items():
        content = content.replace(f']({url})', f']({local_name})')

    deleted_count = 0
    for url in delete_urls:
        pattern = rf'!\[[^\]]*\]\({re.escape(url)}\)\n*'
        new_content = re.sub(pattern, '', content)
        if new_content != content:
            deleted_count += 1
            content = new_content

    content = re.sub(r'\n{3,}', '\n\n', content)

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return {'saved': saved, 'deleted': deleted_count, 'errors': errors}


# ============================================================
# HTML Page
# ============================================================

HTML_PAGE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>图片审核工具</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:system-ui,-apple-system,sans-serif;display:flex;height:100vh;background:#f1f5f9;color:#1e293b}
.sidebar{width:300px;background:#1e293b;color:#e2e8f0;display:flex;flex-direction:column;flex-shrink:0}
.sidebar-hd{padding:14px 16px;border-bottom:1px solid #334155}
.sidebar-hd h2{font-size:16px;margin-bottom:10px;display:flex;align-items:center;gap:8px}
.sidebar-hd select{width:100%;padding:7px 8px;background:#334155;color:#e2e8f0;border:1px solid #475569;border-radius:6px;font-size:13px}
.file-list{flex:1;overflow-y:auto}
.cat-hd{padding:6px 16px;font-size:11px;color:#64748b;background:#0f172a;position:sticky;top:0;z-index:1}
.file-item{padding:7px 16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,0.04);font-size:13px;gap:8px}
.file-item:hover{background:#334155}
.file-item.active{background:#3b82f6}
.file-item.done{opacity:.4}
.file-item .name{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.badge{background:#475569;padding:1px 7px;border-radius:10px;font-size:11px;flex-shrink:0}
.badge.zero{background:transparent;color:#475569}
.stats{padding:10px 16px;font-size:12px;color:#64748b;border-top:1px solid #334155}

.main{flex:1;display:flex;flex-direction:column;min-width:0}
.toolbar{padding:10px 20px;background:#fff;border-bottom:1px solid #e2e8f0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}
.toolbar .info{font-size:14px;color:#64748b}
.toolbar .info strong{color:#1e293b}
.actions{display:flex;gap:8px;align-items:center}
.sel-count{font-size:13px;color:#64748b;margin-right:4px}
.btn{padding:6px 14px;border:none;border-radius:6px;cursor:pointer;font-size:13px;font-weight:500;transition:opacity .15s}
.btn:hover{opacity:.85}
.btn:disabled{opacity:.5;cursor:not-allowed}
.btn-default{background:#e2e8f0;color:#475569}
.btn-success{background:#22c55e;color:#fff}
.btn-danger{background:#ef4444;color:#fff}

.gallery{flex:1;overflow-y:auto;padding:16px;display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px;align-content:start}
.card{background:#fff;border-radius:10px;overflow:hidden;cursor:pointer;border:3px solid transparent;transition:all .15s;position:relative}
.card:hover{transform:translateY(-2px);box-shadow:0 4px 16px rgba(0,0,0,.08)}
.card.selected{border-color:#22c55e}
.card:not(.selected){opacity:.4;filter:grayscale(.6)}
.card-img{height:170px;overflow:hidden;background:#f8fafc;display:flex;align-items:center;justify-content:center}
.card-img img{max-width:100%;max-height:100%;object-fit:contain}
.card-check{position:absolute;top:8px;right:8px;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700}
.card.selected .card-check{background:#22c55e;color:#fff}
.card:not(.selected) .card-check{background:#e2e8f0;color:#94a3b8}
.card-ft{padding:5px 10px;font-size:11px;color:#94a3b8;display:flex;justify-content:space-between;align-items:center}
.card-ft .zoom{cursor:pointer;font-size:16px;line-height:1;padding:2px}
.card-ft .zoom:hover{transform:scale(1.2)}

.modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.85);z-index:100;align-items:center;justify-content:center}
.modal.show{display:flex}
.modal img{max-width:92vw;max-height:92vh;object-fit:contain;border-radius:4px}
.modal .close{position:absolute;top:16px;right:24px;font-size:36px;color:#fff;cursor:pointer;background:none;border:none;line-height:1}
.modal .close:hover{color:#f87171}

.empty{grid-column:1/-1;text-align:center;padding:80px 20px;color:#94a3b8;font-size:16px}
.empty .icon{font-size:48px;margin-bottom:12px}

.loading{grid-column:1/-1;text-align:center;padding:60px;color:#94a3b8}
.loading::after{content:'';display:inline-block;width:20px;height:20px;border:2px solid #cbd5e1;border-top-color:#3b82f6;border-radius:50%;animation:spin .6s linear infinite;margin-left:8px;vertical-align:middle}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>

<div class="sidebar">
  <div class="sidebar-hd">
    <h2>图片审核工具</h2>
    <select id="dirSelect" onchange="selectDir(this.value)">
      <option value="">选择目录...</option>
    </select>
  </div>
  <div class="file-list" id="fileList"></div>
  <div class="stats" id="stats"></div>
</div>

<div class="main">
  <div class="toolbar">
    <div class="info" id="fileInfo">选择一个文件开始审核</div>
    <div class="actions" id="actions" style="display:none">
      <span class="sel-count" id="selCount"></span>
      <button class="btn btn-default" onclick="selectAll()">全选</button>
      <button class="btn btn-default" onclick="selectNone()">全不选</button>
      <button class="btn btn-success" id="execBtn" onclick="execute()">保留选中 &amp; 删除其余</button>
    </div>
  </div>
  <div class="gallery" id="gallery">
    <div class="empty"><div class="icon">🖼</div>从左侧选择文件开始审核图片</div>
  </div>
</div>

<div class="modal" id="modal" onclick="closePreview()">
  <button class="close" onclick="closePreview()">&times;</button>
  <img id="modalImg" onclick="event.stopPropagation()">
</div>

<script>
let currentDir = '', currentFile = '', currentFileIndex = -1;
let files = [], images = [], selected = new Set();

async function api(url) { return (await fetch(url)).json(); }

async function init() {
  const dirs = await api('/api/dirs');
  const sel = document.getElementById('dirSelect');
  dirs.forEach(d => {
    const o = document.createElement('option');
    o.value = d.name; o.textContent = d.name + ' (' + d.count + ' files)';
    sel.appendChild(o);
  });
  if (dirs.length > 0) { sel.value = dirs[0].name; selectDir(dirs[0].name); }
}

async function selectDir(dir) {
  if (!dir) return;
  currentDir = dir;
  document.getElementById('fileList').innerHTML = '<div class="loading">加载中</div>';
  files = await api('/api/files?dir=' + encodeURIComponent(dir));
  renderFileList();
}

function renderFileList() {
  const el = document.getElementById('fileList');
  let html = '', lastCat = null;
  files.forEach((f, i) => {
    if (f.category !== lastCat) {
      html += '<div class="cat-hd">' + (f.category || '根目录') + '</div>';
      lastCat = f.category;
    }
    const cls = (f.image_count === 0 ? ' done' : '') + (f.path === currentFile ? ' active' : '');
    const bcls = f.image_count === 0 ? 'badge zero' : 'badge';
    html += '<div class="file-item' + cls + '" onclick="selectFile(' + i + ')" title="' + f.path + '">' +
      '<span class="name">' + f.name + '</span>' +
      '<span class="' + bcls + '">' + f.image_count + '</span></div>';
  });
  el.innerHTML = html;
  const total = files.length, done = files.filter(f => f.image_count === 0).length;
  document.getElementById('stats').textContent = '无远程图片: ' + done + ' / ' + total;
}

async function selectFile(index) {
  currentFileIndex = index;
  currentFile = files[index].path;
  document.getElementById('gallery').innerHTML = '<div class="loading">加载图片</div>';
  images = await api('/api/images?file=' + encodeURIComponent(currentFile));
  selected = new Set();
  document.getElementById('fileInfo').innerHTML = '<strong>' + files[index].name + '</strong> — ' + images.length + ' 张远程图片';
  document.getElementById('actions').style.display = images.length > 0 ? 'flex' : 'none';
  renderGallery();
  renderFileList();
  // Scroll active file into view
  const active = document.querySelector('.file-item.active');
  if (active) active.scrollIntoView({ block: 'nearest' });
}

function renderGallery() {
  const el = document.getElementById('gallery');
  if (images.length === 0) {
    el.innerHTML = '<div class="empty"><div class="icon">✅</div>没有远程图片</div>';
    updateCount(); return;
  }
  let html = '';
  images.forEach((img, i) => {
    const sel = selected.has(i) ? ' selected' : '';
    const chk = selected.has(i) ? '✓' : (i + 1);
    html += '<div class="card' + sel + '" onclick="toggle(' + i + ')">' +
      '<div class="card-img"><img src="' + img.url + '" loading="lazy" ' +
      'onerror="proxyFb(this,' + i + ')"></div>' +
      '<div class="card-check">' + chk + '</div>' +
      '<div class="card-ft"><span>#' + (i+1) + '</span>' +
      '<span class="zoom" onclick="event.stopPropagation();preview(' + i + ')">🔍</span></div></div>';
  });
  el.innerHTML = html;
  updateCount();
}

function proxyFb(el, i) {
  if (!el.dataset.r) { el.dataset.r = '1'; el.src = '/api/proxy?url=' + encodeURIComponent(images[i].url); }
}

function toggle(i) { if (selected.has(i)) selected.delete(i); else selected.add(i); renderGallery(); }
function selectAll() { images.forEach((_, i) => selected.add(i)); renderGallery(); }
function selectNone() { selected.clear(); renderGallery(); }

function updateCount() {
  document.getElementById('selCount').textContent = '已选 ' + selected.size + ' / ' + images.length;
}

async function execute() {
  const keepUrls = [], deleteUrls = [];
  images.forEach((img, i) => {
    if (selected.has(i)) keepUrls.push(img.url);
    else deleteUrls.push(img.url);
  });
  if (!confirm('保留 ' + keepUrls.length + ' 张图片（下载到本地），删除 ' + deleteUrls.length + ' 张图片引用，确认？')) return;

  const btn = document.getElementById('execBtn');
  btn.textContent = '处理中...'; btn.disabled = true;
  try {
    const r = await fetch('/api/execute', {
      method: 'POST', headers: {'Content-Type':'application/json'},
      body: JSON.stringify({file: currentFile, keep: keepUrls, delete: deleteUrls})
    });
    const res = await r.json();
    let msg = '完成！保存 ' + res.saved.length + ' 张，删除 ' + res.deleted + ' 个引用';
    if (res.errors.length > 0) msg += '\\n\\n下载失败 ' + res.errors.length + ' 张';
    alert(msg);

    files = await api('/api/files?dir=' + encodeURIComponent(currentDir));
    let next = currentFileIndex + 1;
    while (next < files.length && files[next].image_count === 0) next++;
    if (next < files.length) selectFile(next);
    else { renderFileList(); document.getElementById('gallery').innerHTML = '<div class="empty"><div class="icon">🎉</div>当前目录所有文件已审核！</div>'; document.getElementById('actions').style.display = 'none'; }
  } catch(e) { alert('失败: ' + e.message); }
  finally { btn.textContent = '保留选中 & 删除其余'; btn.disabled = false; }
}

function preview(i) {
  const url = images[i].url;
  const img = document.getElementById('modalImg');
  img.src = url;
  img.onerror = function() { if (!this.dataset.r) { this.dataset.r='1'; this.src='/api/proxy?url='+encodeURIComponent(url); } };
  document.getElementById('modal').classList.add('show');
}
function closePreview() { document.getElementById('modal').classList.remove('show'); }

document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closePreview();
  if (e.key === 'ArrowDown' && currentFileIndex < files.length - 1) { e.preventDefault(); selectFile(currentFileIndex + 1); }
  if (e.key === 'ArrowUp' && currentFileIndex > 0) { e.preventDefault(); selectFile(currentFileIndex - 1); }
});

init();
</script>
</body>
</html>"""


# ============================================================
# HTTP Server
# ============================================================

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        if path == '/':
            self._html(HTML_PAGE)
        elif path == '/api/dirs':
            self._json(get_directories())
        elif path == '/api/files':
            d = params.get('dir', [''])[0]
            self._json(get_md_files(d))
        elif path == '/api/images':
            f = params.get('file', [''])[0]
            self._json(extract_images(f))
        elif path == '/api/proxy':
            url = params.get('url', [''])[0]
            self._proxy(url)
        else:
            self.send_error(404)

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = json.loads(self.rfile.read(length)) if length else {}
        parsed = urllib.parse.urlparse(self.path)

        if parsed.path == '/api/execute':
            result = execute_review(
                body.get('file', ''),
                body.get('keep', []),
                body.get('delete', []),
            )
            self._json(result)
        else:
            self.send_error(404)

    def _json(self, data):
        payload = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', len(payload))
        self.end_headers()
        self.wfile.write(payload)

    def _html(self, content):
        payload = content.encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', len(payload))
        self.end_headers()
        self.wfile.write(payload)

    def _proxy(self, url):
        if not url:
            self.send_error(400)
            return
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Referer': 'https://cloud.tencent.com/',
            })
            with urllib.request.urlopen(req, timeout=15) as resp:
                ct = resp.headers.get('Content-Type', 'image/png')
                data = resp.read()
                self.send_response(200)
                self.send_header('Content-Type', ct)
                self.send_header('Content-Length', len(data))
                self.send_header('Cache-Control', 'public, max-age=86400')
                self.end_headers()
                self.wfile.write(data)
        except Exception:
            self.send_error(502)

    def log_message(self, format, *args):
        pass


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8899
    server = HTTPServer(('0.0.0.0', port), Handler)
    print(f"图片审核工具已启动: http://localhost:{port}")
    print("Ctrl+C 停止")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止")


if __name__ == '__main__':
    main()
