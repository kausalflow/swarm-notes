---
created_at: '2026-06-05T08:37:56Z'
source_papers:
- '[[openalex-2606.03097-from-long-news-to-accurate-forecast-importance-aware-fusion]]'
title: Scalable Multimodal Exogenous Fusion
---

**Background:** Incorporating high-dimensional, diverse exogenous information into time-series forecasting systems often creates bottlenecks due to context window constraints and the lack of guidance in retrieval strategies. Integrating these disparate data sources effectively remains a challenge for LLM-based predictive pipelines.

**Question / Future Work:** Investigating efficient, scalable fusion strategies for massive exogenous datasets and expanding RAG-based forecasting to multimodal information sources like event graphs and social media, rather than relying solely on plain text, remains a primary research challenge.

**Why It Matters:** This captures the fundamental limitation of scaling retrieval-augmented forecasting beyond static text and highlights the need for architectures that process heterogeneous, high-volume inputs.

**Evidence:** First, we will investigate more efficient and scalable fusion strategies for larger news pools and longer forecasting horizons. Second, we aim to generalize the method to multimodal exogenous information, such as social media, reports, and event graphs, beyond plain news text.