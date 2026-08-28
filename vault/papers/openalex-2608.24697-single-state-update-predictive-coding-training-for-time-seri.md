---
# CSL-compatible fields
title: "Single State Update Predictive Coding training for Time Series Forecasting and Anomaly Detection"
author:
  - literal: "Matteo Cardoni"
  - literal: "Sam Leroux"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.24697"

# Custom fields
paper_id: "2608.24697"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "continual-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "single-state-update-predictive-coding"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T16:58:47Z"
created_at: "2026-08-28T16:58:47Z"
---

# Single State Update Predictive Coding training for Time Series Forecasting and Anomaly Detection

**Authors**: Matteo Cardoni, Sam Leroux
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.24697](https://arxiv.org/abs/2608.24697)

## Summary

Predictive Coding Networks (PCNs) traditionally suffer from sequential backward error propagation bottlenecks. To address this, the authors introduce a Single State Update Predictive Coding training technique that pairs a Generative PCN with a support Encoding PCN to match neural activations in parallel. Applied to time series anomaly detection, this approach enables stable, continuous, and online learning without sequential propagation delays.

## Key Contributions

- Introduces a Single State Update Predictive Coding training technique that pairs a Generative PCN with a support Encoding PCN to bypass sequential backward error propagation.
- Enables parallel training of neural activations across PCN layers without sequential propagation bottlenecks.
- Demonstrates stable, continuous, online learning when applied to time series anomaly detection.

## Key Concepts

- [[single-state-update-predictive-coding]]: A training technique for Predictive Coding Networks that uses parallel Generative and Encoding PCNs to eliminate sequential error propagation bottlenecks.

## Archivist Review

Approved the single concept representing a novel training paradigm for predictive coding networks, but rejected the open question as it focuses on hardware implementation details rather than a fundamental scientific bottleneck.

### Approved Concepts
- Single State Update Predictive Coding: Addresses the sequential backward error propagation bottleneck in Predictive Coding Networks by enabling parallel training of a Generative PCN and support Encoding PCN.

### Rejected Candidates
- [open_question] Hardware-Accelerated Parallel Predictive Coding (`hardware-accelerated-parallel-predictive-coding`) - low_impact: Reduces to a hardware implementation and engineering efficiency bottleneck rather than a fundamental theoretical limitation of temporal modeling or distribution shift.

## Links

- [Abstract](https://arxiv.org/abs/2608.24697)
- [PDF](https://arxiv.org/pdf/2608.24697)

