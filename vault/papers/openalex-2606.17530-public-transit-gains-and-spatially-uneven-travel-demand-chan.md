---
# CSL-compatible fields
title: "Public transit gains and spatially uneven travel demand changes after NYC congestion pricing"
author:
  - literal: "Donghang Li"
  - literal: "Dingyi Zhuang"
  - literal: "Yunlin Li"
  - literal: "ChenAn Shen"
  - literal: "N. Cao"
  - literal: "Yunhan Zheng"
  - literal: "Shenhao Wang"
  - literal: "Jinhua Zhao"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.17530"

# Custom fields
paper_id: "2606.17530"
paper_source: "openalex"
domain: "time-series,nlp"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "language-model"
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
processed_at: "2026-06-19T09:24:48Z"
created_at: "2026-06-19T09:24:48Z"
---

# Public transit gains and spatially uneven travel demand changes after NYC congestion pricing

**Authors**: Donghang Li, Dingyi Zhuang, Yunlin Li, ChenAn Shen, N. Cao, Yunhan Zheng, Shenhao Wang, Jinhua Zhao
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.17530](https://arxiv.org/abs/2606.17530)

## Summary

This paper evaluates the impact of New York City's 2025 cordon-based congestion pricing policy on urban mobility patterns. By employing time series foundation models to generate probabilistic counterfactuals, the authors overcome the lack of credible control groups typically associated with large-scale urban interventions. Their analysis reveals significant transit ridership gains and spatially uneven travel demand reductions across neighborhoods, offering a scalable method for policy impact assessment.

## Key Contributions

- Introduces a framework using time series foundation models to generate probabilistic counterfactual demand forecasts for urban mobility interventions where control groups are missing.
- Demonstrates that NYC congestion pricing led to significant increases in bus and subway ridership and a modest decline in overall travel demand.
- Identifies spatially heterogeneous and socio-demographically uneven adaptation patterns resulting from the congestion pricing program.

## Open Questions & Future Work

- [[limitations-of-aggregate-counterfactual-forecasting]]

## Archivist Review

The paper proposes a specific application of time series foundation models (TSFMs) as a counterfactual generation tool for urban policy evaluation. I have approved the open question regarding the limitations of aggregate-level counterfactuals, as this is a fundamental research challenge in applying generative forecasting models to causal policy analysis. I have opted not to approve any concepts, as the proposed framework is an application of existing TSFM technology rather than a novel foundational mechanism in the sense defined by the vault.

### Approved Open Questions
- Limitations of aggregate counterfactual forecasting: This identifies a critical bottleneck in the reliability of observational causal inference for urban policy evaluation, distinguishing between statistical forecasting performance and policy impact validity.

## Links

- [Abstract](https://arxiv.org/abs/2606.17530)
- [PDF](https://arxiv.org/pdf/2606.17530)

