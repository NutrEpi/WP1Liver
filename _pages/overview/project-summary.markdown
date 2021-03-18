---
permalink: /docs/project-summary/
layout: single
sidebar:
  nav: "docs"
toc: true
toc_sticky: true
comments: true
share: true
title:  "Project summary"
categories: summary
---

Project summary of NutrEpi WP1 (Liver).

## Objective
The primary goal of the project is to elucidate the effect of micronutrient (vitamins and minerals) on metabolic pathways from a genetic and epigenetic point of view. Specifically, our aim is to analyse and understand the influences of micronutrients in Atlantic salmon feed through [a whole life cycle feeding trial](https://doi.org/10.1016/j.aquaculture.2020.735551){: .btn} (over 54 weeks for salmon) conducted under the EU funded [ARRAINA](https://www.arraina.eu/){: .btn} (advanced research initiatives for nutrition and aquaculture) project.

## Background
With the rapid expansion of the aquaculture industry in the last two decades, we can hardly sustain traditional practices as feeding fish to grow other fish. Hence, aquaculture feeds have been shifted to containing more plant-based materials. Consequently, the optimised levels of nutrition, including micronutrient, are altered and need to be updated to produce healthier and more nutritious fish.

New knowledge regarding genetic and epigenetic regulations acquired through this project may contribute to the global effort on solving a word-wide problem of micronutrient deficiencies called "hidden hunger". Ending all forms of malnutrition including micronutrient deficiencies is one of the [SDGs](https://sdgs.un.org/goals){: .btn} (sustainable development goals) proposed by the UN.

## Feeding trial
Our analyses were based on the liver samples of Atlantic salmon fed with three graded levels of micronutrient supplementation. The main outcome of the feeding trail was summarised in [Vera et al., 2020](https://doi.org/10.1016/j.aquaculture.2020.735551).

### Experimental design
We collected liver samples at the final harvest stage for gene expression and DNA methylation analysis.

{% include figure
  image_path="/assets/images/growth/experimental_design.svg"
  alt="Experimental design"
  caption="Three groups of Atlantic salmon were fed with different levels of micronutrients through the trial." %}

### Experimental feed
Through the trial, Atlantic salmon in triplicate groups - L1, L2, L3 - were fed with graded levels of micronutrient supplements, formulated with nutrition package (NP).

{% capture feed %}
- **L1**: 100% NP (recommended composition of micronutrients)
- **L2**: 200% NP
- **L3**: 400% NP
{% endcapture %}

<div class="notice">
  {{ feed | markdownify }}
</div>

{% include table.html id='table_trial_feed' data=site.data.growth.feed
   caption='Added micronutrient concentrations (mg/kg) within the NP.' %}

### Growth performance

{% capture growth1 %}
- **Smolt**: L2 showed the best growth followed by L3
- **Harvest**: Both L2 and L3 showed significantly better growth
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Body weights</h4>
  {{ growth1 | markdownify }}
</div>

{% capture growth2 %}
- **Smolt**: L1 had a significantly higher HSI than L2 and L3
- **Harvest**: No significant difference among L1, L2 and L3
- `HSI = (Liver weight (g) / Fish weight (g)) × 100`
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Hepatosomatic index (HSI)</h4>
  {{ growth2 | markdownify }}
</div>

<figure class="half">
    <img src="{{ site.baseurl }}/assets/images/growth/weight_barplot.svg" alt="Barplot of Atlantic salmon body weights">
    <img src="{{ site.baseurl }}/assets/images/growth/hsi_barplot.svg" alt="Barplot of Atlantic salmon hepatosomatic index values">
    <figcaption>Body weights and HSI at smolt and final harvest stages.</figcaption>
</figure>

## Main findings of NutrEpi WP1 (liver)

{% capture res1 %}
- **Overall diet effect**: clustering analysis clearly separates our 12 liver samples into three groups by diet.
- **Dose dependent effect**: micronutrient supplements significantly affect several biological pathways, especially those related with lipid metabolism, in a dose dependant manner (L3 < L2 < L1).
{% endcapture %}

<div class="notice--info">
  <h4 class="no_toc">1. Gene expression</h4>
  {{ res1 | markdownify }}
</div>

{% capture res2 %}
- **Overall diet effect**: clustering analysis shows no obvious separations by diet.
- **Affected pathways**: micronutrient supplements significantly affect biological pathways related with cell-adhesion and cell-signalling.
{% endcapture %}

<div class="notice--info">
  <h4 class="no_toc">2. DNA methylation</h4>
  {{ res2 | markdownify }}
</div>

{% capture res3 %}
- Micronutrient supplements significantly *down-regulates* gene expression with L3 having the lowest expression level (L3 < L2 < L1).
- Micronutrient supplements significantly *hyper-methylate* CpG sites in its promoter region (L3 > L2 > L1).
- *acaca* is involved in the *upstream regulation of the lipid biosynthesis* pathway.
{% endcapture %}

<div class="notice--info">
  <h4 class="no_toc">3. Epigenetic regulations of acetyl-CoA carboxylase alpha (<i>acaca</i>)</h4>
  {{ res3 | markdownify }}
</div>

To summarise, our study shows that micronutrient supplementation suppresses liver gene expression in the pathways related to lipid metabolism and increases the methylation rates in the acetyl-CoA carboxylase alpha (*acaca*) gene, which is involved in the upstream regulation of the lipid biosynthesis pathway.

## Page links
- [Gene expression]({{ site.baseurl }}/docs/gene-expression/){: .btn}
- [DNA methylation]({{ site.baseurl }}/docs/dna-methylation/){: .btn}
