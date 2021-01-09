---
permalink: /docs/dmc-l2l1/
layout: splash
title:  "Differentially methylated CpG sites - L2 vs. L1"
categories: dna-methylation dmc l2l1
datatable:
  id: dmcl3l1
  nrow: 2525
  nowrap: "Q-value"
buttons:
  previous: "/docs/differentially-methylated-cpg-site/"
  next: "/docs/dmc-l3l1/"
---

# {{ page.title }}

{% include widepage_buttons.html previous=page.buttons.previous
  next=page.buttons.next %}

Brief summary of L2:L1 DMCs.

## List of the DMCs between L1 and L2 diets

{% include datatable.html id=page.datatable.id
  data=site.data.dmcl2l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}

{% include widepage_buttons.html previous=page.buttons.previous
  next=page.buttons.next %}
