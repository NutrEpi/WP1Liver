---
permalink: /docs/deg-l3l1/
layout: single
classes: wide
sidebar:
  nav: "docs"
title:  "Differentially expressed genes - L3 vs. L1"
categories: gene-expression deg l3l1
datatable:
  id: degl3l1
  nrow: 245
  nowrap: "Adj p-val"
---

## DEGs for L2:L1
We identified 74 DEGs for L2:L1 when the following criteria were applied and L1 was used as control.
1. `abs(LFC) >= 0`
2. `Adjusted p-value < 0.05`

## Page links
- [What are DEGs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [List of DEGs - L2 vs. L1]({{ site.baseurl }}/docs/deg-l2l1/){: .btn}

## List of DEGs between L1 and L3 diets

{% include datatable.html id=page.datatable.id
  data=site.data.degl3l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}
