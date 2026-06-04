---
# CSL-compatible fields
title: "When Tabular Foundation Models Transfer Across Modalities: A Systematic Evaluation Across 95 Datasets, 7 Modalities, and Two Regimes"
author:
  - literal: "Julien Lafrance"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.02106"

# Custom fields
paper_id: "2606.02106"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "foundation-model"
  - "in-context-learning"
  - "multimodal"
  - "benchmark"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tabicl"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:46:43Z"
created_at: "2026-06-04T08:46:43Z"
---

# When Tabular Foundation Models Transfer Across Modalities: A Systematic Evaluation Across 95 Datasets, 7 Modalities, and Two Regimes

**Authors**: Julien Lafrance
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.02106](https://arxiv.org/abs/2606.02106)

## Summary

This paper presents TabICL, a unified classification pipeline that enables in-context inference across seven distinct data modalities using tabular foundation models. By combining Equiangular Tight Frame (ETF) preprocessing with frozen feature extraction, the approach consistently achieves competitive performance against highly-tuned baselines across 95 diverse datasets. The study also provides practical guidelines for model calibration, deployment, and performance forecasting, offering a significant speedup in training and inference compared to full-backbone fine-tuning.

## Key Contributions

- Introduces TabICL, a universal classification pipeline that maps diverse signal modalities (vision, audio, speech, text, molecular, time-series, tabular) to fixed vector representations for in-context tabular foundation model inference.
- Provides a systematic evaluation on 95 datasets, demonstrating that the pipeline achieves competitive performance while running 4-200x faster than traditional full-backbone fine-tuning.
- Establishes a rigorous methodology for performance benchmarking by comparing results against the strongest lightweight tuned baseline on frozen features.
- Proposes a post-hoc rescaling technique for ETF-processed features to restore well-calibrated probabilities, enabling confidence-gated deployment.

## Open Questions & Future Work

- [[saturation-aware-preprocessing-skip-rule]]

## Key Concepts

- [[tabicl]]: A universal classification pipeline combining Equiangular Tight Frame (ETF) preprocessing and tabular foundation models for cross-modal in-context inference.

## Archivist Review

I approved the TabICL concept as it represents a distinct, reusable paradigm for unifying diverse signal modalities for tabular-based in-context learning. The open question regarding a saturation-aware skip rule was approved because it addresses a critical, non-trivial limitation in feature-based pipelines where additional processing can introduce noise or redundancy when features are already near-optimal. I rejected no other candidates as the provided list was already very selective.

### Approved Concepts
- TabICL: It provides a unified, cross-modal classification framework that leverages tabular foundation models via in-context learning.

### Approved Open Questions
- Saturation-aware preprocessing skip rule: Defining the boundaries of when preprocessing architectures provide diminishing or negative returns is essential for robust, automated deployment of foundation models.

## Links

- [Abstract](https://arxiv.org/abs/2606.02106)
- [PDF](https://arxiv.org/pdf/2606.02106)

