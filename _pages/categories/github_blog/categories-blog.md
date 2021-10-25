---
title: "Github Blog"
layout: archive
permalink: /blog/
author_profile: true
sidebar:
  title: "All Posts"
  nav: "side"

---

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% assign posts = site.categories['Github Blog'] %}
{% for post in posts %} {% include archive-single.html type=entries_layout %} {% endfor %}
