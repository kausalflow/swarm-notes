---
created_at: '2026-06-26T08:26:28Z'
source_papers:
- '[[openalex-2606.24677-one-index-for-subsumption-and-roll-up-across-time-geography]]'
title: Dynamic Maintenance of Hierarchy Indexes
---

**Background:** Many hierarchical indexing techniques are designed for static datasets, making the efficient maintenance of these structures under frequent, online data modifications a persistent challenge.

**Question / Future Work:** The development of dynamic maintenance algorithms for unification-based hierarchy indexes (like OEH) is required to extend utility beyond static query performance, particularly in streaming or versioned data environments where the underlying subsumption poset evolves.

**Why It Matters:** Real-world data systems (e.g., knowledge graphs, temporal versioning) are highly dynamic; current static-only limitations hinder the adoption of unified indexing primitives in streaming applications.