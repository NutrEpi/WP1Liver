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

## DMGs for L3:L1
We identified 1997 DMGs for L2:L1. We defined DMGs as the genes that required the following condition.
1. A gene has at least one DMC in its gene body, promoter or flanking region.
2. Only the DMCs for L3:L1 were considered

## Page links
- [What are DMGs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DMGs L2:L1]({{ site.baseurl }}/docs/dmg-l2l1/){: .btn}

## List of the DMGs between L1 and L3 diets

{% include datatable.html id=page.datatable.id
  data=site.data.dmgl3l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}

{% include widepage_buttons.html previous=page.buttons.previous
  next=page.buttons.next %}
