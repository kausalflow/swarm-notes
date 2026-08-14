---
created_at: '2026-08-14T06:07:20Z'
source_papers:
- '[[openalex-2608.10941-physics-informed-diffusion-generative-model-for-time-series]]'
title: Non-Smooth Physics-Informed Generative Modeling
---

**Background:** Generative time-series modeling often struggles to incorporate complex physical laws, particularly when dealing with non-differentiable events or non-smooth industrial dynamics.

**Question / Future Work:** Handling discrete events, non-smooth dynamics like actuator saturation, or complex control logic remains a challenge for gradient-based methods and requires the development of novel hybrid approaches capable of embedding non-differentiable physical laws into generative frameworks.

**Why It Matters:** Extending physics-informed generative models to handle non-smooth and discrete physical dynamics is a fundamental challenge for applying AI safely across broader industrial engineering systems.

**Evidence:** First, our current constraint library is most effective for differentiable or smoothly approximable physical laws. Handling discrete events, non-smooth dynamics like actuator saturation, or complex control logic remains a challenge for gradient-based methods and may require hybrid approaches.