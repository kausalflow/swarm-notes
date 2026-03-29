---
created_at: '2026-03-29T06:07:28Z'
source_papers:
- '[[openalex-2603.24936-tigflow-grpo-trajectory-forecasting-via-interaction-aware-fl]]'
title: Bridging Distribution Fitting and Behavioral Alignment
---

**Background:** Generative models for trajectory forecasting often rely on supervised fitting to match empirical data distributions, which struggles to directly enforce non-differentiable real-world rules.

**Question / Future Work:** The development of methods that can bridge the gap between statistical distribution fitting (like Conditional Flow Matching) and explicit behavioral alignment with complex, non-differentiable rules (like social norms and physical map constraints) remains an open challenge in generating reliable motion predictions.

**Why It Matters:** Successfully bridging this gap is crucial for deploying trajectory forecasters in safety-critical applications like autonomous driving, where adherence to physical and social laws is paramount.

**Evidence:** A central challenge in trajectory forecasting is the gap between statistical distribution fitting and behavior-aware generation. Most recent methods are trained with supervised objectives, which encourage models to match empirical trajectory distributions. Although this strategy captures common motion patterns effectively, it does not directly optimize for compliance with environmental rules. As a result, incorporating non-differentiable physical constraints and social conventions into the training process remains difficult.