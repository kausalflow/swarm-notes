---
created_at: '2026-07-12T07:27:50Z'
source_papers:
- '[[openalex-2607.08635-calibrated-persistent-laplacian-cusum-for-online-change-poin]]'
title: Unified Phase I Estimation Theory
---

**Background:** Online change-point detection methods often depend on parameters estimated from initial data segments, such as whitening matrices and thresholds calibrated via bootstrap techniques. Characterizing the error propagation from these Phase I estimation steps to the online recursive alarm trigger is critical for maintaining performance guarantees in practical deployment.

**Question / Future Work:** Future work is needed to provide a rigorous, unified characterization of the error propagation originating from Phase I parameter estimation, including control-limit estimation via bootstrap methods, model-selection procedures, and dependence induced by overlapping windows. A formal theoretical treatment of these combined estimation errors would improve the reliability of finite-horizon false-alarm control in practical streaming applications.

**Why It Matters:** These estimation errors are primary sources of deviation between theoretical performance and empirical results in real-world deployments. Understanding these bottlenecks is necessary for building more robust and provably reliable online monitoring systems.

**Evidence:** Full coverage of the experimental workflow would further require analyzing the control-limit estimation error of the moving-block bootstrap, candidate-parameter selection error, and dependence induced by overlapping windows.