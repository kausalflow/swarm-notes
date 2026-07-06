---
created_at: '2026-07-06T08:54:41Z'
source_papers:
- '[[openalex-2412.10578-cesar-a-convolutional-echo-state-autoencoder-for-highresolut]]'
title: Handling Irregular Spatial Sampling
---

**Background:** Convolutional neural networks are frequently constrained to regular grid structures, which limits their applicability to observational data sets that are typically collected at irregular spatial locations.

**Question / Future Work:** The current model formulation requires data to be arranged on a regular grid, which is standard for atmospheric simulations but incompatible with many real-world observational datasets collected at scattered sites. Extending this framework to support irregular spatial sampling would likely require incorporating graph neural network architectures or similar unstructured spatial modeling techniques.

**Why It Matters:** This is a major bottleneck for the practical deployment of the proposed model in real-world environmental monitoring applications where sensor placement is often constrained by terrain or infrastructure.

**Evidence:** In its current formulation, CESAR is limited to data on a regular grid, a feature which is very common on simulated data, but not with observational data.