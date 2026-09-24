---
# CSL-compatible fields
title: "ShapeLex: Decoupling Local Shape Symbolization and Global Scale Modeling for Text-Controlled Time Series Generation"
author:
  - literal: "Subo Wei"
  - literal: "Jianqi Gao"
  - literal: "Mingyan Fan"
  - literal: "Shaorong Xie"
  - literal: "Xinzhi Wang"
  - literal: "Yongpeng Dong"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24003"

# Custom fields
paper_id: "2609.24003"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "generative-adversarial-network"
  - "autoregressive"
  - "mixture-of-experts"
  - "forecasting"
  - "evaluation"
  - "benchmark"
  - "multimodal"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "shapelex"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:38:11Z"
created_at: "2026-09-24T09:38:11Z"
---

# ShapeLex: Decoupling Local Shape Symbolization and Global Scale Modeling for Text-Controlled Time Series Generation

**Authors**: Subo Wei, Jianqi Gao, Mingyan Fan, Shaorong Xie, Xinzhi Wang, Yongpeng Dong
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24003](https://arxiv.org/abs/2609.24003)

## Summary

The authors propose ShapeLex, a novel framework for text-controlled time series generation that decouples local shape symbolization from global scale modeling. By inducing a reusable vocabulary of discrete shape units (such as rises and spikes) and using an autoregressive generator alongside a mixture-density scale head, ShapeLex effectively prevents the loss or misplacement of key local structures. Evaluations across twelve public datasets and downstream forecasting tasks show that ShapeLex outperforms existing coupled approaches.

## Key Contributions

- Proposes ShapeLex, a text-controlled time series generation framework that decouples discrete symbolization of local shapes from continuous modeling of global attributes.
- Introduces an interpretable symbolic space using a reusable vocabulary of discrete shape units (e.g., rises, spikes, sharp drops) learned from training data.
- Employs a mixture-density scale head to model overall level and volatility, restoring realistic global scale onto the composed shape skeletons.
- Demonstrates superior performance across twelve public datasets, real user-written text, and downstream forecasting tasks compared to existing methods.

## Open Questions & Future Work

- [[multivariate-text-controlled-time-series-generation]]

## Key Concepts

- [[shapelex]]: A text-controlled time series generation framework that decouples local discrete shape symbolization from global continuous scale modeling.

## Archivist Review

Approved the overarching framework concept 'ShapeLex' as it presents a distinct architectural decoupling of local shape symbolization and global scale modeling for text-controlled generation. Also approved the open question on extending this framework to multivariate settings, while rejecting the vocabulary enrichment question as standard incremental future work.

### Approved Concepts
- ShapeLex: Introduces a novel paradigm for text-controlled time series generation by decoupling local shape symbolization and global scale modeling.

### Approved Open Questions
- Multivariate Text-Controlled Time Series Generation: Multivariate time series generation introduces complex cross-channel dependencies and alignment challenges that univariate shape vocabularies cannot capture directly.

### Rejected Candidates
- [open_question] Rare Shape Vocabulary Enrichment (`rare-shape-vocabulary-enrichment`) - low_impact: Standard future work direction on expanding vocabulary coverage without a specific algorithmic breakthrough mechanism defined.

## Links

- [Abstract](https://arxiv.org/abs/2609.24003)
- [PDF](https://arxiv.org/pdf/2609.24003)

