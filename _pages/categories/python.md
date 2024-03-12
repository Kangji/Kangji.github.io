---
title: Python
layout: archive
permalink: /python/
author_profile: true
sidebar:
  title: All Posts
  nav: side

---

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% assign posts = site.categories['Python'] %}
{% for post in posts %} {% include archive-single.html type=entries_layout %} {% endfor %}