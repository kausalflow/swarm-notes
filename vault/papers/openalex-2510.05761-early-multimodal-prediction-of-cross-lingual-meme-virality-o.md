---
# CSL-compatible fields
title: "Early Multimodal Prediction of Cross-Lingual Meme Virality on Reddit: A Time-Window Analysis"
author:
  - literal: "Sedat Doğan"
  - literal: "Nina Dethlefs"
  - literal: "Debarati Chakraborty"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2510.05761"

# Custom fields
paper_id: "2510.05761"
paper_source: "openalex"
domain: "nlp, multimodal, time-series"
tags:
  - "multimodal"
  - "time-series"
  - "llm"
  - "benchmark"
  - "dataset"
  - "language-model"
  - "vision-language-model"
architectures:
  []
datasets:
  - "reddit-meme-dataset"
concept_slugs:
  - "hybrid-score"
  - "content-ceiling"
dataset_slugs:
  - "reddit-meme-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:26:21Z"
created_at: "2026-05-23T07:26:21Z"
---

# Early Multimodal Prediction of Cross-Lingual Meme Virality on Reddit: A Time-Window Analysis

**Authors**: Sedat Doğan, Nina Dethlefs, Debarati Chakraborty
**Date**: 2026-05-20
**Paper ID**: [openalex:2510.05761](https://arxiv.org/abs/2510.05761)

## Summary

This paper investigates the early prediction of cross-lingual meme virality on Reddit through a comprehensive time-window analysis. The authors introduce a Hybrid Score to normalize engagement across heterogeneous communities and benchmark various predictive models using multimodal features. The study uncovers a 'Content Ceiling' that restricts the effectiveness of content-only models, highlighting the critical role of network and temporal features. Additionally, SHAP analysis reveals that early predictions are driven by network priors, whereas later predictions are increasingly shaped by temporal velocity and acceleration dynamics.

## Key Contributions

- Introduces a large-scale, cross-lingual dataset of 46,578 Reddit memes with over one million engagement tracking points.
- Proposes the 'Hybrid Score' metric to normalize virality metrics across diverse communities using dynamic features.
- Identifies a 'Content Ceiling' performance limit for content-only models, demonstrating the necessity of structural network and temporal features for virality prediction.
- Demonstrates that early meme virality (from 30 minutes) is predictable, with a multimodal XGBoost classifier reaching 0.43 PR AUC.

## Open Questions & Future Work

- [[robust-virality-definition-metrics]]
- [[causal-modeling-of-virality]]

## Key Concepts

- [[hybrid-score]]: A dynamic virality metric that normalizes engagement by community size and incorporates velocity and acceleration features.
- [[content-ceiling]]: An observed performance plateau in virality prediction tasks where content-based signals alone fail to improve accuracy beyond a certain point.

## Archivist Review

The paper provides a thoughtful re-framing of virality prediction as a dynamic process rather than a static classification task. I have approved the 'Hybrid Score' and 'Content Ceiling' as they provide meaningful, reusable terminology for social media forecasting research. The open questions regarding robust virality definitions and causal modeling represent substantial, non-boilerplate research challenges.

### Approved Concepts
- Hybrid Score: Standardizes virality metrics across heterogeneous communities, addressing issues with volume-based thresholds.
- Content Ceiling: Provides a theoretical framework for understanding the limitations of content-centric predictive modeling in virality tasks.

### Approved Open Questions
- Robust Virality Definition Metrics: Establishing a consistent, robust definition of virality is essential for improving the comparability of predictive models across different datasets and research studies.
- Causal Modeling of Virality: Understanding the causal drivers of virality is critical for designing platforms that can better manage information flow, moderate harmful content, and influence the spread of information.

## Datasets

- [[reddit-meme-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2510.05761)
- [PDF](https://arxiv.org/pdf/2510.05761)

