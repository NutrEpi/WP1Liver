---
permalink: /docs/deg-l2l1/
layout: single
classes: wide
sidebar:
  nav: "docs"
title:  "Differentially expressed genes - L2 vs. L1"
categories: gene-expression deg l2l1
datatable:
  id: degl2l1
  nrow: 74
  nowrap: "Adj p-val"
---
Brief summary of L2:L1 DEGs.

## List of the DEGs between L1 and L2 diets

{% include datatable.html id=page.datatable.id
  data=site.data.degl2l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}
