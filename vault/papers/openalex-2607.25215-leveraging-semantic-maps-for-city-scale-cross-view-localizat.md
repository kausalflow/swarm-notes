---
# CSL-compatible fields
title: "Leveraging Semantic Maps for City-Scale Cross-View Localization"
author:
  - literal: "Ethan Fahnestock"
  - literal: "Erick Fuentes"
  - literal: "Philip R. Osteen"
  - literal: "Nicholas Roy"
issued:
  date-parts:
    - [2026, 7, 28]
url: "https://arxiv.org/abs/2607.25215"

# Custom fields
paper_id: "2607.25215"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "vision-language-modelvlm"
  - "robotics"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-31T07:44:38Z"
created_at: "2026-07-31T07:44:38Z"
---

# Leveraging Semantic Maps for City-Scale Cross-View Localization

**Authors**: Ethan Fahnestock, Erick Fuentes, Philip R. Osteen, Nicholas Roy
**Date**: 2026-07-28
**Paper ID**: [openalex:2607.25215](https://arxiv.org/abs/2607.25215)

## Summary

This paper introduces a city-scale cross-view localization framework for robots operating in previously untraversed environments using prior semantic maps like OpenStreetMap. To overcome the scalability bottlenecks of using Vision-Language Models (VLMs) for exhaustive correspondence proposals across large areas, the authors distill a lightweight matcher from a VLM to compute efficient landmark correspondences. These correspondences form an observation likelihood that is integrated over time using a Bayes filter to yield robust pose estimates. Evaluated on a newly released dataset spanning eleven diverse environments—including severe weather and nighttime conditions—the method demonstrates strong generalization capabilities.

## Key Contributions

- Proposes a city-scale cross-view localization framework that leverages rich semantic data from sources like OpenStreetMap without rigid class compression.
- Uses Vision-Language Models (VLMs) to extract relevant landmarks from egocentric panoramas and distill a lightweight matcher for scalable entity correspondence.
- Integrates distilled semantic correspondences into an observation likelihood fused via a Bayes filter to generate continuous pose estimates over time.
- Releases a diverse benchmark dataset spanning eleven environments—including challenging conditions like snowstorms and night in Boston—demonstrating generalization across weather, lighting, and geography.

## Archivist Review

The paper focuses on robotics cross-view localization using semantic maps and vision-language models. Since the vault's skill context centers on time series forecasting, temporal inductive biases, and general ML methodology, the extracted robotics open question is deemed too domain-specific and low-impact for permanent storage.

### Rejected Candidates
- [open_question] Handling Distant Semantic Landmarks (`handling-distant-semantic-landmarks-cross-view-localization`) - low_impact: The paper focuses on robotics cross-view localization rather than time series forecasting or core machine learning methodology, making this question too narrow for the time-series/ML-focused vault.

## Links

- [Abstract](https://arxiv.org/abs/2607.25215)
- [PDF](https://arxiv.org/pdf/2607.25215)

