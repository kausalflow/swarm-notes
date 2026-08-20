---
# CSL-compatible fields
title: "Feedforward Active Speech Suppression Based on Time Series Prediction of Speech Signals Using Neural Networks"
author:
  - literal: "Manami Nishikata"
  - literal: "Shoichi Koyama"
  - literal: "Manami Nishikata"
  - literal: "Shoichi Koyama"
issued:
  date-parts:
    - [2026, 8, 17]
url: "https://arxiv.org/abs/2608.16092"

# Custom fields
paper_id: "2608.16092"
paper_source: "openalex"
domain: "speech"
tags:
  - "speech-recognition"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-20T05:21:03Z"
created_at: "2026-08-20T05:21:03Z"
---

# Feedforward Active Speech Suppression Based on Time Series Prediction of Speech Signals Using Neural Networks

**Authors**: Manami Nishikata, Shoichi Koyama, Manami Nishikata, Shoichi Koyama
**Date**: 2026-08-17
**Paper ID**: [openalex:2608.16092](https://arxiv.org/abs/2608.16092)

## Summary

This paper proposes a feedforward active noise control (ANC) method leveraging neural-network-based time-series prediction to suppress non-stationary speech signals, which are typically challenging for traditional ANC techniques. The authors introduce an adaptive filtering algorithm that calculates linear control filter update values using predicted future signals alongside past and current observations. Numerical experiments demonstrate that noise reduction performance improves when employing both true and neural-network-predicted future signals.

## Key Contributions

- Proposed a feedforward active noise control (ANC) method based on neural-network-based time-series prediction for suppressing non-stationary speech signals.
- Developed an adaptive filtering algorithm where the update value for the linear control filter is calculated using predicted future signals along with current and past signals.
- Demonstrated through numerical experiments that noise reduction is improved when utilizing both true predicted signals and neural-network-predicted signals.

## Open Questions & Future Work

- [[real-time-neural-network-inference-latency-in-active-noise-control]]

## Archivist Review

All concept candidates were rejected because they represent routine applications of neural network prediction to active noise control rather than broadly reusable forecasting mechanisms. One open question addressing real-time inference latency under tight audio sampling constraints was approved as it targets a distinct and recurring systems bottleneck in streaming time-series deployment.

### Approved Open Questions
- Real-Time Neural Network Inference Latency: Real-time hardware deployment is crucial for practical active noise control systems; bridging this latency gap is a key engineering and algorithmic bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.16092)
- [PDF](https://arxiv.org/pdf/2608.16092)

