---
# CSL-compatible fields
title: "Benchmarking Counterfactual Prediction in Epidemic Time Series with Time-Varying Interventions"
author:
  - literal: "Wenhao Mu"
  - literal: "Facundo Yan"
  - literal: "Anik Mumssen"
  - literal: "Marisa Eisenberg"
  - literal: "Alexander Rodríguez"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.05692"

# Custom fields
paper_id: "2606.05692"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "causal-inference"
  - "benchmark"
  - "epidemiology"
architectures:
  []
datasets:
  - "U.S. County Epidemic Dataset"
concept_slugs:
  - "counterfactual-prediction-benchmark-for-epidemic-time-series"
dataset_slugs:
  - "us-county-epidemic-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:18:37Z"
created_at: "2026-06-07T08:18:37Z"
---

# Benchmarking Counterfactual Prediction in Epidemic Time Series with Time-Varying Interventions

**Authors**: Wenhao Mu, Facundo Yan, Anik Mumssen, Marisa Eisenberg, Alexander Rodríguez
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.05692](https://arxiv.org/abs/2606.05692)

## Summary

This paper addresses the lack of realistic benchmarks for time-series causal inference by introducing a large-scale dataset for counterfactual prediction in epidemic modeling. The benchmark leverages a calibrated agent-based model grounded in real-world demographic, mobility, and policy data to generate ground-truth counterfactuals for static and time-varying interventions across 150+ U.S. counties. Evaluation of current causal inference methods on this benchmark reveals significant performance gaps, underscoring the difficulty of causal reasoning under complex dynamic interventions.

## Key Contributions

- Introduces a large-scale counterfactual prediction benchmark for epidemic time series, supporting both static and time-varying interventions.
- Utilizes a calibrated agent-based model to provide ground-truth counterfactual trajectories for over 150 U.S. counties.
- Evaluates state-of-the-art causal inference models, demonstrating significant performance variability and highlighting gaps in current causal reasoning capabilities.

## Open Questions & Future Work

- [[scalable-differentiable-abm-efficiency]]

## Key Concepts

- [[counterfactual-prediction-benchmark-for-epidemic-time-series]]: A large-scale benchmark for evaluating causal inference methods in epidemic time series using a calibrated agent-based model to provide ground-truth counterfactuals for static and time-varying interventions.

## Archivist Review

I have approved the proposed counterfactual prediction benchmark as a concept and the specific U.S. County Epidemic Dataset, as they represent a substantial contribution to causal inference evaluation in epidemiology. I also approved the open question regarding ABM scalability, as it identifies a clear, research-level bottleneck limiting the realism and geographic breadth of epidemic modeling. These approvals adhere to the scarcity mandate, providing essential resources while avoiding generic or duplicate entries.

### Approved Concepts
- Counterfactual Prediction Benchmark for Epidemic Time Series: Addresses the critical scarcity of benchmarks with ground-truth counterfactuals for time-series causal inference in epidemiology.

### Approved Open Questions
- Scalable Differentiable ABM Efficiency: Computational constraints in ABMs limit the population size and resolution of epidemic simulations, which is a major hurdle for scaling counterfactual benchmarks.

## Datasets

- [[us-county-epidemic-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2606.05692)
- [PDF](https://arxiv.org/pdf/2606.05692)

