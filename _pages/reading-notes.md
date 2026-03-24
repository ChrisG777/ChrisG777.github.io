---
layout: default
permalink: /reading-notes/
title: reading notes
nav: true
nav_order: 3
---

<style>
.rn-controls {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}
.rn-search {
  flex: 1;
  min-width: 200px;
  padding: 0.5rem 0.75rem;
  border: 1px solid var(--global-divider-color);
  border-radius: 6px;
  font-size: 0.9rem;
  font-family: inherit;
  background: var(--global-bg-color);
  color: var(--global-text-color);
  outline: none;
  transition: border-color 0.15s ease;
}
.rn-search:focus {
  border-color: var(--global-theme-color);
}
.rn-sort {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
  color: var(--global-text-color-light);
}
.rn-sort select {
  padding: 0.4rem 0.6rem;
  border: 1px solid var(--global-divider-color);
  border-radius: 6px;
  font-size: 0.85rem;
  font-family: inherit;
  background: var(--global-bg-color);
  color: var(--global-text-color);
  cursor: pointer;
}
.rn-count {
  font-size: 0.85rem;
  color: var(--global-text-color-light);
  margin: 0 0 1rem;
}
.rn-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.rn-card {
  display: block;
  padding: 1rem 1.25rem;
  background: var(--global-bg-color);
  border: 1px solid var(--global-divider-color);
  border-radius: 8px;
  color: inherit;
  transition: border-color 0.15s ease;
}
.rn-card:hover {
  border-color: var(--global-theme-color);
}
.rn-card a {
  color: var(--global-theme-color);
  text-decoration: none;
}
.rn-card a:hover {
  text-decoration: underline;
}
.rn-card-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1rem;
}
.rn-card-title {
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
  color: var(--global-text-color);
  line-height: 1.4;
}
.rn-card-year {
  font-size: 0.8rem;
  color: var(--global-text-color-light);
  white-space: nowrap;
}
.rn-card-subtitle {
  display: block;
  margin-top: 0.15rem;
  font-size: 0.85rem;
  color: var(--global-text-color-light);
  font-style: italic;
}
.rn-card-institutions {
  display: block;
  margin-top: 0.25rem;
  font-size: 0.85rem;
  color: var(--global-text-color-light);
}
.rn-card-tags {
  display: flex;
  gap: 0.35rem;
  margin-top: 0.5rem;
  flex-wrap: wrap;
}
.rn-tag {
  font-size: 0.75rem;
  padding: 0.15rem 0.5rem;
  background: var(--global-divider-color);
  color: var(--global-text-color-light);
  border-radius: 4px;
}
.rn-tag-partial {
  background: #fef3c7;
  color: #92400e;
}
.rn-card-meta {
  display: flex;
  gap: 1rem;
  margin-top: 0.35rem;
  font-size: 0.8rem;
  color: var(--global-text-color-light);
}
</style>

<div class="post">
  <header class="post-header">
    <h1 class="post-title">{{ site.blog_name }}</h1>
    <p class="post-description">{{ site.blog_description }}</p>
  </header>

  <div class="rn-controls">
    <input type="text" class="rn-search" id="rn-search" placeholder="Search papers...">
    <div class="rn-sort">
      <label>Filter by:</label>
      <select id="rn-filter">
        <option value="">All</option>
      </select>
    </div>
    <div class="rn-sort">
      <label>Sort by:</label>
      <select id="rn-sort">
        <option value="dateRead">Date Read</option>
        <option value="paperDate">Paper Date</option>
        <option value="title">Title</option>
      </select>
    </div>
  </div>

  <p class="rn-count" id="rn-count"></p>

  <div class="rn-list" id="rn-list"></div>
</div>

