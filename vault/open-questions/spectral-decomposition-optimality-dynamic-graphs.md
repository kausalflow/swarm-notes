---
created_at: '2026-05-09T07:01:37Z'
source_papers:
- '[[openalex-2605.04957-delving-into-non-exchangeability-for-conformal-prediction-in]]'
title: Spectral Decomposition Optimality in Dynamic Graphs
---

**Background:** Conformal prediction relies on the assumption of data exchangeability, which is frequently violated in complex systems such as graph-structured multivariate time series characterized by cross-node coupling and global trends.

**Question / Future Work:** While the proposed spectral graph conditional exchangeability (SGCE) framework provides a methodology for conformal prediction by conditioning high-frequency components on low-frequency trends, the effectiveness of this decomposition depends on the ability to perfectly separate these components. It remains an open question how to rigorously optimize the spectral filter kernels and the associated cutoff scales to maximize the conditional exchangeability of the resulting high-frequency residuals while simultaneously minimizing spectral leakage. Furthermore, it is unresolved how this approach generalizes to time-varying graph structures, where the graph topology—and consequently the spectral domain itself—evolves over time, potentially necessitating dynamic spectral decomposition techniques.

**Why It Matters:** The validity of the proposed conformal prediction method is fundamentally tied to the quality of the spectral decomposition; identifying universal principles for optimal filtering in this context is critical for broadening the applicability of spectral-based UQ to non-stationary or dynamic networks.

**Evidence:** The formal statement of Theorem 5.2 is provided in Appendix C, which formalizes the trade-off between implementation constraints and theoretical validity... it demonstrates that the coverage gap is controllable... as the spectral filter approaches an ideal band-pass... and the high-frequency couplings vanish... the total gap disappears.