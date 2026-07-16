---
created_at: '2026-07-16T07:14:56Z'
source_papers:
- '[[openalex-2607.11412-uncertainty-quantification-for-eo-regression-tasks-building]]'
title: Uncertainty calibration for saturated targets
---

**Background:** In Earth Observation (EO) regression tasks, models often struggle with high-target values due to data deficiency and sensor saturation, which leads to systematic underestimation and unreliable uncertainty estimates in these extreme ranges.

**Question / Future Work:** Developing uncertainty estimation methods that remain robust and well-calibrated in the presence of signal saturation and data scarcity at the extreme tails of the target distribution remains an unresolved challenge. Currently, standard approaches often see uncertainty intervals widen in these regions without fully capturing the magnitude of the prediction error.

**Why It Matters:** Addressing uncertainty calibration in high-value, saturated regions is critical for the operational reliability of EO products in applications like biomass monitoring and urban planning.

**Evidence:** the largest prediction discrepancies appear in the high-value tail, where the estimated uncertainties are least reliable.