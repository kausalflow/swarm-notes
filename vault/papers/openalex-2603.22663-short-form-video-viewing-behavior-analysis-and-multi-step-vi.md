---
# CSL-compatible fields
title: "Short-Form Video Viewing Behavior Analysis and Multi-Step Viewing Time Prediction"
author:
  - literal: "Vu Thi Hai Yen"
  - literal: "Duc V. Nguyen"
  - literal: "Cao Anh Minh Huy"
  - literal: "Truong Thu Huong"
issued:
  date-parts:
    - [2026, 3, 24]
url: "https://arxiv.org/abs/2603.22663"

# Custom fields
paper_id: "2603.22663"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  - "Short-Form Video Viewing Behavior Dataset"
concept_slugs:
  - "chunk-based-preloading-optimization"
dataset_slugs:
  - "short-form-video-viewing-behavior-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T15:43:58Z"
created_at: "2026-03-27T15:43:58Z"
---

# Short-Form Video Viewing Behavior Analysis and Multi-Step Viewing Time Prediction

**Authors**: Vu Thi Hai Yen, Duc V. Nguyen, Cao Anh Minh Huy, Truong Thu Huong
**Date**: 2026-03-24
**Paper ID**: [openalex:2603.22663](https://arxiv.org/abs/2603.22663)

## Summary

This paper investigates user viewing behavior in short-form video streaming to optimize chunk-based preloading, aiming to reduce data wastage caused by early skips. The authors present a measurement study that constructed a public dataset containing viewing times for 100 diverse short videos. They then benchmarked the predictive accuracy of standard time-series forecasting algorithms, including Auto-ARIMA, AR, LR, SVR, and DTR, for multi-step viewing time prediction. The results indicate that Auto-ARIMA provided the most stable and lowest forecasting errors across experimental settings, suggesting its suitability for guiding optimized preloading strategies.

## Key Contributions

- Conducted a measurement study to construct a public user behavior dataset containing viewing times for one hundred short videos across various categories.
- Evaluated the performance of standard time-series forecasting algorithms (Auto-ARIMA, AR, LR, SVR, DTR) for predicting user viewing time in short-form video streaming.
- Found that Auto-ARIMA generally achieved the lowest and most stable forecasting errors for predicting user viewing time compared to other standard methods.

## Limitations

The study focuses on predicting viewing time for a fixed set of one hundred short videos, and the generalizability to a constantly changing, large-scale platform feed is not fully assessed. The evaluation only covers standard time-series methods.

## Open Questions & Future Work

- [[advanced-forecasting-models-for-viewing-time]]
- [[adaptive-preloading-strategies-optimization]]

## Key Concepts

- [[chunk-based-preloading-optimization]]: An approach to reducing data wastage in short-form video streaming by dividing videos into chunks and preloading them adaptively based on predicted viewing behavior.

## Archivist Review

The analysis yielded one strong candidate concept central to the paper's optimization goal, which was approved. The publicly released dataset was approved as a primary contribution. Two future work items concerning improving the predictive models and developing the adaptive preloading system based on those predictions were deemed substantial open questions worth tracking. All other candidates were either boilerplate or directly related to the approved items, leading to their rejection.

### Approved Concepts
- Chunk-based Preloading Optimization: The optimization of chunk-based preloading directly addresses the primary problem of data wastage in short-form video streaming, making it a central practical goal.

### Approved Open Questions
- Explore advanced forecasting models: Exploring more advanced forecasting models is necessary because the study's best-performing model, Auto-ARIMA, still produces non-trivial errors (e.g., RMSE around 6.0–8.5), and better prediction accuracy directly translates to reduced data wastage in the streaming system.
- Investigate adaptive preloading strategies: Developing adaptive preloading strategies based on improved viewing time prediction is technically important as it directly addresses the core problem of minimizing data wastage while maintaining Quality of Experience (QoE) in short-form video delivery.

### Rejected Candidates
- [dataset] Short-Form Video Viewing Behavior Dataset (`short-form-video-viewing-behavior-dataset`) - generic: The dataset was approved as it is a primary contribution and is publicly available.
- [open_question] Explore advanced forecasting models (`advanced-forecasting-models-for-viewing-time`) - generic: The open question was approved as it represents a clear next step beyond the limited scope of standard models tested.
- [open_question] Investigate adaptive preloading strategies (`adaptive-preloading-strategies-optimization`) - generic: The open question was approved as it focuses on the practical optimization system directly enabled by the predictive model.
- [concept] Chunk-based Preloading Optimization (`chunk-based-preloading-optimization`) - generic: The concept was approved as it defines the core problem being solved with time-series prediction in this domain.

## Datasets

- [[short-form-video-viewing-behavior-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2603.22663)
- [PDF](https://arxiv.org/pdf/2603.22663)

