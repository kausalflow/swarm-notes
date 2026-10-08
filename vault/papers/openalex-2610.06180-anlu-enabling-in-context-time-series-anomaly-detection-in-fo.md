---
# CSL-compatible fields
title: "Anlu: Enabling In-Context Time Series Anomaly Detection in Foundation Models via Counterfactual Supervision"
author:
  - literal: "Tian Lan"
  - literal: "Yifei Gao"
  - literal: "Yimeng Lu"
  - literal: "Xuming An"
  - literal: "Meng Wang"
  - literal: "Yue Pan"
  - literal: "Wenjun He"
  - literal: "Chen Zhang"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.06180"

# Custom fields
paper_id: "2610.06180"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "in-context-learning"
  - "foundation-model"
  - "pre-training"
architectures:
  []
datasets:
  []
concept_slugs:
  - "counterfactual-supervision"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:41:02Z"
created_at: "2026-10-08T11:41:02Z"
---

# Anlu: Enabling In-Context Time Series Anomaly Detection in Foundation Models via Counterfactual Supervision

**Authors**: Tian Lan, Yifei Gao, Yimeng Lu, Xuming An, Meng Wang, Yue Pan, Wenjun He, Chen Zhang
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.06180](https://arxiv.org/abs/2610.06180)

## Summary

Anlu enables in-context time series anomaly detection using frozen foundation models via reference-conditioned detection. To prevent models from learning shortcuts and ignoring reference records, the authors introduce counterfactual supervision, which pairs queries with conflicting reference rules. Integrating a reference memory and zero-initialized gated adapters, Anlu increases the mean VUS-PR of a frozen TSFM from 0.542 to 0.607 across the 350 TSB-AD-U benchmark sequences.

## Key Contributions

- Proposes Anlu, enabling in-context time series anomaly detection via reference-conditioned detection on frozen foundation models.
- Introduces counterfactual supervision to prevent models from ignoring context references by pairing queries with conflicting reference rules.
- Improves the mean VUS-PR of a frozen time-series foundation model from 0.542 to 0.607 on the 350 TSB-AD-U evaluation sequences.

## Limitations

None explicitly discussed in the abstract.

## Key Concepts

- [[counterfactual-supervision]]: A training supervision strategy that pairs a query with multiple conflicting reference records to force models to utilize in-context conditioning.

## Archivist Review

Applied strict screening guidelines, approving only the core conceptual mechanism of counterfactual supervision while filtering out model names and routine benchmark datasets.

### Approved Concepts
- Counterfactual Supervision: It solves the shortcut-learning problem where a detector ignores the conditioning reference by enforcing reference-dependent label divergence across counterfactual reference pairings.

### Rejected Candidates
- [concept] Anlu (`anlu`) - not_reusable: Model/framework name rather than a reusable core mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2610.06180)
- [PDF](https://arxiv.org/pdf/2610.06180)

