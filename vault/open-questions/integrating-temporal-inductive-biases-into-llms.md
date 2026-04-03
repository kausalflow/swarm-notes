---
created_at: '2026-04-03T06:06:49Z'
source_papers:
- '[[openalex-2603.29974-meteorology-driven-gpt4ap-a-multi-task-forecasting-llm-for-a]]'
title: Integrating temporal inductive biases into LLMs
---

**Background:** Large language models adapted for time-series forecasting often lack the explicit temporal inductive biases present in specialized architectures, limiting their performance in high-data settings.

**Question / Future Work:** Develop hybrid architectures that integrate explicit temporal modeling (e.g., spectral or state-space components) with LLM-based representational learning to improve forecasting accuracy across both low-data and data-rich regimes.

**Why It Matters:** This is a critical bottleneck for scaling LLM-based forecasters to compete with established state-of-the-art time-series models across all performance regimes.

**Evidence:** GPT4AP does not currently surpass specialized architectures in long-term forecasting under data-rich conditions.