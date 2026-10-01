---
created_at: '2026-10-01T11:15:11Z'
source_papers:
- '[[openalex-2609.36765-graph-spectral-flow-matching-for-multivariate-time-series-an]]'
title: Dynamic Graph Flow Matching
---

**Background:** Multivariate time series anomaly detection frequently models system topologies using static graphs, which limits applicability in scenarios where relationships dynamically evolve over time.

**Question / Future Work:** Future work aims to extend graph-spectral flow matching frameworks to accommodate dynamically evolving graphs rather than relying strictly on a fixed graph topology.

**Why It Matters:** Extending flow-matching anomaly detection to dynamic graphs is vital for real-world industrial environments where sensor interdependencies change constantly.

**Evidence:** First, it relies on a fixed graph, making it unsuitable when we have dynamically evolving graphs. Moreover, computing the graph Fourier basis can become costly as the number of variables increases. Future work could extend GRASP to be compatible with dynamic graphs and develop scalable approximations to graph spectral operations.