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
paper_source: "arxiv"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "forecasting"
  - "convolutional-neural-network"
  - "recurrent-neural-network"
  - "attention-mechanism"
  - "self-supervised-learning"
architectures:
  []
datasets:
  - "ocean temperature data"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T09:10:15Z"
created_at: "2026-03-27T09:10:15Z"
---

# Spatiotemporal System Forecasting with Irregular Time Steps via Masked Autoencoder

**Authors**: Kewei Zhu, Yanze Xin, Jinwei Hu, Xiaoyuan Cheng, Yiming Yang, Sibo Cheng
**Date**: 2026-03-26
**Paper ID**: [arxiv:2603.25597](https://arxiv.org/abs/2603.25597)

## Summary

This paper introduces the Physics-Spatiotemporal Masked Autoencoder (PSMAE) to address the challenge of forecasting high-dimensional systems with irregular time steps, often caused by sparse or missing observations. The method employs a hybrid architecture combining convolutional autoencoders for spatial feature extraction and masked autoencoders optimized for irregular temporal modeling, utilizing attention to reconstruct the full sequence in one step. By avoiding explicit data imputation, PSMAE preserves the underlying physical integrity of the dynamical system's field representation. Evaluations across simulated and real-world ocean temperature datasets show that PSMAE significantly outperforms conventional convolutional and recurrent network baselines in accuracy and robustness.

## Key Contributions

- Introduction of the Physics-Spatiotemporal Masked Autoencoder (PSMAE) tailored for irregular time-step forecasting, avoiding explicit data imputation.
- Integration of convolutional autoencoders for spatial feature learning and masked autoencoders adapted for irregular temporal patterns within a single prediction pass.
- Demonstrated significant improvement in prediction accuracy and robustness over traditional CNN and RNN methods on simulated and real-world high-dimensional system data.

## Limitations

The evaluation is primarily demonstrated on simulated datasets and ocean temperature data, and performance on other highly complex dynamical systems remains to be fully explored.

## Open Questions & Future Work

- [[transformer-quadratic-complexity-scalability]]
- [[advanced-positional-embeddings-irregular-time]]
- [[advanced-spatial-encoding-techniques]]
- [[multi-objective-optimization-structural-fidelity]]
- [[broader-validation-real-world-generalization]]

## Key Concepts

- [Physics-Spatiotemporal Masked Autoencoder](../concepts/physics-spatiotemporal-masked-autoencoder.md): A novel forecasting method integrating convolutional autoencoders for spatial feature extraction with masked autoencoders optimized for irregular time series, using attention for single-pass sequence reconstruction.

## Datasets

- [ocean temperature data](../datasets/ocean-temperature-data.md)

## Limitations

The evaluation is primarily demonstrated on simulated datasets and ocean temperature data, and performance on other highly complex dynamical systems remains to be fully explored.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.25597)
- [PDF](https://arxiv.org/pdf/2603.25597)

