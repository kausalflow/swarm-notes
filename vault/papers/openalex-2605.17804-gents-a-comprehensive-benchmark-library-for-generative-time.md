---
# CSL-compatible fields
title: "GenTS: A Comprehensive Benchmark Library for Generative Time Series Models"
author:
  - literal: "Chenxi Wang"
  - literal: "Xiaorong Wang"
  - literal: "Peiyang Li"
  - literal: "Yi Wang"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.17804"

# Custom fields
paper_id: "2605.17804"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "generative-adversarial-network"
  - "diffusion-model"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:28:53Z"
created_at: "2026-05-21T08:28:53Z"
---

# GenTS: A Comprehensive Benchmark Library for Generative Time Series Models

**Authors**: Chenxi Wang, Xiaorong Wang, Peiyang Li, Yi Wang
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.17804](https://arxiv.org/abs/2605.17804)

## Summary

GenTS is a comprehensive benchmark library designed to address the lack of standardized workflows for generative time series models. Unlike traditional libraries focused on discriminative tasks like MSE-based forecasting, GenTS supports complex generative paradigms such as diffusion and adversarial learning. The framework provides modular, extensible tools for preprocessing, model evaluation, and systematic benchmarking across various time series analysis tasks.

## Key Contributions

- Introduces GenTS, a modular benchmark library tailored specifically for generative time series modeling paradigms rather than traditional discriminative tasks.
- Provides a unified pipeline for data preprocessing, model integration, and evaluation that supports diverse approaches including diffusion and adversarial training.
- Conducts a systematic benchmarking study on generative models across multiple tasks and provides actionable guidelines for model selection and future research.

## Open Questions & Future Work

- [[robust-generative-time-series-evaluation]]
- [[online-adaptive-generative-time-series]]

## Archivist Review

The paper introduces a library (GenTS) which serves as a software utility rather than a novel conceptual or algorithmic contribution. I have approved two open questions that capture the fundamental research challenges identified in the benchmarking study, while rejecting the library itself and its sub-components as they are considered local software tooling rather than foundational research concepts.

### Approved Open Questions
- Robust Generative Evaluation Metrics: The field lacks a standardized and robust method for evaluating generative quality, which directly impacts the community's ability to rank models fairly and meaningfully across diverse time series domains.
- Online Adaptive Generative Paradigms: Bridging this gap is essential for deploying advanced generative models in latency-sensitive, real-world production environments.

## Links

- [Abstract](https://arxiv.org/abs/2605.17804)
- [PDF](https://arxiv.org/pdf/2605.17804)

