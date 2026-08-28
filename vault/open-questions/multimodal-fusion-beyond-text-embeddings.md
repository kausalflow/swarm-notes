---
created_at: '2026-08-28T16:59:02Z'
source_papers:
- '[[openalex-2608.25128-when-does-context-routing-help-a-systematic-study-of-multi-m]]'
title: Multimodal Fusion Beyond Text Embeddings
---

**Background:** Multi-modal time series forecasting methods integrate auxiliary context features into temporal predictions, but it remains unclear whether reported performance gains stem from genuine context utilization or incidental architectural effects.

**Question / Future Work:** Investigate whether multi-modal fusion and context routing mechanisms can be reliably extended and generalized beyond text embeddings to diverse auxiliary modalities such as high-frequency financial news, tabular covariates, images, and audio streams.

**Why It Matters:** Understanding modality-agnostic applicability is crucial since practical forecasting systems frequently ingest heterogeneous auxiliary streams (e.g., satellite imagery, transactional tables, and audio feeds) rather than text alone.

**Evidence:** The datasets we evaluate provide context as embeddings of textual side information (Time-MMD) or financial news (FinMultiTime); we do not test image or audio modalities. We use “fusion” throughout in this embedding-level sense.