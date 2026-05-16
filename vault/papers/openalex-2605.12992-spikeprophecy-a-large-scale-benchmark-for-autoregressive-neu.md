---
# CSL-compatible fields
title: "SpikeProphecy: A Large-Scale Benchmark for Autoregressive Neural Population Forecasting"
author:
  - literal: "John R. Minnick"
  - literal: "Jinghui Geng"
  - literal: "Kamran Hussain"
  - literal: "Jesus Gonzalez-Ferrer"
  - literal: "Ash Robbins"
  - literal: "Mohammed A. Mostajo-Radji"
  - literal: "David Haussler"
  - literal: "Jason K. Eshraghian"
  - literal: "Mircea Teodorescu"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.12992"

# Custom fields
paper_id: "2605.12992"
paper_source: "openalex"
domain: "biology"
tags:
  - "benchmark"
  - "dataset"
  - "autoregressive"
  - "ssm"
  - "transformer"
  - "lstm"
  - "evaluation"
architectures:
  - "mamba"
  - "transformer"
  - "lstm"
datasets:
  []
concept_slugs:
  - "population-metric-decomposition-for-neural-spike-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:09:35Z"
created_at: "2026-05-16T07:09:35Z"
---

# SpikeProphecy: A Large-Scale Benchmark for Autoregressive Neural Population Forecasting

**Authors**: John R. Minnick, Jinghui Geng, Kamran Hussain, Jesus Gonzalez-Ferrer, Ash Robbins, Mohammed A. Mostajo-Radji, David Haussler, Jason K. Eshraghian, Mircea Teodorescu
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.12992](https://arxiv.org/abs/2605.12992)

## Summary

SpikeProphecy is a large-scale benchmark designed to advance causal, autoregressive forecasting of neural population spike counts. Moving beyond aggregate Pearson correlation, the paper introduces a population metric decomposition that separates performance into temporal, spatial, and alignment-based dimensions, revealing granular insights into model behavior. Evaluated across 105 Neuropixels sessions using various SSM, Transformer, LSTM, and spiking architectures, the framework highlights consistent brain-region predictability patterns and identifies biophysical evaluation floors. Additionally, the study provides a negative result regarding ANN-to-SNN transfer using KL-on-output-rates distillation in this domain.

## Key Contributions

- Introduces SpikeProphecy, the first large-scale benchmark for autoregressive causal neural population forecasting.
- Proposes a population metric decomposition that disentangles aggregate performance into temporal fidelity, spatial pattern accuracy, and magnitude-invariant alignment.
- Demonstrates through 105 Neuropixels sessions that the decomposition reveals consistent brain-region predictability rankings and biophysical evaluation floors independent of specific model architectures.

## Open Questions & Future Work

- [[neural-population-forecasting-evaluation-standardization]]

## Key Concepts

- [[population-metric-decomposition-for-neural-spike-forecasting]]: A multi-faceted evaluation framework that decomposes aggregate spike-count prediction performance into temporal, spatial, and alignment components.

## Archivist Review

I approved the metric decomposition concept as it introduces a novel evaluation framework for multi-channel signals, and the corresponding open question on standardization to address the reliance on flawed aggregate metrics. The distillation question was rejected as it addresses a specific method failure rather than a broad, persistent research bottleneck. No datasets were approved as the ones cited are standard, well-established public benchmarks in neuroscience.

### Approved Concepts
- Population metric decomposition for neural spike forecasting: It enables a granular analysis of multi-neuron dynamics that aggregate scalar metrics currently obscure, making it a critical methodology for evaluating complex signal-based forecasting models.

### Approved Open Questions
- Standardizing Neural Forecasting Evaluation: Current aggregate metrics mask critical structure in neural population data, leading to a potential misallocation of research efforts.

### Rejected Candidates
- [open_question] Distillation in Poisson Domains (`ann-to-snn-distillation-poison-domain`) - low_impact: While a negative result, this is a narrow research question about a specific training technique rather than a fundamental open problem in the field.

## Links

- [Abstract](https://arxiv.org/abs/2605.12992)
- [PDF](https://arxiv.org/pdf/2605.12992)

