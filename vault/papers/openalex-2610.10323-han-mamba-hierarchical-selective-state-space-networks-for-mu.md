---
# CSL-compatible fields
title: "HAN-Mamba: Hierarchical Selective State Space Networks for Multi-Scale Financial Volatility Forecasting"
author:
  - literal: "Mihai Bogdan Deaconu"
  - literal: "Ioan Daniel Pop"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.10323"

# Custom fields
paper_id: "2610.10323"
paper_source: "openalex"
domain: "finance"
tags:
  - "mamba"
  - "state-space-model"
  - "ssm"
  - "long-context"
  - "forecasting"
  - "benchmark"
architectures:
  - "mamba"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:35:59Z"
created_at: "2026-10-09T11:35:59Z"
---

# HAN-Mamba: Hierarchical Selective State Space Networks for Multi-Scale Financial Volatility Forecasting

**Authors**: Mihai Bogdan Deaconu, Ioan Daniel Pop
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.10323](https://arxiv.org/abs/2610.10323)

## Summary

HAN-Mamba is a hybrid model for multi-scale financial volatility forecasting that replaces quadratic Transformer encoders in the hierarchical HAN-T architecture with selective state space (Mamba) encoders, retaining a lightweight attention fuser. The model naturally captures persistent memory and abrupt regime shifts in volatility through input-dependent gating. Evaluated on the Optiver Realized Volatility Prediction benchmark, HAN-Mamba achieves superior accuracy with 33% fewer parameters and scales efficiently to longer high-frequency contexts.

## Key Contributions

- Proposes HAN-Mamba, a hybrid architecture combining linear-time selective state space encoders with a permutation-invariant attention fuser for multi-scale financial volatility forecasting.
- Improves mean RMSPE to 0.1942 (vs. 0.1965 for HAN-T) on the Optiver Realized Volatility Prediction benchmark while using 33% fewer parameters.
- Extends high-frequency context from 60 to 240 buckets without saturating, reducing RMSPE further to 0.1927 and supporting constant-time streaming updates.

## Archivist Review

After reviewing the paper and vault guidelines, no concepts or open questions met the stringent bar for standalone vault notes. The proposed architecture variant (HAN-Mamba) is closely tied to prior work (HAN-T) and specific financial volatility settings, while the open question regarding bidirectional SSMs is too speculative and paper-internal to warrant a permanent vault entry.

### Rejected Candidates
- [open_question] Bidirectional SSMs for Volatility (`bidirectional-ssm-volatility-volatility-forecasting`) - paper_local: paper_local

## Links

- [Abstract](https://arxiv.org/abs/2610.10323)
- [PDF](https://arxiv.org/pdf/2610.10323)

