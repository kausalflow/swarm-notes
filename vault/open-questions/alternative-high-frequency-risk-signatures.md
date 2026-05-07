---
created_at: '2026-05-07T07:38:33Z'
source_papers:
- '[[openalex-2605.02326-large-scale-asset-selection-via-metric-dependence-with-enric]]'
title: Alternative High-Frequency Risk Signatures
---

**Background:** Modern asset selection pipelines often rely on specific intraday data signatures to represent risk. Research in this field aims to determine which high-frequency features most effectively capture risk dynamics for large-scale portfolio construction.

**Question / Future Work:** There is a need to explore alternative high-frequency risk state signatures beyond the intraday absolute log-price-change curve, such as jump-robust, multi-resolution, or other complex intraday features in enhancing the Metric Dependence Screening (MDS) procedure.

**Why It Matters:** Identifying more informative risk signatures could significantly improve the quality of the asset universe passed to portfolio optimizers.

**Evidence:** The framework is not limited to the intraday absolute log-price-change signature used here. It can incorporate alternative high frequency risk state signatures, including jump robust and multi resolution intraday features.