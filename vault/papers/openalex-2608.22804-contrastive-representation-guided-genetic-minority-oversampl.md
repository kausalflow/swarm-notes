---
# CSL-compatible fields
title: "Contrastive Representation-Guided Genetic Minority Oversampling for Imbalanced Time-Series Classification"
author:
  - literal: "Wenbin Pei"
  - literal: "Yunrong Hao"
  - literal: "Zhen Liu"
  - literal: "Guan Wang"
  - literal: "Bing Xue"
  - literal: "Yiu-Ming Cheung"
  - literal: "Qiang Zhang"
  - literal: "Wenbin Pei"
  - literal: "Yunrong Hao"
  - literal: "Zhen Liu"
  - literal: "Guan Wang"
  - literal: "Bing Xue"
  - literal: "Yiu-Ming Cheung"
  - literal: "Qiang Zhang"
issued:
  date-parts:
    - [2026, 8, 24]
url: "https://arxiv.org/abs/2608.22804"

# Custom fields
paper_id: "2608.22804"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "text-classification"
  - "contrastive-learning"
  - "few-shot-learning"
  - "data-augmentation"
  - "synthetic-data-augmentation"
  - "evolutionary-algorithm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fremgp"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-27T15:58:23Z"
created_at: "2026-08-27T15:58:23Z"
---

# Contrastive Representation-Guided Genetic Minority Oversampling for Imbalanced Time-Series Classification

**Authors**: Wenbin Pei, Yunrong Hao, Zhen Liu, Guan Wang, Bing Xue, Yiu-Ming Cheung, Qiang Zhang, Wenbin Pei, Yunrong Hao, Zhen Liu, Guan Wang, Bing Xue, Yiu-Ming Cheung, Qiang Zhang
**Date**: 2026-08-24
**Paper ID**: [openalex:2608.22804](https://arxiv.org/abs/2608.22804)

## Summary

This paper introduces FreMGP, a frequency-domain representation-guided multi-tree genetic programming approach designed to address severe class imbalance in time-series classification. It leverages a contrastive learning-based frequency-domain class-discriminative representation module to guide evolutionary search, thereby overcoming the limited generalization and poor diversity of conventional interpolation-based and generative oversampling methods. Experiments show that FreMGP effectively enhances the classification performance of both general machine learning and deep learning models.

## Key Contributions

- Proposes FreMGP, a Frequency-domain representation-guided Multi-tree Genetic Programming-based oversampling approach for imbalanced time-series classification.
- Develops a frequency-domain class-discriminative representation module based on contrastive learning to guide evolutionary search toward generating high-quality synthetic time-series samples.
- Demonstrates that FreMGP outperforms existing oversampling methods across multiple classifiers including both general machine learning and deep learning models.

## Open Questions & Future Work

- [[efficient-evolutionary-oversampling-strategies]]

## Key Concepts

- [[fremgp]]: A frequency-domain representation-guided multi-tree genetic programming oversampling method for imbalanced time-series classification.

## Archivist Review

Approved the novel FreMGP framework for handling class imbalance in time-series via contrastive-guided genetic programming, along with the specific open question regarding the computational efficiency of evolutionary oversampling strategies.

### Approved Concepts
- Frequency-domain representation-guided Multi-tree Genetic Programming-based oversampling approach (FreMGP): Core methodological framework proposed in the paper for handling severe class imbalance in time-series classification via contrastive representation guidance and multi-tree genetic programming.

### Approved Open Questions
- Efficient Evolutionary Oversampling Strategies: High computational complexity is a major bottleneck limiting the practical scalability of evolutionary computation methods in large-scale machine learning data augmentation tasks.

## Links

- [Abstract](https://arxiv.org/abs/2608.22804)
- [PDF](https://arxiv.org/pdf/2608.22804)

