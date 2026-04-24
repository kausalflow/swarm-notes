---
# CSL-compatible fields
title: "Calibrating Scientific Foundation Models with Inference-Time Stochastic Attention"
author:
  - literal: "Akash Yadav"
  - literal: "Taiwo A. Adebiyi"
  - literal: "Ruda Zhang"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2604.19530"

# Custom fields
paper_id: "2604.19530"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "attention-mechanism"
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "stochastic-attention"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T07:00:14Z"
created_at: "2026-04-24T07:00:14Z"
---

# Calibrating Scientific Foundation Models with Inference-Time Stochastic Attention

**Authors**: Akash Yadav, Taiwo A. Adebiyi, Ruda Zhang
**Date**: 2026-04-21
**Paper ID**: [openalex:2604.19530](https://arxiv.org/abs/2604.19530)

## Summary

Transformer-based scientific foundation models often struggle with calibrated uncertainty, relying on deterministic outputs that are unsuitable for high-stakes decision-making. This paper introduces Stochastic Attention, a lightweight inference-time modification that replaces traditional softmax weights with normalized multinomial samples. By tuning a single concentration parameter through a post-hoc objective, the model produces well-calibrated predictive ensembles without the computational overhead of full retraining. Empirical results demonstrate that this approach consistently outperforms traditional uncertainty-aware methods in sharpness and calibration across various scientific forecasting benchmarks.

## Key Contributions

- Proposes Stochastic Attention, an inference-time mechanism for transformer models that enables uncertainty quantification via randomized attention weights.
- Introduces a lightweight, univariate calibration objective for post-hoc tuning of the concentration parameter in Stochastic Attention.
- Demonstrates that Stochastic Attention yields superior calibration and sharper prediction intervals compared to existing uncertainty-aware baselines on scientific forecasting tasks.

## Key Concepts

- [[stochastic-attention]]: An inference-time modification for transformer architectures that replaces deterministic softmax attention weights with normalized multinomial samples to generate calibrated uncertainty ensembles.

## Archivist Review

I approved the Stochastic Attention concept because it introduces a novel, reusable inference-time uncertainty quantification mechanism that can be applied to diverse transformer architectures without retraining. The calibration objective was rejected as it is a specific technical implementation detail tied to the overarching Stochastic Attention framework. No datasets or open questions were approved as none met the strict criteria for standalone long-term value.

### Approved Concepts
- Stochastic Attention: Provides a method for post-hoc uncertainty quantification in frozen transformer models without requiring expensive model retraining.

### Rejected Candidates
- [concept] Stochastic Attention Calibration Objective (`stochastic-attention-calibration-objective`) - subcomponent_of_broader_mechanism: This is a sub-component of the primary Stochastic Attention mechanism and does not warrant a separate, permanent note.

## Links

- [Abstract](https://arxiv.org/abs/2604.19530)
- [PDF](https://arxiv.org/pdf/2604.19530)

