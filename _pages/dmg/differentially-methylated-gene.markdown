---
permalink: /docs/differentially-methylated-gene/
layout: single
sidebar:
  nav: "docs"
toc: true
toc_sticky: true
comments: true
share: true  
title:  "What are DMGs?"
categories: summary dna-methylation dmg
---
DMG stands for differentially methylated genes. A DMC is a gene that has at least one DMC on its gene body, promoter or flanking region.

## Treatment and control groups
We used three groups - L1, L2 and L3 diets - to define DMGs. L1 diet was used as control.

{% capture comps %}
- **L2:L1**: L2 vs. L1 with using L1 as control
- **L3:L1**: L3 vs. L1 with using L1 as control
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Data sets for differential expression analysis</h4>
  {{ comps | markdownify }}
</div>

See [Experimental feed]({{ site.baseurl }}/docs/project-summary/#experimental-feed){: .btn} for details about L1, L2 and L3 groups.

## Definition of DMGs
We used [methylKit](https://bioconductor.org/packages/methylKit/){: .btn} to define DMCs with the following criteria.

1. `abs(percentage methylation differences) >= 20%`
2. `Q-value < 0.01`

We then defined DMGs as genes with at least one DMC in the following genomic regions.

{% capture regions %}
1. Exon
2. Intron
3. P250 (proximal promoter)
4. P1K (promoter)
5. P6K (distal promoter)
6. Flanks (potential enhancer region)
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Genomic regions for RRBS read mapping</h4>
  {{ regions | markdownify }}
</div>

<figure>
  <img src="{{ site.baseurl }}/assets/images/dna/genomic_regions_liver.svg" alt="Genomic regions for RRBS read alignment" >
  <figcaption>Definition of genomic regions for RRBS read alignment.</figcaption>
</figure>

## Differentially methylated genes
There are no noticeable differences between L2:L1 and L3:L1 in terms of the number of DMGs.

{% capture dmgs %}
- **L2 vs. L1**: 1998 DMGs
- **L3 vs. L1**: 1997 DMGs
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Identified DMGs for L2:L1 and L3:L1</h4>
  {{ dmgs | markdownify }}
</div>

Most DMGs have only one DMC for both L2:L1 and L3:L1.

## Analysis of DMGs
We further analysed DMGs to understand the differences of DNA methylation profiles affected by micronutrients.

### Functional annotation databases
- [KEGG](https://www.genome.jp/kegg/){: .btn} (Kyoto Encyclopedia of Genes and Genomes)
- [GO](http://geneontology.org/){: .btn} (Gene Ontology)

### Functional annotation method
- [ORA](https://doi.org/10.1093/bioinformatics/bth456){: .btn} (over representation analysis)

## List of DMGs with gene symbols and gene names
- [List of DMGs - L2 vs. L1]({{ site.baseurl }}/docs/dmg-l2l1/){: .btn}
- [List of DMGs - L3 vs. L1]({{ site.baseurl }}/docs/dmg-l3l1/){: .btn}
- [Excel files (Downloads page)]({{ site.baseurl }}/docs/downloads/#9-excel-files-for-degs-dmcs-and-dmgs){: .btn}
