---
created_at: '2026-09-19T09:03:40Z'
source_papers:
- '[[openalex-2609.18157-tensor-bekk-conditional-covariance-modeling-and-inference-fo]]'
title: Extensions of Tensor-BEKK Models
---

**Background:** Tensor-valued time series models capture multiway structures in high-dimensional economic and financial data but require flexible covariance dynamics without excessive parameter growth.

**Question / Future Work:** Extend the T-BEKK recursion to accommodate asymmetric volatility responses and higher-order dynamics while preserving its modewise interpretation, and investigate sparsity or low-rank restrictions on mode-specific ARCH and GARCH matrices to achieve further dimension reduction in large-scale settings.

**Why It Matters:** Crucial for enhancing the modeling flexibility of tensor-based conditional covariance frameworks to handle financial asymmetries and extremely high ambient dimensions.

**Evidence:** First, the T-BEKK recursion could be extended to accommodate asymmetric volatility responses and higher-order dynamics while preserving its modewise interpretation. Second, when some mode dimensions are large, sparsity or low-rank restrictions on the mode-specific ARCH and GARCH matrices may provide further dimension reduction.