---
permalink: /docs/dmc-l3l1/
layout: single
classes: wide
sidebar:
  nav: "docs"
title:  "Differentially methylated CpG sites - L3 vs. L1"
categories: dna-methylation dmc l3l1
datatable:
  id: dmcl3l1
  nrow: 2555
  nowrap: "Q-value"
buttons:
  previous: "/docs/dmc-l2l1/"
  next: /docs/differentially-methylated-gene/
---

## DMCs for L3:L1
We identified 2555 DMCs for L3:L1 when the following criteria were applied and L1 was used as control.
1. `abs(percentage methylation difference) >= 20%`
2. `Q-value < 0.01`

## Page links
- [What are DMCs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DMCs L2:L1]({{ site.baseurl }}/docs/dmc-l2l1/){: .btn}

## Relevant Excel files
[Excel files (Downloads page)]({{ site.baseurl }}/docs/downloads/#9-excel-files-for-degs-dmcs-and-dmgs){: .btn} contain more information than the list presented here.

{% capture excel %}
- Dataset_04_CpG_L3L1.xlsx
{% endcapture %}

<div class="notice">
  {{ excel | markdownify }}
</div>

## List of the DMCs between L1 and L3 diets

{% include datatable.html id=page.datatable.id
  data=site.data.dmc.dmcl3l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}

{% include widepage_buttons.html previous=page.buttons.previous
  next=page.buttons.next %}
