---
# CSL-compatible fields
title: "MIRANDA: MId-feature RANk-adversarial Domain Adaptation toward climate change-robust ecological forecasting with deep learning"
author:
  - literal: "Yuchang Jiang"
  - literal: "Jan Dirk Wegner"
  - literal: "Vivien Sainte Fare Garnot"
issued:
  date-parts:
    - [2026, 4, 1]
url: "https://arxiv.org/abs/2604.00800"

# Custom fields
paper_id: "2604.00800"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "domain-adaptation"
  - "adversarial-examples"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "miranda-mid-feature-rank-adversarial-domain-adaptation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-04T05:49:59Z"
created_at: "2026-04-04T05:49:59Z"
---

# MIRANDA: MId-feature RANk-adversarial Domain Adaptation toward climate change-robust ecological forecasting with deep learning

**Authors**: Yuchang Jiang, Jan Dirk Wegner, Vivien Sainte Fare Garnot
**Date**: 2026-04-01
**Paper ID**: [openalex:2604.00800](https://arxiv.org/abs/2604.00800)

## Summary

MIRANDA addresses the challenge of applying deep learning to phenology modeling under climate-induced temporal distribution shifts. Unlike conventional domain adaptation that focuses on final representations, MIRANDA applies rank-based adversarial regularization on intermediate features to enforce year-invariance. This approach mitigates the negative impacts of covariate and label shifts inherent in long-term ecological data. Results on a 70-year phenological dataset demonstrate enhanced robustness compared to standard adversarial methods, aligning deep learning performance more closely with traditional mechanistic models.

## Key Contributions

- Introduced MIRANDA, a domain adaptation framework that applies rank-based adversarial regularization on intermediate features to handle continuous temporal and label shifts.
- Addressed the limitations of conventional adversarial DA, which often fail under climate-induced distribution shifts by not accounting for label shifts.
- Achieved improved robustness to climatic distribution shifts on a 70-year, 67,800-observation phenological dataset, narrowing the performance gap between deep learning and mechanistic models.

## Open Questions & Future Work

- [[climatic-shift-extrapolation-robustness]]

## Key Concepts

- [[miranda-mid-feature-rank-adversarial-domain-adaptation]]: A domain adaptation framework using rank-based adversarial regularization on intermediate features to enforce year-invariance in time-series representations.

## Archivist Review

I approved MIRANDA as a concept because it introduces a distinct rank-based adversarial approach to domain adaptation that specifically addresses continuous, rather than binary, temporal shifts. I approved the open question regarding robustness to climatic distribution shifts because it highlights a fundamental limitation in non-stationary time-series forecasting that persists beyond this paper's specific solution. No datasets were approved as none were cited as reusable benchmarks or standardized sources.

### Approved Concepts
- Mid-feature Rank-adversarial Domain Adaptation (MIRANDA): Provides a robust approach to domain adaptation in the presence of continuous temporal distribution shifts and label shifts, a common bottleneck in environmental forecasting.

### Approved Open Questions
- Robustness to climatic distribution shifts: This is technically important because it addresses the identified limitations of current data-driven models when deployed under environmental conditions that lie outside their historical training distributions, a critical bottleneck for reliable long-term ecological forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2604.00800)
- [PDF](https://arxiv.org/pdf/2604.00800)

