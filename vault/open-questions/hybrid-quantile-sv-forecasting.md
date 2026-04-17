---
created_at: '2026-04-17T06:29:10Z'
source_papers:
- '[[openalex-2604.12927-forecasting-oil-prices-across-the-distribution-a-quantile-va]]'
title: Hybrid Quantile-SV Forecasting Frameworks
---

**Background:** Oil price forecasting models generally struggle to capture upside tail risks (price spikes) compared to downside tail risks (price collapses). Stochastic volatility models often perform better at capturing these spikes than existing quantile-based approaches.

**Question / Future Work:** Develop hybrid modeling frameworks that integrate quantile-specific coefficients (for modeling downside asymmetries) with stochastic volatility (for modeling upside price movements) to provide more comprehensive tail risk assessment in volatile commodity markets.

**Why It Matters:** This addresses the critical bottleneck where quantile VAR models show asymmetric performance, failing to characterize extreme upside price spikes as effectively as downside risk.

**Evidence:** The persistent difficulty in forecasting right-tail events suggests that upside risks may require hybrid approaches combining quantile-specific coefficients with stochastic volatility, or alternative predictors designed to capture supply disruption risks.