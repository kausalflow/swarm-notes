---
created_at: '2026-06-07T08:20:03Z'
source_papers:
- '[[openalex-2606.06007-diffusion-models-for-adaptive-sequential-data-generation]]'
title: Adaptive Sequential Diffusion Design
---

**Background:** Diffusion models are typically designed for static data or joint trajectory generation, which can implicitly violate causal structures in sequential data.

**Question / Future Work:** Research is needed into building diffusion-based generative frameworks that generate sequential data while strictly enforcing adaptiveness, ensuring each generated step depends only on historical information.

**Why It Matters:** Non-anticipative generation is fundamental for applications in finance, real-time control, and simulation where causality determines decision-making.

**Evidence:** Designing diffusion models that can simulate sequential data in an adapted manner, and hence without anticipation of future information, therefore remains an open challenge.