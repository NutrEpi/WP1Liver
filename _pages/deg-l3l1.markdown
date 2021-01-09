---
permalink: /docs/deg-l3l1/
layout: single
classes: wide
sidebar:
  nav: "docs"
title:  "Differentially expressed genes - L3 vs. L1"
categories: gene-expression deg l3l1
---
Brief summary of L3:L1 DEGs.

## List of the DEGs between L1 and L3 diets

<table id="degl3l1" class="display">
  {% for row in site.data.degl3l1 %}
    {% if forloop.first %}
    <thead> <tr>
      {% for pair in row %}
        {% if pair[0] == "Adj p-val" %}
          <th nowrap="nowrap">{{ pair[0] }}</th>
        {% else %}
          <th>{{ pair[0] }}</th>
        {% endif %}
      {% endfor %}
    </tr> </thead>
    <tbody>
    {% endif %}

    <tr>
    {% for pair in row %}
      <td>{{ pair[1] }}</td>
    {% endfor %}
    </tr>
  {% endfor %}
  </tbody>
</table>

<script>
const dataTable = new DataTable("#degl3l1", {
    perPage: 245,
    layout: {
      top: "{search}",
      bottom: "{info}"
    },
});
</script>
