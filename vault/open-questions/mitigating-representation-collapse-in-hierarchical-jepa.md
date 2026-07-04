---
created_at: '2026-07-04T07:35:57Z'
source_papers:
- '[[openalex-2607.01145-a-lightweight-self-supervised-learning-framework-for-multiva]]'
title: Mitigating Representation Collapse in Hierarchical-JEPA
---

**Background:** Joint-Embedding Predictive Architectures (JEPAs) are often susceptible to representation collapse, where the model learns constant or trivial embeddings during training.

**Question / Future Work:** Hierarchical JEPA designs introduce new stability challenges as both internal stages must maintain distinctiveness to avoid representation collapse; identifying robust stabilization techniques for these deep architectures remains an open problem.

**Why It Matters:** Mitigating collapse is essential for the practical scaling and deployment of hierarchical self-supervised learning architectures in time-series domains.

**Evidence:** Due to representation collapse, concatenating two JEPAs is a double-edged design, since both the input and output of the subsequent JEPA are prone to representation collapse.