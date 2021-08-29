---
title: "Backend"
layout: archive
permalink: /backend/
author_profile: true

---

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% assign posts = site.categories.Backend %}
{% for post in posts %} {% include archive-single.html type=entries_layout %} {% endfor %}
