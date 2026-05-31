---
created_at: '2026-05-31T08:08:30Z'
source_papers:
- '[[openalex-2605.29401-rethinking-post-training-recipes-for-multimodal-time-series]]'
title: Beyond simple forecast revision
---

**Background:** Multimodal time-series forecasting requires integrating numerical history with unstructured semantic context, yet existing approaches struggle to balance TSFM-based numerical performance with LLM-based reasoning capabilities.

**Question / Future Work:** There is a need to explore interaction mechanisms between LLMs and TSFMs beyond simple forecast revision, such as integrating code execution for data manipulation or advanced tool-use frameworks. These alternative modalities could enhance the model's ability to process richer information sources or query external knowledge bases.

**Why It Matters:** This addresses a fundamental architectural limitation; as forecasting moves beyond simple text-numerical alignment, the current 'reviser' paradigm may lack the flexibility required for more complex reasoning or external data retrieval.