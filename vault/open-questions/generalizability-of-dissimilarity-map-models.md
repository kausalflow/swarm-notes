---
created_at: '2026-03-29T06:07:49Z'
source_papers:
- '[[openalex-2603.25139-dissimilarity-based-persistent-coverage-control-of-multi-rob]]'
title: Generalizability of Dissimilarity Map Models
---

**Background:** Dynamic sensor positioning for spatial forecasting, such as solar irradiance prediction, requires strategies that balance coverage with the need for data in regions with high predictive uncertainty.

**Question / Future Work:** The current framework, while effective, relies on a dissimilarity map derived from a specific kriging model for guiding mobile sensors. A crucial next step is investigating the generalizability of the persistent coverage control algorithm when paired with other spatial interpolation or machine learning models used for generating the dissimilarity map.

**Why It Matters:** The dependence on a specific kriging model limits the broad applicability of the proposed control scheme; testing against alternative uncertainty quantification methods (like Gaussian Processes with different kernels or other spatial ML models) is necessary to validate its general robustness.

**Evidence:** future work on the robustness and applicability of the proposed persistent coverage control algorithm with various spatial interpolation or machine learning models for uncertainty quantification.