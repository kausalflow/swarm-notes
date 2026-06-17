---
# CSL-compatible fields
title: "Noise-Adaptive Predictive Dynamical Decoupling"
author:
  - literal: "Ali Abu-Nada"
  - literal: "Subhashish Banerjee"
  - literal: "Lian-Ao Wu"
issued:
  date-parts:
    - [2026, 6, 14]
url: "https://arxiv.org/abs/2606.15769"

# Custom fields
paper_id: "2606.15769"
paper_source: "openalex"
domain: "physics"
tags:
  - "reinforcement-learning"
  - "forecasting"
  - "physics"
architectures:
  []
datasets:
  []
concept_slugs:
  - "noise-adaptive-predictive-dynamical-decoupling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:27:00Z"
created_at: "2026-06-17T09:27:00Z"
---

# Noise-Adaptive Predictive Dynamical Decoupling

**Authors**: Ali Abu-Nada, Subhashish Banerjee, Lian-Ao Wu
**Date**: 2026-06-14
**Paper ID**: [openalex:2606.15769](https://arxiv.org/abs/2606.15769)

## Summary

This paper introduces a noise-adaptive dynamical decoupling framework that replaces conventional static control pulse schedules with machine-learning-based forecasts of quantum coherence. By modeling the instantaneous dynamics of a qubit interacting with random telegraph noise, the system adaptively applies control pulses in response to environmental fluctuations. Numerical simulations confirm that this predictive approach outperforms periodic protocols, particularly in non-Markovian and non-stationary regimes where memory effects and temporal noise evolution are prevalent.

## Key Contributions

- Introduced a noise-adaptive dynamical decoupling framework integrating open-quantum-system modeling with ML forecasting to protect quantum coherence.
- Demonstrated significant performance gains over periodic decoupling protocols in both non-Markovian and non-stationary noise environments.
- Showed superior coherence preservation using comparable pulse counts, highlighting the efficiency of instantaneous, forecast-based adaptive control.

## Open Questions & Future Work

- [[generalizable-adaptive-quantum-control]]

## Key Concepts

- [[noise-adaptive-predictive-dynamical-decoupling]]: A framework for quantum decoherence protection that dynamically adjusts pulse schedules using ML-based noise forecasting.

## Archivist Review

I approved the Noise-Adaptive Predictive Dynamical Decoupling concept as it introduces a novel, reusable paradigm for predictive adaptive control in physical systems, moving beyond static protocols. I also approved the open question regarding the generalization of such adaptive control, as it addresses a fundamental bottleneck in applying these methods to real-world, non-stationary noisy hardware. No datasets were approved as none were cited or central to the paper's contribution.

### Approved Concepts
- Noise-Adaptive Predictive Dynamical Decoupling: It introduces a novel paradigm for quantum control by replacing static pulse sequences with machine-learning-driven adaptive intervention based on instantaneous noise forecasting.

### Approved Open Questions
- Generalizing Adaptive Quantum Control: Broadening the applicability of predictive dynamical decoupling to unknown, non-stationary, and multi-source noise environments is critical for the scalability of fault-tolerant quantum computing in practical hardware.

## Links

- [Abstract](https://arxiv.org/abs/2606.15769)
- [PDF](https://arxiv.org/pdf/2606.15769)

