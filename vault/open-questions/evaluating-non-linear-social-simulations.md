---
created_at: '2026-04-16T06:29:17Z'
source_papers:
- '[[openalex-2604.11466-slalom-simulation-lifecycle-analysis-via-longitudinal-observ]]'
title: Evaluating non-linear social simulations
---

**Background:** Agent-based social simulations frequently exhibit non-linear temporal dynamics, such as branching paths or complex feedback loops, which deviate from monotonic sequential progression.

**Question / Future Work:** Existing longitudinal evaluation techniques often rely on metrics like Dynamic Time Warping, which assume monotonic alignment. Research is needed to develop validation frameworks that can quantify process fidelity in simulations with branching, cyclical, or non-linear structural topologies.

**Why It Matters:** This addresses a fundamental limitation in the current state-of-the-art for evaluating agent trajectories, allowing for more realistic and complex modeling beyond linear sequences.

**Evidence:** the use of DTW assumes a monotonic temporal progression. Consequently, this metric cannot accurately evaluate simulations that exhibit radical branching, looping topologies, or non-linear social time.