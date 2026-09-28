---
layout: archive
title: "Projects & Writing"
permalink: /projects/
author_profile: true
---

{% include base_path %}

Class papers, data projects, and short essays, mostly on East Asian economics.

{% assign sections = "paper:Papers|data:Data Projects|essay:Essays" | split: "|" %}
{% assign all_projects = site.projects | sort: "date" | reverse %}

{% if all_projects.size == 0 %}
<p><em>First projects coming soon.</em></p>
{% endif %}

{% for section in sections %}
  {% assign parts = section | split: ":" %}
  {% assign entries = all_projects | where: "kind", parts[0] %}
  {% if entries.size > 0 %}
<h2>{{ parts[1] }}</h2>
    {% for post in entries %}
      {% include archive-single.html %}
    {% endfor %}
  {% endif %}
{% endfor %}
