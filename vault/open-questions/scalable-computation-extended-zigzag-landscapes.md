---
created_at: '2026-09-10T09:17:22Z'
source_papers:
- '[[openalex-2412.11925-spatiotemporal-persistence-landscapes]]'
title: Scalable Computation of Extended Zigzag Landscapes
---

**Background:** The computational overhead of evaluating persistence landscapes across comprehensive parameter spaces of extended zigzag modules remains high due to the exhaustive calculation of barcodes for individual paths.

**Question / Future Work:** The computational complexity and memory consumption associated with calculating persistence landscapes for extended zigzag modules across high-resolution parameter grids remain a significant bottleneck. Future work needs to explore efficient approximation algorithms, advanced data structures, or optimized simplicial complex constructions to improve scalability for large-scale time series datasets.

**Why It Matters:** Computational efficiency is critical for applying topological summaries like persistence landscapes to high-dimensional or long time series in practical machine learning pipelines.

**Evidence:** However, currently one disadvantage is the large computational cost and the high memory consumption. For every index in the parameter space one has to compute the persistence landscape as the barcode of a zigzag module through the parameter space.