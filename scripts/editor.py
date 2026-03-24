#!/usr/bin/env python3
"""Dev-only editor for reading notes. Run alongside Jekyll serve.

Usage: python scripts/editor.py
Opens at http://localhost:5555/editor
"""

import http.server
import json
import os
import re
import base64
import urllib.parse
from pathlib import Path

PORT = 5555
REPO = Path(__file__).resolve().parent.parent
POSTS_DIR = REPO / "_posts"
IMG_DIR = REPO / "assets" / "img" / "distillations"


def parse_post(filepath):
    """Parse a Jekyll post file into metadata + content."""
    text = filepath.read_text()
    if not text.startswith("---"):
        return None
    end = text.index("---", 3)
    import yaml
    fm = yaml.safe_load(text[3:end])
    content = text[end + 3:].strip()
    return fm, content


def slug_from_filename(filename):
    """Extract slug from YYYY-MM-DD-slug.md"""
    m = re.match(r"\d{4}-\d{2}-\d{2}-(.+)\.md$", filename)
    return m.group(1) if m else filename.replace(".md", "")


def find_post(slug):
    """Find a post file by slug."""
    for f in POSTS_DIR.iterdir():
        if f.suffix == ".md" and slug_from_filename(f.name) == slug:
            return f
    return None


def list_posts():
    """List all distillation posts."""
    posts = []
    for f in sorted(POSTS_DIR.iterdir(), reverse=True):
        if not f.suffix == ".md":
            continue
        try:
            fm, _ = parse_post(f)
        except Exception:
            continue
        if fm and "distillation" in (fm.get("categories") or []):
            posts.append({
                "slug": slug_from_filename(f.name),
                "title": fm.get("title", ""),
                "summaryTitle": fm.get("description", ""),
                "dateRead": str(fm.get("date", ""))[:10],
                "paperDate": fm.get("paper_date", ""),
                "paperUrl": fm.get("paper_url", ""),
                "institutions": fm.get("institutions") or [],
                "tags": [t for t in (fm.get("tags") or []) if t != "partial-read"],
                "readInFull": "partial-read" not in (fm.get("tags") or []),
            })
    return posts


def save_post(data):
    """Save a post (create or update)."""
    import yaml

    slug = data["slug"]
    date_read = data.get("dateRead", "")
    if not date_read:
        from datetime import date
        date_read = date.today().isoformat()

    tags = list(data.get("tags") or [])
    if not data.get("readInFull", True) and "partial-read" not in tags:
        tags.append("partial-read")

    fm = {
        "layout": "post",
        "title": data["title"],
        "date": date_read,
        "description": data.get("summaryTitle", ""),
        "tags": tags,
        "categories": ["distillation"],
        "giscus_comments": False,
        "related_posts": False,
    }
    if data.get("paperUrl"):
        fm["paper_url"] = data["paperUrl"]
    if data.get("institutions"):
        fm["institutions"] = data["institutions"]
    if data.get("paperDate"):
        fm["paper_date"] = data["paperDate"]

    fm_yaml = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # Rewrite image paths in content
    content = data.get("content", "")

    # If editing, remove old file (date may have changed)
    old_file = find_post(slug)
    if old_file:
        old_file.unlink()

    filename = f"{date_read}-{slug}.md"
    filepath = POSTS_DIR / filename
    filepath.write_text(f"---\n{fm_yaml}---\n\n{content}\n")
    return {"ok": True, "file": str(filepath)}


def delete_post(slug):
    """Delete a post and its images."""
    f = find_post(slug)
    if f:
        f.unlink()
    img_dir = IMG_DIR / slug
    if img_dir.is_dir():
        import shutil
        shutil.rmtree(img_dir)
    return {"ok": True}


def upload_image(slug, filename, b64data):
    """Save an uploaded image."""
    img_dir = IMG_DIR / slug
    img_dir.mkdir(parents=True, exist_ok=True)
    img_path = img_dir / filename
    img_path.write_bytes(base64.b64decode(b64data))
    return {"ok": True, "path": f"/assets/img/distillations/{slug}/{filename}"}


