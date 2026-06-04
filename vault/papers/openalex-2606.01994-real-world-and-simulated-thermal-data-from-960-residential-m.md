---
# CSL-compatible fields
title: "Real-world and simulated thermal data from 960 residential multi-zone buildings in Central Europe"
author:
  - literal: "Fabian Raisch"
  - literal: "Matthias Kersken"
  - literal: "Markus Male"
  - literal: "Benjamin Tischler"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.01994"

# Custom fields
paper_id: "2606.01994"
paper_source: "openalex"
domain: "time-series"
tags:
  - "dataset"
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  - "thermbuild"
concept_slugs:
  []
dataset_slugs:
  - "thermbuild"
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:43:38Z"
created_at: "2026-06-04T08:43:38Z"
---

# Real-world and simulated thermal data from 960 residential multi-zone buildings in Central Europe

**Authors**: Fabian Raisch, Matthias Kersken, Markus Male, Benjamin Tischler
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.01994](https://arxiv.org/abs/2606.01994)

## Summary

This paper introduces the ThermBuild dataset, a large-scale repository comprising both real-world measurements and high-fidelity TRNSYS simulations of thermal dynamics in residential buildings. Covering 960 diverse building configurations across five European climates, the dataset provides 15-minute interval data for heat pump operations, heating distribution, and zone-level indoor variables. It is explicitly designed to advance research in building energy control, fault detection, and cross-domain thermal modeling.

## Key Contributions

- Introduces the ThermBuild dataset, a comprehensive collection of thermal operational data for 960 multi-zone residential buildings.
- Provides high-resolution (15-minute) multi-year time series covering heat pump systems, hot water distribution, weather, and indoor climate variables.
- Enables benchmarking and development of data-driven thermal dynamics models, fault detection systems, and simulation-to-reality transfer techniques.

## Open Questions & Future Work

- [[simulation-to-reality-transfer-in-buildings]]

## Archivist Review

The paper introduces a significant new dataset for residential thermal dynamics, which is approved for the vault due to its scale and the inclusion of both real-world and simulated components. The proposed open question regarding simulation-to-reality transfer is a critical, well-defined research challenge in building energy systems, warranting permanent tracking. No new concepts were approved as the paper describes a data collection effort rather than a novel methodological paradigm.

### Approved Open Questions
- Bridging Simulation-to-Reality Gap: This is a fundamental challenge for the practical deployment of data-driven control and fault detection algorithms in buildings, as training models purely on simulated data often fails to capture the complexity of real-world operational environments.

## Datasets

- [[thermbuild]]

## Links

- [Abstract](https://arxiv.org/abs/2606.01994)
- [PDF](https://arxiv.org/pdf/2606.01994)

