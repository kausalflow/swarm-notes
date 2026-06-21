---
created_at: '2026-06-21T08:53:49Z'
source_papers:
- '[[openalex-2606.19825-enhancing-graph-neural-networks-using-proximity-graphs-for-d]]'
title: Optimal Graph Construction Methods
---

**Background:** Graph neural networks require a predefined graph structure to model relationships between data points, yet environmental and remote sensing data are typically stored in tabular formats without explicit topological linkages. The choice of graph construction method, such as Delaunay triangulation or k-nearest neighbors, directly influences the spatial dependencies captured by the model.

**Question / Future Work:** There is a need to systematically determine the optimal graph construction method tailored to specific environmental applications. While different proximity graphs—such as Delaunay, Gabriel, k-Nearest Neighbor, and Yao graphs—have been explored for dust emission forecasting, the theoretical foundations for choosing the best structure for varying spatiotemporal dynamics remain unresolved. Future work should focus on identifying generalizable rules or adaptive methods for selecting graph topologies that best reflect the physical or environmental relationships inherent in diverse spatial processes.

**Why It Matters:** The performance of GNNs is highly sensitive to the graph structure. As environmental datasets expand to include more complex variables, understanding how to construct graphs that accurately reflect underlying physical phenomena rather than relying on heuristic proximity measures is critical for improving predictive reliability.