EDITOR_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Reading Notes Editor</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f8fafc; color: #1e293b; }
.layout { display: flex; height: 100vh; }
.sidebar { width: 280px; background: #fff; border-right: 1px solid #e2e8f0; overflow-y: auto; padding: 1rem 0; flex-shrink: 0; }
.sidebar h3 { padding: 0 1rem; margin-bottom: 0.5rem; font-size: 0.9rem; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em; }
.sidebar-item { display: block; padding: 0.5rem 1rem; text-decoration: none; color: #334155; font-size: 0.85rem; border-left: 3px solid transparent; cursor: pointer; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.sidebar-item:hover { background: #f1f5f9; }
.sidebar-item.active { background: #eff6ff; border-left-color: #2563eb; color: #2563eb; font-weight: 600; }
.sidebar-item.new { color: #2563eb; font-weight: 600; }
.main { flex: 1; overflow-y: auto; padding: 2rem; }
.header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
.header h2 { font-size: 1.3rem; }
.actions { display: flex; gap: 0.5rem; }
.btn { padding: 0.4rem 1rem; border: 1px solid #e2e8f0; border-radius: 6px; background: #fff; font-size: 0.85rem; cursor: pointer; text-decoration: none; color: #334155; }
.btn:hover { background: #f1f5f9; }
.btn.save { background: #2563eb; color: #fff; border-color: #2563eb; }
.btn.save:hover { background: #1d4ed8; }
.btn.delete { color: #dc2626; border-color: #fecaca; }
.btn.delete:hover { background: #fef2f2; }
.msg { padding: 0.5rem 0.75rem; margin-bottom: 1rem; border-radius: 6px; font-size: 0.85rem; background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; }
.msg.err { background: #fef2f2; color: #991b1b; border-color: #fecaca; }
.fields { display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 1rem; }
.field label { display: block; font-size: 0.8rem; color: #64748b; margin-bottom: 0.25rem; font-weight: 500; }
.field input[type="text"], .field input[type="date"] { width: 100%; padding: 0.4rem 0.6rem; border: 1px solid #e2e8f0; border-radius: 6px; font-size: 0.9rem; font-family: inherit; }
.field input:focus { outline: none; border-color: #2563eb; }
.row { display: flex; gap: 0.75rem; }
.row .field { flex: 1; }
.checkbox-field { display: flex; align-items: center; gap: 0.4rem; padding-top: 1.2rem; }
.checkbox-field label { display: flex; align-items: center; gap: 0.4rem; font-size: 0.9rem; color: #334155; }
.content-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem; }
.content-header label { font-size: 0.8rem; color: #64748b; font-weight: 500; }
textarea { width: 100%; height: calc(100vh - 420px); min-height: 200px; padding: 0.75rem; border: 1px solid #e2e8f0; border-radius: 6px; font-family: 'SF Mono', 'Fira Code', monospace; font-size: 0.85rem; resize: vertical; line-height: 1.5; }
textarea:focus { outline: none; border-color: #2563eb; }
</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar" id="sidebar">
    <h3>Reading Notes</h3>
    <div class="sidebar-item new" onclick="newPost()">+ New</div>
  </aside>
  <div class="main">
    <div class="header">
      <h2 id="heading">New Reading Note</h2>
      <div class="actions">
        <button class="btn save" onclick="save()">Save</button>
        <button class="btn delete" id="deleteBtn" onclick="deletePost()" style="display:none">Delete</button>
      </div>
    </div>
    <div id="msg"></div>
    <div class="fields">
      <div class="field"><label>Paper Title</label><input type="text" id="f-title" placeholder="Full paper title"></div>
      <div class="field"><label>Summary Title (subtitle)</label><input type="text" id="f-summary" placeholder="Short name"></div>
      <div class="row">
        <div class="field"><label>Paper Date</label><input type="text" id="f-paperDate" placeholder="2025-06-12"></div>
        <div class="field"><label>Date Read</label><input type="text" id="f-dateRead" placeholder="2025-11-04"></div>
      </div>
      <div class="field"><label>Paper URL</label><input type="text" id="f-url" placeholder="https://arxiv.org/abs/..."></div>
      <div class="row">
        <div class="field"><label>Institutions (comma-separated)</label><input type="text" id="f-institutions" placeholder="MIT, Anthropic"></div>
        <div class="field checkbox-field"><label><input type="checkbox" id="f-readInFull" checked> Read in full</label></div>
      </div>
      <div class="field" id="slugField"><label>Slug (auto from title if empty)</label><input type="text" id="f-slug" placeholder="my-paper-slug"></div>
    </div>
    <div class="content-header">
      <label>Notes (Markdown)</label>
      <div class="actions">
        <button class="btn" onclick="document.getElementById('fileInput').click()">Upload Image</button>
        <input type="file" id="fileInput" accept="image/*" multiple style="display:none" onchange="handleFileUpload(event)">
      </div>
    </div>
    <textarea id="f-content" placeholder="Write your notes in markdown..." onpaste="handlePaste(event)"></textarea>
  </div>
</div>
<script>
var currentSlug = null;
var posts = [];

function $(id) { return document.getElementById(id); }

function genSlug(title) {
  return title.toLowerCase().replace(/[^a-z0-9\\s-]/g, ' ').replace(/\\s+/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '').substring(0, 80);
}

function showMsg(text, err) {
  var el = $('msg');
  el.innerHTML = '<div class="msg' + (err ? ' err' : '') + '">' + text + '</div>';
  setTimeout(function() { el.innerHTML = ''; }, 3000);
}

function loadList() {
  fetch('/api/list').then(r => r.json()).then(function(data) {
    posts = data;
    var html = '<h3>Reading Notes</h3><div class="sidebar-item new" onclick="newPost()">+ New</div>';
    data.forEach(function(p) {
      var cls = 'sidebar-item' + (p.slug === currentSlug ? ' active' : '');
      html += '<div class="' + cls + '" onclick="loadPost(\\'' + p.slug.replace(/'/g, "\\\\'") + '\\')" title="' + (p.title || '').replace(/"/g, '&quot;') + '">' + (p.summaryTitle || p.title) + '</div>';
    });
    $('sidebar').innerHTML = html;
  });
}

function newPost() {
  currentSlug = null;
  $('heading').textContent = 'New Reading Note';
  $('f-title').value = '';
  $('f-summary').value = '';
  $('f-paperDate').value = '';
  $('f-dateRead').value = '';
  $('f-url').value = '';
  $('f-institutions').value = '';
  $('f-readInFull').checked = true;
  $('f-slug').value = '';
  $('f-content').value = '';
  $('slugField').style.display = '';
  $('deleteBtn').style.display = 'none';
  loadList();
}

function loadPost(slug) {
  fetch('/api/get/' + slug).then(r => r.json()).then(function(data) {
    currentSlug = slug;
    $('heading').textContent = 'Edit: ' + (data.summaryTitle || data.title);
    $('f-title').value = data.title || '';
    $('f-summary').value = data.summaryTitle || '';
    $('f-paperDate').value = data.paperDate || '';
    $('f-dateRead').value = data.dateRead || '';
    $('f-url').value = data.paperUrl || '';
    $('f-institutions').value = (data.institutions || []).join(', ');
    $('f-readInFull').checked = data.readInFull !== false;
    $('f-slug').value = slug;
    $('f-content').value = data.content || '';
    $('slugField').style.display = 'none';
    $('deleteBtn').style.display = '';
    loadList();
  });
}

function save() {
  var slug = currentSlug || $('f-slug').value || genSlug($('f-title').value);
  if (!slug) { showMsg('Title or slug required', true); return; }
  var body = {
    slug: slug,
    title: $('f-title').value,
    summaryTitle: $('f-summary').value || $('f-title').value,
    paperDate: $('f-paperDate').value,
    dateRead: $('f-dateRead').value,
    paperUrl: $('f-url').value,
    institutions: $('f-institutions').value.split(',').map(s => s.trim()).filter(Boolean),
    readInFull: $('f-readInFull').checked,
    tags: [],
    content: $('f-content').value,
  };
  fetch('/api/save', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(body) })
    .then(r => r.json()).then(function(data) {
      if (data.ok) {
        showMsg('Saved!');
        currentSlug = slug;
        $('slugField').style.display = 'none';
        $('deleteBtn').style.display = '';
        loadList();
      } else { showMsg('Error: ' + (data.error || 'unknown'), true); }
    }).catch(e => showMsg('Error: ' + e.message, true));
}

function deletePost() {
  if (!currentSlug) return;
  if (!confirm('Delete "' + ($('f-title').value || currentSlug) + '"?')) return;
  fetch('/api/delete', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({slug: currentSlug}) })
    .then(r => r.json()).then(function(data) { if (data.ok) newPost(); });
}

function insertImage(filename, slug) {
  var ta = $('f-content');
  var pos = ta.selectionStart || ta.value.length;
  var before = ta.value.slice(0, pos);
  var after = ta.value.slice(pos);
  ta.value = before + '![](/assets/img/distillations/' + slug + '/' + filename + ')' + after;
  showMsg('Image uploaded: ' + filename);
}

function uploadFile(file) {
  var slug = currentSlug || $('f-slug').value || genSlug($('f-title').value);
  if (!slug) { showMsg('Set a title before uploading images', true); return; }
  var reader = new FileReader();
  reader.onload = function() {
    var b64 = reader.result.split(',')[1];
    var ext = file.name.split('.').pop().toLowerCase() || 'png';
    var filename = 'img-' + Date.now() + '.' + ext;
    fetch('/api/upload-image', { method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({slug: slug, filename: filename, data: b64})
    }).then(r => r.json()).then(function(data) { if (data.ok) insertImage(filename, slug); });
  };
  reader.readAsDataURL(file);
}

function handleFileUpload(e) {
  Array.from(e.target.files).forEach(function(f) { if (f.type.startsWith('image/')) uploadFile(f); });
  e.target.value = '';
}

function handlePaste(e) {
  var items = (e.clipboardData || {}).items;
  if (!items) return;
  for (var i = 0; i < items.length; i++) {
    if (items[i].type.startsWith('image/')) {
      e.preventDefault();
      uploadFile(items[i].getAsFile());
      break;
    }
  }
}

loadList();
</script>
</body>
</html>"""


class EditorHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        if path in ("/editor", "/editor/"):
            self._respond(200, "text/html", EDITOR_HTML)
        elif path == "/api/list":
            self._json(list_posts())
        elif path.startswith("/api/get/"):
            slug = path[len("/api/get/"):]
            f = find_post(slug)
            if not f:
                self._json({"error": "not found"}, 404)
                return
            fm, content = parse_post(f)
            self._json({
                "slug": slug,
                "title": fm.get("title", ""),
                "summaryTitle": fm.get("description", ""),
                "dateRead": str(fm.get("date", ""))[:10],
                "paperDate": fm.get("paper_date", ""),
                "paperUrl": fm.get("paper_url", ""),
                "institutions": fm.get("institutions") or [],
                "tags": [t for t in (fm.get("tags") or []) if t != "partial-read"],
                "readInFull": "partial-read" not in (fm.get("tags") or []),
                "content": content,
            })
        else:
            self._respond(404, "text/plain", "Not found")

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))

        if path == "/api/save":
            self._json(save_post(body))
        elif path == "/api/delete":
            self._json(delete_post(body["slug"]))
        elif path == "/api/upload-image":
            self._json(upload_image(body["slug"], body["filename"], body["data"]))
        else:
            self._json({"error": "not found"}, 404)

    def _respond(self, code, ctype, body):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body.encode() if isinstance(body, str) else body)

    def _json(self, data, code=200):
        self._respond(code, "application/json", json.dumps(data))

    def log_message(self, fmt, *args):
        print(f"[editor] {args[0]}")


if __name__ == "__main__":
    print(f"Editor running at http://localhost:{PORT}/editor")
    print("(Run alongside 'bundle exec jekyll serve' for live preview)")
    server = http.server.HTTPServer(("", PORT), EditorHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nEditor stopped.")
