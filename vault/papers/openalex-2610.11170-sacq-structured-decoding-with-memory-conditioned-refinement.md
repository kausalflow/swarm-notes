---
# CSL-compatible fields
title: "SACQ: Structured Decoding with Memory-Conditioned Refinement for Long-Horizon Forecasting"
author:
  - literal: "Guo Cheng"
  - literal: "Zhengzhuo Xu"
  - literal: "Chenchen Jing"
  - literal: "Jingyi Hou"
  - literal: "SACQ"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11170"

# Custom fields
paper_id: "2610.11170"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "long-context"
  - "attention-mechanism"
  - "patch-based-encoder"
  - "robustness"
  - "loss-function"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:52:50Z"
created_at: "2026-10-10T10:52:50Z"
---

# SACQ: Structured Decoding with Memory-Conditioned Refinement for Long-Horizon Forecasting

**Authors**: Guo Cheng, Zhengzhuo Xu, Chenchen Jing, Jingyi Hou, SACQ
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11170](https://arxiv.org/abs/2610.11170)

## Summary

Long-term time series forecasting models typically rely on a flattened readout head that implicitly couples future positions, making them sensitive to noise and input corruption. To address this, the authors introduce SACQ, a structured prediction head featuring a two-stage decoding pipeline with a coarse scaffold and memory-conditioned cross-attention refinement. Combined with a batch-adaptive scaled log-cosh loss, SACQ significantly improves robustness and accuracy across various backbones like PatchTST, DLinear, and patch-Mamba.

## Key Contributions

- Introduced SACQ, a structured decoding head replacing standard flatten readouts for long-term time series forecasting while keeping encoders unchanged.
- Employs a two-stage decoding pipeline featuring a coarse patch-grid scaffold followed by memory-conditioned cross-attention refinement with a learned per-patch gate.
- Proposes a batch-adaptive scaled log-cosh loss function to stabilize optimization and enhance robustness against noise and input corruption under long horizons.
- Demonstrated top-tier test MSE/MAE performance across PatchTST, DLinear, and patch-Mamba backbones with minimal parameter overhead.

## Archivist Review

Strictly evaluated the proposed open question and rejected it as standard incremental performance/latency tuning future work. No concepts or datasets met the strict novelty and reusability standards.

### Rejected Candidates
- [open_question] Low-Latency Structured Decoding Variants (`low-latency-structured-decoding`) - low_impact: Standard future work about reducing computational overhead and latency without a distinct, permanent theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.11170)
- [PDF](https://arxiv.org/pdf/2610.11170)

