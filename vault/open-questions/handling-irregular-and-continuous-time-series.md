---
created_at: '2026-09-03T09:16:55Z'
source_papers:
- '[[openalex-2608.31013-tspfn-a-temporal-tabular-foundation-model-for-physiological]]'
title: Handling Irregularly Sampled Time Series
---

**Background:** Tabular foundation models such as TabPFN lack native mechanisms to process the temporal and channel-wise dependencies inherent to physiological time series.

**Question / Future Work:** Extend the underlying foundation model architectures and pretraining frameworks to natively accommodate streaming, continuous-time, or irregularly sampled physiological recordings without relying on rigid windowing or uniform grid constraints.

**Why It Matters:** Crucial for expanding tabular foundation models to handle continuous or irregularly sampled real-world medical data streams beyond fixed-length windows.

**Evidence:** While tabular foundation models such as TabPFN offer an attractive alternative to conventional fine-tuning through in-context learning, they are not designed to capture the temporal dependencies inherent to physiological signals.