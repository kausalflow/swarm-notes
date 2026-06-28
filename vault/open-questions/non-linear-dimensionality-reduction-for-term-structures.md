---
created_at: '2026-06-28T08:16:22Z'
source_papers:
- '[[openalex-2606.26815-data-driven-duration-management-term-structure-forecasting-u]]'
title: Non-linear dimensionality for yield curves
---

**Background:** Dimensionality reduction techniques are essential for modeling term structures, yet traditional linear approaches like PCA often lack the flexibility to capture complex nonlinearities during periods of market stress or structural breaks. While autoencoders have been introduced as non-linear alternatives for factor extraction, their comparative advantage in performance and interpretability versus established methods like Dynamic Nelson-Siegel (DNS) remains context-dependent.

**Question / Future Work:** There is an unresolved need to determine the conditions under which autoencoder-based non-linear dimensionality reduction provides a statistically and economically significant improvement over traditional, interpretable parametric models for term structure forecasting, particularly when applied to high-dimensional datasets or in regimes with significant structural shifts. While current results indicate AEs for rate compression did not outperform other methods in the studied set, it remains an open question whether their utility increases in higher-dimensional settings or if their potential for applications beyond forecasting, such as stress testing and scenario generation, can be rigorously quantified against existing industry standards.

**Why It Matters:** Clarifying the specific domains where non-linear dimensionality reduction outperforms linear counterparts is critical for moving beyond empirical benchmarking and establishing a theoretical basis for the adoption of machine learning in fixed-income risk management.

**Evidence:** We do not dismiss the potential value of AEs for interest rates. We believe AEs for zero-rate compression can have even greater value in higher-dimensional settings... AEs for interest rates may also prove useful in contexts beyond forecasting, such as data reconstruction, scenario generation, risk management, or stress testing applications.