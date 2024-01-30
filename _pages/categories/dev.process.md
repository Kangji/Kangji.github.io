---
title: Process
layout: archive
permalink: /dev/process/
author_profile: true
sidebar:
  title: All Posts
  nav: side

---

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% assign posts = site.categories['Process'] %}
{% for post in posts %} {% include archive-single.html type=entries_layout %} {% endfor %}