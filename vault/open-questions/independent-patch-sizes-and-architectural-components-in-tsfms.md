---
created_at: '2026-11-05T12:51:18Z'
source_papers:
- '[[openalex-2611.02750-investigating-the-effects-of-the-patch-size-in-time-series-f]]'
title: Disentangling Patch Size and Architecture
---

**Background:** Time series foundation models employ various temporal patch sizes and architectures (encoder-only vs. decoder-only), but the combined effect of these choices under matched pretraining conditions remains insufficiently understood across diverse forecasting horizons.

**Question / Future Work:** Determine how independent selection of input and output patch sizes, varied architectural components (such as normalization, positional encodings, and output heads), and extended training budgets or alternative data mixtures interact to influence the downstream performance and compute-accuracy Pareto frontiers of encoder-only and decoder-only time series foundation models.

**Why It Matters:** Understanding the disentangled impact of input versus output patch sizes and specific architectural components is crucial for establishing universal design principles for time series foundation models rather than architecture-specific heuristics.

**Evidence:** The two model families necessarily differ in components beyond their attention patterns, including normalization, positional encoding, output heads, and parameter counts; cross-family differences therefore cannot be attributed exclusively to the encoder-decoder distinction. In the decoder-only experiments, the same patch size is used for both inputs and outputs. Varying P therefore changes both the input granularity and the number of autoregressive decoding steps, and the observed trends may not hold when input and output patch sizes are selected independently...