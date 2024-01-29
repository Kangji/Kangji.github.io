---
title: Verilog
layout: archive
permalink: /verilog/
author_profile: true
sidebar:
  title: All Posts
  nav: side

---

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% assign posts = site.categories['Verilog'] %}
{% for post in posts %} {% include archive-single.html type=entries_layout %} {% endfor %}