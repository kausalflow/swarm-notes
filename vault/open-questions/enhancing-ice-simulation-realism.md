---
created_at: '2026-05-21T08:32:32Z'
source_papers:
- '[[openalex-2605.18268-time-series-extrinsic-regression-of-ion-cyclotron-emission-s]]'
title: Improving ICE simulation realism
---

**Background:** Ion Cyclotron Emission (ICE) spectra in magnetized fusion plasmas are influenced by kinetic and geometric factors, such as non-homogeneous magnetic fields and mode conversion, which are often omitted in simplified 1D simulations.

**Question / Future Work:** Establishing a more robust mapping between simulation-based training sets and experimental observations requires extending current 1D3V particle-in-cell simulation frameworks to account for 2D/3D geometry, spatially varying electromagnetic fields, and wave propagation physics. This is essential for improving the cross-domain generalization of models trained on synthetic data to the complex, non-ideal conditions found in real-world magnetic fusion devices.

**Why It Matters:** This is critical for improving the generalizability of machine learning models trained on synthetic data to the complex, non-ideal conditions found in real-world magnetic fusion devices.

**Evidence:** The periodic simulation domain implies a homogeneous, infinite 1D plasma without source or sink effects, complex geometry, spatially-varying background electromagnetic fields or mode conversion.