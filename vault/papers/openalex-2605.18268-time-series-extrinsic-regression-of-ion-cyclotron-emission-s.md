---
# CSL-compatible fields
title: "Time Series Extrinsic Regression of Ion Cyclotron Emission Spectra Trained on Particle-In-Cell Simulations"
author:
  - literal: "Ethan Attwood"
  - literal: "J.W.S. Cook"
  - literal: "Peter Hill"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.18268"

# Custom fields
paper_id: "2605.18268"
paper_source: "openalex"
domain: "physics"
tags:
  - "time-series"
  - "regression"
  - "simulation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "time-series-extrinsic-regression"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:32:32Z"
created_at: "2026-05-21T08:32:32Z"
---

# Time Series Extrinsic Regression of Ion Cyclotron Emission Spectra Trained on Particle-In-Cell Simulations

**Authors**: Ethan Attwood, J.W.S. Cook, Peter Hill
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.18268](https://arxiv.org/abs/2605.18268)

## Summary

This paper addresses the inverse problem of inferring magnetised plasma parameters from Ion Cyclotron Emission (ICE) spectra. By training Time-Series Extrinsic Regression (TSER) models on synthetic spectra generated from 1D3V particle-in-cell simulations of the magnetoacoustic cyclotron instability, the authors enable rapid diagnostic parameter recovery. The approach is validated on experimental spectra from the JET fusion device, demonstrating high accuracy and near real-time inference capability for reactor-relevant plasma parameters.

## Key Contributions

- Develops a TSER-based framework to solve the inverse problem of mapping plasma parameters from Ion Cyclotron Emission (ICE) spectra.
- Demonstrates that bulk and fast ion parameters can be accurately recovered from JET ICE spectra using models trained on synthetic data from 1D3V particle-in-cell simulations.
- Achieves near real-time diagnostic capability for plasma parameter recovery, facilitating practical application in fusion power plants.

## Open Questions & Future Work

- [[enhancing-ice-simulation-realism]]

## Key Concepts

- [[time-series-extrinsic-regression]]: A machine learning framework for predicting continuous extrinsic variables from time-series data.

## Archivist Review

The paper is a straightforward application of Time Series Extrinsic Regression (TSER) to a physical inverse problem. I have approved TSER as a central concept and an open question focused on the limitation of 1D kinetic simulations in capturing real-world fusion device complexity, which is a known challenge for synthetic-to-real workflows in plasma physics.

### Approved Concepts
- Time Series Extrinsic Regression (TSER): The paper frames the inverse problem of mapping plasma parameters from ICE spectra as a TSER task, which is central to the methodological approach.

### Approved Open Questions
- Improving ICE simulation realism: This is critical for improving the generalizability of machine learning models trained on synthetic data to the complex, non-ideal conditions found in real-world magnetic fusion devices.

### Rejected Candidates
- [open_question] Improving ICE simulation realism (`enhancing-ice-simulation-realism-rejected-duplicate-reasoning`) - other: The candidate was approved as it identifies a critical bottleneck in bridging synthetic-to-real physics modeling.

## Links

- [Abstract](https://arxiv.org/abs/2605.18268)
- [PDF](https://arxiv.org/pdf/2605.18268)

