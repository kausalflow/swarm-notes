---
# CSL-compatible fields
title: "Subsample-based Estimation under Dynamic Contamination"
author:
  - literal: "Yukai Yang"
  - literal: "Rickard Sandberg"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.17676"

# Custom fields
paper_id: "2604.17676"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "robustness"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "patch-removal-operator"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:56:42Z"
created_at: "2026-04-23T06:56:42Z"
---

# Subsample-based Estimation under Dynamic Contamination

**Authors**: Yukai Yang, Rickard Sandberg
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.17676](https://arxiv.org/abs/2604.17676)

## Summary

This paper demonstrates that standard subsample-based robust estimation techniques fail in dynamic time series models because contamination propagates through residual filters, distorting the estimation objective. To resolve this, the authors introduce a 'patch removal operator' that transforms index sets to account for the residual footprint of contaminated data points. This approach restores estimator consistency in contaminated dynamic settings while preserving the desirable properties of the original estimator under clean data conditions. The work provides a rigorous framework for valid robust estimation by explicitly accounting for temporal residual dependencies.

## Key Contributions

- Identified and characterized the fundamental failure of traditional subsample-based estimation in dynamic time series due to residual propagation of contamination.
- Introduced the patch removal operator, a propagation-compatible index transformation that effectively isolates the residual footprint of contaminated observations.
- Proved that the patch removal operator restores consistency for residual-based estimators under contamination without affecting asymptotic properties in clean settings.

## Open Questions & Future Work

- [[information-criteria-for-robust-dynamic-estimation]]

## Key Concepts

- [[patch-removal-operator]]: A transformation operator for index sets in dynamic time series that removes the residual footprint of contamination to restore estimator consistency.

## Archivist Review

I approved the 'patch removal operator' as it introduces a novel and reusable structural solution to the problem of residual contamination propagation. I also approved one open question regarding robust information criteria, as it targets a clear theoretical gap in applying the proposed framework to model selection. The second proposed open question regarding contamination magnitude estimation was rejected as it is less central to the primary consistency contribution.

### Approved Concepts
- Patch removal operator: It addresses the structural failure of traditional subsampling in dynamic time series caused by residual propagation.

### Approved Open Questions
- Robust Information Criteria for Dynamic Estimation: Model selection is critical for reliable inference in dynamic models, and existing criteria are known to be biased or inconsistent under contamination.

## Links

- [Abstract](https://arxiv.org/abs/2604.17676)
- [PDF](https://arxiv.org/pdf/2604.17676)

