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
Short description of our RNA-seq analysis.

## RNA-seq

We used RNA sequencing (RNA-seq) - high-throughput sequence technology based on next-generation sequencing (NGS) - to analyse the transcriptome profiles affected by our experimental feed with different micronutrient compositions.

## RNA-seq samples
18 liver samples were collected at the final harvest stage for RNA-seq.

- L1 diet: 6 samples
- L2 diet: 6 samples
- L3 diet: 6 samples

{% include datatable_sortonly.html id='table_rnaseq'
  data=site.data.rnaseq_samples nrow=18 %}

## Bioinformatics pipelne for RNA-seq
We used various bioinformatics algorithms and methods to analyse our RNA-seq samples.
The following tools were those we used in our main RNA-seq pipeline.
- [cutadapt](https://cutadapt.readthedocs.io/en/stable/){: .btn} (quality control)
- [MultiQC](https://multiqc.info/){: .btn} (quality control report)
- [HISAT2](http://daehwankimlab.github.io/hisat2/){: .btn} (read alignment)
- [featureCounts](http://daehwankimlab.github.io/hisat2/){: .btn} (quantification)
- [DESeq2](https://bioconductor.org/packages/release/bioc/html/DESeq2.html){: .btn} (differential expression analysis)

## Page links
*DEG: differentially expressed gene*
- [What are DEGs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DEGs L2:L1]({{ site.baseurl }}/docs/degl2l1/){: .btn}
- [DEGs L3:L1]({{ site.baseurl }}/docs/degl3l1/){: .btn}
