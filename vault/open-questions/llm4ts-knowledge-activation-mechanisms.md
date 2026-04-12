---
created_at: '2026-04-12T06:19:33Z'
source_papers:
- '[[openalex-2510.12847-lifting-manifolds-to-mitigate-pseudo-alignment-in-llm4ts]]'
title: Activating LLM Knowledge for Time-Series
---

**Background:** Large language models (LLMs) used for time series forecasting often exhibit a 'pseudo-alignment' phenomenon, where the model's representations of time series and language tokens become superficially aligned due to the interplay between the LLM's intrinsic cone effect and the low-dimensional manifold of time-series data.

**Question / Future Work:** Research is needed to identify architectural modifications or training strategies that effectively activate latent knowledge within pretrained LLMs for time-series forecasting without relying on heuristic-based manifold enhancement or triggering detrimental pseudo-alignment. The development of more principled, automated mechanisms that distinguish between modality-specific features and shared semantic information is essential for improving downstream performance.

**Why It Matters:** Understanding how to genuinely leverage LLM knowledge for time series is crucial for overcoming performance bottlenecks caused by pseudo-alignment and moving beyond ad-hoc architectural adjustments.

**Evidence:** What may be the root causes for pseudo-alignment? and (2) Which architectural modifications or training strategies can effectively activate the rich knowledge of LLMs for time series forecasting?