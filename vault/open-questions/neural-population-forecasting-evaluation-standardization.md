---
created_at: '2026-05-16T07:09:35Z'
source_papers:
- '[[openalex-2605.12992-spikeprophecy-a-large-scale-benchmark-for-autoregressive-neu]]'
title: Standardizing Neural Forecasting Evaluation
---

**Background:** Neural population models, such as those predicting future spike counts, are typically evaluated using aggregate scalar metrics like Pearson correlation, which can obscure distinct performance characteristics across different brain regions and neuron types.

**Question / Future Work:** The community lacks a consensus on how to properly decompose and report population-level forecasting performance to expose specific model failure modes, such as the distinction between temporal dynamics tracking and spatial pattern fidelity. Establishing standardized, multi-axis evaluation protocols is necessary to guide future architectural developments for neural data.

**Why It Matters:** Current aggregate metrics mask critical structure in neural population data, leading to a potential misallocation of research efforts.

**Evidence:** We argue that how we evaluate spike forecasting matters as much as what we build, and introduce SpikeProphecy, the first large-scale benchmark for causal, autoregressive spike-count forecasting on real electrophysiology recordings.