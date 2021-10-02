---
title: "Refactoring"
layout: archive
permalink: /dev/refactoring/
author_profile: true
sidebar:
  title: "All Posts"
  nav: "side"

---

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% assign posts = site.categories.Refactoring %}
{% for post in posts %} {% include archive-single.html type=entries_layout %} {% endfor %}
