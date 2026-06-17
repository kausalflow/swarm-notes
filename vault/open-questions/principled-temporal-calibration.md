---
created_at: '2026-06-17T09:25:37Z'
source_papers:
- '[[openalex-2606.16356-simulation-augmented-multi-step-split-conformal-prediction-f]]'
title: Principled Calibration for Temporal Dependence
---

**Background:** Conformal prediction methods provide valid coverage guarantees under exchangeability, but these guarantees are often violated in time-series forecasting due to temporal dependence and non-stationarity. Achieving reliable coverage for aggregated time-series targets—such as annual sums or growth rates—requires addressing these dependencies within the calibration process.

**Question / Future Work:** There is a lack of principled calibration schemes for conformal prediction in time-series forecasting that formally account for temporal dependence. Developing a theoretical framework that rigorously incorporates temporal structure into the calibration of multi-step, aggregated forecasts remains a significant open challenge.

**Why It Matters:** Current methods rely on heuristic aggregation and lack formal coverage guarantees for non-stationary or dependent data, making them insufficient for safety-critical applications in finance or supply chain management.

**Evidence:** Investigating principled calibration schemes that account for temporal dependence is an important direction for future work.