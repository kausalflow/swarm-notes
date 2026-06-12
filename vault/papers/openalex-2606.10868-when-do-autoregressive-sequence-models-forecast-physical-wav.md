---
# CSL-compatible fields
title: "When Do Autoregressive Sequence Models Forecast Physical Wavefields? A Controlled Study on Synthetic Seismograms"
author:
  - literal: "Waleed Esmail"
  - literal: "Stuart Russell"
  - literal: "Jana Klinge"
  - literal: "Alexander Kappes"
  - literal: "Christine Thomas"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10868"

# Custom fields
paper_id: "2606.10868"
paper_source: "openalex"
domain: "time-series"
tags:
  - "language-model"
  - "autoregressive"
  - "time-series"
  - "forecasting"
  - "long-context"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:53:36Z"
created_at: "2026-06-12T08:53:36Z"
---

# When Do Autoregressive Sequence Models Forecast Physical Wavefields? A Controlled Study on Synthetic Seismograms

**Authors**: Waleed Esmail, Stuart Russell, Jana Klinge, Alexander Kappes, Christine Thomas
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10868](https://arxiv.org/abs/2606.10868)

## Summary

This study systematically analyzes the stability of autoregressive sequence models in forecasting oscillatory physical signals, specifically using synthetic seismograms. By performing controlled ablations on the SeismoGPT architecture, the authors find that multi-token prediction is the dominant factor in mitigating phase drift and error accumulation during long-horizon rollouts. Furthermore, the results highlight a crucial sensitivity to context length, where generalization performance collapses if the input window does not cover the characteristic P-S interval.

## Key Contributions

- Demonstrates that multi-token prediction is the primary driver of rollout stability in physical wavefield autoregressive models, providing a +0.040 median NCC improvement.
- Establishes a critical context-ratio threshold near unity, below which model generalization for seismic P-S intervals collapses.
- Identifies that phase-aware objectives are required to resolve residual polarity inversion failures, as traditional magnitude-based spectral losses are insufficient.

## Open Questions & Future Work

- [[phase-aware-objectives-oscillatory-signals]]

## Archivist Review

The study provides a valuable analysis of long-horizon rollout stability for oscillatory signals, identifying key limitations in current magnitude-based losses. The identified open question regarding phase-aware objectives is significant for physical signal forecasting. I rejected the SeismoGPT concept as it represents a specific model instance used for local ablation study rather than a general, reusable technique.

### Approved Open Questions
- Phase-aware objectives for forecasting: Addressing polarity and phase errors is critical for improving the long-horizon fidelity of autoregressive models in physical domains like seismology and gravitational-wave analysis, where phase alignment is essential for scientific interpretation.

### Rejected Candidates
- [concept] SeismoGPT (`seismogpt`) - paper_local: SeismoGPT is an architecture-specific implementation used as an experimental testbed rather than a generalized, reusable methodological concept.

## Links

- [Abstract](https://arxiv.org/abs/2606.10868)
- [PDF](https://arxiv.org/pdf/2606.10868)

