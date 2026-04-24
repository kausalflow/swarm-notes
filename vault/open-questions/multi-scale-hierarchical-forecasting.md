---
created_at: '2026-04-24T06:58:28Z'
source_papers:
- '[[openalex-2502.11340-s2tx-cross-attention-multi-scale-state-space-transformer-for]]'
title: Multi-Scale Hierarchical Forecasting
---

**Background:** State-of-the-art time series forecasting models often employ hybrid architectures to combine global context from state-space models and local features from transformers, typically using a two-scale hierarchy.

**Question / Future Work:** Developing architectures that effectively integrate more than two temporal scales while maintaining a lightweight computational footprint is an unresolved problem, particularly for long sequences where intermediate temporal dynamics are informative.

**Why It Matters:** Moving beyond binary (local vs. global) scale hierarchies is a substantial research direction for capturing multi-scale phenomena in time series forecasting.

**Evidence:** Another limitation is the lack of diversity in the multi-scale approach. The current architecture only deals with global and local patches with no learning of the intermediates scales.