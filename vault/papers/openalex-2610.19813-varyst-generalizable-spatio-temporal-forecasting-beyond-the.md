---
# CSL-compatible fields
title: "VaryST: Generalizable Spatio-Temporal Forecasting Beyond the Closed-World Setting"
author:
  - literal: "Shengnan Guo"
  - literal: "Jinjun Cheng"
  - literal: "Xiaowei Mao"
  - literal: "Jianhao Zhang"
  - literal: "Haochen Lv"
  - literal: "Yang Jiang"
  - literal: "YiHeng Huang"
  - literal: "Yan Lin"
  - literal: "Youfang Lin"
  - literal: "Huaiyu Wan"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.19813"

# Custom fields
paper_id: "2610.19813"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "few-shot-learning"
  - "zero-shot-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "varyst"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:55:27Z"
created_at: "2026-10-17T08:55:27Z"
---

# VaryST: Generalizable Spatio-Temporal Forecasting Beyond the Closed-World Setting

**Authors**: Shengnan Guo, Jinjun Cheng, Xiaowei Mao, Jianhao Zhang, Haochen Lv, Yang Jiang, YiHeng Huang, Yan Lin, Youfang Lin, Huaiyu Wan
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.19813](https://arxiv.org/abs/2610.19813)

## Summary

This paper introduces VaryST, a compact spatio-temporal forecasting model that overcomes the closed-world limitations of traditional models by dynamically adapting to changing temporal distributions, evolving spatial domains, and fluctuating observation availability. VaryST achieves robust zero- and few-shot generalization through long-term history-derived node representations, dynamic functional support node selection, and selective historical patch masking during training. Extensive evaluations across six real-world datasets and seventeen baselines show superior in-domain accuracy and out-of-domain robustness.

## Key Contributions

- Proposes VaryST, a compact spatio-temporal forecasting model designed to generalize beyond closed-world settings by dynamically constructing predictive context from long-term observations.
- Implements node representations derived from long-term histories to adapt to temporal changes and dynamic functional support node selection to handle spatial changes.
- Employs a selective historical patch-masking strategy during training to maintain robustness under varying observation availability.
- Demonstrates through extensive experiments on six real-world datasets and seventeen baselines that VaryST achieves strong in-domain accuracy alongside robust zero- and few-shot generalization.

## Open Questions & Future Work

- [[generalizable-spatio-temporal-forecasting-beyond-closed-world]]

## Key Concepts

- [[varyst]]: A compact spatio-temporal forecasting model designed to generalize across changing temporal distributions, spatial domains, and observation availability.

## Archivist Review

Approved the core model concept 'VaryST' and the open question regarding open-world spatio-temporal forecasting generalization. Adhered strictly to the scarcity policy and skill review guidelines.

### Approved Concepts
- VaryST: VaryST is the core model proposed in the paper for generalizable spatio-temporal forecasting beyond the closed-world setting.

### Approved Open Questions
- Generalizable Spatio-Temporal Forecasting: This is technically important because moving beyond closed-world assumptions in spatio-temporal machine learning requires robust representations that are invariant or dynamically adaptive to multi-dimensional distribution shifts.

## Links

- [Abstract](https://arxiv.org/abs/2610.19813)
- [PDF](https://arxiv.org/pdf/2610.19813)

