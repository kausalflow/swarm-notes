---
# CSL-compatible fields
title: "DAD4TS: Data-Augmentation-Oriented Diffusion Model for Time-Series Forecasting with Small-Scale Data"
author:
  - literal: "Masahiro Suzuki"
  - literal: "Bohui Xia"
  - literal: "Hiroto Yamamoto"
  - literal: "Masanori Miyahara"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.17866"

# Custom fields
paper_id: "2605.17866"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "reinforcement-learning"
  - "synthetic-data-augmentation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dad4ts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:26:58Z"
created_at: "2026-05-21T08:26:58Z"
---

# DAD4TS: Data-Augmentation-Oriented Diffusion Model for Time-Series Forecasting with Small-Scale Data

**Authors**: Masahiro Suzuki, Bohui Xia, Hiroto Yamamoto, Masanori Miyahara
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.17866](https://arxiv.org/abs/2605.17866)

## Summary

DAD4TS addresses the challenge of small-scale data in time-series forecasting by integrating a diffusion-based generator with reinforcement learning. The system simultaneously trains the generator and the forecasting model, using the latter's performance as a reward signal to synthesize samples that specifically target accuracy improvements. By leveraging geometric space projections rather than standard VAE-based approaches, the method achieves robust data augmentation even with limited observations.

## Key Contributions

- Introduced DAD4TS, a diffusion-based augmentation framework that employs reinforcement learning to guide sample generation toward maximizing forecasting accuracy.
- Replaced conventional VAE-based training with geometric space projections to enhance diffusion model stability in small-data regimes.
- Demonstrated consistent performance improvements across six real-world datasets and eight diverse baseline forecasting models.

## Key Concepts

- [[dad4ts]]: A framework for diffusion-based data augmentation in time-series forecasting where sample generation is guided by reinforcement learning to optimize downstream model accuracy.

## Archivist Review

I approved DAD4TS as a concept because it represents a distinct and reusable paradigm for integrating reinforcement learning with generative diffusion models to address small-sample forecasting challenges. I rejected other candidates as they were either redundant or covered by this primary concept. No datasets were approved because the paper did not propose novel benchmarks but rather tested on existing ones.

### Approved Concepts
- DAD4TS: It integrates a diffusion-based generator with reinforcement learning, where the forecasting model serves as an agent to guide the synthesis of high-utility training samples.

### Rejected Candidates
- [concept] Reinforcement Learning Controlled Diffusion Synthesis (`rl-controlled-diffusion-synthesis`) - duplicate_existing: This is synonymous with the core mechanism of DAD4TS, which is already being approved as a standalone concept.

## Links

- [Abstract](https://arxiv.org/abs/2605.17866)
- [PDF](https://arxiv.org/pdf/2605.17866)

