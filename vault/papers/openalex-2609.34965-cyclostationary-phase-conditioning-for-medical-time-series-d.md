---
# CSL-compatible fields
title: "Cyclostationary Phase Conditioning for Medical Time Series Diffusion"
author:
  - literal: "Samuel Ruiperez-Campillo"
  - literal: "Michele Copetti"
  - literal: "Jorge da Silva Goncalves"
  - literal: "Sonia Laguna"
  - literal: "Julia Elisabeth Vogt"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34965"

# Custom fields
paper_id: "2609.34965"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "diffusion-model"
  - "restoration"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:49:33Z"
created_at: "2026-09-30T10:49:33Z"
---

# Cyclostationary Phase Conditioning for Medical Time Series Diffusion

**Authors**: Samuel Ruiperez-Campillo, Michele Copetti, Jorge da Silva Goncalves, Sonia Laguna, Julia Elisabeth Vogt
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34965](https://arxiv.org/abs/2609.34965)

## Summary

Physiological time series such as cardiac and brain recordings exhibit cyclostationarity, which is often obscured by noise and artifacts, making signal restoration crucial. Existing diffusion methods condition only on corrupted observations and learn cyclic structure implicitly, whereas this paper proposes two inductive biases: a shift-covariant wavelet representation and dense per-sample phase conditioning. Additionally, the authors introduce a training-free cyclostationarity index to predict the utility of phase conditioning and an antithetic coupling technique to reduce sampling variance and evaluation steps.

## Key Contributions

- Proposes two inductive biases encoding cyclostationarity for physiological time-series diffusion: a shift-covariant wavelet representation and dense per-sample phase conditioning.
- Introduces a training-free cyclostationarity index that quantifies phase structure and predicts when phase conditioning will improve restoration.
- Proposes antithetic coupling of reverse trajectories to reduce sampling variance and achieve comparable performance with fivefold fewer network evaluations.

## Archivist Review

The proposed open question is a straightforward modality extension (single-channel to multi-channel physiological recordings) and lacks the deep theoretical novelty required for vault admission. No other concepts or datasets were provided or warranted approval under the strict scarcity policy.

### Rejected Candidates
- [open_question] Multi-channel Cyclostationary Diffusion Extension (`multi-channel-cyclostationary-diffusion`) - low_impact: Routine extension of a single-channel physiological diffusion framework to multi-channel arrays, representing incremental future work rather than an architectural bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.34965)
- [PDF](https://arxiv.org/pdf/2609.34965)

