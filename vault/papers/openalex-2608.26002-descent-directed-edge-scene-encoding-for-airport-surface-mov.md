---
# CSL-compatible fields
title: "DESCENT: Directed Edge Scene Encoding for Airport Surface Movement Prediction"
author:
  - literal: "Alexander Prutsch"
  - literal: "David Schinagl"
  - literal: "Horst Possegger"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.26002"

# Custom fields
paper_id: "2608.26002"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "transformer"
  - "attention-mechanism"
  - "forecasting"
  - "trajectory-prediction"
architectures:
  - "encoder-decoder"
datasets:
  - "amelia-10"
concept_slugs:
  []
dataset_slugs:
  - "amelia-10"
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T17:00:37Z"
created_at: "2026-08-28T17:00:37Z"
---

# DESCENT: Directed Edge Scene Encoding for Airport Surface Movement Prediction

**Authors**: Alexander Prutsch, David Schinagl, Horst Possegger
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.26002](https://arxiv.org/abs/2608.26002)

## Summary

Advanced automation for airport ground operations requires robust motion forecasting under strict topological constraints and heterogeneous dynamics. To address this, the authors propose DESCENT, a transformer-based architecture equipped with a Potential Reachable Set (PRS) context sampling mechanism and a detection transformer-based decoder. Evaluations on the Amelia-10 benchmark show that DESCENT outperforms state-of-the-art baselines, especially in safety-critical, long-horizon forecasting scenarios.

## Key Contributions

- Proposes DESCENT, a transformer-based architecture tailored for heterogeneous dynamics and strict topological constraints in airport surface movements.
- Introduces a Potential Reachable Set (PRS) context sampling mechanism to adaptively collect airfield environment context across operational phases.
- Demonstrates significant performance improvements over state-of-the-art baselines on the Amelia-10 benchmark, particularly in safety-critical long-horizon scenarios.

## Archivist Review

Rigorously applied vault selectivity rules. The proposed concept (Directed Edge Scene Encoding) is domain-specific to airport surface movement and lacks broad standalone reusability, while the open question is an application integration goal. Amelia-10 is approved as a specific named dataset central to the paper's evaluation claims.

### Rejected Candidates
- [concept] Directed Edge Scene Encoding (`directed-edge-scene-encoding`) - paper_local: Paper-internal architecture and encoding scheme tailored to airport surface movement, lacking general standalone reusability across broader forecasting tasks.
- [open_question] Integrated Automated Airfield Safety Systems (`integrated-automated-airfield-safety-systems`) - paper_local: A paper-local application integration direction rather than a fundamental technical research question or unresolved bottleneck in time series or forecasting methodology.

## Datasets

- [[amelia-10]]

## Links

- [Abstract](https://arxiv.org/abs/2608.26002)
- [PDF](https://arxiv.org/pdf/2608.26002)

