---
created_at: '2026-10-09T11:36:25Z'
source_papers:
- '[[openalex-2610.09090-tucker-bottleneck-attention-for-multi-dimensional-sequence-m]]'
title: Adaptive Tucker Rank Selection
---

**Background:** Tucker bottleneck attention (TuBA) relies on empirically determined Tucker ranks to control the core size of multidimensional hidden tensors for sequence modeling.

**Question / Future Work:** The investigation of adaptive or automated rank selection strategies for Tucker bottleneck attention remains an important open challenge, as current implementations rely on manually tuned hyperparameters for the Tucker core dimensions.

**Why It Matters:** Eliminating the need for manual hyperparameter tuning of tensor ranks is crucial for scaling Tucker-based attention to diverse architectures and datasets without costly grid searches.

**Evidence:** Currently, Tucker ranks are selected empirically, and our evaluation focuses on data with native multidimensional structure. Future work could investigate adaptive rank selection and extend TuBA to long one-dimensional sequences, where the choice of tensorization introduces an additional modeling decision.