---
# CSL-compatible fields
title: "Scale-Aware Pretraining of Time Series Foundation Models via Multi-Patch Token Alignment and Hybrid Masking"
author:
  - literal: "Taihua Chen"
  - literal: "Xiang Ma"
  - literal: "Yixin Zhang"
  - literal: "Tailin Zhan"
  - literal: "Manyu Sun"
  - literal: "Lizhen Cui"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.20005"

# Custom fields
paper_id: "2608.20005"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "pre-training"
  - "foundation-model"
  - "patching"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "scale-aware-token-alignment"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:19:29Z"
created_at: "2026-08-23T05:19:29Z"
---

# Scale-Aware Pretraining of Time Series Foundation Models via Multi-Patch Token Alignment and Hybrid Masking

**Authors**: Taihua Chen, Xiang Ma, Yixin Zhang, Tailin Zhan, Manyu Sun, Lizhen Cui
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.20005](https://arxiv.org/abs/2608.20005)

## Summary

Pretraining time series foundation models across heterogeneous datasets with varying sampling frequencies often suffers from fragmented representations or rigid fixed patch sizes. To resolve this, the authors propose SATS, which features a scale-aware token alignment mechanism utilizing a contrastive-inspired regularizer to align representation spaces across different patch scales. Additionally, a hybrid masking strategy combining random and contiguous masking is introduced to capture multi-scale temporal patterns. Extensive experiments show SATS achieves state-of-the-art performance on LSTF and GIFT-Eval benchmarks with significantly higher efficiency.

## Key Contributions

- Proposes SATS, a scale-aware pretraining framework for time series foundation models that treats patch size as an explicit notion of scale.
- Introduces a contrastive-inspired alignment regularizer to harmonize representation spaces across heterogeneous sampling frequencies and patch sizes.
- Employs a hybrid masking strategy combining random and contiguous masking to capture multi-scale temporal structures.
- Achieves a 9.2% improvement in MSE and an 8.3% gain in GIFT-Eval MASE over competitive baselines while boosting model efficiency by 65.6%.

## Key Concepts

- [[scale-aware-token-alignment]]: A mechanism treating patch size as an explicit notion of scale and using contrastive-inspired alignment to unify representation spaces across heterogeneous sampling frequencies.

## Archivist Review

Approved the central scale-aware token alignment mechanism as a reusable concept for multi-scale time series foundation model pretraining, while rejecting the hybrid masking subcomponent as a standard modeling variation. No standalone datasets or open questions met the stringent inclusion thresholds.

### Approved Concepts
- Scale-Aware Token Alignment: Serves as the core novelty for handling varying sampling frequencies across heterogeneous time series datasets by aligning representation spaces.

### Rejected Candidates
- [concept] Hybrid Masking Strategy (`hybrid-masking-strategy`) - subcomponent_of_broader_mechanism: Combining random and contiguous masking is a standard technique variant rather than a uniquely novel foundational primitive.

## Links

- [Abstract](https://arxiv.org/abs/2608.20005)
- [PDF](https://arxiv.org/pdf/2608.20005)

