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
  {% if "publications" in post.type %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

<h3>Peer-reviewed conference proceedings</h3>

<ul>
{% for post in site.publications reversed %}
{% if "conferenceproceedings" in post.type %}
  {% include archive-single.html %}
{% endif %}
{% endfor %}
</ul>

<h3>Talks</h3>

<h4>Contributed Talks</h4>
<ul>
{% for post in site.publications reversed %}
  {% if "contributedtalks" in post.type %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

<h4>Seminar Talks</h4>
<ul>
{% for post in site.publications reversed %}
  {% if "seminartalks" in post.type %}
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
