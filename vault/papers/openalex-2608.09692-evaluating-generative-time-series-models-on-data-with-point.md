---
# CSL-compatible fields
title: "Evaluating Generative Time-Series Models on Data with Point Masses"
author:
  - literal: "Jian Xu"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09692"

# Custom fields
paper_id: "2608.09692"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:08:50Z"
created_at: "2026-08-13T06:08:50Z"
---

# Evaluating Generative Time-Series Models on Data with Point Masses

**Authors**: Jian Xu
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09692](https://arxiv.org/abs/2608.09692)

## Summary

This paper investigates the evaluation of generative time-series models on data containing point masses (such as zero-inflated series like rainfall or ride requests). The author reveals that standard rolling-origin evaluation protocols severely distort probability mass structures between evaluation windows and the full dataset, which can completely reverse model conclusions. By benchmarking seven models across multiple seeds, the study shows that an autoregressive hurdle model significantly outperforms conditional flow models, and highlights high variance in occurrence statistics across seeds for flow-based approaches.

## Key Contributions

- Identifies a critical flaw in the rolling-origin evaluation protocol for time-series data with point masses, where evaluation windows exhibit probability mass structures drastically differing from the overall dataset (e.g., 42% vs 13% zeros).
- Introduces a control mechanism for CRPS to measure the exact contribution of temporal coupling by destroying the temporal structure while keeping CRPS invariant by construction.
- Evaluates seven generative models across five seeds and finds that an autoregressive hurdle model outperforms conditional flow models on five out of six datasets by up to a factor of 153.
- Demonstrates that conditional flow models exhibit high variance in occurrence statistics (up to 62% variation across training seeds) and that baseline models are entirely deterministic.

## Open Questions & Future Work

- [[native-point-mass-generative-modeling]]

## Archivist Review

Approved the open question on native point-mass generative modeling due to its clear relevance to zero-inflated and intermittent time series. No concepts or datasets met the strict novelty and reusability standards.

### Approved Open Questions
- Native Point-Mass Generative Modeling: Current continuous-state models like flows and diffusion struggle fundamentally with data containing probability masses on single values, leading to evaluation anomalies and poor modeling of intermittent phenomena.

### Rejected Candidates
- [open_question] Native Point-Mass Generative Modeling (`native-point-mass-generative-modeling`) - other: The open question is well-formulated and important for zero-inflated time series, so it is approved.

## Links

- [Abstract](https://arxiv.org/abs/2608.09692)
- [PDF](https://arxiv.org/pdf/2608.09692)

