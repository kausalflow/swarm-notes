---
created_at: '2026-06-12T08:53:36Z'
source_papers:
- '[[openalex-2606.10868-when-do-autoregressive-sequence-models-forecast-physical-wav]]'
title: Phase-aware objectives for forecasting
---

**Background:** Autoregressive sequence models for forecasting oscillatory physical signals, such as seismograms, often suffer from phase drift during long-horizon rollouts due to error accumulation. While multi-token prediction and spectral losses can mitigate these errors, they are primarily magnitude-based and often fail to penalize polarity inversions.

**Question / Future Work:** There is a need to develop phase-aware objective functions for autoregressive forecasting models to penalize polarity inversions and phase drift in oscillatory signals, as current magnitude-based spectral losses are invariant to phase and cannot address these failure modes. Future work should investigate incorporating complex-STFT terms, group-delay components, or explicit correlation-based penalties into the training objective.

**Why It Matters:** Addressing polarity and phase errors is critical for improving the long-horizon fidelity of autoregressive models in physical domains like seismology and gravitational-wave analysis, where phase alignment is essential for scientific interpretation.

**Evidence:** The dominant residual failure is a polarity inversion that a magnitude-based spectral loss cannot, by construction, penalize, identifying phase-aware objectives as the natural next step.