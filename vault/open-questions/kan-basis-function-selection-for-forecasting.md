---
created_at: '2026-04-30T07:23:41Z'
source_papers:
- '[[openalex-2604.23968-decompkan-decomposed-patch-kan-for-long-term-time-series-for]]'
title: Optimal KAN Basis Functions
---

**Background:** Kolmogorov-Arnold Networks (KANs) use B-spline basis functions as learnable edges, offering potential advantages in transparency and functional representation over standard MLPs.

**Question / Future Work:** There is a need for a rigorous investigation into how different basis functions (Fourier, Chebyshev, RBF, Gabor, etc.) interact with temporal signal structures when used within a decomposed forecasting architecture, as the interaction between basis choice and signal properties remains under-explored.

**Why It Matters:** The basis function choice is central to the KAN representational framework and impacts domain-specific performance, making it a critical research direction for KAN-based time series modeling.

**Evidence:** a rigorous study of alternative basis functions (Fourier, Chebyshev, RBF, Gabor) within the decomposed Patch-KAN framework, as preliminary synthetic experiments (Appendix D) suggest that basis choice interacts with signal structure in ways that merit deeper investigation