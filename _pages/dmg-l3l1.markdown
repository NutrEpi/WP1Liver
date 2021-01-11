---
permalink: /docs/dmg-l3l1/
layout: splash
title:  "Differentially methylated genes - L3 vs. L1"
categories: dna-methylation dmg l3l1
datatable:
  id: dmgl3l1
  nrow: 1997
buttons:
  previous: "/docs/dmg-l2l1/"
  next: "/docs/downloads/"
---

# {{ page.title }}

{% include widepage_buttons.html previous=page.buttons.previous
  next=page.buttons.next %}

Brief summary of L3:L1 DMGs.

## List of the DMGs between L1 and L3 diets

{% include datatable.html id=page.datatable.id
  data=site.data.dmgl3l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}

{% include widepage_buttons.html previous=page.buttons.previous
  next=page.buttons.next %}
