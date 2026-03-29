---
# CSL-compatible fields
title: "Spatiotemporal System Forecasting with Irregular Time Steps via Masked Autoencoder"
author:
  - literal: "Kewei Zhu"
  - literal: "Yanze Xin"
  - literal: "Jinwei Hu"
  - literal: "Xiaoyuan Cheng"
  - literal: "Yiming Yang"
  - literal: "Sibo Cheng"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25597"

# Custom fields
paper_id: "2603.25597"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "forecasting"
  - "convolutional-neural-network"
  - "attention-mechanism"
  - "self-supervised-learning"
architectures:
  - "cnn"
datasets:
  []
concept_slugs:
  - "physics-spatiotemporal-masked-autoencoder"
  - "irregular-time-step-mae-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:07:07Z"
created_at: "2026-03-29T06:07:07Z"
---

# Spatiotemporal System Forecasting with Irregular Time Steps via Masked Autoencoder

**Authors**: Kewei Zhu, Yanze Xin, Jinwei Hu, Xiaoyuan Cheng, Yiming Yang, Sibo Cheng
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25597](https://arxiv.org/abs/2603.25597)

## Summary

This paper introduces the Physics-Spatiotemporal Masked Autoencoder (P-STMAE) to address the challenge of forecasting high-dimensional dynamical systems where measurements occur at irregular time steps. The P-STMAE framework integrates a CNN-based autoencoder for spatial feature learning with a Masked Autoencoder tailored for irregular time series dynamics, utilizing attention to reconstruct the complete sequence in one pass. By reconstructing the underlying physical sequence directly, the model avoids the need for explicit data imputation, improving accuracy and robustness against nonlinearities. Evaluations on simulated and real-world ocean temperature datasets show superior performance compared to conventional recurrent and convolutional approaches.

## Key Contributions

- Proposed the Physics-Spatiotemporal Masked Autoencoder (P-STMAE) to forecast high-dimensional dynamical systems with irregular time steps.
- The method leverages a combination of convolutional autoencoders for spatial feature extraction and MAE adapted for irregular time series using attention for unified sequence reconstruction.
- Demonstrated significant improvements in prediction accuracy and robustness over traditional convolutional and recurrent methods on simulated and real-world ocean temperature data.
- The approach successfully handles irregular sampling by avoiding explicit data imputation while preserving system integrity.

## Limitations

The evaluation appears focused on physical system simulations and ocean data; generalizability to other types of irregular time series (e.g., finance, sensor logs) is not explicitly detailed.

## Open Questions & Future Work

- [[transformer-quadratic-complexity-scalability]]
- [[multi-objective-optimization-structure-accuracy-balance]]

## Key Concepts

- [[physics-spatiotemporal-masked-autoencoder]]: A novel masked autoencoder framework that combines convolutional autoencoders for spatial feature learning and masked autoencoding tailored for irregular time series, using attention for holistic sequence reconstruction.
- [[irregular-time-step-mae-forecasting]]: Applying the Masked Autoencoder reconstruction principle to high-dimensional time series data sampled at irregular intervals without explicit imputation.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 2 concept(s), 2 open question(s), and 0 dataset(s), with 3 rejected candidate note(s).

### Approved Concepts
- Physics-Spatiotemporal Masked Autoencoder: This is the novel architecture proposed to handle irregular time steps in high-dimensional dynamical system forecasting by integrating spatial feature extraction with time-series masking and reconstruction.
- Irregular Time Step Forecasting with MAE: The core technical innovation is adapting the Masked Autoencoder (MAE) strategy, typically for vision/NLP, to directly model and reconstruct time series with missing/irregular data points.

### Approved Open Questions
- Enhance Transformer Scalability: The quadratic complexity is a known scalability bottleneck for transformers, and overcoming it is crucial for applying this method to longer-term forecasting or higher-resolution data where sequence length is large.
- Balance Point-wise Accuracy and Structure: Addressing this trade-off is crucial for scientific applications where both local numerical correctness and global structure/conservation properties are important.

### Rejected Candidates
- [open_question] Advanced Spatial Encoding Techniques (`advanced-physical-field-encoding-for-cae`) - paper_local: This candidate is a specific suggestion for improving the existing CAE component of the main concept, making it a local future work item rather than a universally significant open question.
- [open_question] Advanced Positional Embeddings (`advanced-positional-embeddings-for-irregular-time`) - paper_local: This is a specific implementation improvement related to the Transformer component's positional encoding, better categorized as a local future work direction than a universal open question.
- [open_question] Broader Real-World Validation (`broader-real-world-dataset-validation`) - low_impact: This is a boilerplate request for more experiments, specifically on more datasets, which is a generic type of future work.

## Links

- [Abstract](https://arxiv.org/abs/2603.25597)
- [PDF](https://arxiv.org/pdf/2603.25597)

