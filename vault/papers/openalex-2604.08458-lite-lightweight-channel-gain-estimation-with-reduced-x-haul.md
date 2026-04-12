---
# CSL-compatible fields
title: "LITE: Lightweight Channel Gain Estimation with Reduced X-Haul CSI Signaling in O-RAN"
author:
  - literal: "David Goez"
  - literal: "Marco Piazzola"
  - literal: "Giulia Costa"
  - literal: "Achiel Colpaert"
  - literal: "Rodney Martínez Alonso"
  - literal: "Esra Aycan Beyazit"
  - literal: "Nina Slamnik-Krijestorac"
  - literal: "Johann M. Márquez-Barja"
  - literal: "Miguel Camelo Botero"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2604.08458"

# Custom fields
paper_id: "2604.08458"
paper_source: "openalex"
domain: "speech"
tags:
  - "cnn"
  - "lstm"
  - "model-compression"
  - "quantization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "lite-lightweight-intelligent-trajectory-estimator"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:21:09Z"
created_at: "2026-04-12T06:21:09Z"
---

# LITE: Lightweight Channel Gain Estimation with Reduced X-Haul CSI Signaling in O-RAN

**Authors**: David Goez, Marco Piazzola, Giulia Costa, Achiel Colpaert, Rodney Martínez Alonso, Esra Aycan Beyazit, Nina Slamnik-Krijestorac, Johann M. Márquez-Barja, Miguel Camelo Botero
**Date**: 2026-04-09
**Paper ID**: [openalex:2604.08458](https://arxiv.org/abs/2604.08458)

## Summary

LITE is a lightweight pipeline designed for Cell-Free Massive MIMO in O-RAN to address bandwidth constraints caused by frequent CSI exchanges. It utilizes a 1D-CNN autoencoder for data compression at the Distributed Unit and an asymmetric Squeeze-and-Excitation-enhanced BiLSTM at the Near-RT-RIC for channel gain forecasting. The approach significantly reduces computational complexity and transport overhead while maintaining high prediction accuracy and enabling high-throughput real-time deployment.

## Key Contributions

- Introduced LITE, an O-RAN compatible pipeline achieving 50% CSI compression and 83.39% model complexity reduction.
- Demonstrated that an asymmetric SE-BiLSTM predictor improves forecasting accuracy by 5% over standard BiLSTM baselines.
- Achieved 147k Queries per Second (QPS) in a TensorRT-optimized deployment, representing a 4.6x throughput gain for real-time channel gain estimation.

## Open Questions & Future Work

- [[adaptive-csi-compression-prediction-optimization]]

## Key Concepts

- [[lite-lightweight-intelligent-trajectory-estimator]]: A split-computing pipeline that combines 1D-CNN autoencoders with SE-BiLSTM predictors to balance CSI compression with predictive accuracy in O-RAN systems.

## Archivist Review

Approved the LITE pipeline architecture as it introduces a reusable split-computing design for edge-based wireless forecasting. One open question regarding adaptive CSI compression was approved due to its specific focus on the interplay between transport constraints and prediction accuracy in O-RAN; other proposed open questions were rejected as they described generic optimization tasks.

### Approved Concepts
- LITE (Lightweight Intelligent Trajectory Estimator): The paper proposes a specialized split-compute architecture for channel-state prediction in O-RAN that is highly relevant for future resource-constrained network edge tasks.

### Approved Open Questions
- Adaptive CSI compression and prediction: Dynamic adaptation of compression and prediction is crucial for maintaining performance and resource efficiency under unpredictable network loads in real-world O-RAN deployments.

### Rejected Candidates
- [open_question] Model compression for resource-constrained RICs (`model-compression-for-resource-constrained-ric`) - generic: The research direction is overly generic and primarily lists standard optimization techniques (quantization, pruning, NAS) without identifying a unique bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2604.08458)
- [PDF](https://arxiv.org/pdf/2604.08458)

