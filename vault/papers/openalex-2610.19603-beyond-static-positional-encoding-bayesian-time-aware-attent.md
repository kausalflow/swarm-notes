---
# CSL-compatible fields
title: "Beyond Static Positional Encoding: Bayesian Time-aware Attention for Non-Stationary Long-term Time Series Forecasting"
author:
  - literal: "Xinjie Lan"
  - literal: "Yunbo Mei"
  - literal: "Leheng Zhou"
  - literal: "Hao Qi"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.19603"

# Custom fields
paper_id: "2610.19603"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "self-attention"
  - "time-series"
  - "forecasting"
  - "long-context"
  - "positional-encoding"
  - "mixture-of-experts"
  - "moe"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "bayesian-time-aware-attention"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:54:39Z"
created_at: "2026-10-17T08:54:39Z"
---

# Beyond Static Positional Encoding: Bayesian Time-aware Attention for Non-Stationary Long-term Time Series Forecasting

**Authors**: Xinjie Lan, Yunbo Mei, Leheng Zhou, Hao Qi
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.19603](https://arxiv.org/abs/2610.19603)

## Summary

This paper addresses the limitation of static positional encodings in non-stationary long-term time series forecasting by interpreting self-attention through a Bayesian posterior lens over attended positions. The authors derive a population-level ELBO that exposes the suboptimality of fixed temporal biases under heterogeneous temporal dynamics, and subsequently introduce Bayesian Time-aware Attention (BTA). BTA employs a mixture-of-experts router to dynamically combine temporal kernels and produce input-conditioned, head-specific positional biases, improving forecasting robustness across standard transformer backbones.

## Key Contributions

- Interprets self-attention as a Bayesian posterior over attended positions, unifying content priors and temporal-evidence likelihoods induced by positional encoding.
- Derives a population-level ELBO characterizing the limitations of static positional encoding under varying temporal dependence structures in non-stationary time series.
- Proposes Bayesian Time-aware Attention (BTA), leveraging a mixture-of-experts router to generate input-conditioned, head-specific positional biases.
- Demonstrates consistent performance improvements across multiple Transformer backbones on standard long-term time series forecasting benchmarks.

## Key Concepts

- [[bayesian-time-aware-attention]]: A self-attention mechanism that reformulates positional bias as a Bayesian posterior and uses a mixture-of-experts router to dynamically adapt temporal kernels for non-stationary time series forecasting.

## Archivist Review

Approved the central methodological contribution, Bayesian Time-aware Attention, as it provides a distinct, reusable probabilistic framing and adaptive MoE positional bias mechanism for non-stationary time series. No open questions or datasets met the strict novelty and standalone threshold.

### Approved Concepts
- Bayesian Time-aware Attention: Introduces a novel probabilistic formulation of self-attention incorporating a Bayesian posterior view of positional encoding and an MoE-based adaptive temporal kernel router for non-stationary time series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2610.19603)
- [PDF](https://arxiv.org/pdf/2610.19603)

