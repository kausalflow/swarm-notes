---
# CSL-compatible fields
title: "Predict, Then Retrieve: Cross-Instance Future-State Retrieval from Video Prefixes"
author:
  - literal: "Quynh Vo"
  - literal: "Thong Nguyen"
  - literal: "Vinh-Hien Do"
  - literal: "Cong-Duy Nguyen"
  - literal: "Anh-Tuan Luu"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.04426"

# Custom fields
paper_id: "2608.04426"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "video-language-model"
  - "retrieval-augmented-generation"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "predictive-state-retrieval"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-08T05:35:29Z"
created_at: "2026-08-08T05:35:29Z"
---

# Predict, Then Retrieve: Cross-Instance Future-State Retrieval from Video Prefixes

**Authors**: Quynh Vo, Thong Nguyen, Vinh-Hien Do, Cong-Duy Nguyen, Anh-Tuan Luu
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.04426](https://arxiv.org/abs/2608.04426)

## Summary

The paper introduces Predictive State Retrieval (PSR), a task requiring models to observe a short video prefix and temporal question to retrieve external instances depicting an object's future state. To study this, the authors build a graded benchmark and propose LFTR, a lightweight retriever that uses frozen encoders with cross-space fusion and hard-negative training. Results show that future forecasting—rather than retrieval—is the primary bottleneck, with LFTR significantly narrowing the gap at lower inference costs.

## Key Contributions

- Introduced Predictive State Retrieval (PSR), a new task combining video prefix anticipation with cross-instance future-state retrieval across multiple temporal horizons.
- Constructed a benchmark from four datasets featuring human-validated ground truth, difficulty tiers, and an oracle ceiling.
- Proposed LFTR, a lightweight frozen-encoder retriever that combines cross-space fusion and hard-negative training to narrow the forecasting gap at lower inference cost.

## Limitations

Performance remains bottlenecked by future forecasting accuracy rather than retrieval capacity, as demonstrated by ceiling decomposition showing high retrievability under oracle states.

## Open Questions & Future Work

- [[oracle-free-latent-rollout-read-rule]]

## Key Concepts

- [[predictive-state-retrieval]]: A task where a model observes a video prefix and a temporal question to retrieve external video or image instances depicting an object's future state.

## Archivist Review

Approved the core task concept 'Predictive State Retrieval' and the open question regarding oracle-free latent rollout reading rules. No named benchmark datasets were provided in the text to merit dataset vault inclusion.

### Approved Concepts
- Predictive State Retrieval: Introduces a novel cross-instance future-state retrieval task combining anticipation and multi-horizon retrieval.

### Approved Open Questions
- Oracle-Free Latent Rollout Read Rule: Extracting full temporal information from learned latent trajectories without supervision degradation is crucial for advancing predictive video modeling and long-horizon forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2608.04426)
- [PDF](https://arxiv.org/pdf/2608.04426)

