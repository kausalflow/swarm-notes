---
created_at: '2026-09-24T09:39:20Z'
source_papers:
- '[[openalex-2609.24294-toward-gpu-resident-climate-models-a-feasibility-study-on-lo]]'
title: End-to-End Compressed SHT Transpositions
---

**Background:** Pseudospectral numerical weather prediction models rely heavily on the Spherical Harmonic Transform, which requires expensive global all-to-all pencil transpositions that form the primary communication bottleneck at scale.

**Question / Future Work:** Evaluate the end-to-end performance and combined communication speedup of applying online GPU-resident lossy compression to both the row-wise and column-wise pencil transpositions required by the complete Spherical Harmonic Transform.

**Why It Matters:** Understanding the compound performance and error propagation of compressing multiple successive communication phases in spectral transforms is crucial for end-to-end GPU-resident climate model optimization.

**Evidence:** In this work we only addressed the first all-to-all transposition (by rows). The second transposition (by columns) is structurally analogous; the compression rationale and error analysis apply equally. End-to-end SHT performance would require both transpositions to be compressed...