<script>
(function() {
  var posts = [
    {% for post in site.posts %}
      {% if post.categories contains "distillation" %}
      {
        title: {{ post.title | jsonify }},
        subtitle: {{ post.description | jsonify }},
        url: {{ post.url | relative_url | jsonify }},
        dateRead: {{ post.date | date: "%Y-%m-%d" | jsonify }},
        paperDate: {{ post.paper_date | jsonify }},
        paperUrl: {{ post.paper_url | jsonify }},
        institutions: {{ post.institutions | default: "" | jsonify }},
        tags: {{ post.tags | default: "" | jsonify }}
      }{% unless forloop.last %},{% endunless %}
      {% endif %}
    {% endfor %}
  ];

  var total = posts.length;

  // Collect unique institutions and tags
  var instSet = {};
  var tagSet = {};
  posts.forEach(function(p) {
    if (p.institutions) p.institutions.forEach(function(i) { instSet[i] = true; });
    if (p.tags) p.tags.forEach(function(t) { tagSet[t] = true; });
  });
  var allInstitutions = Object.keys(instSet).sort();
  var allTags = Object.keys(tagSet).sort();

  // Build filter dropdown with optgroups
  var filterEl = document.getElementById('rn-filter');

  // Read status group
  var statusGroup = document.createElement('optgroup');
  statusGroup.label = 'Read status';
  var fullOpt = document.createElement('option');
  fullOpt.value = 'status:full';
  fullOpt.textContent = 'Fully read';
  statusGroup.appendChild(fullOpt);
  filterEl.appendChild(statusGroup);

  if (allInstitutions.length > 0) {
    var instGroup = document.createElement('optgroup');
    instGroup.label = 'Institution';
    allInstitutions.forEach(function(inst) {
      var opt = document.createElement('option');
      opt.value = 'inst:' + inst;
      opt.textContent = inst;
      instGroup.appendChild(opt);
    });
    filterEl.appendChild(instGroup);
  }

  // Filter out "partial-read" from displayed tags
  var displayTags = allTags.filter(function(t) { return t !== 'partial-read'; });
  if (displayTags.length > 0) {
    var tagGroup = document.createElement('optgroup');
    tagGroup.label = 'Tag';
    displayTags.forEach(function(tag) {
      var opt = document.createElement('option');
      opt.value = 'tag:' + tag;
      opt.textContent = tag;
      tagGroup.appendChild(opt);
    });
    filterEl.appendChild(tagGroup);
  }

  document.getElementById('rn-search').addEventListener('input', render);
  document.getElementById('rn-sort').addEventListener('change', render);
  document.getElementById('rn-filter').addEventListener('change', render);

  function formatDate(d) {
    if (!d) return '';
    var parts = d.split('-');
    if (parts.length === 1) return parts[0];
    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    return months[parseInt(parts[1], 10) - 1] + ' ' + parts[0];
  }

  function render() {
    var q = document.getElementById('rn-search').value.toLowerCase().trim();
    var sortBy = document.getElementById('rn-sort').value;

    var filterVal = document.getElementById('rn-filter').value;

    var filtered = posts.filter(function(p) {
      if (q) {
        var haystack = (p.title + ' ' + p.subtitle + ' ' + (p.institutions || []).join(' ') + ' ' + (p.tags || []).join(' ')).toLowerCase();
        if (haystack.indexOf(q) === -1) return false;
      }
      if (filterVal) {
        var parts = filterVal.split(':');
        var type = parts[0];
        var value = parts.slice(1).join(':');
        if (type === 'inst') {
          if (!p.institutions || p.institutions.indexOf(value) === -1) return false;
        } else if (type === 'tag') {
          if (!p.tags || p.tags.indexOf(value) === -1) return false;
        } else if (type === 'status' && value === 'full') {
          if (p.tags && p.tags.indexOf('partial-read') !== -1) return false;
        }
      }
      return true;
    });

    filtered.sort(function(a, b) {
      if (sortBy === 'dateRead') return (b.dateRead || '').localeCompare(a.dateRead || '');
      if (sortBy === 'paperDate') return (b.paperDate || '').localeCompare(a.paperDate || '');
      if (sortBy === 'title') return a.title.localeCompare(b.title);
      return 0;
    });

    document.getElementById('rn-count').textContent = 'Showing ' + filtered.length + ' of ' + total + ' papers';

    var html = '';
    filtered.forEach(function(p) {
      html += '<div class="rn-card" onclick="window.location.href=\'' + p.url + '\'" style="cursor:pointer;">';
      html += '<div class="rn-card-header">';
      html += '<h3 class="rn-card-title">' + p.title + '</h3>';
      if (p.paperDate) html += '<span class="rn-card-year">Published ' + formatDate(p.paperDate) + '</span>';
      html += '</div>';
      if (p.subtitle && p.subtitle !== p.title) {
        html += '<span class="rn-card-subtitle">' + p.subtitle + '</span>';
      }
      if (p.institutions && p.institutions.length > 0) {
        html += '<span class="rn-card-institutions">' + p.institutions.join(', ') + '</span>';
      }
      html += '<div class="rn-card-meta">';
      if (p.dateRead) html += '<span>Read: ' + p.dateRead + '</span>';
      if (p.paperUrl) html += '<span><a href="' + p.paperUrl + '" onclick="event.stopPropagation();" target="_blank">Paper ↗</a></span>';
      html += '</div>';
      var displayTags = (p.tags || []).filter(function(t) { return t !== 'partial-read'; });
      var isPartial = p.tags && p.tags.indexOf('partial-read') !== -1;
      if (displayTags.length > 0 || isPartial) {
        html += '<div class="rn-card-tags">';
        if (isPartial) html += '<span class="rn-tag rn-tag-partial">Partial read</span>';
        displayTags.forEach(function(t) {
          html += '<span class="rn-tag">' + t + '</span>';
        });
        html += '</div>';
      }
      html += '</div>';
    });

    document.getElementById('rn-list').innerHTML = html;
  }

  render();
})();
</script>
