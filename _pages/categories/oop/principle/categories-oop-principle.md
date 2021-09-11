---
title: "OOP Principle"
layout: archive
permalink: /oop/principle/
author_profile: true
sidebar:
  title: "All Posts"
  nav: "side"

---

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% assign posts = site.categories['OOP Principle'] %}
{% for post in posts %} {% include archive-single.html type=entries_layout %} {% endfor %}
