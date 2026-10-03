---
# CSL-compatible fields
title: "The Nixtlaverse: An Open-Source Ecosystem for Forecasting"
author:
  - literal: "Olivier Sprangers"
  - literal: "Max Mergenthaler Canseco"
  - literal: "Marco Peixeiro"
  - literal: "Saul Caballero Ramirez"
  - literal: "Mariana Menchero García"
  - literal: "Jing-Qiang Goh"
  - literal: "Han Wang"
  - literal: "Nïkhil Gupta"
  - literal: "Rogelio Melo"
  - literal: "Senbong Gee"
  - literal: "Cristian Challú"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.39741"

# Custom fields
paper_id: "2609.39741"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
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
processed_at: "2026-10-03T10:08:11Z"
created_at: "2026-10-03T10:08:11Z"
---

# The Nixtlaverse: An Open-Source Ecosystem for Forecasting

**Authors**: Olivier Sprangers, Max Mergenthaler Canseco, Marco Peixeiro, Saul Caballero Ramirez, Mariana Menchero García, Jing-Qiang Goh, Han Wang, Nïkhil Gupta, Rogelio Melo, Senbong Gee, Cristian Challú
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.39741](https://arxiv.org/abs/2609.39741)

## Summary

The Nixtlaverse is an open-source ecosystem of Python libraries designed to unify time series forecasting across statistical, machine-learning, and neural model families via shared long-format panel data and keyed forecast contracts. By evaluating these models on public M5 competition data, the authors benchmark runtime and memory scaling bottlenecks for each model family and demonstrate sparse forecast reconciliation across large hierarchies. This ecosystem bridges disparate forecasting methodologies into a cohesive framework with reproducible benchmarks.

## Key Contributions

- Introduces the Nixtlaverse, an open-source ecosystem of Python libraries for time series forecasting sharing uniform long-format panel data and keyed forecast contracts.
- Demonstrates unified evaluation of statistical, machine-learning, neural models, and external engines via rolling-origin evaluation on the M5 dataset.
- Profiles runtime and peak memory scaling across panel sizes from 100 to 30,490 series, identifying bottlenecks per model family.
- Performs sparse forecast reconciliation across all 42,840 series of the M5 hierarchy where dense implementations failed.

## Archivist Review

Adhering to our stringent selectivity criteria, we approved no concepts, open questions, or datasets from this software ecosystem overview paper. The paper describes an open-source Python library ecosystem (the Nixtlaverse) and its design principles for shared data and output contracts, which constitutes a software engineering case study rather than a novel ML methodology concept or a core scientific research bottleneck.

### Rejected Candidates
- [open_question] Streamlining Ecosystem Coordination Overhead (`streamlining-ecosystem-coordination-overhead`) - low_impact: Reflects a software maintenance and repository management task rather than a foundational research or algorithmic bottleneck in forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2609.39741)
- [PDF](https://arxiv.org/pdf/2609.39741)

