---
created_at: '2026-06-12T08:53:54Z'
source_papers:
- '[[openalex-2606.10641-camasa-a-cam-based-dataset-from-the-masa-living-lab]]'
title: Robust Pseudonym Reconciliation Methods
---

**Background:** Privacy-preserving standards in cooperative intelligent transportation systems mandate the frequent rotation of station identifiers to prevent long-term tracking. This rotation makes continuous trajectory reconstruction challenging when using raw broadcast messages.

**Question / Future Work:** Developing robust, automated methods for pseudonym reconciliation is necessary to ensure the accuracy of vehicle tracking across long-term deployments. Current heuristic approaches often struggle with false associations in high-density traffic, necessitating advanced trajectory matching that accounts for complex movement patterns and V2X signal characteristics.

**Why It Matters:** Effective vehicle re-identification is fundamental for accurate trajectory prediction and traffic analysis in C-ITS, especially as privacy regulations continue to mandate frequent identifier rotations.

**Evidence:** the pseudonym-reconciliation procedure, although empirically validated and constrained by physical motion consistency, remains a heuristic data-association process and may introduce residual false merges or splits in highly dense traffic scenarios.