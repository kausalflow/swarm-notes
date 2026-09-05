---
# CSL-compatible fields
title: "SMart: A Multi-source Multi-phase Time Series Representation Transfer Framework"
author:
  - literal: "Fang He"
  - literal: "Wang-Chien Lee"
issued:
  date-parts:
    - [2026, 9, 2]
url: "https://arxiv.org/abs/2609.02203"

# Custom fields
paper_id: "2609.02203"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "representation-learning"
  - "self-supervised-learning"
  - "transformer"
  - "pre-training"
  - "time-classification"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-05T08:41:51Z"
created_at: "2026-09-05T08:41:51Z"
---

# SMart: A Multi-source Multi-phase Time Series Representation Transfer Framework

**Authors**: Fang He, Wang-Chien Lee
**Date**: 2026-09-02
**Paper ID**: [openalex:2609.02203](https://arxiv.org/abs/2609.02203)

## Summary

This paper introduces SMart, a multi-source multi-phase time series representation transfer framework designed to overcome limitations in existing self-supervised time series recovery and single-source representation learning. SMart features a multi-phase recurrence plots recovery task with three alternative modes to embed time series dynamics and a source dataset selector to choose suitable source datasets for pre-training. Extensive experiments demonstrate that SMart outperforms state-of-the-art methods in time series representation learning, classification, and regression tasks on both univariate and multivariate benchmarks.

## Key Contributions

- Proposes SMart, a multi-source multi-phase time series representation transfer framework with a multi-phase recurrence plots recovery task and a source dataset selector.
- Outperforms state-of-the-art models for time series representation learning, classification, and regression on both univariate and multivariate time series datasets.
- Reduces mean absolute error by up to 19.5% for time series regression and increases average accuracy by up to 1.34% for time series classification.

## Archivist Review

All candidates were rejected because they are paper-local architectural components and specific future work items rather than reusable, broad contributions or canonical datasets.

### Rejected Candidates
- [concept] SMart framework (`smart-framework`) - paper_local: The SMart framework is specific to this paper's particular pre-training architecture and lacks broader adoption across the literature.
- [open_question] Efficient Multi-Source Selection for Time Series (`efficient-multivariate-source-selection`) - paper_local: This open question is primarily a paper-internal future work direction on computational complexity and scaling for their specific source selector component.

## Links

- [Abstract](https://arxiv.org/abs/2609.02203)
- [PDF](https://arxiv.org/pdf/2609.02203)

