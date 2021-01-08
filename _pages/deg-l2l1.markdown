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

## List of DEGs between L1 and L3 diets

Need to use a JS table here.

<table id="degl2l1" class="display">
  {% for row in site.data.authors %}
    {% if forloop.first %}
    <thead> <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
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
const dataTable = new DataTable("#degl2l1");
</script>
