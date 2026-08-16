---
# CSL-compatible fields
title: "Defensive Boosting for Online Probabilistic Forecasting"
author:
  - literal: "Georgy Noarov"
  - literal: "Aaron Roth"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.13554"

# Custom fields
paper_id: "2608.13554"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "online-learning"
  - "probabilistic-forecasting"
  - "boosting"
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
processed_at: "2026-08-16T05:17:56Z"
created_at: "2026-08-16T05:17:56Z"
---

# Defensive Boosting for Online Probabilistic Forecasting

**Authors**: Georgy Noarov, Aaron Roth
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.13554](https://arxiv.org/abs/2608.13554)

## Summary

The paper studies online probabilistic forecasting against an adaptive adversary and introduces the Defensive Booster, an efficient algorithm that unifies the guarantees of online gradient boosting and online weak-to-strong boosting. By operationalizing the dual view of boosting, the algorithm achieves Brier score competitiveness with the span of a weak hypothesis class on every sequence while ensuring zero classification error when a smooth weak-learning condition holds. Furthermore, it operates efficiently using a single weak-class learner, yielding orders-of-magnitude faster runtime alongside strong predictive performance on synthetic and real datasets.

## Key Contributions

- Proposes Defensive Booster, an efficient online probabilistic forecasting algorithm that integrates online gradient boosting and online weak-to-strong boosting guarantees.
- Achieves Brier score competitiveness with the span of a weak hypothesis class $H$ on every adaptive sequence while simultaneously guaranteeing zero classification error under a smooth weak-learning condition.
- Operationalizes the dual view of boosting to construct ex-post hard-core certificates when the weak-learning condition fails, using only a single weak-class learner rather than large ensembles.
- Demonstrates orders-of-magnitude faster runtime and strong predictive performance across synthetic and real data streams compared to prior online boosting baselines.

## Open Questions & Future Work

- [[defensive-boosting-beyond-regression]]

## Archivist Review

Approved the open question exploring the extension of defensive boosting to multi-class and complex prediction settings, as it addresses a substantive theoretical bottleneck. No concepts met the high threshold for standalone vault notes, adhering to strict selectivity rules.

### Approved Open Questions
- Extensive Multi-Class Defensive Boosting: Extending defensive boosting beyond binary and bounded regression to more complex structured prediction tasks is a crucial direction for broadening the applicability of online boosting algorithms.

## Links

- [Abstract](https://arxiv.org/abs/2608.13554)
- [PDF](https://arxiv.org/pdf/2608.13554)

