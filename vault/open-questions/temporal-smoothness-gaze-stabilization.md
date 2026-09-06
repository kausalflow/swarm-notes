---
created_at: '2026-09-06T09:01:13Z'
source_papers:
- '[[openalex-2609.03868-gazefs-target-centered-gaze-trajectory-forecasting-and-stabi]]'
title: Temporal Smoothness in Gaze Stabilization
---

**Background:** Target-centered gaze interaction requires correcting systematic offsets in gaze-head tracking while maintaining temporal smoothness and managing task-aligned phase transitions.

**Question / Future Work:** The integration of explicit temporal smoothness objectives with target-centered gaze stabilization remains an open challenge, as current models optimize spatial centering and residual contraction at the expense of introducing a residual motion cost or temporal jitter.

**Why It Matters:** Crucial for bridging the gap between spatial gaze correction and perceptual jitter reduction in real-time extended reality (XR) interaction systems.

**Evidence:** GazeFS therefore improves Focus target centering and empirical residual contraction while leaving temporal smoothness as a separate objective.