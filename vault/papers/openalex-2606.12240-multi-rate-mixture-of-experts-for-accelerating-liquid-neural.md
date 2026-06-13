---
# CSL-compatible fields
title: "Multi-Rate Mixture of Experts for Accelerating Liquid Neural Network Training"
author:
  - literal: "Shilong Zong"
  - literal: "Almuatazbellah Boker"
  - literal: "Hoda Eldardiry"
issued:
  date-parts:
    - [2026, 6, 10]
url: "https://arxiv.org/abs/2606.12240"

# Custom fields
paper_id: "2606.12240"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "mixture-of-experts"
  - "attention-mechanism"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multi-rate-mixture-of-experts-mr-moe"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-13T08:16:44Z"
created_at: "2026-06-13T08:16:44Z"
---

# Multi-Rate Mixture of Experts for Accelerating Liquid Neural Network Training

**Authors**: Shilong Zong, Almuatazbellah Boker, Hoda Eldardiry
**Date**: 2026-06-10
**Paper ID**: [openalex:2606.12240](https://arxiv.org/abs/2606.12240)

## Summary

The paper introduces the Multi-Rate Mixture-of-Experts (MR-MoE) framework to address the limitations of standard Liquid Neural Networks (LNNs) in capturing heterogeneous temporal dynamics. By employing multiple LNN experts operating at distinct time scales and an adaptive gating network, the model effectively separates fast and slow temporal patterns. Further, the integration of feature-level and temporal attention mechanisms enables the model to ignore noisy inputs and focus on salient historical states, resulting in superior predictive performance and efficiency on multivariate time-series benchmarks.

## Key Contributions

- Introduces the Multi-Rate Mixture-of-Experts (MR-MoE) framework, which leverages LNN-based experts specialized for different time scales to model heterogeneous time-series dynamics.
- Integrates feature-level and temporal attention mechanisms into the LNN backbone to enhance robustness against noise and improve the modeling of long-range dependencies.
- Demonstrates consistent improvements in AUROC and AUPRC over monolithic LNNs, standard MoE models, and LSTMs on multivariate time-series prediction tasks while maintaining high computational efficiency.

## Open Questions & Future Work

- [[decoupled-multi-time-scale-training]]
- [[learnable-time-constants-lnn]]

## Key Concepts

- [[multi-rate-mixture-of-experts-mr-moe]]: A Liquid Neural Network framework where multiple experts specialize in distinct temporal scales, enabling the separation of fast-changing dynamics from slow-evolving trends.

## Archivist Review

The paper introduces a coherent framework for multi-scale temporal modeling by extending Liquid Neural Networks with Mixture-of-Experts. The proposed MR-MoE architecture and its associated open questions regarding training decoupling and learnable time constants are highly relevant to advancing continuous-time time-series modeling. I have approved the MR-MoE concept and two foundational open questions regarding its optimization and adaptability.

### Approved Concepts
- Multi-Rate Mixture-of-Experts (MR-MoE): The framework provides a novel mechanism to handle heterogeneous temporal scales in continuous-time dynamics models, which is a significant challenge in time-series forecasting.

### Approved Open Questions
- Decoupled Multi-Time-Scale Training Strategy: Decoupling training is critical for improving the specialized performance of experts and ensuring the model architecture successfully separates dynamics as intended by the multi-rate design.
- Learnable Time Constants in LNNs: Making time constants learnable is essential for reducing manual hyperparameter tuning and enabling the model to capture the true underlying temporal structure of the input data.

## Links

- [Abstract](https://arxiv.org/abs/2606.12240)
- [PDF](https://arxiv.org/pdf/2606.12240)

