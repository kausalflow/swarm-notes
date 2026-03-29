---
created_at: '2026-03-29T06:08:10Z'
source_papers:
- '[[openalex-2603.25687-on-neural-scaling-laws-for-weather-emulation-through-continu]]'
title: Scaling laws for probabilistic emulation
---

**Background:** The transition from deterministic to probabilistic models is a major direction in weather forecasting, often involving techniques like diffusion models or ensemble training to capture inherent chaos.

**Question / Future Work:** Develop and analyze neural scaling laws for weather emulation models trained using probabilistic objectives (e.g., diffusion models or CRPS-based ensemble training) instead of the current deterministic MSE loss, to see if probabilistic training exhibits different scaling behaviors and yields better diagnostics for chaotic systems.

**Why It Matters:** Understanding how scaling laws behave under probabilistic objectives is necessary to guide the development of next-generation foundation models for atmospheric science.

**Evidence:** The main limitation of this paper is its focus on deterministic training of the weather model. Given the inherently chaotic nature of weather, probabilistic estimates are often more informative for forecasting at future time points, with metrics such as continuous ranked probability scores (CRPS) and spread-skill ratios (SSR) providing better diagnostics for a model’s predictive capability. Addressing this would involve training (or cooling down) models using diffusion objectives [...] or CRPS-based ensemble training [...] and this may exhibit different scaling behaviors—this is left for future work.