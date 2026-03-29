---
created_at: '2026-03-29T06:08:36Z'
source_papers:
- '[[openalex-2603.25289-revealing-the-influence-of-participant-failures-on-model-qua]]'
title: Simultaneous participant crash impact
---

**Background:** Research into participant failures in Federated Learning systems has often focused on the impact of a single participant dropping out.

**Question / Future Work:** Investigate the collective impact of multiple simultaneous participant crashes within a single round of cross-silo Federated Learning to determine how the resulting data loss aggregates and affects model quality compared to isolated failures.

**Why It Matters:** Understanding multi-participant failure scenarios is vital for deploying robust fault-tolerance mechanisms that account for correlated failures in distributed systems.

**Evidence:** Despite that, in a real-world setting, it is possible that multiple participants can crash at the same time due to network failures.