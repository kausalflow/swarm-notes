---
# CSL-compatible fields
title: "Spatio-Temporal Scheduling Prediction Under Backhaul Delay for Resilient Coordinated Beamforming"
author:
  - literal: "Prashant Kumar Singh"
  - literal: "Shubham Vaishnav"
  - literal: "Ahmet Gokceoglu"
  - literal: "Li Wang"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08454"

# Custom fields
paper_id: "2607.08454"
paper_source: "openalex"
domain: "nlp"
tags:
  - "graph-neural-network"
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:28:26Z"
created_at: "2026-07-12T07:28:26Z"
---

# Spatio-Temporal Scheduling Prediction Under Backhaul Delay for Resilient Coordinated Beamforming

**Authors**: Prashant Kumar Singh, Shubham Vaishnav, Ahmet Gokceoglu, Li Wang
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08454](https://arxiv.org/abs/2607.08454)

## Summary

This paper addresses the performance degradation of coordinated beamforming in 5G networks caused by backhaul-induced information staleness. The authors propose a two-stage framework using a Spectral Temporal Graph Neural Network (StemGNN) to forecast future user equipment scheduling states from delayed observations. By replacing stale input data with these high-accuracy predictions, the approach significantly recovers sum rate and cell-edge fairness, outperforming conventional sequence modeling baselines like LSTM and GRU. The findings validate that framing backhaul latency as a spatio-temporal forecasting task enables robust inter-cell coordination in delay-constrained environments.

## Key Contributions

- Introduces a two-stage predictive framework for coordinated beamforming that treats backhaul latency as a spatio-temporal forecasting problem.
- Utilizes a Spectral Temporal Graph Neural Network (StemGNN) to predict future UE scheduling states, replacing stale inputs to mitigate performance degradation in distributed 5G networks.
- Achieves 87.57% mean scheduling prediction accuracy on a massive MIMO downlink, outperforming LSTM, GRU, RNN, and Markov chain baselines.
- Demonstrates that the proposed prediction framework recovers 57-73% of the sum rate loss and up to 83% of the Lag-1 fairness loss caused by backhaul delays.

## Open Questions & Future Work

- [[closed-loop-distributional-shift-in-wireless-scheduling-prediction]]
- [[uncertainty-aware-scheduling-prediction-for-robust-beamforming]]

## Archivist Review

I approved two open questions concerning the fundamental challenges of closed-loop distributional shift and uncertainty-aware prediction in delay-constrained wireless networks. I rejected the architecture 'StemGNN' as it is a well-known model, not a new contribution of the paper. I also rejected the UMi channel model as it is a simulation methodology rather than a benchmark dataset.

### Approved Open Questions
- Closed-loop distributional shift mitigation: This is a fundamental challenge for any closed-loop learned controller in dynamic environments, and addressing it is crucial for ensuring the long-term stability and reliability of AI-assisted wireless resource allocation.
- Uncertainty-aware predictive beamforming: Uncertainty-aware predictions directly enhance system robustness and fault tolerance in edge-based wireless networks, as they provide a mechanism to safely handle unreliable information or backhaul anomalies.

### Rejected Candidates
- [concept] Spectral Temporal Graph Neural Network (`StemGNN`) - not_novel: This is an existing architecture, not a new concept introduced by the paper.
- [dataset] Quadriga Urban Micro (UMi) channels (`quadriga-urban-micro-umi-channels`) - other: This is a simulation environment/standardized channel model rather than a curated dataset for forecasting research.

## Links

- [Abstract](https://arxiv.org/abs/2607.08454)
- [PDF](https://arxiv.org/pdf/2607.08454)

