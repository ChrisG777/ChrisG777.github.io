#!/usr/bin/env python3
"""Convert React distillations to al-folio blog posts."""

import json
import os
import re
import shutil
import yaml

BACKUP_DIR = os.path.expanduser("~/site-backup-react")
DISTILLATIONS_JSON = os.path.join(BACKUP_DIR, "distillations.json")
MD_DIR = os.path.join(BACKUP_DIR, "distillations")
IMG_DIR = os.path.join(BACKUP_DIR, "distillations", "images")

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_POSTS = os.path.join(REPO_DIR, "_posts")
OUT_IMG = os.path.join(REPO_DIR, "assets", "img", "distillations")


def sanitize_slug(slug):
    """Remove +, (, ) from slug for Jekyll filename compatibility."""
    slug = slug.replace("+", "")
    slug = slug.replace("(", "").replace(")", "")
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def rewrite_image_paths(content, original_slug, sanitized_slug):
    """Rewrite ![...](filename.png) to use al-folio image path."""
    def replacer(match):
        prefix = match.group(1)  # everything before ![
        alt = match.group(2)
        src = match.group(3)
        if src.startswith("http://") or src.startswith("https://"):
            return match.group(0)
        return f"{prefix}![{alt}](/assets/img/distillations/{sanitized_slug}/{src})"

    # Match optional link prefix [![...](...) and standalone ![](...)
    # This handles both ![](file.png) and [![](file.png)](url)
    return re.sub(r"((?:\[)?)!\[([^\]]*)\]\(([^)]+)\)", replacer, content)


def build_frontmatter(entry):
    """Build Jekyll frontmatter dict from distillation entry."""
    tags = list(entry.get("tags", []) or [])
    if entry.get("readInFull") is False:
        tags.append("partial-read")

    fm = {
        "layout": "post",
        "title": entry["title"],
        "date": entry["dateRead"],
        "description": entry.get("summaryTitle", ""),
        "tags": tags,
        "categories": ["distillation"],
        "giscus_comments": False,
        "related_posts": False,
    }
    if entry.get("url"):
        fm["paper_url"] = entry["url"]
    if entry.get("institutions"):
        fm["institutions"] = entry["institutions"]
    if entry.get("paperDate"):
        fm["paper_date"] = entry["paperDate"]

    return fm


def frontmatter_to_yaml(fm):
    """Serialize frontmatter to YAML string."""
    return yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)


def migrate():
    os.makedirs(OUT_POSTS, exist_ok=True)
    os.makedirs(OUT_IMG, exist_ok=True)

    with open(DISTILLATIONS_JSON, "r") as f:
        entries = json.load(f)

    print(f"Migrating {len(entries)} distillations...")
    migrated = 0
    errors = []

    for entry in entries:
        slug = entry["slug"]
        sanitized = sanitize_slug(slug)
        date = entry["dateRead"]

        # Read markdown content
        md_path = os.path.join(MD_DIR, f"{slug}.md")
        if not os.path.exists(md_path):
            errors.append(f"Missing markdown: {md_path}")
            continue

        with open(md_path, "r") as f:
            content = f.read()

        # Rewrite image paths
        content = rewrite_image_paths(content, slug, sanitized)

        # Build frontmatter
        fm = build_frontmatter(entry)
        fm_yaml = frontmatter_to_yaml(fm)

        # Write post file
        post_filename = f"{date}-{sanitized}.md"
        post_path = os.path.join(OUT_POSTS, post_filename)

        with open(post_path, "w") as f:
            f.write("---\n")
            f.write(fm_yaml)
            f.write("---\n\n")
            f.write(content)

        # Copy images
        img_src = os.path.join(IMG_DIR, slug)
        img_dst = os.path.join(OUT_IMG, sanitized)
        if os.path.isdir(img_src):
            if os.path.exists(img_dst) and sanitized != slug:
                # Merge images if slug was sanitized and dir already exists
                for img_file in os.listdir(img_src):
                    shutil.copy2(os.path.join(img_src, img_file), img_dst)
            else:
                shutil.copytree(img_src, img_dst, dirs_exist_ok=True)

        migrated += 1

    print(f"Successfully migrated {migrated} posts to {OUT_POSTS}")
    if errors:
        print(f"Errors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")

    # Verify: check that image references in posts point to existing files
    print("\nVerifying image references...")
    missing_images = []
    for post_file in os.listdir(OUT_POSTS):
        post_path = os.path.join(OUT_POSTS, post_file)
        with open(post_path, "r") as f:
            post_content = f.read()

        for match in re.finditer(r"!\[[^\]]*\]\((/assets/img/distillations/[^)]+)\)", post_content):
            img_path = os.path.join(REPO_DIR, match.group(1).lstrip("/"))
            if not os.path.exists(img_path):
                missing_images.append(f"{post_file}: {match.group(1)}")

    if missing_images:
        print(f"Missing images ({len(missing_images)}):")
        for m in missing_images[:20]:
            print(f"  - {m}")
        if len(missing_images) > 20:
            print(f"  ... and {len(missing_images) - 20} more")
    else:
        print("All image references verified!")


if __name__ == "__main__":
    migrate()
