---
# CSL-compatible fields
title: "Model- and Layer-Level Closed-Loop Forecasting with SSM-Based Spiking Neural Networks"
author:
  - literal: "Erik Stolt"
  - literal: "Sanja Karilanova"
  - literal: "Ayça Özçelikkale"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.28495"

# Custom fields
paper_id: "2610.28495"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "state-space-model"
  - "ssm"
  - "mamba"
  - "benchmark"
architectures:
  - "mamba"
datasets:
  - "ett-small"
concept_slugs:
  - "spiking-state-space-models"
dataset_slugs:
  - "ett-small"
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:40:00Z"
created_at: "2026-10-23T09:40:00Z"
---

# Model- and Layer-Level Closed-Loop Forecasting with SSM-Based Spiking Neural Networks

**Authors**: Erik Stolt, Sanja Karilanova, Ayça Özçelikkale
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.28495](https://arxiv.org/abs/2610.28495)

## Summary

This paper investigates time-series forecasting using Spiking Neural Networks (SNNs) framed as Deep State-Space Models (Deep SSMs). To address the challenge of autoregressive generation with discrete spike-based communications, the authors propose model-level and layer-level closed-loop forecasting strategies where self-generated values are fed back into the network. Evaluated on the ETT-small datasets, the proposed approaches match or outperform the zero-masking S4 baseline and perform competitively with state-of-the-art methods like SpaceTime, offering insights into the trade-offs of low-bit quantized activations.

## Key Contributions

- Introduces model-level and layer-level closed-loop forecasting strategies for Spiking Neural Networks (SNNs) acting as Deep State-Space Models (Deep SSMs).
- Demonstrates that closed-loop SNN forecasting approaches perform comparably to or better than the zero-masking baseline in S4 and match SpaceTime on the ETT-small datasets.
- Highlights the trade-off between continuous activations and low-bit quantized spike-based activations in time-series forecasting frameworks.

## Open Questions & Future Work

- [[forecasting-with-snn-open-question]]

## Key Concepts

- [[spiking-state-space-models]]: A biologically inspired class of deep state-space models where computing blocks communicate through discrete spikes.

## Archivist Review

The vault accepts the core architectural concept of spiking state-space models and the open question regarding autoregressive forecasting with spiking neural networks, while rejecting paper-local closed-loop implementation variants. ETT-small is canonicalized to ett-small.

### Approved Concepts
- Spiking State-Space Models: Presents a novel fusion of spiking neural networks and deep state-space models for time-series forecasting.

### Approved Open Questions
- Forecasting with Spiking Neural Networks: Addressing this question is vital for enabling efficient neuromorphic time-series forecasting and understanding the trade-offs of low-bit quantized activations in autoregressive generation.

### Rejected Candidates
- [concept] Model- and Layer-Level Closed-Loop Forecasting (`closed-loop-forecasting-snn`) - subcomponent_of_broader_mechanism: This represents a paper-local subcomponent and implementation strategy rather than a broadly recurring independent paradigm.

## Datasets

- [[ett-small]]

## Links

- [Abstract](https://arxiv.org/abs/2610.28495)
- [PDF](https://arxiv.org/pdf/2610.28495)

