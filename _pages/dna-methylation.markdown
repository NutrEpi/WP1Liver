---
permalink: /docs/dna-methylation/
layout: single
sidebar:
  nav: "docs"
toc: true
toc_sticky: true
comments: true
share: true
title:  "Summary of DNA methylation analysis"
categories: summary dna-methylation dmc dmg
---
Short description of our DNA methylation analysis.

## RRBS

We used RRBS (reduced representation bisulfite sequencing) to analyse the DNA methylation profiles affected by our experimental feed with different micronutrient compositions. RRBS utilises restriction enzymes to target CpG rich regions in the genome. We used two different enzymes for our RRBS analysis.

1. MspI (recognition sequence : `5' CCGG`)
2. TaqI (recognition sequence : `5' TCGA`)

## RRBS samples
21 liver samples were collected at the final harvest stage for RRBS sequencing.

- L1 diet: 9 samples
- L2 diet: 6 samples
- L3 diet: 6 samples

{% include datatable_sortonly.html id='table_rrbs'
  data=site.data.rrbs_samples nrow=21 %}

## Bioinformatics pipelne for RRBS
We used various bioinformatics algorithms and methods to analyse our RRBS samples.
The following tools were those we used in our main RRBS pipeline.
- [FastQC](https://cutadapt.readthedocs.io/en/stable/){: .btn} (quality control)
- [Trim Galore!](https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/){: .btn} (adapter trimming)
- [MultiQC](https://multiqc.info/){: .btn} (quality control report)
- [Bismark](https://www.bioinformatics.babraham.ac.uk/projects/bismark/){: .btn} (read alignment)
- [methylKit](https://bioconductor.org/packages/release/bioc/html/DESeq2.html){: .btn} (differential methylation analysis)

## Page links
*DMC: differentially methylated CpG site*
- [What are DMCs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DMCs L2:L1]({{ site.baseurl }}/docs/dmc-l2l1/){: .btn}
- [DMCs L3:L1]({{ site.baseurl }}/docs/dmc-l3l1/){: .btn}

*DMG: differentially methylated gene*
- [What are DMGs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DMGs L2:L1]({{ site.baseurl }}/docs/dmg-l2l1/){: .btn}
- [DMGs L3:L1]({{ site.baseurl }}/docs/dmg-l3l1/){: .btn}
