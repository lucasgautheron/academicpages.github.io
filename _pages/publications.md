---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can find my articles on <u><a href="https://scholar.google.com/citations?user=oyl_rgUAAAAJ">my Google Scholar profile</a>.</u>
Publication records include self-assessed <a href="https://credit.niso.org/">CRediT</a> statements characterizing my areas of contribution. Hover <img src="{{ base_path }}/images/question.svg" style="display:inline; height:1em" title="Show abstract" /> icons to show the abstract.

{% assign tags = "" | split: ',' %}

{% for post in site.publications %}
  {% if post.tags %}
    {% for tag in post.tags %}
      {% assign filteredArray = tags | where: 'tag', tag.tag %}
      {% if filteredArray.size == 0 %}
        {% assign tags = tags | push: tag %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" type="text/javascript"></script>
<script type="text/javascript">
$(document).ready(function () {
  alert("hi");
  {% for tag in tags %}
    $("#toggle-{{ tag.id }}").click(function () {
      target = "ul li.publication:not(:has(div span.{{ tag.id }}))";

      if ($("#toggle-{{ tag.id }}").css('background-color') == 'gray') {
        $("#toggle-{{ tag.id }}").css('background-color', '');
        $("#toggle-{{ tag.id }}").css('color', '');
        $(target).show();
      } else {
        $("#toggle-{{ tag.id }}").css('background-color', 'gray');
        $("#toggle-{{ tag.id }}").css('color', 'white');
        $(target).hide();
      }
    });
    
  {% endfor %}
});
</script>

<div id="pubs">
{% for tag in tags %}
<div style="white-space:nowrap; display: inline-block;">
  <span id="toggle-{{ tag.id }}" class="publication_tag {{ tag.id }}" style="background-color: {{ tag.color }}; color: {{ tag.text_color }};">{{ tag.tag }}</span>
</div>
{% endfor %}

{% include base_path %}

<h3>Preprints</h3>

<ul>
{% for post in site.publications reversed %}
  {% if post.type contains "preprints" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

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

<h4>Invited Talks</h4>
<ul>
{% for post in site.publications reversed %}
  {% if post.type contains "invitedtalks" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

<h4>Contributed Talks</h4>
<ul>
{% for post in site.publications reversed %}
  {% if post.type contains "contributedtalks" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
</ul>

<h3>Selected press articles</h3>

<ul>
{% for post in site.publications reversed %}
  {% if post.type contains "press" %}
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

</div>