---
created_at: '2026-10-29T11:11:00Z'
source_papers:
- '[[openalex-2610.35545-efficient-probabilistic-weather-forecasting-at-quarter-degre]]'
title: Scaling Transport Attention to Higher Resolutions
---

**Background:** High-resolution probabilistic weather forecasting using machine learning remains computationally demanding during both training and inference.

**Question / Future Work:** Determine whether two-sided transport attention mechanisms like Kantorovich Attention can scale effectively to even higher spatial resolutions (beyond quarter-degree) or larger architectures without prohibitive computational overhead.

**Why It Matters:** Scaling sparse transport attention to ultra-high resolutions is critical for capturing finer regional atmospheric dynamics and expanding the accessibility of frontier weather models.

**Evidence:** Bringing this efficiency to 0.25° meets two challenges... Dense self-attention over all points is prohibitive... Here we present Astra... which puts experiments at full resolution, from larger architectures to richer training objectives, within reach of groups without multi-node clusters.