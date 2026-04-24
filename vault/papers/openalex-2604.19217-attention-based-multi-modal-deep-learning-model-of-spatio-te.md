---
# CSL-compatible fields
title: "Attention-based Multi-modal Deep Learning Model of Spatio-temporal Crop Yield Prediction with Satellite, Soil and Climate Data"
author:
  - literal: "Gopal Krishna Shyam"
  - literal: "Ila Chandrakar"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2604.19217"

# Custom fields
paper_id: "2604.19217"
paper_source: "openalex"
domain: "nlp"
tags:
  - "attention-mechanism"
  - "multimodal"
  - "convolutional-neural-network"
  - "time-series"
  - "forecasting"
architectures:
  - "cnn"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T07:00:29Z"
created_at: "2026-04-24T07:00:29Z"
---

# Attention-based Multi-modal Deep Learning Model of Spatio-temporal Crop Yield Prediction with Satellite, Soil and Climate Data

**Authors**: Gopal Krishna Shyam, Ila Chandrakar
**Date**: 2026-04-21
**Paper ID**: [openalex:2604.19217](https://arxiv.org/abs/2604.19217)

## Summary

This paper introduces the Attention-Based Multi-Modal Deep Learning Framework (ABMMDLF) for spatio-temporal crop yield prediction. By fusing satellite imagery, time-series meteorological data, and static soil properties, the model captures dynamic environmental relationships often missed by conventional approaches. The architecture leverages CNNs for spatial feature extraction and a temporal attention mechanism to weight critical phenological periods, significantly improving predictive performance over baseline models.

## Key Contributions

- Introduces ABMMDLF, a multimodal deep learning framework that integrates multi-year satellite imagery, time-series meteorological data, and soil properties for crop yield prediction.
- Utilizes a CNN-based spatial feature extractor combined with a temporal attention mechanism to prioritize key phenological periods.
- Achieves an R^2 score of 0.89, outperforming baseline models in spatio-temporal crop yield prediction.

## Open Questions & Future Work

- [[federated-learning-for-agricultural-data-privacy]]

## Archivist Review

The paper presents a standard application of multimodal deep learning for domain-specific forecasting. The proposed architecture (CNN + Temporal Attention) is well-understood and not a novel research concept. I have approved the open question regarding federated learning as it identifies a specific barrier to scaling predictive modeling in this domain, while rejecting the blockchain suggestion as it lies outside the core ML research focus.

### Approved Open Questions
- Federated Learning for Agricultural Privacy: This is a critical bottleneck for scaling agricultural AI models, as organizations are often reluctant to pool proprietary or sensitive field-level data.

### Rejected Candidates
- [open_question] Blockchain-Integrated Agricultural Data Security (`blockchain-integrated-agricultural-data-security`) - low_impact: The proposed integration of blockchain into data pipelines is a systemic architecture choice rather than a foundational machine learning or time-series research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2604.19217)
- [PDF](https://arxiv.org/pdf/2604.19217)

