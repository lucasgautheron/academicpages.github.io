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
  var tag_state = {};

  {% for tag in tags %}
    tag_state["{{ tag.id }}"] = {
      color: "{{ tag.color }}",
      text_color: "{{ tag.text_color }}",
      selected: false
    };
  {% endfor %}

  function restore_tag_color(tag_id) {
    $("#toggle-" + tag_id + "").css('background-color', tag_state[tag_id].color);
    $("#toggle-" + tag_id + "").css('color', tag_state[tag_id].text_color);
  }

  function grayout_tag(tag_id) {
    $("#toggle-" + tag_id + "").css('background-color', 'rgb(164, 164, 164)');
    $("#toggle-" + tag_id + "").css('color', 'white');
  }

  function select_tag(tag_id) {
    tag_state[tag_id].selected = true;
    target = "ul li.publication:not(:has(div span." + tag_id + "))";
    $(target).hide();
  }

  function deselect_tag(tag_id) {
    tag_state[tag_id].selected = false;
    target = "ul li.publication:not(:has(div span." + tag_id + "))";
    $(target).show();
  }


  {% for tag in tags %}
    $("#toggle-{{ tag.id }}").click(function () {
      tag_id = "{{ tag.id }}";
      target = "ul li.publication:not(:has(div span.{{ tag.id }}))";

      tag_state[tag_id].selected = !tag_state[tag_id].selected;

      console.log(tag_id); 
      console.log(tag_state[tag_id].selected); 
      console.log($("#toggle-{{ tag.id }}").css('background-color')); 

      if (tag_state[tag_id].selected == true) {
        for (tag in tag_state) {
          if (tag_state[tag].selected == true) {
            deselect_tag(tag);
          }
        }
        select_tag(tag_id);
      } else {
        deselect_tag(tag_id);
      }

      n_selected = 0;
      for (tag in tag_state) {
        if (tag_state[tag].selected == true) {
          n_selected++;
        }
      }
      
      for (tag in tag_state) {
        if (n_selected == 0 || tag_state[tag].selected == true) {
          restore_tag_color(tag);
        }
        else {
          grayout_tag(tag);
        }
      }
      
    });
    
  {% endfor %}
});
</script>

{% for tag in tags %}
<div style="white-space:nowrap; display: inline-block;">
  <span id="toggle-{{ tag.id }}" class="publication_tag {{ tag.id }}" style="background-color: {{ tag.color }}; color: {{ tag.text_color }}; margin-right: 4px;">{{ tag.tag }}</span>
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