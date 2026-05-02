---
created_at: '2026-05-02T06:57:16Z'
source_papers:
- '[[openalex-2604.26802-a-control-framework-for-induced-seismicity-mitigation-in-gro]]'
title: Real-time Seismicity Rate Estimation
---

**Background:** Seismicity rate is a statistical construct representing the frequency of seismic events and is not directly observable in real-time subsurface operations. Current control frameworks rely on estimating seismicity rate from discrete earthquake catalogs, which introduces significant uncertainty and temporal lag.

**Question / Future Work:** The development of robust, real-time estimation methods for the seismicity rate remains a critical bottleneck. Controllers must rely on estimators derived from sparse and stochastic seismic event data, and future work is needed to improve the accuracy, latency, and reliability of these estimates to ensure the stability of closed-loop feedback control systems in reservoirs.

**Why It Matters:** This is a fundamental bottleneck for implementing feedback control in seismicity mitigation, as the controller performance is strictly limited by the fidelity and responsiveness of the input state estimation.

**Evidence:** First and most important, SR is not a directly measurable quantity in practice. ... The control module reads the seismic events that happened in the reservoir’s region in discrete-time intervals ... and estimates the regional SR.