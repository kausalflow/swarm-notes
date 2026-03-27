---
created_at: '2026-03-27T15:44:26Z'
source_papers:
- '[[openalex-2603.23323-pnap-lifecycle-aware-edge-multi-state-sleep-for-energy-effic]]'
title: Distributed PNap Orchestration
---

**Background:** In Multi-access Edge Computing (MEC), managing the power state of edge servers (ECs) must be coordinated with the state of the services they host, as services cannot be processed while ECs are sleeping.

**Question / Future Work:** The work introduces a hybrid approach combining STGCN forecasting with scalable heuristics, but acknowledges that fully data-driven, user-level forecasting approaches are computationally prohibitive for large networks. Future work is needed to develop distributed versions of the proposed orchestration framework to handle scaling across a larger number of users, ECs, and services, where centralized computation and signaling overhead could become excessive.

**Why It Matters:** Developing a distributed version is crucial for the practical scalability of lifecycle-aware energy-saving orchestration in large-scale MEC deployments.

**Evidence:** PNap assumes the presence of a centralized orchestrator that performs estimations and decides for the entire network. But as the number of users, ECs, and services grows, the computational and signaling overhead of a centralized approach could become prohibitive. For this reason, future work will focus on developing a distributed version of PNap, capable of scaling efficiently while retaining its benefits.