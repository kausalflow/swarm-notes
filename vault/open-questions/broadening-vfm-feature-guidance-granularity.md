---
created_at: '2026-04-16T06:28:59Z'
source_papers:
- '[[openalex-2604.11707-representations-before-pixels-semantics-guided-hierarchical]]'
title: Expanding VFM feature guidance
---

**Background:** Hierarchical video prediction models decompose the task into semantic representation forecasting followed by conditional pixel synthesis. These models often rely on pretrained vision foundation models (VFMs) to guide the generative process.

**Question / Future Work:** Future work is needed to explore the breadth and granularity of VFM features used for guidance. Integrating more structured semantic priors, such as explicit 3D perception cues, scene-level geometry, or collaborative encoders, could enhance multimodal reasoning and improve the structural integrity of the generated predictions.

**Why It Matters:** This is a key architectural bottleneck identified by the authors as the next logical step to improve the structural accuracy of hierarchical video prediction beyond existing VFM feature approaches.