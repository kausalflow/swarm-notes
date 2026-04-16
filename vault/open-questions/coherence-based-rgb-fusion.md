---
created_at: '2026-04-16T06:29:29Z'
source_papers:
- '[[openalex-2604.11190-cross-sensor-rgb-spectrograms-a-visual-method-for-anomaly-de]]'
title: Coherence-based RGB spectrogram fusion
---

**Background:** Visualisations of three-sensor magnetometer data currently rely on raw power spectral density to generate RGB spectrograms, often discarding phase information and cross-correlations.

**Question / Future Work:** Incorporating joint normalization or magnitude-squared coherence measures into the RGB channel mapping to preserve phase and absolute-amplitude information, providing a more comprehensive view of sensor health.

**Why It Matters:** Enhances the diagnostic capability of the visualisation by capturing phase relationships and absolute amplitude disparities that are currently lost in the power-spectrum-only approach.

**Evidence:** a complementary view that uses joint normalisation, or that substitutes the magnitude-squared coherence γ^2_{ij} ... for the raw power spectra, would carry phase and absolute-amplitude information into the colour channels.