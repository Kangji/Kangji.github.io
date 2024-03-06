---
title: Coq Spec
layout: archive
permalink: /coq/coq_spec/
author_profile: true
sidebar:
  title: All Posts
  nav: side

---

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% assign posts = site.categories['Coq Spec'] %}
{% for post in posts %} {% include archive-single.html type=entries_layout %} {% endfor %}