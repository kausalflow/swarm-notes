---
# CSL-compatible fields
title: "CLOSURE: Cross-Channel Closure for Multivariate Time Series Anomaly Detection"
author:
  - literal: "Fan Xu"
  - literal: "Hao Wu"
  - literal: "Zhi Song"
  - literal: "Hanbo Huang"
  - literal: "Wenzhuo Ma"
  - literal: "Nan Wang"
  - literal: "Wei Gong"
  - literal: "Xibin Zhao"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35753"

# Custom fields
paper_id: "2610.35753"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
  - "diffusion-model"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:10:20Z"
created_at: "2026-10-29T11:10:20Z"
---

# CLOSURE: Cross-Channel Closure for Multivariate Time Series Anomaly Detection

**Authors**: Fan Xu, Hao Wu, Zhi Song, Hanbo Huang, Wenzhuo Ma, Nan Wang, Wei Gong, Xibin Zhao
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35753](https://arxiv.org/abs/2610.35753)

## Summary

Multivariate time series anomaly detection often relies solely on reconstruction errors, which fail to distinguish between familiar operating transitions and actual relational breakdowns between variables. To address this ambiguity, the authors propose CLOSURE, which decouples anomaly detection into two separate prediction tasks: recoverability, handled by a memory-conditioned diffusion reconstructor, and cross-channel consistency, handled by a relation-closure operator with sparse signed gates. These two independent scores are then reconciled via calibration on normal data. Extensive experiments on public benchmark streams demonstrate that CLOSURE consistently outperforms existing reconstruction-, frequency-, and topology-based detectors.

## Key Contributions

- Proposes CLOSURE for multivariate time series anomaly detection, evaluating recoverability and cross-channel consistency as two separate prediction tasks.
- Employs a diffusion reconstructor conditioned on a discrete memory of normal temporal bases for the recoverability task.
- Utilizes a relation-closure operator with sparse signed gates that predicts each channel exclusively from its peers, withholding the target's own trajectory to assess cross-channel consistency.
- Demonstrates consistent outperformance over recent reconstruction-, frequency-, and topology-based detectors on public benchmark streams.

## Open Questions & Future Work

- [[cross-channel-closure-distribution-shift]]

## Archivist Review

Reviewed the paper and analysis. No concept candidates were submitted by the extractor, but the single open question on cross-channel closure under distribution shift is rigorous, addresses a genuine limitation of decoupled reconstruction/consistency checks in anomaly detection, and fits the vault standards well.

### Approved Open Questions
- Cross-Channel Closure Under Shift: Understanding how decoupled cross-channel consistency checks perform under non-stationary shifts and streaming deployments is crucial for real-world industrial monitoring where assumptions of static normal operating distributions frequently fail.

### Rejected Candidates
- [open_question] Cross-Channel Closure Under Shift (`cross-channel-closure-distribution-shift`) - generic: Already included or checked against vault guidelines, but let us evaluate whether it is sufficiently distinct. Actually, no concept candidates were provided by the analysis, and the single open question is well-formulated and important for anomaly detection under distribution shift.

## Links

- [Abstract](https://arxiv.org/abs/2610.35753)
- [PDF](https://arxiv.org/pdf/2610.35753)

