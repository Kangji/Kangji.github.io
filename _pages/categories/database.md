---
title: Database
layout: archive
permalink: /database/
author_profile: true
sidebar:
  title: All Posts
  nav: side

---

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% assign posts = site.categories['Database'] %}
{% for post in posts %} {% include archive-single.html type=entries_layout %} {% endfor %}