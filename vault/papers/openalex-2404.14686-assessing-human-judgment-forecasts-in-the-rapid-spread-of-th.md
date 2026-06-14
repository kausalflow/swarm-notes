---
# CSL-compatible fields
title: "Assessing human judgment forecasts in the rapid spread of the mpox outbreak: insights and challenges for pandemic preparedness"
author:
  - literal: "Thomas McAndrew"
  - literal: "Maimuna S. Majumder"
  - literal: "Andrew A. Lover"
  - literal: "Srini Venkatramanan"
  - literal: "Paolo Bocchini"
  - literal: "Tamay Besiroglu"
  - literal: "Allison Codi"
  - literal: "Gaia Dempsey"
  - literal: "Sam Abbott"
  - literal: "Sylvain Chevalier"
  - literal: "Nikos I Bosse"
  - literal: "Juan Cambeiro"
  - literal: "David Braun"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2404.14686"

# Custom fields
paper_id: "2404.14686"
paper_source: "openalex"
domain: "nlp"
tags:
  - "forecast-reconciliation"
  - "benchmark"
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
processed_at: "2026-06-14T08:38:29Z"
created_at: "2026-06-14T08:38:29Z"
---

# Assessing human judgment forecasts in the rapid spread of the mpox outbreak: insights and challenges for pandemic preparedness

**Authors**: Thomas McAndrew, Maimuna S. Majumder, Andrew A. Lover, Srini Venkatramanan, Paolo Bocchini, Tamay Besiroglu, Allison Codi, Gaia Dempsey, Sam Abbott, Sylvain Chevalier, Nikos I Bosse, Juan Cambeiro, David Braun
**Date**: 2026-06-11
**Paper ID**: [openalex:2404.14686](https://arxiv.org/abs/2404.14686)

## Summary

This paper evaluates the efficacy of human judgment forecasting during the early stages of the 2022 mpox outbreak. By comparing collective human forecasts against standard statistical models like random walks and autoregressive methods, the authors reveal that human ensembles provide superior accuracy for 2-8 week horizons but struggle with immediate, 1-week predictions. The study highlights critical pitfalls in how human forecasts are solicited, specifically suggesting that logarithmic scales may inflate uncertainty and contribute to systematic underestimation of exponential outbreak growth.

## Key Contributions

- Analyzed 1275 human judgment forecasts from 442 individuals regarding the 2022 mpox outbreak, comparing performance against statistical baselines (random walk, autoregressive, doubling time).
- Demonstrated that human judgment ensembles outperform computational models for 2-8 week ahead forecasting horizons, while random walk models performed better for 1-week ahead predictions.
- Identified systematic biases in human forecasting, specifically the tendency to underestimate outbreak size and the negative impact of logarithmic scale elicitation on uncertainty interval accuracy.

## Open Questions & Future Work

- [[zero-probability-assignment-forecasting]]
- [[logarithmic-vs-natural-scale-forecast-misperception]]

## Archivist Review

The paper investigates human judgment in pandemic forecasting, providing specific insights into elicitation biases. I have approved two open questions that define actionable research paths for improving human-in-the-loop forecasting platforms. No concepts were approved because the findings primarily describe empirical phenomena rather than new, reusable algorithmic forecasting mechanisms or representation methods.

### Approved Open Questions
- Impact of Zero Probability Assignments: This is a critical, actionable improvement for public health forecasting platforms to increase the reliability of crowd-sourced probability assessments.
- Logarithmic Scale Forecast Misperception: This targets a fundamental limitation in forecast elicitation design that may lead to systematically biased human judgment in pandemic scenarios.

### Rejected Candidates
- [dataset] Mpox Human Judgment Forecast Dataset (`mpox-human-judgment-forecast-dataset`) - low_impact: The dataset is small and highly specific to a single past event, lacking the general utility and scale required for a reusable vault dataset.

## Links

- [Abstract](https://arxiv.org/abs/2404.14686)
- [PDF](https://arxiv.org/pdf/2404.14686)

