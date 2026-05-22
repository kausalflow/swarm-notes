---
created_at: '2026-05-22T08:16:37Z'
source_papers:
- '[[openalex-2605.19249-beyond-extrapolation-knowledge-utilization-paradigm-with-bid]]'
title: Architecture-agnostic knowledge utilization scaling
---

**Background:** Knowledge utilization paradigms for time-series forecasting often rely on augmenting existing backbones with auxiliary information to stabilize long-horizon predictions.

**Question / Future Work:** The integration of auxiliary continuation-style information currently necessitates either backbone-specific tuning or risks sub-optimal performance when treated as a plug-and-play module. Research is required to make these paradigms architecture-agnostic without sacrificing performance, particularly when scaling to large foundation models where joint fine-tuning is computationally prohibitive.

**Why It Matters:** This issue is critical for the practical adoption of retrieval-enhanced forecasting across a wide variety of existing model architectures, especially large-scale foundation models where full re-training or joint fine-tuning is computationally prohibitive.