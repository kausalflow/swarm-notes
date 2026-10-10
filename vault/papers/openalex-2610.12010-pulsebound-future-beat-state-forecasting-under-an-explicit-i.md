---
# CSL-compatible fields
title: "PulseBound: Future-Beat State Forecasting Under an Explicit Information Boundary"
author:
  - literal: "Chenyang Xu"
  - literal: "Donglin Xie"
  - literal: "Xi Xiang"
  - literal: "Xiaoyu Li"
  - literal: "Yufan Lu"
  - literal: "Jiqiun Gao"
  - literal: "Yi Zhao"
  - literal: "Xin-Yi Li"
  - literal: "Guangpu Zhu"
  - literal: "Zijian Wang"
  - literal: "Xiwen Yang"
  - literal: "Dezhen Wang"
  - literal: "Lin Chen"
  - literal: "Shenda Hong"
  - literal: "Leilei Li"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.12010"

# Custom fields
paper_id: "2610.12010"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "representation-learning"
  - "pre-training"
  - "fine-tuning"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "pulsebound"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:53:08Z"
created_at: "2026-10-10T10:53:08Z"
---

# PulseBound: Future-Beat State Forecasting Under an Explicit Information Boundary

**Authors**: Chenyang Xu, Donglin Xie, Xi Xiang, Xiaoyu Li, Yufan Lu, Jiqiun Gao, Yi Zhao, Xin-Yi Li, Guangpu Zhu, Zijian Wang, Xiwen Yang, Dezhen Wang, Lin Chen, Shenda Hong, Leilei Li
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.12010](https://arxiv.org/abs/2610.12010)

## Summary

The paper introduces PulseBound, a representation learner for photoplethysmography (PPG) that prevents causal leakage by enforcing an explicit stored-window information boundary. By combining prefix-only normalization, suffix replacement, and aligned masking, PulseBound achieves stored-suffix invariance, ensuring that withheld future suffixes cannot influence model predictions or context. Evaluated on MIMIC and VitalDB groups, PulseBound significantly outperforms persistence baselines and achieves superior performance across 13 downstream tasks.

## Key Contributions

- Introduces PulseBound, a physiological representation learner for photoplethysmography (PPG) featuring an explicit stored-window information boundary to eliminate causal leakage.
- Achieves stored-suffix invariance, ensuring changes to withheld future suffixes do not alter forecast contexts or model predictions.
- Reduces nine-state transformed-space MAE relative to last-visible-beat persistence by 28.06% on MIMIC and 22.22% on VitalDB held-out groups.
- Outperforms baseline models across 13 downstream tasks under both frozen linear probing and full fine-tuning.

## Limitations

Future work could extend the stored-window information boundary to multi-modal physiological streams beyond photoplethysmography and electrocardiography.

## Open Questions & Future Work

- [[end-to-end-streaming-causality-ppg]]

## Key Concepts

- [[pulsebound]]: A photoplethysmography representation learner enforcing strict causal information access via an explicit stored-window boundary and stored-suffix invariance.

## Archivist Review

Approved the core concept PulseBound for its novel stored-suffix invariance and explicit stored-window information boundary mechanism. Approved one open question addressing end-to-end streaming causality in physiological signal modeling. All other dataset and implementation details were filtered out as paper-local or routine.

### Approved Concepts
- PulseBound: Central methodology of the paper, introducing an explicit stored-window information boundary and stored-suffix invariance for predictive photoplethysmography representation learning.

### Approved Open Questions
- End-to-End Streaming Causality for PPG: Crucial for deploying biosignal foundation models in real-time streaming clinical environments where raw physiological data streams continuously without pre-segmented windows.

## Links

- [Abstract](https://arxiv.org/abs/2610.12010)
- [PDF](https://arxiv.org/pdf/2610.12010)

