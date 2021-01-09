---
permalink: /docs/dmg-l2l1/
layout: splash
title:  "Differentially methylated genes - L2 vs. L1"
categories: dna-methylation dmg l2l1
datatable:
  id: dmgl2l1
  nrow: 1998
buttons:
  previous: "/docs/differentially-methylated-gene/"
  next: "/docs/dmg-l3l1/"
---

# {{ page.title }}

{% include widepage_buttons.html previous=page.buttons.previous
  next=page.buttons.next %}

Brief summary of L2:L1 DMGs.

## List of the DMGs between L1 and L2 diets

{% include datatable.html id=page.datatable.id
  data=site.data.dmgl2l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}

{% include widepage_buttons.html previous=page.buttons.previous
  next=page.buttons.next %}
