---
created_at: '2026-05-10T07:23:58Z'
source_papers:
- '[[openalex-2605.05975-physical-fidelity-reconstruction-via-improved-consistency-di]]'
title: Adaptive Noise Schedules
---

**Background:** The fidelity–realism trade-off in generative physical reconstruction is currently managed by a static, dataset-specific hyperparameter controlling the noise injection level at inference.

**Question / Future Work:** There is a need to develop adaptive or content-dependent noise-injection schedules during inference. Current models rely on a fixed initialization time (τ), which acts as a global trade-off between fidelity to low-resolution observations and the generation of fine-scale physical features; however, optimal noise levels likely vary spatially or temporally depending on local turbulence intensity and feature scales.

**Why It Matters:** Developing adaptive schedules is crucial for improving local reconstruction accuracy in non-stationary turbulent flows where the local information content and signal-to-noise ratio of coarse observations vary significantly.