---
created_at: '2026-10-23T09:40:00Z'
source_papers:
- '[[openalex-2610.28495-model-and-layer-level-closed-loop-forecasting-with-ssm-based]]'
title: Forecasting with Spiking Neural Networks
---

**Background:** Spiking neural networks require resolving how autoregressive forecasting recursion is performed when future input values are unavailable.

**Question / Future Work:** Investigating how to optimally perform forecasting with spiking neural networks remains an open challenge, particularly given that the standard autoregressive nature of sequence processing requires values that are unavailable during the forecasting phase.

**Why It Matters:** Addressing this question is vital for enabling efficient neuromorphic time-series forecasting and understanding the trade-offs of low-bit quantized activations in autoregressive generation.

**Evidence:** However, how to best perform forecasting with SNNs is an open question, where the standard autoregressive nature of the data processing with SNNs requires values that are not available during the forecasting phase.