---
created_at: '2026-04-18T06:07:27Z'
source_papers:
- '[[openalex-2604.13478-deepbullwhip-an-open-source-simulation-and-benchmarking-for]]'
title: Multi-Product Demand Modeling
---

**Background:** Supply chain simulation currently relies on univariate demand models, whereas real-world supply chain management requires accounting for interactions between multiple products.

**Question / Future Work:** The existing demand generators are limited to univariate time series models. Future work is required to extend the demand generator abstract base class to support multivariate time series, which would allow for the analysis of multi-product demand and substitution effects within the bullwhip framework.

**Why It Matters:** Real-world demand is often correlated across products; ignoring this correlation limits the accuracy of bullwhip analyses in realistic multi-SKU inventory environments.