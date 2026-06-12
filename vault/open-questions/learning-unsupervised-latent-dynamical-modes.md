---
created_at: '2026-06-12T08:52:52Z'
source_papers:
- '[[openalex-2606.10592-dirichlet-guided-group-forecasting-for-alleviating-over-smoo]]'
title: Learning Unsupervised Latent Dynamical Modes
---

**Background:** Time series forecasting models often experience over-smoothing due to the compression of non-convex latent dynamical modes under single-realization supervision.

**Question / Future Work:** It remains an open question how to effectively learn latent dynamical modes and their selection probabilities in scenarios where the training data provides only one realized trajectory per history. Future work is needed to explore unsupervised or self-supervised methods for identifying these modes, as well as developing computationally efficient hierarchical uncertainty representations.

**Why It Matters:** Addressing mode collapse in multi-modal forecasting is critical for regime-sensitive applications like financial or energy forecasting.

**Evidence:** the latent mode M is not observed. For each historical window, the dataset usually provides only one realized future trajectory, which corresponds to one realized mode. Other dynamically plausible modes under the same observed history are not directly supervised.