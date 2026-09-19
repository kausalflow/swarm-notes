---
# CSL-compatible fields
title: "QUALS: Corpus Equilibrium for Universal Forecasting via Pattern Quantization and Learnability Synchronization"
author:
  - literal: "Yujie Li"
  - literal: "Zezhi Shao"
  - literal: "Chengqing Yu"
  - literal: "Yisong Fu"
  - literal: "Weijie Zhu"
  - literal: "Yifan Du"
  - literal: "Jilin Hu"
  - literal: "Bin Yang"
  - literal: "Yongjun Xu"
  - literal: "Fei Wang"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.20156"

# Custom fields
paper_id: "2609.20156"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "pre-training"
  - "zero-shot-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quals"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-19T09:03:51Z"
created_at: "2026-09-19T09:03:51Z"
---

# QUALS: Corpus Equilibrium for Universal Forecasting via Pattern Quantization and Learnability Synchronization

**Authors**: Yujie Li, Zezhi Shao, Chengqing Yu, Yisong Fu, Weijie Zhu, Yifan Du, Jilin Hu, Bin Yang, Yongjun Xu, Fei Wang
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.20156](https://arxiv.org/abs/2609.20156)

## Summary

The paper introduces QUALS, a large-scale time series corpus equilibrium framework that improves data efficiency and zero-shot forecasting performance for foundation models. QUALS consists of two core components: a pattern quantization framework that decodes heterogeneous patterns using vector quantization and uniform binning, and a learnability synchronization framework that calibrates sampling weights to bridge optimization gaps across motifs. Extensive experiments show that pre-training on QUALS achieves superior zero-shot performance using only a small fraction of the training data.

## Key Contributions

- Proposes QUALS, a large-scale time series corpus equilibrium framework designed to address data diversity and optimize training data efficiency for time series foundation models.
- Introduces a pattern quantization framework that decodes heterogeneous patterns from mixed corpora using vector quantization and uniform binning.
- Develops a learnability synchronization framework that calibrates sampling weights for heterogeneous patterns to bridge the optimization gap between simple and complex motifs.
- Demonstrates that pre-training on QUALS achieves superior zero-shot forecasting performance while using only a small fraction of the original training data.

## Open Questions & Future Work

- [[corpus-equilibrium-multimodal-scaling]]

## Key Concepts

- [[quals]]: A large-scale time series corpus equilibrium framework that uses pattern quantization and learnability synchronization to maximize data efficiency for zero-shot forecasting.

## Archivist Review

Approved the core framework concept (QUALS) as a distinctive and reusable data curation mechanism for time series pre-training, along with a pertinent open question regarding corpus equilibrium scaling. No evaluation datasets were mentioned.

### Approved Concepts
- QUALS: Introduces a novel corpus equilibrium framework for time series foundation models combining pattern quantization and learnability synchronization.

### Approved Open Questions
- Corpus Equilibrium for Multimodal Forecasting: Understanding how data diversity and learnability interact in multi-modal or ultra-large scale forecasting models is crucial for building truly efficient foundation models.

## Links

- [Abstract](https://arxiv.org/abs/2609.20156)
- [PDF](https://arxiv.org/pdf/2609.20156)

