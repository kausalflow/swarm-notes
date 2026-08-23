---
created_at: '2026-08-23T05:19:35Z'
source_papers:
- '[[openalex-2608.20009-exphy-a-benchmark-for-explicit-physical-property-learning-in]]'
title: Trajectory vs Property Accuracy
---

**Background:** Existing physical reasoning benchmarks evaluate future motion and interaction prediction without explicitly tying performance to the underlying object-level physical parameters such as mass, friction, and restitution.

**Question / Future Work:** Investigate the exact relationship between trajectory forecasting accuracy and physical property estimation accuracy, examining why low trajectory error does not necessarily guarantee correct recovery of underlying physical properties and how models can be designed to reliably learn both dimensions simultaneously.

**Why It Matters:** Crucial for understanding whether physical reasoning models genuinely learn underlying physics or merely memorize trajectory patterns.

**Evidence:** Property-level analyses reveal that accurate trajectory forecasting does not necessarily imply accurate recovery of the underlying physical properties.