---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can find my articles on <u><a href="https://scholar.google.com/citations?user=oyl_rgUAAAAJ">my Google Scholar profile</a>.</u>
Publication records include self-assessed <a href="https://credit.niso.org/">CRediT</a> statements characterizing my areas of contribution.

{% include base_path %}

<h3>Peer-reviewed publications</h3>

<ul>
{% for post in site.publications reversed %}
  {% if post.type contains "publications" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

<h3>Peer-reviewed conference proceedings</h3>

<ul>
{% for post in site.publications reversed %}
{% if post.type contains "conferenceproceedings" %}
  {% include archive-single.html %}
{% endif %}
{% endfor %}
</ul>

<h3>Talks</h3>

<h4>Contributed Talks</h4>
<ul>
{% for post in site.publications reversed %}
  {% if post.type contains "contributedtalks" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

<h4>Seminar Talks</h4>
<ul>
{% for post in site.publications reversed %}
  {% if post.type contains "seminartalks" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>
<h3>Other publications</h3>

<ul>
{% for post in site.publications reversed %}
  {% if post.type contains "other" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>
