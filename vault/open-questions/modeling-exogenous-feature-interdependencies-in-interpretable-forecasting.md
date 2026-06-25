---
created_at: '2026-06-25T08:19:33Z'
source_papers:
- '[[openalex-2606.23425-interpretable-kolmogorov-arnold-network-with-feature-isolate]]'
title: Modeling Exogenous Feature Interdependencies
---

**Background:** Electricity load forecasting models often struggle to balance high predictive accuracy with structural interpretability when capturing the influence of complex exogenous features like human mobility. Kolmogorov-Arnold Networks (KANs) offer interpretability, but their current architectures often rely on independent feature processing which risks ignoring underlying correlations between exogenous variables.

**Question / Future Work:** Research is needed to develop methods for explicitly modeling cross-feature interdependencies and synergistic effects among exogenous variables within interpretable architectures like KANs, moving beyond simple feature-isolated designs. This could provide a more holistic understanding of behavioral drivers in electricity load without sacrificing the benefits of structural interpretability.

**Why It Matters:** Capturing complex, real-world correlations between multiple exogenous drivers is critical for improving the realism and accuracy of interpretable forecasting models.

**Evidence:** future research could explore methods to explicitly model potential interdependencies and interactions among the different mobility features themselves before or within the KAN layer.