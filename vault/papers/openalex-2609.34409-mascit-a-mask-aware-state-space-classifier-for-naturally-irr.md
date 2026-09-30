---
# CSL-compatible fields
title: "MASCIT: A Mask-Aware State Space Classifier for Naturally Irregular Time Series"
author:
  - literal: "Yoo-Min Jung"
  - literal: "Hyeon-Gi Kim"
  - literal: "Jonghun Park"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34409"

# Custom fields
paper_id: "2609.34409"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "state-space-model"
  - "ssm"
  - "mamba"
  - "classification"
  - "robustness"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "mascit"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:50:06Z"
created_at: "2026-09-30T10:50:06Z"
---

# MASCIT: A Mask-Aware State Space Classifier for Naturally Irregular Time Series

**Authors**: Yoo-Min Jung, Hyeon-Gi Kim, Jonghun Park
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34409](https://arxiv.org/abs/2609.34409)

## Summary

Naturally irregular time series feature asynchronous observations, missing values, unequal lengths, and nonuniform sampling that often disrupt standard dense adapters. To address this, the authors propose MASCIT, a mask-aware state space classifier that explicitly supplies observation masks to the encoder and excludes invalid steps from gated temporal aggregation. Evaluated across 34 irregular time series datasets, MASCIT achieves the strongest aggregate point estimate and maintains the lowest point rank across various irregularity indicators. Furthermore, factorial ablations reveal that partial selectivity outperforms full selectivity within these state space model backbones.

## Key Contributions

- Proposes MASCIT, a mask-aware state space classifier for naturally irregular time series that supplies observation masks to the encoder and excludes invalid steps from gated temporal aggregation.
- Evaluated across 34 irregular time series datasets, achieving the strongest aggregate point estimate and lowest point rank across six irregularity indicators.
- Demonstrates through factorial ablations that partial selectivity is favored over full selectivity in state space model backbones for irregular temporal data.

## Open Questions & Future Work

- [[test-independent-selection-selective-ssm]]

## Key Concepts

- [[mascit]]: A mask-aware state space classifier that explicitly incorporates observation masks and excludes invalid steps during gated temporal aggregation for irregular time series.

## Archivist Review

Approved the core MASCIT architecture as a reusable mask-aware state space classifier for irregular time series and the open question regarding test-independent selection for selective SSMs. Applied rigorous scarcity and utility criteria, rejecting generic ML terms.

### Approved Concepts
- MASCIT: Core novel architecture combining observation masks with selective state space models for irregular time series classification.

### Approved Open Questions
- Test-Independent Selection for SSMs: Important for deploying selective state space models in real-world scenarios without incurring heavy validation overhead or overfitting to specific test sets.

## Links

- [Abstract](https://arxiv.org/abs/2609.34409)
- [PDF](https://arxiv.org/pdf/2609.34409)

