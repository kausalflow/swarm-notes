---
created_at: '2026-06-07T08:18:45Z'
source_papers:
- '[[openalex-2606.06285-trace-a-temporal-conditional-estimation-for-multimodal-time]]'
title: Generative Modeling of Absent Modalities
---

**Background:** The current paradigm for multimodal time series foundation models primarily treats missingness and irregular sampling as a value imputation problem. This often results in a loss of conditional uncertainty and distorted temporal dynamics, as most models rely on deterministic completion techniques rather than generative conditional estimation.

**Question / Future Work:** There is a need to extend conditional estimation from partial observation to explicit generative modeling for entirely absent modalities. Current approaches often rely on the backbone's existing routing mechanisms rather than a principled generative process for synthesis.

**Why It Matters:** Addressing complete modality absence is a critical challenge for real-world multimodal time series foundation models, as it represents a more complex scenario than partial missingness.