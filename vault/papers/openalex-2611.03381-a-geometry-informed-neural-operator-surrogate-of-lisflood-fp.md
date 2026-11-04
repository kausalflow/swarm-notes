---
# CSL-compatible fields
title: "A Geometry-Informed Neural Operator surrogate of LISFLOOD-FP for rapid pluvial-fluvial flood forecasting: the case of Forlì, Italy"
author:
  - literal: "Samuele Maria Garofalo"
  - literal: "Fabio Limardo"
  - literal: "Simonetta Bodojra"
  - literal: "Mohammad Amin Nabian"
  - literal: "Mehdi Taghizadeh"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.03381"

# Custom fields
paper_id: "2611.03381"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-04T12:41:01Z"
created_at: "2026-11-04T12:41:01Z"
---

# A Geometry-Informed Neural Operator surrogate of LISFLOOD-FP for rapid pluvial-fluvial flood forecasting: the case of Forlì, Italy

**Authors**: Samuele Maria Garofalo, Fabio Limardo, Simonetta Bodojra, Mohammad Amin Nabian, Mehdi Taghizadeh
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.03381](https://arxiv.org/abs/2611.03381)

## Summary

Physically based two-dimensional hydraulic models are too slow for real-time inundation forecasting, so the authors propose a time-dependent geometry-informed neural operator (GINO) surrogate of LISFLOOD-FP for the municipality of Forlì, Italy. Trained on 216 simulations derived from public gauge observations using an autoregressive GINO architecture, the surrogate predicts volume-conserving polygon-mean depths on a Voronoi mesh. Tested on 38 unseen independent events, it achieves high accuracy (CSI of 0.934 at 0.05m, R^2 of 0.984 for maximum-depth maps) while drastically reducing computation time to 1.7 seconds per 72-hour forecast and 6.2 seconds for a 50-member ensemble.

## Key Contributions

- Developed a geometry-informed neural operator (GINO) surrogate of the LISFLOOD-FP hydraulic model for rapid pluvial-fluvial flood forecasting in Forlì, Italy.
- Achieved a critical success index (CSI) of 0.934 at 0.05m and 0.844 at 0.3m, alongside a depth RMSE of 0.008m and an R^2 of 0.984 on 38 independent observed events.
- Accelerated 72-hour forecasts from 55 seconds (LISFLOOD-FP) to 1.7 seconds, and reduced 50-member ensemble computation time from 46 minutes to 6.2 seconds on a single NVIDIA A10G GPU.

## Open Questions & Future Work

- [[multi-domain-neural-operator-flood-forecasting-and-operational-coupling]]

## Archivist Review

Strict review applied: rejected the domain-specific geometry-informed neural operator surrogate as a paper-local application of existing neural operators, but approved the open question regarding multi-domain generalization and operational coupling for neural operator flood models.

### Approved Open Questions
- Multi-Domain Neural Operator Flood Forecasting: Scaling neural operator surrogates across multiple geographic domains and coupling them directly with operational meteorological forecasts are critical steps for deploying reliable, region-wide early warning systems.

### Rejected Candidates
- [concept] Geometry-Informed Neural Operator (GINO) Surrogate (`geometry-informed-neural-operator-ginos-surrogate`) - not_novel: Neural operators and their application to physics simulation surrogates are already standard frameworks in the literature, making a paper-specific application instance insufficiently novel as a standalone vault note.

## Links

- [Abstract](https://arxiv.org/abs/2611.03381)
- [PDF](https://arxiv.org/pdf/2611.03381)

