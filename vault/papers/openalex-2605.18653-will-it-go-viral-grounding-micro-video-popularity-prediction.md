---
# CSL-compatible fields
title: "Will It Go Viral? Grounding Micro-Video Popularity Prediction on the Open Web"
author:
  - literal: "Ryang Heo"
  - literal: "Dongha Lee"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.18653"

# Custom fields
paper_id: "2605.18653"
paper_source: "openalex"
domain: "nlp"
tags:
  - "language-model"
  - "multimodal"
  - "time-series"
  - "forecasting"
  - "dataset"
architectures:
  []
datasets:
  - "WEBSHORTS"
concept_slugs:
  - "rationale-guided-regression"
dataset_slugs:
  - "webshorts"
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:37:25Z"
created_at: "2026-05-21T08:37:25Z"
---

# Will It Go Viral? Grounding Micro-Video Popularity Prediction on the Open Web

**Authors**: Ryang Heo, Dongha Lee
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.18653](https://arxiv.org/abs/2605.18653)

## Summary

This paper addresses the challenge of micro-video popularity prediction (MVPP) by grounding forecasts in real-time open-web context rather than platform-internal video history. The authors introduce the WEBSHORTS dataset, which pairs 14K short-form videos with structured evidence-cards capturing external attention trends. To leverage this, they propose SHORTS-CAST, a framework that generates dimension-wise rationales from web evidence to guide popularity regression and adapts to shifting trends using delayed labels. Experiments confirm that integrating external open-web context and trend-aware adaptation is essential for accurate forecasting in fast-evolving ecosystems.

## Key Contributions

- Introduces WEBSHORTS, a micro-video dataset pairing 14K short-form videos with structured open-web context collected at upload time to enable trend-aware forecasting.
- Proposes SHORTS-CAST, a framework that models popularity by generating dimension-wise rationales from external web context to guide regression.
- Demonstrates that SHORTS-CAST significantly outperforms corpus-based retrieval and standard online adaptation methods in both offline and delayed-label popularity prediction scenarios.

## Open Questions & Future Work

- [[cross-platform-mvpp-generalization]]

## Key Concepts

- [[rationale-guided-regression]]: A forecasting approach that generates explicit dimension-wise rationales from external context to guide regression models.

## Archivist Review

I approved the concept of 'Rationale-Guided Regression' as it captures a novel, reusable mechanism for grounding forecasts in structured rationale-based context. 'WEBSHORTS' was approved as a named dataset. The open question was narrowed to focus on the platform-generalization bottleneck, as drift detection in time-series is already well-represented in the vault.

### Approved Concepts
- Rationale-Guided Regression: This represents a shift from raw content or latent embeddings to explicable, dimension-wise reasoning as an inductive bias for forecasting.

### Approved Open Questions
- Cross-Platform Popularity Generalization: Critical for determining whether open-web grounding provides a universal signal or is fundamentally limited by platform-specific closed-loop dynamics.

### Rejected Candidates
- [concept] SHORTS-CAST (`shorts-cast`) - subcomponent_of_broader_mechanism: This is a specific framework name; the core reusable innovation is better captured by 'Rationale-Guided Regression'.
- [open_question] Adaptive Drift Detection in MVPP (`adaptive-drift-detection-mvpp`) - duplicate_existing: This is a specific instantiation of general drift detection; existing questions on drift detection and adaptive thresholds already exist.

## Datasets

- [[webshorts]]

## Links

- [Abstract](https://arxiv.org/abs/2605.18653)
- [PDF](https://arxiv.org/pdf/2605.18653)

