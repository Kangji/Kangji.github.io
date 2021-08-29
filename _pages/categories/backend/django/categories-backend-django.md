---
title: "Django"
layout: archive
permalink: /backend/django/
author_profile: true

---

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% assign posts = site.categories.Django %}
{% for post in posts %} {% include archive-single.html type=entries_layout %} {% endfor %}
