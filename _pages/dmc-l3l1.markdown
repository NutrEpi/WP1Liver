---
permalink: /docs/dmc-l3l1/
layout: splash
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

# {{ page.title }}

{% include widepage_buttons.html previous=page.buttons.previous
  next=page.buttons.next %}

Brief summary of L3:L1 DMCs.

## List of the DMCs between L1 and L3 diets

{% include datatable.html id=page.datatable.id
  data=site.data.dmcl3l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}

{% include widepage_buttons.html previous=page.buttons.previous
  next=page.buttons.next %}
