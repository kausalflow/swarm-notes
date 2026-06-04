---
created_at: '2026-06-04T08:46:29Z'
source_papers:
- '[[openalex-2606.01770-adaptive-auto-harness-sustained-self-improvement-for-agentic]]'
title: Direct Estimation of Auto-Harness Losses
---

**Background:** Auto-harness systems for LLM agents currently rely on aggregating historical execution data into a single, evolving harness, which often leads to performance degradation in open-ended, non-stationary task streams. The gap between an arbitrary deployed harness and an oracle harness can be analytically decomposed into evolution loss and adaptation loss, representing the limitation of the harness-construction methodology and the lack of per-task specialization, respectively.

**Question / Future Work:** There is a need for robust empirical estimators for the evolution loss ($L_{\text{evo}}$) and adaptation loss ($L_{\text{adapt}}$) as defined in the paper's analytical framework. Currently, these losses are diagnosed indirectly via bottleneck analyses, ablations, and routing controls, but the authors note that they are not directly estimated oracle quantities, leaving the exact contribution of each to performance gaps in different deployment regimes somewhat speculative.

**Why It Matters:** Formalizing these losses into directly computable metrics would allow for automated, per-task diagnostics in real-world deployments, enabling systems to dynamically decide whether to invest more compute in evolving general capabilities or in improving solve-time routing strategies.