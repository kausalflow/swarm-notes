---
created_at: '2026-07-09T08:19:39Z'
source_papers:
- '[[openalex-2607.05127-physically-relevant-information-learning-in-high-dimensional]]'
title: Determining Effective TiDe Dimensionality
---

**Background:** The TiDe framework enables the construction of high-dimensional state spaces by taking successive time-derivatives of univariate time-series, which allows for the exploration of complex dynamical systems without traditional dimensionality reduction. While lower-order derivatives typically capture the primary physical information in the systems examined, the effective dimensionality of more complex, unknown systems remains to be determined.

**Question / Future Work:** Future investigations should systematically determine the optimal or effective dimensionality required to capture the full dynamical complexity of diverse physical systems beyond those studied here. Specifically, identifying when higher-order derivatives (beyond the second or third order) provide meaningful physical information versus when they merely accumulate numerical noise or redundancy is an open challenge for arbitrary systems.

**Why It Matters:** Establishing a robust, universal heuristic for determining the effective TiDe dimensionality is critical to preventing 'information frustration' and performance degradation caused by adding redundant or noise-dominated dimensions in large-scale applications.

**Evidence:** Since the TiDe framework can be formally extended up to arbitrarily high derivative orders, its application to other dynamical systems may reveal different scenarios. In particular, systems with sharper transitions or richer high-frequency features may benefit from the inclusion of higher derivatives (capturing patterns in e.g. accelerations, jerks, snaps, etc.).