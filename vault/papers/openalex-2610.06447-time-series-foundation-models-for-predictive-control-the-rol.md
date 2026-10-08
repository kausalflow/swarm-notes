---
# CSL-compatible fields
title: "Time-series Foundation Models for Predictive Control: The Role of Excitation"
author:
  - literal: "Mazen Amria"
  - literal: "Jasper Hoffmann"
  - literal: "Philipp Bordne"
  - literal: "Anna Rothenhäusler"
  - literal: "Lilli Frison"
  - literal: "Harald Taxt Walnum"
  - literal: "Sebastien Gros"
  - literal: "Joschka Bödecker"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.06447"

# Custom fields
paper_id: "2610.06447"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "model-predictive-control"
  - "foundation-model"
  - "zero-shot-learning"
  - "fine-tuning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:40:22Z"
created_at: "2026-10-08T11:40:22Z"
---

# Time-series Foundation Models for Predictive Control: The Role of Excitation

**Authors**: Mazen Amria, Jasper Hoffmann, Philipp Bordne, Anna Rothenhäusler, Lilli Frison, Harald Taxt Walnum, Sebastien Gros, Joschka Bödecker
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.06447](https://arxiv.org/abs/2610.06447)

## Summary

This paper investigates the application of time-series foundation models (TSFMs) to model predictive control (MPC) using residential heat-pump control as a test bed. The authors discover that while TSFMs exhibit strong zero-shot forecasting, low forecast error does not ensure that the model accurately captures system responses to alternative control actions. Their findings reveal that TSFMs can successfully recover the true input-response relationship provided the inference context contains sufficient independent control excitation, though fine-tuning and feature smoothing mitigate this requirement only partially.

## Key Contributions

- Demonstrates that low forecast error in time-series foundation models (TSFMs) does not guarantee accurate capture of system responses to alternative control actions in model predictive control (MPC).
- Identifies that TSFMs can successfully recover the system's input-response relationship when the inference context contains sufficient independent control excitation.
- Shows that common fine-tuning pipelines and feature smoothing reduce, but do not fully eliminate, the dependence on in-context control excitation.
- Evaluates the role of excitation using residential heat-pump control as a test bed, highlighting promise for shorter context windows in closed-loop settings.

## Limitations

Current TSFMs require sufficiently informative control variation in the inference context to reliably perform model predictive control, which may not always be present naturally.

## Open Questions & Future Work

- [[optimal-context-design-excitation-tsfm]]

## Archivist Review

The paper investigates the role of control excitation when applying time-series foundation models to model predictive control. The open question on optimal context design and excitation is retained because it targets a fundamental limitation in conditioning foundation models on control trajectories. No concepts or datasets met the strict novelty and reusability standards.

### Approved Open Questions
- Optimal Context Design and Excitation: Addressing this question helps minimize operational disruptions caused by active system excitation while maximizing model fidelity for predictive control.

### Rejected Candidates
- [open_question] Real-World Transfer of TSFM-Based MPC (`real-world-transfer-tsfm-mpc`) - low_impact: Addresses general real-world transfer without capturing a specific algorithmic or foundational bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.06447)
- [PDF](https://arxiv.org/pdf/2610.06447)

