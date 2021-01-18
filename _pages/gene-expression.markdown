---
permalink: /docs/gene-expression/
layout: single
sidebar:
  nav: "docs"
toc: true
toc_sticky: true
comments: true
share: true
title:  "Summary of gene expression analysis"
categories: summary gene-expression deg
---
A brief summary of our RNA-seq analysis.

## RNA-seq

We used RNA sequencing (RNA-seq) - high-throughput sequence technology based on next-generation sequencing (NGS) - to analyse the transcriptome profiles affected by our experimental feed with different micronutrient compositions.

## RNA-seq samples
We collected 18 liver samples at the final harvest stage for RNA-seq.

{% capture feed_groups %}
- **L1 diet**: 6 samples
- **L2 diet**: 6 samples
- **L3 diet**: 6 samples
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">The number of samples for each group</h4>
  {{ feed_groups | markdownify }}
</div>

{% include datatable_sortonly.html id='table_rnaseq'
  data=site.data.rnaseq_samples nrow=18 %}

## Bioinformatics pipelne for RNA-seq
We used various bioinformatics algorithms and methods to analyse our RNA-seq samples.
The following tools were those we used in our main RNA-seq pipeline.
- [cutadapt](https://cutadapt.readthedocs.io/en/stable/){: .btn} (quality control)
- [MultiQC](https://multiqc.info/){: .btn} (quality control report)
- [HISAT2](http://daehwankimlab.github.io/hisat2/){: .btn} (read alignment)
- [featureCounts](http://daehwankimlab.github.io/hisat2/){: .btn} (quantification)
- [DESeq2](https://bioconductor.org/packages/DESeq2/){: .btn} (differential expression analysis)

## Results
### Overall diet effect
Clustering analysis clearly separates our 12 liver samples into three groups by diet with L2 being in the middle.
<figure>
    <img src="{{ site.baseurl }}/assets/images/pca_liver_top500.svg" alt="PCA bi-plot for RNA-seq samples" >
    <figcaption>PCA (principal component analysis) bi-plot with top 500 high variance genes of RNA-seq counts with VST (variance stabilization transformation).</figcaption>
</figure>

### Differentially expressed genes
L3 diet affected gene expression profiles more than L2 diet in terms of the number of DEGs.

{% capture degs %}
- **L2 vs. L1**: 74 DEGs
- **L3 vs. L1**: 245 DEGs
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Identified DEGs for L2:L1 and L3:L1</h4>
  {{ degs | markdownify }}
</div>

<figure class="half">
    <img src="{{ site.baseurl }}/assets/images/volcate_l1l2_a.svg" alt="Violin plot of L2:L1 DEGs">
    <img src="{{ site.baseurl }}/assets/images/volcate_l1l3_a.svg" alt="Violin plot of L3:L1 DEGs">
    <figcaption>Body weights and HSI at smolt and final harvest stages.</figcaption>
</figure>

See [What are DEGs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn} for more details about DEGs.

### Significantly affected biological pathways
Gene expression patterns in lipid metabolism were affected in a dose dependant manner (L3 < L2 < L1).

[GSEA](https://www.gsea-msigdb.org/gsea/index.jsp){: .btn} (gene set enrichment analysis) showed
that most [KEGG](https://www.genome.jp/kegg/){: .btn} (Kyoto Encyclopedia of Genes and Genomes
) enriched pathways were down-regulated by micronutrient supplements.

{% include table.html id='table_rnaseq_gsea' data=site.data.rnaseq_gsea
   caption='Enriched KEGG pathways by GSEA (gene set enrichment analysis).' %}

## Page links
*Overview*
- [Project summary]({{ site.baseurl }}/docs/project-summary/){: .btn}
- [DNA methylation]({{ site.baseurl }}/docs/dna-methylation/){: .btn}

*DEG: differentially expressed gene*
- [What are DEGs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DEGs L2:L1]({{ site.baseurl }}/docs/degl2l1/){: .btn}
- [DEGs L3:L1]({{ site.baseurl }}/docs/degl3l1/){: .btn}
