---
title: "Stochastic Attention"
slug: "stochastic-attention"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2604.19530-calibrating-scientific-foundation-models-with-inference-time]]"
processed_at: "2026-04-24T07:00:14Z"
created_at: "2026-04-24T07:00:14Z"
---

# Stochastic Attention

> *Auto-generated stub. Edit this file to add more details.*

An inference-time modification for transformer architectures that replaces deterministic softmax attention weights with normalized multinomial samples to generate calibrated uncertainty ensembles.


## Why It Matters

Provides a method for post-hoc uncertainty quantification in frozen transformer models without requiring expensive model retraining.

## Evidence

> We propose Stochastic Attention, a lightweight inference-time modification that randomizes attention by replacing softmax weights with normalized multinomial samples controlled by a single concentration parameter

## Related Papers

- [[openalex-2604.19530-calibrating-scientific-foundation-models-with-inference-time]]
