---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can find my articles on <u><a href="https://scholar.google.com/citations?user=oyl_rgUAAAAJ">my Google Scholar profile</a>.</u>
Publication records include self-assessed <a href="https://www.elsevier.com/authors/policies-and-guidelines/credit-author-statement">CRediT</a> statements characterizing my areas of contribution.

{% include base_path %}

<h3>Peer-reviewed publications</h3>

<ul>
{% for post in site.publications reversed %}
  {% if post.type == "publication" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

<h3>Peer-reviewed conference proceedings</h3>

<ul>
{% for post in site.publications reversed %}
{% if post.type == "conference proceedings" %}
  {% include archive-single.html %}
{% endif %}
{% endfor %}
</ul>

<h3>Talks</h3>

<ul>
{% for post in site.publications reversed %}
  {% if post.type == "talk" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

<h3>Other publications</h3>

<ul>
{% for post in site.publications reversed %}
  {% if post.type != "publication" and post.type != "conference proceedings" and post.type != "talk" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>
