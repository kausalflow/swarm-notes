---
# CSL-compatible fields
title: "Routing Channel-Patch Dependencies in Time Series Forecasting with Graph Spectral Decomposition"
author:
  - literal: "Dongyuan Li"
  - literal: "Shun Zheng"
  - literal: "Chang Xu"
  - literal: "Jiang Bian"
  - literal: "Renhe Jiang"
issued:
  date-parts:
    - [2026, 3, 14]
url: "https://arxiv.org/abs/2603.13702"

# Custom fields
paper_id: "2603.13702"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "graph-neural-network"
  - "forecasting"
  - "multihead-attention"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:09:41Z"
created_at: "2026-03-27T14:09:41Z"
---

# Routing Channel-Patch Dependencies in Time Series Forecasting with Graph Spectral Decomposition

**Authors**: Dongyuan Li, Shun Zheng, Chang Xu, Jiang Bian, Renhe Jiang
**Date**: 2026-03-14
**Paper ID**: [openalex:2603.13702](https://arxiv.org/abs/2603.13702)

## Summary

This paper introduces xCPD, a plug-and-play module designed to dynamically resolve the trade-off between Channel-Independent (CI) and Channel-Dependent (CD) modeling in time series forecasting. xCPD employs graph spectral decomposition to transform the input into the frequency domain, where signal patches are categorized into low, mid, and high-frequency bands based on spectral energy. A subsequent channel-adaptive routing mechanism then selectively engages experts tailored to these frequency bands, allowing for input-aware control over inter-channel interactions. This approach enables the model to capture smooth trends (low-frequency), local fluctuations (mid-frequency), and abrupt changes (high-frequency) effectively. The module consistently enhances the performance of underlying forecasting models across diverse benchmarks.

## Key Contributions

- Proposes xCPD, a generic plugin that adaptively models channel-patch dependencies using graph spectral decomposition to balance CI and CD modeling strategies.
- Projects multivariate signals into the frequency domain using a shared graph Fourier basis and groups patches into low-, mid-, and high-frequency bands based on spectral energy.
- Introduces a channel-adaptive routing mechanism that dynamically adjusts inter-channel interaction for each patch by activating frequency-specific experts, enabling fine-grained modeling of trends, fluctuations, and transitions.
- Demonstrates that xCPD can be seamlessly integrated with existing CI/CD forecasting models, consistently improving accuracy and generalization across various benchmarks.

## Limitations

The description focuses heavily on the mechanism and mentions consistent enhancement across benchmarks, but specific quantitative results or comparisons against state-of-the-art baselines (statistical or deep learning) are not detailed in the abstract.

## Open Questions & Future Work

- [[incorporating-external-domain-knowledge-in-spectral-grouping]]
- [[adaptive-interpretable-graph-filtering-strategies]]
- [[expanding-plugin-applicability-structured-prediction]]
- [[integrating-spectral-modeling-foundation-models]]

## Key Concepts

- [Channel-Patch Dependencies Routing](../concepts/channel-patch-dependency-routing.md): A mechanism that adaptively balances Channel-Independent (CI) and Channel-Dependent (CD) modeling by leveraging graph spectral decomposition to route information based on patch frequency bands.

## Limitations

The description focuses heavily on the mechanism and mentions consistent enhancement across benchmarks, but specific quantitative results or comparisons against state-of-the-art baselines (statistical or deep learning) are not detailed in the abstract.

## Links

- [Abstract](https://arxiv.org/abs/2603.13702)
- [PDF](https://arxiv.org/pdf/2603.13702)

