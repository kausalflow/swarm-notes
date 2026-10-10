---
created_at: '2026-10-10T10:52:09Z'
source_papers:
- '[[openalex-2610.12232-training-on-the-future-a-delay-aware-audit-of-test-time-adap]]'
title: Delay-Aware Test-Time Adaptation
---

**Background:** Test-time adaptation (TTA) methods for time-series forecasting update deployed models or lightweight correctors using incoming ground truth, but practical delays in label release often create discrepancies between standard evaluations and real-world deployment.

**Question / Future Work:** Investigate the integration and performance trade-offs of combining online closed-form adaptive filters with neural time-series foundation models under realistic, non-zero label delays and pipeline latencies.

**Why It Matters:** Important for bridging classical adaptive signal processing with modern deep learning foundations for reliable streaming predictions under delayed feedback.

**Evidence:** Concurrent ORCA (Dai et al., 2026) trains a linear residual adapter from a replay buffer that implements the same maturity rule we use, evidence that the causal protocol is becoming standard, and is a natural future competitor. Neither varies the delay or audits the TTA stack.