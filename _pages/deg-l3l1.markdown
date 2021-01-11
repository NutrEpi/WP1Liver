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
Brief summary of L3:L1 DEGs.

## List of the DEGs between L1 and L3 diets

{% include datatable.html id=page.datatable.id
  data=site.data.degl3l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}
