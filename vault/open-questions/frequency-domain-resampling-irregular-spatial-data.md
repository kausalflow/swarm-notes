---
created_at: '2026-07-31T07:44:33Z'
source_papers:
- '[[openalex-2504.19337-frequency-domain-resampling-for-gridded-spatial-data]]'
title: Frequency Domain Resampling for Irregular Spatial Data
---

**Background:** In frequency domain analysis of spatial processes, spectral mean statistics capture covariance structures via periodogram aggregates, but existing bootstrap approximations often struggle with complex variance structures arising from non-Gaussianity or higher-order cumulants.

**Question / Future Work:** Extending frequency domain resampling methods, such as the Hybrid Frequency Domain Bootstrap (HFDB), from gridded lattice data to irregularly spaced spatial observations remains an open problem, presenting non-trivial challenges regarding multiplicative periodogram biases, non-vanishing additive bias from frequency grid selection, and the lack of general distributional theory for spectral means under non-regular sampling locations.

**Why It Matters:** Real-world spatial data are frequently collected at irregular, non-gridded locations rather than regular integer lattices. Developing frequency domain bootstrap and subsampling methods for irregular spatial data is crucial for broadening the applicability of nonparametric spectral inference.

**Evidence:** While we have focused on gridded spatial data here, the general HFDB approach of approximating the complicated distribution of spectral mean statistics, by combining periodogram resampling with subsampling variance corrections, can potentially be extended to inference about spatial processes with irregular sampling locations... Finally, general distributional theory for spectral means under non-regular locations remains a difficult and open problem.