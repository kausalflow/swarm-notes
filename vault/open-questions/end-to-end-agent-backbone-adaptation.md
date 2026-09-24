---
created_at: '2026-09-24T09:37:42Z'
source_papers:
- '[[openalex-2609.24862-when-tomorrow-becomes-today-self-evolving-policies-for-agent]]'
title: End-to-End Agent Backbone Adaptation
---

**Background:** Agentic time series forecasting systems rely on static orchestration rules to coordinate numerical models, reasoning strategies, and intervention rules, causing a mismatch as underlying temporal dynamics and component effectiveness evolve.

**Question / Future Work:** Investigate how to expand agentic forecasting frameworks beyond frozen-backbone architectures to support dynamic adaptation of the underlying foundation models, analytical tools, and semantic reasoners rather than solely updating the orchestration policy (expert trust, path selection, and intervention strength).

**Why It Matters:** Crucial for determining whether end-to-end gradient updates or active fine-tuning of the core foundation models and reasoners can further improve agentic time-series forecasting under distribution drift compared to restricting adaptation strictly to the orchestration layer.

**Evidence:** The language model, numerical forecasters, analytical tools, and prompts remain frozen while the orchestration policy evolves.