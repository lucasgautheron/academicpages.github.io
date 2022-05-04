---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can find my articles on <u><a href="https://scholar.google.com/citations?user=oyl_rgUAAAAJ">my Google Scholar profile</a>.</u>

{% include base_path %}

<ul>
{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
<ul>
