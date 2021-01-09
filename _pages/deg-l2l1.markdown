---
permalink: /docs/deg-l2l1/
layout: single
classes: wide
sidebar:
  nav: "docs"
title:  "Differentially expressed genes - L2 vs. L1"
categories: gene-expression deg l2l1
---
Brief summary of L2:L1 DEGs.

## List of the DEGs between L1 and L2 diets

<table id="degl2l1" class="display">
  {% for row in site.data.degl2l1 %}
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
const dataTable = new DataTable("#degl2l1", {
    perPage: 74,
    layout: {
      top: "{search}",
      bottom: "{info}"
    },
});
</script>
