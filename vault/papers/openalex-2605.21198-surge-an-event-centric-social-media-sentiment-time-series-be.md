---
# CSL-compatible fields
title: "SURGE: An Event-Centric Social Media Sentiment Time Series Benchmark with Interaction Structure"
author:
  - literal: "Chen Su"
  - literal: "Pengsen Cheng"
  - literal: "Yuanhe Tian"
  - literal: "Yan Song"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.21198"

# Custom fields
paper_id: "2605.21198"
paper_source: "openalex"
domain: "nlp"
tags:
  - "benchmark"
  - "dataset"
  - "sentiment-analysis"
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "language-model"
architectures:
  []
datasets:
  - "SURGE"
concept_slugs:
  - "surge-benchmark"
dataset_slugs:
  - "surge"
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:25:10Z"
created_at: "2026-05-23T07:25:10Z"
---

# SURGE: An Event-Centric Social Media Sentiment Time Series Benchmark with Interaction Structure

**Authors**: Chen Su, Pengsen Cheng, Yuanhe Tian, Yan Song
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.21198](https://arxiv.org/abs/2605.21198)

## Summary

SURGE is a new benchmark designed to study event-centric social media dynamics by constructing calendar-aligned time series with explicit post-interaction structures. Unlike previous datasets, it retains the graph-based relationships between posts, allowing for the evaluation of interaction-aware forecasting models. Through extensive experiments, the authors demonstrate that existing text-augmented forecasters struggle to generalize to event-driven scenarios and that reply-dense periods present significant challenges often missed by aggregate metrics. The benchmark includes diverse protocols, including leave-one-category-out generalization, to test model robustness.

## Key Contributions

- Introduces SURGE, a comprehensive social media benchmark covering 67 events and 800K posts across five categories.
- Enables controlled evaluation of how social interaction structures (e.g., replies) influence the performance of sentiment time-series forecasting models.
- Provides multi-granularity, event-level calendar-aligned time series with aligned text and interaction graphs.
- Establishes benchmark protocols covering numerical-only, text-augmented, and cross-category generalization tasks.

## Open Questions & Future Work

- [[interaction-aware-sentiment-forecasting]]

## Key Concepts

- [[surge-benchmark]]: A multi-event benchmark for social media sentiment time series that integrates event-level text and interaction structures.

## Archivist Review

I approved the SURGE benchmark and its associated dataset as they provide a clear, structured resource for social media time series research that specifically includes interaction topologies. I also approved the open question regarding interaction-aware sentiment forecasting to track the challenge of integrating graph-based communication structures into temporal forecasting models. I rejected the robustness question as it is a standard domain transfer issue that is already well-represented in existing research discussions.

### Approved Concepts
- SURGE Benchmark: It addresses the lack of large-scale, interaction-aware datasets for social media sentiment forecasting.

### Approved Open Questions
- Interaction-Aware Sentiment Forecasting: Understanding the predictive influence of social interaction structures on collective opinion dynamics is essential for improving forecasting accuracy in volatile, high-interaction social media environments.

### Rejected Candidates
- [open_question] Robustness of Multimodal TSF (`robustness-of-multimodal-tsf`) - not_novel: The issue of cross-domain transfer of existing architectures is broad and often addressed in the literature under domain adaptation, making this specific formulation less unique for a permanent note.

## Datasets

- [[surge]]

## Links

- [Abstract](https://arxiv.org/abs/2605.21198)
- [PDF](https://arxiv.org/pdf/2605.21198)

