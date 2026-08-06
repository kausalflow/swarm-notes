---
# CSL-compatible fields
title: "CARE: A Cascaded Framework for Efficient and Reliable Time Series Anomaly Detection"
author:
  - literal: "Zemin Chao"
  - literal: "Qianhui Xu"
  - literal: "Jianhe Cen"
  - literal: "Guangzhi Ge"
  - literal: "Xiao Chen"
  - literal: "Hoangzhi Wang"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.01885"

# Custom fields
paper_id: "2608.01885"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
  - "efficiency"
  - "model-compression"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:31:28Z"
created_at: "2026-08-06T07:31:28Z"
---

# CARE: A Cascaded Framework for Efficient and Reliable Time Series Anomaly Detection

**Authors**: Zemin Chao, Qianhui Xu, Jianhe Cen, Guangzhi Ge, Xiao Chen, Hoangzhi Wang
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.01885](https://arxiv.org/abs/2608.01885)

## Summary

The authors propose CARE, a model-agnostic cascaded inference framework designed to improve the efficiency of time series anomaly detection. By integrating a Lightweight Pre-filter Model (LPM) with a Residual MLP AutoEncoder, Normality-Conditioned Gating, and a Structure Attention module, CARE filters out high-confidence normal samples and selectively routes only uncertain samples to a high-capacity Complex Detection Model (CDM). Extensive experiments across eight benchmarks demonstrate significant inference speedups of 2.7x to 4.8x without sacrificing detection quality.

## Key Contributions

- Proposed CARE, a model-agnostic cascaded inference framework combining a Lightweight Pre-filter Model (LPM) and a Complex Detection Model (CDM) for time series anomaly detection.
- Introduced a Residual MLP AutoEncoder with a Normality-Conditioned Gating mechanism and Structure Attention to capture channel-wise anomaly contributions and filter high-confidence normal samples.
- Achieved 2.7x to 4.8x inference speedup across eight real-world benchmarks while maintaining competitive detection quality compared to state-of-the-art methods.

## Open Questions & Future Work

- [[adaptive-routing-evolving-time-series]]

## Archivist Review

Applied rigorous selectivity criteria, rejecting paper-local frameworks and subcomponents while retaining the single high-impact open question regarding adaptive routing in evolving time series environments.

### Approved Open Questions
- Adaptive Routing for Evolving Time Series: Crucial for deploying efficient cascaded models in streaming or non-stationary environments where static pre-filtering thresholds fail over time.

### Rejected Candidates
- [concept] CARE Cascaded Inference Framework (`care-framework`) - paper_local: Paper-internal cascading architecture for time series anomaly detection, lacking broad standalone reusability outside this specific implementation.
- [concept] Normality-Conditioned Gating (`normality-conditioned-gating`) - subcomponent_of_broader_mechanism: Subcomponent mechanism local to the lightweight pre-filter model of the paper.

## Links

- [Abstract](https://arxiv.org/abs/2608.01885)
- [PDF](https://arxiv.org/pdf/2608.01885)

