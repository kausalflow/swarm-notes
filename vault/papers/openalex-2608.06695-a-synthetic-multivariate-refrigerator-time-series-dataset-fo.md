---
# CSL-compatible fields
title: "A synthetic multivariate refrigerator time-series dataset for predictive maintenance"
author:
  - literal: "Islam Benamirouche"
  - literal: "Djemel Ziou"
  - literal: "Feriel Fass"
issued:
  date-parts:
    - [2026, 8, 24]
url: "https://arxiv.org/abs/2608.06695"

# Custom fields
paper_id: "2608.06695"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-26T05:22:33Z"
created_at: "2026-08-26T05:22:33Z"
---

# A synthetic multivariate refrigerator time-series dataset for predictive maintenance

**Authors**: Islam Benamirouche, Djemel Ziou, Feriel Fass
**Date**: 2026-08-24
**Paper ID**: [openalex:2608.06695](https://arxiv.org/abs/2608.06695)

## Summary

This paper introduces a synthetic multivariate time-series dataset and a physics-inspired simulator for predictive maintenance in 27 refrigerators. Operating at a one-minute resolution, each refrigerator simulates complex phenomena such as ambient temperature variations, door-use patterns, electrical characteristics, and six types of progressive degradation with explicit failure logs. The associated Python generator allows users to customize operating conditions and degradation schedules for tasks like anomaly detection and remaining useful life estimation.

## Key Contributions

- Released a synthetic multivariate time-series dataset of 27 refrigerators generated via a physics-inspired simulator at one-minute resolution.
- Incorporated six types of progressive degradation, ambient variations, door-use patterns, and thermostat/compressor dynamics across 15 to 20 sensor outputs per unit.
- Provided accompanying Python data generator and configuration files to support heterogeneous equipment learning and downstream predictive maintenance tasks.

## Limitations

The dataset is entirely synthetic, relying on a simplified physics-inspired simulator rather than empirical recordings from physical machinery.

## Archivist Review

The paper introduces a synthetic dataset and simulator for predictive maintenance rather than proposing a new modeling concept or theoretical mechanism. Per the review policy, generic future validation tasks do not qualify as standalone open questions, so no items are approved.

### Rejected Candidates
- [open_question] Real-World Validation in Predictive Maintenance (`real-world-validation-predictive-maintenance`) - low_impact: Generic future work on validating simulated models on real-world data without specific theoretical or methodological depth.

## Links

- [Abstract](https://arxiv.org/abs/2608.06695)
- [PDF](https://arxiv.org/pdf/2608.06695)

