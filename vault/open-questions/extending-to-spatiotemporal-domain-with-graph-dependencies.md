---
created_at: '2026-03-29T06:07:36Z'
source_papers:
- '[[openalex-2603.25046-mp-moe-matrix-profile-guided-mixture-of-experts-for-precipit]]'
title: Extend to Spatiotemporal Domain
---

**Background:** Current precipitation forecasting models often rely on 1D time-series analysis at the basin scale, which simplifies the problem by overlooking correlated atmospheric phenomena across neighboring geographical areas.

**Question / Future Work:** Future work should focus on extending the current 1D time-series, basin-scale framework to a full spatiotemporal domain by integrating graph-based dependencies. This extension is necessary to ensure regional consistency in forecasts across adjacent catchments, which is crucial for accurate large-scale hazard assessment.

**Why It Matters:** Moving from 1D to spatiotemporal modeling is critical for capturing large-scale atmospheric correlation and improving regional hazard forecasting consistency.

**Evidence:** The current implementation focuses on 1D time-series modeling at the basin scale, a choice that prioritizes local structural fidelity over broader spatiotemporal field correlations. ... Future research will focus on extending the framework to the spatiotemporal domain by incorporating graph-based dependencies, ensuring regional consistency across neighboring catchments.