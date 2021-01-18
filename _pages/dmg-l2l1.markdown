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

## DMGs for L2:L1
We identified 1998 DMGs for L2:L1. We defined DMGs as the genes that required the following conditions.
1. A gene has at least one DMC in its gene body, promoter or flanking region.
2. Only the DMCs for L2:L1 were considered

## Page links
- [What are DMGs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DMGs L3:L1]({{ site.baseurl }}/docs/dmg-l3l1/){: .btn}

## List of the DMGs between L1 and L2 diets

{% include datatable.html id=page.datatable.id
  data=site.data.dmgl2l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}

{% include widepage_buttons.html previous=page.buttons.previous
  next=page.buttons.next %}
