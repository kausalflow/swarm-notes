---
created_at: '2026-07-09T08:19:19Z'
source_papers:
- '[[openalex-2607.05095-fast-a-holistic-framework-for-optimizing-memory-io-computati]]'
title: DTDGs Training Optimization Bottlenecks
---

**Background:** Continuous-time dynamic graphs (CTDGs) and discrete-time dynamic graphs (DTDGs) exhibit distinct temporal properties requiring different training optimizations.

**Question / Future Work:** Designing system-level optimizations and temporal sampling strategies specifically tailored for the snapshot-based nature of DTDGs remains a significant bottleneck compared to existing CTDG-focused training frameworks.

**Why It Matters:** DTDGs are a fundamental representation for many time-series and graph tasks; closing the performance gap in training them is essential for broad-spectrum dynamic graph learning.

**Evidence:** Similar to TGL (Zhou et al., 2022), our framework can support TGNNs on DTDGs but its performance remains suboptimal. We leave the design of optimizations specifically for DTDG-style training as future work.