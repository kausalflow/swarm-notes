---
created_at: '2026-05-31T08:10:36Z'
source_papers:
- '[[openalex-2605.29976-evaluating-skill-and-stability-of-archesweather-and-archeswe]]'
title: Improving climate model OOD generalization
---

**Background:** Machine learning models for atmospheric dynamics are frequently trained on weather forecasting tasks with short lead times and later adapted for climate emulation by incorporating slowly-varying boundary conditions like sea surface temperatures. When these models are subjected to out-of-distribution (OOD) forcings, such as elevated warming scenarios, they often exhibit reduced sensitivity compared to traditional physics-based models due to regression-to-the-mean effects.

**Question / Future Work:** There is an unresolved need for architectures that improve climate model generalization under out-of-distribution forcing scenarios, such as developing dedicated coupling modules that ensure the atmospheric model's output remains physically consistent with the prescribed forcings.

**Why It Matters:** Ensuring robust model responses to out-of-distribution forcings is essential for using data-driven emulators to reliably forecast future climate change scenarios.

**Evidence:** First, the deterministic ArchesWeather models predict the next state directly. Because of the regression to the mean effect, models conditioned on OOD forcings are biased to predict states closer to the training distribution’s mean... Making these models fully generalizable to future climate change scenarios is an area of active research.