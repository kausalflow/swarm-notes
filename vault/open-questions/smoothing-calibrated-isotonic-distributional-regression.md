---
created_at: '2026-10-25T09:29:59Z'
source_papers:
- '[[openalex-2610.31258-on-the-calibration-of-isotonic-distributional-regression]]'
title: Calibrated Smoothing for Isotonic Distributional Regression
---

**Background:** Isotonic distributional regression (IDR) estimates conditional distributions under order restrictions but produces discrete cumulative distribution functions that can lead to calibration artifacts.

**Question / Future Work:** Develop smoothing techniques or alternative post-processing methods for isotonic distributional regression (IDR) that eliminate Thomae's function-like probability integral transform (PIT) spiking artifacts while preserving probabilistic calibration and avoiding undesirable deviations from uniformity.

**Why It Matters:** Crucial for deploying non-parametric probabilistic forecasting models reliably across domains like meteorology and energy without suffering from hidden calibration artifacts caused by discreteness.