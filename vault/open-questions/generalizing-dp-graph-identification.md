---
created_at: '2026-04-24T07:01:18Z'
source_papers:
- '[[openalex-2509.20460-differential-privacy-of-network-parameters-from-a-system-ide]]'
title: Generalizing DP for Graph Identification
---

**Background:** System identification involves reconstructing internal system parameters from observed input-output data, while differential privacy provides a framework for ensuring that the release of statistical outputs preserves the privacy of individual data points.

**Question / Future Work:** Extending DP privacy guarantees for Graph Shift Operators beyond Gaussian-noised input signals to non-Gaussian noise mechanisms and non-linear system dynamics is necessary to bridge the gap between theoretical models and real-world cyber-physical system security.

**Why It Matters:** Extending the privacy analysis to non-Gaussian noise and non-linear dynamics is critical for moving beyond theoretical linear models to real-world complex systems.

**Evidence:** The central question is: without altering H(S), can the DP signals u_t protect S and limit an adversary’s ability to identify it? ... We address this by deriving explicit conditions on the noise structure of u_t under a Gaussian prior.