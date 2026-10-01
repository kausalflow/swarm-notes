---
created_at: '2026-10-01T11:14:29Z'
source_papers:
- '[[openalex-2609.37435-variational-augmented-invertible-koopman-autoencoder-for-pro]]'
title: CRPS-Based Koopman Autoencoder Training
---

**Background:** Continuous ranked probability score (CRPS)-based loss functions are gaining popularity for training probabilistic neural forecasting models in Earth system sciences and global atmospheric modeling.

**Question / Future Work:** Investigate and evaluate training Koopman autoencoder models directly using a CRPS-based loss criterion instead of likelihood-based objectives, aiming to improve computational scaling for large state dimensions while maintaining calibration.

**Why It Matters:** Directly addresses the computational scaling bottleneck of likelihood-based training for high-dimensional states, which is critical for scaling Koopman autoencoders to massive spatio-temporal Earth science and fluid dynamics applications.

**Evidence:** Interesting directions for future work might include training our model with a CRPS-based loss criterion, as is becoming increasingly popular for global atmosphere forecasting models.