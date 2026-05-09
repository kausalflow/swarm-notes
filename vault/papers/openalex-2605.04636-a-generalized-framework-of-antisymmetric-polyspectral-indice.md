---
# CSL-compatible fields
title: "A Generalized Framework of Antisymmetric Polyspectral Indices for Identifying High-Order Neural Interactions"
author:
  - literal: "Alessio Basti"
  - literal: "Rikkert Hindriks"
  - literal: "Ruggero Freddi"
  - literal: "Gian Luca Romani"
  - literal: "Vittorio Pizzella"
  - literal: "Guido Nolte"
  - literal: "Laura Marzetti"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2605.04636"

# Custom fields
paper_id: "2605.04636"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "antisymmetric-cross-polyspectral-indices"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:02:59Z"
created_at: "2026-05-09T07:02:59Z"
---

# A Generalized Framework of Antisymmetric Polyspectral Indices for Identifying High-Order Neural Interactions

**Authors**: Alessio Basti, Rikkert Hindriks, Ruggero Freddi, Gian Luca Romani, Vittorio Pizzella, Guido Nolte, Laura Marzetti
**Date**: 2026-05-06
**Paper ID**: [openalex:2605.04636](https://arxiv.org/abs/2605.04636)

## Summary

This paper proposes a general framework of antisymmetric cross-polyspectral indices to identify high-order neural interactions where a frequency of interest arises from the summation of multiple component frequencies. By design, these indices are robust to instantaneous volume conduction artifacts that frequently contaminate neurophysiological signal analysis. Theoretical properties are validated through simulations of cubic nonlinearities and applied to EEG data to reveal novel multi-frequency network dynamics with potential implications for personalized brain stimulation protocols.

## Key Contributions

- Introduces a general family of antisymmetric cross-polyspectral indices to quantify high-order harmonic neural dependencies across multiple time series.
- Proves that these indices are intrinsically robust to zero-lag instantaneous mixing (volume conduction) artifacts.
- Demonstrates the detection of significant higher-order dependencies in empirical EEG recordings that remain invisible to standard analytic metrics.

## Open Questions & Future Work

- [[real-time-estimation-tradeoffs]]

## Key Concepts

- [[antisymmetric-cross-polyspectral-indices]]: A family of indices for quantifying high-order harmonic dependencies in time series that are inherently robust to instantaneous linear mixing (volume conduction).

## Archivist Review

The antisymmetric cross-polyspectral indices are approved as they provide a robust, reusable mathematical framework for addressing linear spillover in high-order time-series analysis. The open question on real-time trade-offs is approved for its focus on the critical, well-defined bottleneck of balancing estimation precision with temporal latency in closed-loop systems. Other candidates were rejected for being standard research validation steps or too generic to justify a permanent vault note.

### Approved Concepts
- Antisymmetric Cross-Polyspectral Indices: This framework provides a novel, principled approach to decoupling genuine nonlinear high-order interactions from linear instantaneous artifacts in time-series data, a recurring problem in signal processing and neuroscience.

### Approved Open Questions
- Real-time spectral estimation trade-offs: Determining these trade-offs is critical for moving beyond offline signal analysis toward practical, personalized closed-loop neuromodulation protocols.

### Rejected Candidates
- [open_question] Generality of cross-frequency couplings (`generality-of-cross-frequency-coupling`) - low_impact: The question of inter-subject consistency is a standard validation hurdle for almost any proposed biomarker and lacks a specific mechanism to investigate.

## Links

- [Abstract](https://arxiv.org/abs/2605.04636)
- [PDF](https://arxiv.org/pdf/2605.04636)

