---
title: "Operating Systems"
layout: archive
permalink: /os/synchronization/
author_profile: true
sidebar:
  title: "All Posts"
  nav: "side"

---

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% assign posts = site.categories.Synchronization %}
{% for post in posts %} {% include archive-single.html type=entries_layout %} {% endfor %}
