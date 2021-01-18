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
A brief summary of our DNA methylation analysis.

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

## Definition of genomic regions
Functions of DNA methylation can be different depending on the types of regions where methylation occurs.
We split the genome into seven different regions for our RRBS analysis.

1. Exon
2. Intron
3. P250 (proximal promoter)
4. P1K (promoter)
5. P6K (distal promoter)
6. Flanks (potential enhancer region)
7. IGR (intergenic region)

<figure>
  <img src="{{ site.baseurl }}/assets/images/genomic_regions.svg" alt="Genomic regions for RRBS read alignment" >
  <figcaption>Definition of genomic regions for RRBS read alignment.</figcaption>
</figure>

## Bioinformatics pipelne for RRBS
We used various bioinformatics algorithms and methods to analyse our RRBS samples.
The following tools were those we used in our main RRBS pipeline.
- [FastQC](https://cutadapt.readthedocs.io/en/stable/){: .btn} (quality control)
- [Trim Galore!](https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/){: .btn} (adapter trimming)
- [MultiQC](https://multiqc.info/){: .btn} (quality control report)
- [Bismark](https://www.bioinformatics.babraham.ac.uk/projects/bismark/){: .btn} (read alignment)
- [methylKit](https://bioconductor.org/packages/methylKit/){: .btn} (differential methylation analysis)

## Results
### Overall diet effect
Unlike RNA-seq samples, t-SNE clustering analysis showed no obvious separations of RRBS samples by diet.
<figure>
    <img src="{{ site.baseurl }}/assets/images/rrbs_tsne.svg" alt="t-SNE clustering for RRBS samples" >
    <figcaption>t-SNE (t-distributed stochastic neighbor embedding) clustering of 21 RRBS samples.</figcaption>
</figure>

### Differentially methylated CpG sites
There are no noticeable differences between L2:L1 and L3:L1 as well as hypo- and hyper-methylation in terms of the number of DMCs.
- Identified 2521 DMCs for L2:L1
- Identified 2555 DMCs for L3:L1

See [What are DMCs?]({{ site.baseurl }}/docs/differentially-methylated-cpg-site/){: .btn} for more details.

<figure>
    <img src="{{ site.baseurl }}/assets/images/dmc.png" alt="Volcano plots of DMCs">
    <figcaption>Volcano plots of DMCs.</figcaption>
</figure>

### Significantly affected biological pathways
ORA (over representation analysis) on [KEGG](https://www.genome.jp/kegg/){: .btn} (Kyoto Encyclopedia of Genes and Genomes) pathways showed that micronutrient supplement significantly affected DNA methylation profiles in cell-adhesion and cell-signalling pathways.

{% include table.html id='table_rrbs_ora' data=site.data.rrbs_ora
   caption='Enriched KEGG pathways by ORA (over representation analysis).' %}

## Page links
*Overview*
- [Project summary]({{ site.baseurl }}/docs/project-summary/){: .btn}
- [Gene expression]({{ site.baseurl }}/docs/gene-expression/){: .btn}

*DMC: differentially methylated CpG site*
- [What are DMCs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DMCs L2:L1]({{ site.baseurl }}/docs/dmc-l2l1/){: .btn}
- [DMCs L3:L1]({{ site.baseurl }}/docs/dmc-l3l1/){: .btn}

*DMG: differentially methylated gene*
- [What are DMGs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DMGs L2:L1]({{ site.baseurl }}/docs/dmg-l2l1/){: .btn}
- [DMGs L3:L1]({{ site.baseurl }}/docs/dmg-l3l1/){: .btn}
