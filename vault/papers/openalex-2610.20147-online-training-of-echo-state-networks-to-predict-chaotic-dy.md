---
# CSL-compatible fields
title: "Online training of Echo State Networks to predict chaotic dynamical systems"
author:
  - literal: "A. Provata"
  - literal: "Markos Syroukis"
  - literal: "Johanne Hizanidis"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.20147"

# Custom fields
paper_id: "2610.20147"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "reservoir"
  - "dynamical-systems"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:56:27Z"
created_at: "2026-10-17T08:56:27Z"
---

# Online training of Echo State Networks to predict chaotic dynamical systems

**Authors**: A. Provata, Markos Syroukis, Johanne Hizanidis
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.20147](https://arxiv.org/abs/2610.20147)

## Summary

This paper investigates the influence of reservoir topology, specifically Erdos-Renyi random and Watts-Strogatz small-world networks, on the prediction performance of online-trained Echo State Networks (ESNs) applied to chaotic dynamical systems. Using the Lorenz, Rossler, and FitzHugh-Nagumo models, the authors show that optimal forecasting accuracy is achieved when reservoir link-density is near and immediately above the critical point of mean-field bond percolation. These findings provide guidelines for designing efficient real-time forecasting frameworks in dynamically evolving systems.

## Key Contributions

- Investigates the effects of reservoir topology (Erdos-Renyi random networks and Watts & Strogatz small-world networks) on online-trained Echo State Networks for chaotic dynamical systems forecasting.
- Demonstrates that optimal prediction performance is achieved for sparse reservoirs with link-densities near and immediately above the critical point of mean-field bond percolation.
- Evaluates prediction performance on the Lorenz and Rossler chaotic models and the FitzHugh-Nagumo limit cycle model.

## Archivist Review

In accordance with the review policy, I have kept the vault strictly selective and rejected the generic open question regarding alternative activation functions and ridge regression as incremental future work. No concepts or datasets met the threshold for standalone vault entry.

### Rejected Candidates
- [open_question] Alternative Activation Functions and Offline ESN Training (`alternative-architectures-and-activation-functions-for-esns`) - low_impact: The question proposes standard variations such as activation functions and offline ridge regression without identifying a specific profound bottleneck or theoretical limitation.

## Links

- [Abstract](https://arxiv.org/abs/2610.20147)
- [PDF](https://arxiv.org/pdf/2610.20147)

