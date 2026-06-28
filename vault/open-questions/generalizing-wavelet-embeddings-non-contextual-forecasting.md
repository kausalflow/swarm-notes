---
created_at: '2026-06-28T08:15:37Z'
source_papers:
- '[[openalex-2606.26487-speaking-numbers-to-llms-multi-wavelet-number-embeddings-for]]'
title: Generalizing Wavelet Embeddings
---

**Background:** Large language models (LLMs) often rely on discrete tokenization, which can obscure the ordinal and continuous nature of numerical data in time series forecasting tasks. While specific input embedding techniques can mitigate this, the integration of these techniques into broader, non-contextual or alternative tokenization-based forecasting architectures remains underexplored.

**Question / Future Work:** There is a need to determine the generalizability of multi-wavelet number embeddings (TempoWave) to forecasting pipelines that do not specifically leverage contextual information or that rely on standard discretization and binning methods. Future work should investigate whether this embedding interface can maintain its performance advantages in these more conventional, non-contextual forecasting environments.

**Why It Matters:** Understanding if this embedding technique is universally beneficial across various types of forecasting architectures, rather than just those already utilizing external context, is critical for establishing it as a general-purpose improvement for numerical LLM interfaces.

**Evidence:** A promising direction for future work is to investigate whether TempoWave also benefits non-contextual forecasting pipelines that rely on discretization or binning-based tokenization of time series values.