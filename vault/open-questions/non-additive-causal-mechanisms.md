---
created_at: '2026-05-29T08:37:47Z'
source_papers:
- '[[openalex-2605.26759-time-series-causal-discovery-via-context-conditioned-and-cau]]'
title: Non-additive causal mechanisms
---

**Background:** Structural causal models for time series data often rely on the assumption of an Additive Noise Model (ANM) to ensure structural identifiability and causal discovery.

**Question / Future Work:** While Additive Noise Models provide theoretical advantages for causal identification, they struggle to represent complex, non-additive phenomena such as multiplicative noise or non-linear entanglement found in diverse real-world time series. Research is needed to develop more flexible, non-additive causal mechanisms that maintain structural identifiability.

**Why It Matters:** The current reliance on ANM limits the applicability of time-series causal discovery to systems where non-additive noise is prevalent. Developing non-additive models is a key bottleneck for advancing robust and generalizable causal discovery in complex, noisy real-world environments.

**Evidence:** The SCM assumes an Additive Noise Model (ANM). Although ANM is theoretically advantageous for guaranteeing causal identifiability... it may not capture complex, non-additive external disturbances (e.g., multiplicative noise or nonlinear entanglement) present in reality.