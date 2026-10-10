---
created_at: '2026-10-10T10:53:08Z'
source_papers:
- '[[openalex-2610.12010-pulsebound-future-beat-state-forecasting-under-an-explicit-i]]'
title: End-to-End Streaming Causality for PPG
---

**Background:** Photoplethysmography (PPG) representation learning relies heavily on predicting future signal states or waveforms, but causal attention mechanisms are often insufficient to prevent information leakage from future samples through global normalizations or transforms.

**Question / Future Work:** Investigate how to enforce strict causal information boundaries and causal preprocessing pipelines end-to-end (from raw signal acquisition through offline filtering and resampling to final model tokenization) rather than solely at the stored preprocessed-window interface.

**Why It Matters:** Crucial for deploying biosignal foundation models in real-time streaming clinical environments where raw physiological data streams continuously without pre-segmented windows.

**Evidence:** The guarantee begins at the stored-window interface; it is intentionally narrower than end-to-end streaming causality, which would also require boundary-preserving upstream preprocessing.