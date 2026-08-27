---
# CSL-compatible fields
title: "Modalities Should Talk to Each Other: Dual-Stream Multimodal Learning for Long-Horizon Influenza Forecasting"
author:
  - literal: "Seyed Mohammad Hossein Hashemi"
  - literal: "Mohsen Hooshmand"
  - literal: "Parvin Razzaghi"
issued:
  date-parts:
    - [2026, 8, 24]
url: "https://arxiv.org/abs/2608.23373"

# Custom fields
paper_id: "2608.23373"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
  - "dataset"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "dual-stream-attention"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-27T15:58:47Z"
created_at: "2026-08-27T15:58:47Z"
---

# Modalities Should Talk to Each Other: Dual-Stream Multimodal Learning for Long-Horizon Influenza Forecasting

**Authors**: Seyed Mohammad Hossein Hashemi, Mohsen Hooshmand, Parvin Razzaghi
**Date**: 2026-08-24
**Paper ID**: [openalex:2608.23373](https://arxiv.org/abs/2608.23373)

## Summary

The paper introduces Dual-Stream Attention (DSA), a multimodal deep learning framework for long-horizon influenza-like illness forecasting that bridges numerical epidemiological signals and noisy text headlines. By employing a bidirectional cross-modal attention mechanism, DSA allows numerical and textual streams to mutually condition each other before passing through a causal temporal model. Evaluated on the Time-MMD health-domain dataset and an external-geography dataset, DSA substantially outperforms existing transformer and language-model baselines for 12-week-ahead forecasting.

## Key Contributions

- Proposes Dual-Stream Attention (DSA), a multimodal deep learning framework for long-horizon influenza-like illness forecasting that uses bidirectional cross-modal attention between numerical and textual streams.
- Achieves a median test MSE of 0.416 on the Time-MMD health-domain dataset, outperforming iTransformer, TaTS, and GPT4MTS with mean-error reductions of 54.95%, 37.29%, and 67.23% for 12-week-ahead forecasting.
- Demonstrates robust generalizability, ranking first among nine evaluated baselines on an external-geography dataset and maintaining lower worst-window errors.
- Shows via perturbation-based faithfulness analysis that the learned cross-modal attention is functionally informative under targeted masking, with a stronger effect in the text-to-numerical direction.

## Open Questions & Future Work

- [[long-horizon-multimodal-forecasting-scaling]]

## Key Concepts

- [[dual-stream-attention]]: A multimodal deep learning framework that fuses numerical epidemiological signals and noisy text headlines via bidirectional cross-modal attention for long-horizon influenza forecasting.

## Archivist Review

Approved the central framework 'Dual-Stream Attention' and one open question concerning long-horizon multimodal forecasting scaling while rejecting subcomponents and datasets per vault guidelines.

### Approved Concepts
- Dual-Stream Attention: Introduces a bidirectional cross-modal conditioning mechanism specifically tailored for fusing numeric epidemiological signals and noisy text headlines in long-horizon influenza forecasting.

### Approved Open Questions
- Extending Multimodal Forecast Horizons: Extending forecast horizons is crucial for long-term public health planning and tests the scalability of cross-modal conditioning mechanisms over extended durations.

### Rejected Candidates
- [concept] Cross-Modal Attention (`cross-modal-attention`) - subcomponent_of_broader_mechanism: Standard attention mechanism name widely used across multimodal literature, lacking specific novelty to this paper alone.
- [dataset] Time-MMD (`time-mmd`) - not_reusable: Mentioned as a health-domain dataset but already standard or generic enough that it does not require a standalone permanent encyclopedic entry compared to foundational models.
- [open_question] Cross-Disease and Geographical Generalization (`cross-disease-geographical-generalization`) - low_impact: A bit broad and routine for empirical applications, lacking a specific architectural or theoretical bottleneck to track.

## Links

- [Abstract](https://arxiv.org/abs/2608.23373)
- [PDF](https://arxiv.org/pdf/2608.23373)

