---
# CSL-compatible fields
title: "UTOPYA: A Multimodal Deep Learning Framework for Physics-Informed Anomaly Detection and Time-Series Prediction"
author:
  - literal: "Robson W. S. Pessoa"
  - literal: "Julien Amblard"
  - literal: "Alessandra Russo"
  - literal: "Idelfonso B. R. Nogueira"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.18188"

# Custom fields
paper_id: "2605.18188"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
  - "multimodal"
  - "physics-informed-machine-learning"
  - "forecasting"
  - "attention-mechanism"
  - "curriculum-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "utopya-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:31:07Z"
created_at: "2026-05-21T08:31:07Z"
---

# UTOPYA: A Multimodal Deep Learning Framework for Physics-Informed Anomaly Detection and Time-Series Prediction

**Authors**: Robson W. S. Pessoa, Julien Amblard, Alessandra Russo, Idelfonso B. R. Nogueira
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.18188](https://arxiv.org/abs/2605.18188)

## Summary

UTOPYA is a multimodal deep learning framework designed for simultaneous anomaly detection, time-series prediction, and phase classification in batch distillation processes. It fuses eight data modalities using FiLM-conditioned cross-modal attention and gated fusion, while incorporating physics-informed regularization to maintain thermodynamic constraints. Evaluated on the Arweiler et al. (2026) batch distillation dataset, UTOPYA significantly outperforms standard baselines like PCA and LSTM autoencoders, proving that static context integration is vital for high-performance process monitoring. The study further clarifies the efficacy of various training strategies, revealing that several standard regularization techniques fail in data-scarce process monitoring tasks.

## Key Contributions

- Introduces UTOPYA, a 15.2M-parameter multimodal framework that achieves a window-level test AUROC of 0.832 for anomaly detection in batch distillation.
- Proposes a physics-informed regularisation scheme enforcing temporal smoothness and thermodynamic monotonicity, combined with a curriculum learning strategy based on physical difficulty.
- Demonstrates that static context via FiLM conditioning is the critical enabler for performance, providing a +0.145 AUROC lift over unimodal baselines.
- Provides a comprehensive negative results analysis showing that common regularization techniques like Mixup and stochastic weight averaging degrade generalization in this data-scarce industrial context.

## Open Questions & Future Work

- [[phase-dependent-physics-constraints]]

## Key Concepts

- [[utopya-framework]]: A multimodal framework for joint anomaly detection and forecasting in transient industrial processes, utilizing FiLM-conditioned attention and physics-constrained training.

## Archivist Review

I approved the UTOPYA framework as a specific architectural pattern for industrial multimodal process monitoring. I also approved the open question regarding phase-dependent physics constraints because it identifies a critical failure mode of standard physics-informed training when applied to non-steady-state industrial dynamics. Other candidates were either too broad or did not meet the archival standard for standalone novelty.

### Approved Concepts
- UTOPYA Framework: UTOPYA represents a specialized multimodal architecture design for high-dimensional, multi-sensor industrial batch processes, explicitly integrating physics-informed regularization with cross-modal fusion.

### Approved Open Questions
- Adaptive Physics-Informed Constraints: This is a fundamental limitation in applying physics-informed machine learning to entire industrial process lifecycles rather than isolated steady-state windows.

### Rejected Candidates
- [open_question] Cross-system transfer learning efficacy (`cross-system-transfer-learning-batch-distillation`) - generic: This is a generic request for cross-dataset generalization rather than a specific unresolved mechanism or fundamental research question.

## Links

- [Abstract](https://arxiv.org/abs/2605.18188)
- [PDF](https://arxiv.org/pdf/2605.18188)

