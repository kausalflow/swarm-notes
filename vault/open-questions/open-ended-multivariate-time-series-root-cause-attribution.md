---
created_at: '2026-08-30T10:10:25Z'
source_papers:
- '[[openalex-2608.27182-tracebench-controlled-evaluation-of-llm-agents-for-time-seri]]'
title: Open-ended Multivariate Time-Series Diagnosis
---

**Background:** Large language model agents are increasingly evaluated on time-series anomaly detection and root-cause attribution, but existing benchmarks lack standardized physical simulations and multi-turn execution controls.

**Question / Future Work:** Future work involves expanding agentic root-cause attribution benchmarks beyond low-dimensional mechanical systems to support multi-parameter interventions, continuous or irregular sampling, and unconstrained open-ended hypothesis formulation without predefined closed-set label options.

**Why It Matters:** Extending controlled time-series diagnosis benchmarks to open-ended, multi-parameter, and irregularly sampled environments is critical for evaluating real-world operational readiness in complex industrial and software systems.

**Evidence:** First, TraceBench uses a closed-ended label set to enable unambiguous evaluation and clean comparisons across conditions. However, this format does not fully capture the open-ended nature of root-cause analysis... Second, it is limited to regularly sampled, fully observed trajectories from low-dimensional mechanical systems with at most one instantaneous parameter change.