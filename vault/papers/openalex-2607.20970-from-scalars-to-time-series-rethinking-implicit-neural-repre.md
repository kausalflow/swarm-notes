---
# CSL-compatible fields
title: "From Scalars to Time Series: Rethinking Implicit Neural Representations for Time-Varying Volumetric Data"
author:
  - literal: "Weihan Zhang"
  - literal: "X Zhao"
  - literal: "Y Peng"
  - literal: "Yuqi Chen"
  - literal: "J Tao"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2607.20970"

# Custom fields
paper_id: "2607.20970"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "time-series"
  - "mixture-of-experts"
  - "moe"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-26T07:29:37Z"
created_at: "2026-07-26T07:29:37Z"
---

# From Scalars to Time Series: Rethinking Implicit Neural Representations for Time-Varying Volumetric Data

**Authors**: Weihan Zhang, X Zhao, Y Peng, Yuqi Chen, J Tao
**Date**: 2026-07-23
**Paper ID**: [openalex:2607.20970](https://arxiv.org/abs/2607.20970)

## Summary

This paper rethinks implicit neural representations (INRs) for time-varying volumetric data by replacing dense spatiotemporal coordinate sampling with sequence-level supervision over spatially indexed time series. By learning each spatial location from its full temporal evolution, the proposed approach eliminates the need for dense sampling, reduces training costs, and improves reconstruction quality. Furthermore, the authors combine this sequence-level formulation with mixture-of-experts architectures to better handle heterogeneous temporal dynamics.

## Key Contributions

- Revisits implicit neural representations for time-varying volumetric data by shifting from dense coordinate-wise scalar sampling to sequence-level supervision over spatially indexed time series.
- Eliminates the need for dense spatiotemporal sampling during optimization, significantly reducing training cost while improving reconstruction quality across various INR architectures.
- Introduces a mixture-of-experts (MoE) instantiation built on top of the sequence-level time series formulation to provide superior capacity allocation under heterogeneous temporal dynamics.

## Archivist Review

Applied strict scarcity and reusability standards. No concepts or open questions met the high bar for permanent vault storage.

### Rejected Candidates
- [open_question] Adaptive Expert Selection and Dynamic Capacity Allocation for Time-Varying INRs (`adaptive-expert-selection-dynamic-capacity-allocation-time-varying-inrs`) - paper_local: Standard paper-internal future work direction lacking a standalone universal bottleneck.
- [open_question] Incorporating Spatiotemporal Dependencies and Structured Priors in INRs (`incorporating-spatiotemporal-dependencies-structured-priors-inrs`) - generic: Generic future work proposing standard spatial priors in representation learning.

## Links

- [Abstract](https://arxiv.org/abs/2607.20970)
- [PDF](https://arxiv.org/pdf/2607.20970)

