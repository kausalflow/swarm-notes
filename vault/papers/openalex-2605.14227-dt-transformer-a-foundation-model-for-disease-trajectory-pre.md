---
# CSL-compatible fields
title: "DT-Transformer: A Foundation Model for Disease Trajectory Prediction on a Real-world Health System"
author:
  - literal: "Yunying Zhu"
  - literal: "Andrew R. Weckstein"
  - literal: "Kueiyu Joshua Lin"
  - literal: "Jie Yang"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14227"

# Custom fields
paper_id: "2605.14227"
paper_source: "openalex"
domain: "medicine"
tags:
  - "llm"
  - "language-model"
  - "transformer"
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "dt-transformer"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:32:00Z"
created_at: "2026-05-17T07:32:00Z"
---

# DT-Transformer: A Foundation Model for Disease Trajectory Prediction on a Real-world Health System

**Authors**: Yunying Zhu, Andrew R. Weckstein, Kueiyu Joshua Lin, Jie Yang
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14227](https://arxiv.org/abs/2605.14227)

## Summary

DT-Transformer is a foundation model designed for predicting disease trajectories using longitudinal data from massive, multi-hospital electronic health records. By training on 57.1 million EHR entries from over 1.7 million patients, the model effectively captures clinical complexity across diverse hospital and outpatient settings. It achieves superior performance in next-event prediction, demonstrating robust discriminative power across a wide spectrum of disease categories in both retrospective and prospective evaluations.

## Key Contributions

- Introduces DT-Transformer, a foundation model trained on 57.1M structured EHR entries from 1.7M patients across a multi-hospital health network.
- Demonstrates strong predictive performance with a median AUC of 0.871 for next-event prediction across 896 disease categories.
- Validates the efficacy of health system-scale training for building clinical forecasting models that generalize beyond single-hospital constraints.

## Open Questions & Future Work

- [[health-data-fragmentation-impact]]
- [[long-term-disease-trajectory-modeling]]

## Key Concepts

- [[dt-transformer]]: A transformer-based foundation model for longitudinal electronic health record analysis and disease trajectory prediction.

## Archivist Review

The paper is approved for its contributions to clinical foundation models at health-system scale. The concepts and open questions were vetted for their relevance to the broader time-series forecasting research agenda, particularly regarding longitudinal data fragmentation and architectural temporal representation. Generic implementation details were omitted in favor of the overarching model and fundamental research challenges.

### Approved Concepts
- DT-Transformer: The model addresses the challenge of building foundation models for clinical forecasting using multi-hospital, system-scale longitudinal data.

### Approved Open Questions
- Impact of fragmented health data: Data fragmentation is a persistent, systemic barrier to the performance and generalizability of clinical forecasting models.
- Optimizing long-term trajectory modeling: Optimizing architectural approaches for long-term health trajectory modeling is a prerequisite for moving beyond simple diagnostic classification to robust clinical decision support.

## Links

- [Abstract](https://arxiv.org/abs/2605.14227)
- [PDF](https://arxiv.org/pdf/2605.14227)

