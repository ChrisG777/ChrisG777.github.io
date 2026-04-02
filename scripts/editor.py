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


EDITOR_HTML_PATH = Path(__file__).parent / "editor.html"


class EditorHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        if path in ("/editor", "/editor/"):
            self._respond(200, "text/html", EDITOR_HTML_PATH.read_text())
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
