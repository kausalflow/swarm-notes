---
created_at: '2026-05-03T07:13:52Z'
source_papers:
- '[[openalex-2604.27967-differentiable-latent-structure-discovery-for-interpretable]]'
title: Scalability of latent structures
---

**Background:** Multi-task Gaussian processes suffer from computational complexity that scales poorly with the number of tasks, latent factors, and temporal density.

**Question / Future Work:** Investigating computational strategies to decouple the scalability of latent path discovery from the number of measured variables, such as hierarchical pathway assignment or block-sparse kernel approximations, is required for large-scale clinical application.

**Why It Matters:** Scalability remains a primary bottleneck for deploying high-fidelity structure-learning models on large-scale EHR datasets with high-dimensional feature spaces.

**Evidence:** From a design standpoint, LP-StructGP currently faces scalability limitations. ... A simple remedy is to assign latent pathway components only to a subset of nodes (e.g., root nodes).