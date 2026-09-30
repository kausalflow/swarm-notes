---
created_at: '2026-09-30T10:49:39Z'
source_papers:
- '[[openalex-2609.33276-chronoflow-hierarchical-flow-matching-for-irregular-time-ser]]'
title: Discrete Structure and Conditioning Shift
---

**Background:** Hierarchical generative models for irregular time series rely on continuous relaxations, rounding, and thresholding steps that can introduce conditioning shift between training and inference phases.

**Question / Future Work:** Address conditioning shift and discrete structure handling in hierarchical flow matching models for irregular time series generation. Specifically, investigate discrete flow matching and consistency-preserving decoding methods to better bridge the gap between continuous relaxations during training and discrete categorical rounding/thresholding operations at inference time.

**Why It Matters:** Conditioning shift between ground-truth training inputs and generated upstream conditions is a central bottleneck in multi-stage hierarchical generative models, impacting error propagation and overall fidelity.

**Evidence:** Discrete flow matching (Gat et al., 2024) and consistency-preserving decoding are promising extensions. Downstream stages are trained with ground-truth conditions but receive generated conditions at inference, leaving a conditioning shift that the eICU interventions diagnose without resolving.