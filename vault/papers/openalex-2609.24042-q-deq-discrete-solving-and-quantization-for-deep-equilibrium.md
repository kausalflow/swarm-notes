---
# CSL-compatible fields
title: "Q-DEQ: Discrete Solving and Quantization for Deep Equilibrium Models in Time Series Forecasting under Edge Deployment Coding Constraints"
author:
  - literal: "Ruotong Yang"
  - literal: "Hongdong Zhu"
  - literal: "Qi Gao"
  - literal: "Yin Ma"
  - literal: "Hai Wei"
  - literal: "Kai Wen"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24042"

# Custom fields
paper_id: "2609.24042"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "quantization"
  - "model-compression"
  - "optimization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "q-deq"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:38:02Z"
created_at: "2026-09-24T09:38:02Z"
---

# Q-DEQ: Discrete Solving and Quantization for Deep Equilibrium Models in Time Series Forecasting under Edge Deployment Coding Constraints

**Authors**: Ruotong Yang, Hongdong Zhu, Qi Gao, Yin Ma, Hai Wei, Kai Wen
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24042](https://arxiv.org/abs/2609.24042)

## Summary

The paper introduces Q-DEQ, a framework for deep equilibrium models in time series forecasting tailored for edge deployment by formulating fixed-point updates as discrete optimization problems. Instead of continuous Anderson solvers, Q-DEQ constructs local quadratic residual models and binary-encodes direction coefficients into quadratic unconstrained binary optimization (QUBO) problems solved via simulated annealing or a coherent Ising machine (CIM). Combined with W8A8 quantization, Q-DEQ significantly reduces static weight storage and parameter counts while matching explicit baseline forecasting accuracy.

## Key Contributions

- Proposes Q-DEQ, which formulates local updates in deep equilibrium model (DEQ) forward solving as discrete quadratic unconstrained binary optimization (QUBO) problems.
- Enables solving local DEQ updates using simulated annealing or a coherent Ising machine (CIM) physical backend with binary encoding of direction coefficients.
- Combines DEQ parameter sharing with W8A8 quantization, achieving static weight storage reductions of 4.3x to 12.8x across five multivariate time series benchmarks.
- Maintains competitive forecasting accuracy with relative MSE differences ranging from -1.16% to +2.90% compared to explicit multi-layer baselines.

## Limitations

None explicitly highlighted in the abstract beyond evaluating on specific hardware/simulated backends for QUBO solving.

## Open Questions & Future Work

- [[edge-hardware-validation-and-latency-profiling]]

## Key Concepts

- [[q-deq]]: A deep equilibrium model variant that formulates local forward-solving updates as quadratic unconstrained binary optimization (QUBO) solved via simulated annealing or coherent Ising machines.

## Archivist Review

Approved the central Q-DEQ concept and edge hardware validation open question while keeping selections strictly scarce. Rejected the second open question as it relates heavily to paper-local evaluations and empirical tracking on specific horizons.

### Approved Concepts
- Q-DEQ: It introduces discrete optimization via QUBO and coherent Ising machines for solving deep equilibrium model fixed-point updates.

### Approved Open Questions
- Edge Hardware Validation and Profiling: Essential for translating theoretical edge-deployment storage savings into concrete hardware performance metrics and energy efficiencies.

### Rejected Candidates
- [open_question] Systematic Solver-Level Evaluation and Convergence (`systematic-solver-level-evaluation-and-convergence`) - paper_local: paper_local

## Links

- [Abstract](https://arxiv.org/abs/2609.24042)
- [PDF](https://arxiv.org/pdf/2609.24042)

