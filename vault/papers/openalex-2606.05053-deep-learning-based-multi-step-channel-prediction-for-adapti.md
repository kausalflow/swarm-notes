---
# CSL-compatible fields
title: "Deep Learning Based Multi-Step Channel Prediction for Adaptive Underwater Acoustic OFDM Systems"
author:
  - literal: "Tian Tian"
  - literal: "Ying Zhang"
  - literal: "Agastya Raj"
  - literal: "Fei-Yun Wu"
  - literal: "Marco Ruffini"
issued:
  date-parts:
    - [2026, 6, 3]
url: "https://arxiv.org/abs/2606.05053"

# Custom fields
paper_id: "2606.05053"
paper_source: "openalex"
domain: "speech"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "long-context"
architectures:
  - "transformer"
datasets:
  []
concept_slugs:
  - "patchcsi-t"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-06T07:40:26Z"
created_at: "2026-06-06T07:40:26Z"
---

# Deep Learning Based Multi-Step Channel Prediction for Adaptive Underwater Acoustic OFDM Systems

**Authors**: Tian Tian, Ying Zhang, Agastya Raj, Fei-Yun Wu, Marco Ruffini
**Date**: 2026-06-03
**Paper ID**: [openalex:2606.05053](https://arxiv.org/abs/2606.05053)

## Summary

This paper proposes an adaptive OFDM framework for underwater acoustic communication that leverages a novel Transformer-based model, PatchCSI-T, for multistep channel prediction. PatchCSI-T utilizes feature-independent modeling and parameter sharing to achieve low-latency and accurate CSI forecasting. When integrated with a greedy adaptive modulation and power allocation scheme, the approach demonstrates superior performance in end-to-end bit error rate and spectral efficiency compared to existing methods. The effectiveness of the framework is validated on real-world UWA channel datasets.

## Key Contributions

- Introduces PatchCSI-T, a Transformer-based model for multistep underwater acoustic (UWA) channel state information (CSI) prediction.
- Achieves improved end-to-end bit error rate (BER) and spectral efficiency in adaptive OFDM underwater communication systems.
- Provides a framework integrating predictive CSI modeling with greedy adaptive modulation and power allocation.

## Open Questions & Future Work

- [[uwa-channel-prediction-scalability-and-realtime-testing]]

## Key Concepts

- [[patchcsi-t]]: A Transformer-based channel state information prediction model using feature-independent modeling and parameter sharing for adaptive underwater acoustic systems.

## Archivist Review

I approved the PatchCSI-T model architecture as a distinct and potentially reusable approach to channel state information forecasting, characterized by feature-independent patching and parameter sharing. I also approved the open question regarding real-world evaluation in underwater channels, as this addresses a specific, technically challenging bottleneck in the transition from simulation to real-time at-sea deployment.

### Approved Concepts
- PatchCSI-T: It is the core model architecture proposed for accurate, low-latency CSI forecasting in UWA channels.

### Approved Open Questions
- Evaluation in Realistic Underwater Conditions: The performance of predictive models is sensitive to the specific statistical properties of the acoustic channel, making validation in open-ocean conditions essential to confirm practical feasibility.

## Links

- [Abstract](https://arxiv.org/abs/2606.05053)
- [PDF](https://arxiv.org/pdf/2606.05053)

