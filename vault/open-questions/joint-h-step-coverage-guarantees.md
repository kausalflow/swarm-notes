---
created_at: '2026-04-11T05:54:37Z'
source_papers:
- '[[openalex-2604.07325-conformal-prediction-with-time-series-data-via-sequential-co]]'
title: Joint H-step prediction coverage
---

**Background:** Most conformal prediction methods for time-series focus on one-step-ahead prediction intervals or sets. Ensuring robust joint coverage guarantees for entire sequences of future observations remains an open challenge.

**Question / Future Work:** Developing joint H-step ahead prediction regions is necessary to provide coverage guarantees over entire sequences rather than individual time points, which is critical for decision-making in applications like inventory management or energy load forecasting.

**Why It Matters:** Joint coverage is a fundamental requirement for sequential decision-making where cumulative risk is the primary metric of concern.

**Evidence:** We believe certain problems benefit from a coverage guarantee on the joint prediction sets over H steps.