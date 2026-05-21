---
# CSL-compatible fields
title: "TSLANet: Rethinking Transformers for Time Series Representation Learning"
author:
  - literal: "Emadeldeen Eldele"
  - literal: "Mohamed Ragab"
  - literal: "Zhenghua Chen"
  - literal: "Min Wu"
  - literal: "Xiaoli Li"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2404.08472"

# Custom fields
paper_id: "2404.08472"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "classification"
  - "self-supervised-learning"
  - "efficient-transformer"
  - "fourier-neural-operator"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-spectral-block"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:25:53Z"
created_at: "2026-05-21T08:25:53Z"
---

# TSLANet: Rethinking Transformers for Time Series Representation Learning

**Authors**: Emadeldeen Eldele, Mohamed Ragab, Zhenghua Chen, Min Wu, Xiaoli Li
**Date**: 2026-05-18
**Paper ID**: [openalex:2404.08472](https://arxiv.org/abs/2404.08472)

## Summary

TSLANet is a lightweight convolutional framework designed to overcome the efficiency and robustness limitations of Transformers in time series analysis. By leveraging a novel Adaptive Spectral Block, the model processes features in both temporal and frequency domains while applying adaptive thresholding to mitigate noise. It further incorporates an Interactive Convolution Block and self-supervised learning to improve temporal representation, achieving state-of-the-art results across diverse time series tasks including forecasting, classification, and anomaly detection.

## Key Contributions

- Proposed TSLANet, a lightweight and universal convolutional framework for time series analysis that avoids the computational overhead of Transformers.
- Introduced the Adaptive Spectral Block, which utilizes Fourier analysis to perform adaptive thresholding for noise suppression and capture cross-domain dependencies.
- Achieved state-of-the-art performance across forecasting, classification, and anomaly detection benchmarks with superior robustness to noise.

## Open Questions & Future Work

- [[cnn-long-horizon-scaling-limitations]]

## Key Concepts

- [[adaptive-spectral-block]]: A module that uses Fourier analysis to perform feature representation in both temporal and frequency domains with noise-suppressing adaptive thresholding.

## Archivist Review

The 'Adaptive Spectral Block' is approved as a representative innovation in the ongoing trend of spectral-domain time series modeling. The 'CNN Long-Horizon Scaling Limitations' open question captures the architectural trade-off between convolutional efficiency and global dependency modeling identified by the authors. The 'Interactive Convolution Block' was rejected as a subcomponent lack of unique identity compared to general convolutional refinement strategies.

### Approved Concepts
- Adaptive Spectral Block: It is the core architectural innovation enabling simultaneous modeling of local and global dependencies with noise suppression via adaptive thresholding.

### Approved Open Questions
- CNN Long-Horizon Scaling Limitations: Bridging the gap between the computational efficiency of CNNs and the global modeling capability of Transformers is critical for developing universal, lightweight forecasting frameworks.

## Links

- [Abstract](https://arxiv.org/abs/2404.08472)
- [PDF](https://arxiv.org/pdf/2404.08472)

