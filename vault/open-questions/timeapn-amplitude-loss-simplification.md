---
created_at: '2026-03-27T14:08:54Z'
source_papers:
- '[[openalex-2603.17436-timeapn-adaptive-amplitude-phase-non-stationarity-normalizat]]'
title: Amplitude Loss Function Simplification
---

**Background:** Time series forecasting models often struggle with non-stationary data, leading to degraded predictive performance due to evolving amplitude and phase characteristics.

**Question / Future Work:** Investigating whether the explicit modeling of amplitude information in the loss function ($\mathcal{L}_{\mathrm{MPPM}}$) alongside mean and phase, as proposed by TimeAPN, can be replaced or simplified while maintaining or exceeding current performance benchmarks, given that the main reconstruction relied on phase correction and mean addition, not explicit amplitude reconstruction via IFT.