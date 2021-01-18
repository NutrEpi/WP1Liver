---
permalink: /docs/differentially-expressed-gene/
layout: single
sidebar:
  nav: "docs"
toc: true
toc_sticky: true
comments: true
share: true
title:  "What are DEGs?"
categories: summary gene-expression deg
---
DEG stands for differentially expressed gene. The difference of gene expression is statistically significant between treatment and control groups for each DEG.

## Treatment and control groups
We used three groups - L1, L2 and L3 diets - to calculate DEGs. L1 diet was used as control.

- L2:L1 - L2 vs. L1 with using L1 as control
- L3:L1 - L3 vs. L1 with using L1 as control

See [Experimental feed]({{ site.baseurl }}/docs/project-summary/#experimental-feed){: .btn} for details about L1, L2 and L3 groups.

## Statistical calculation
We used [DESeq2](https://bioconductor.org/packages/DESeq2/){: .btn} to calculate LFCs (log-fold changes) and adjusted p-values. Positive LFCs indicate up-regulation, whereas negative LFCs indicate down-regulation based on the L1 expression level. We used the following criteria to define our DEGs.

1. `abs(LFC) >= 0`
2. `Adjusted p-value < 0.05`

## Differentially expressed genes
L3 diet affected gene expression profiles more than L2 diet in terms of the number of DEGs.
- Identified 74 DEGs for L2:L1
- Identified 245 DEG sor L3:L1

<figure class="half">
    <img src="{{ site.baseurl }}/assets/images/volcate_l1l2_a.svg" alt="Violin plot of L2:L1 DEGs">
    <img src="{{ site.baseurl }}/assets/images/volcate_l1l3_a.svg" alt="Violin plot of L3:L1 DEGs">
    <figcaption>Body weights and HSI at smolt and final harvest stages.</figcaption>
</figure>

## Analysis of DEGs
We further analysed DEGs to understand the genetic regulations affected by micronutrients.
- ORA (over representation analysis) on [KEGG](https://www.genome.jp/kegg/) (Kyoto Encyclopedia of Genes and Genomes) pathways
- [GSEA](https://www.gsea-msigdb.org/gsea/index.jsp) (gene set enrichment analysis) on [KEGG](https://www.genome.jp/kegg/)
- ORA (over representation analysis) on [GO](http://geneontology.org/) (Gene Ontology) terms
- Linking with DNA methylation result

## List of DEGs with gene symbols and gene names
- [List of DEGs - L2 vs. L1]({{ site.baseurl }}/docs/deg-l2l1/){: .btn}
- [List of DEGs - L3 vs. L1]({{ site.baseurl }}/docs/deg-l3l1/){: .btn}
