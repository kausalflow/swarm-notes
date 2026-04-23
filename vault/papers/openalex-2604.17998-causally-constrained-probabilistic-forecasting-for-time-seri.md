---
# CSL-compatible fields
title: "Causally-Constrained Probabilistic Forecasting for Time-Series Anomaly Detection"
author:
  - literal: "Pooyan Khosravinia"
  - literal: "João Gama"
  - literal: "Bruno Veloso"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.17998"

# Custom fields
paper_id: "2604.17998"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "anomaly-detection"
  - "graph-neural-network"
  - "forecasting"
  - "interpretability"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "causally-guided-transformer-cgt"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:55:10Z"
created_at: "2026-04-23T06:55:10Z"
---

# Causally-Constrained Probabilistic Forecasting for Time-Series Anomaly Detection

**Authors**: Pooyan Khosravinia, João Gama, Bruno Veloso
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.17998](https://arxiv.org/abs/2604.17998)

## Summary

This paper introduces a Causally Guided Transformer (CGT) for multivariate time-series anomaly detection, which constrains predictive modeling using explicit time-lagged causal graph priors. The architecture employs hard parent masking for causal pathways and a safety-gated shadow path to incorporate non-causal residual information without compromising causal reliability. The method identifies anomalies via adaptive negative log-likelihood thresholding and enables root-cause localization using counterfactual clamping, consistently outperforming existing methods on ASD and SMD benchmarks.

## Key Contributions

- Introduced the Causally Guided Transformer (CGT), which integrates an explicit time-lagged causal graph prior using hard parent masking.
- Implemented a shadow auxiliary path with safety-gated blending to capture residual correlations while maintaining causal integrity.
- Achieved SOTA performance on ASD (96.19% F1) and SMD (95.32% F1) benchmarks while providing superior root-cause localization through counterfactual clamping.

## Open Questions & Future Work

- [[joint-causal-structure-learning-anomaly-detection]]

## Key Concepts

- [[causally-guided-transformer-cgt]]: A Transformer-based architecture that uses hard parent masking based on causal discovery to constrain prediction pathways.

## Archivist Review

The paper introduces a structured approach to integrating causal discovery into time-series forecasting. I approved the CGT architecture as it represents a clear, reusable pattern for constrained attention modeling. I also approved an open question regarding the joint learning of causal structure and detection models, as it captures a critical bottleneck in the field of causal time-series analysis. Routine benchmarks and subcomponent mechanisms were rejected in accordance with the preservation policy.

### Approved Concepts
- Causally Guided Transformer (CGT): Integrates explicit time-lagged causal graph priors via hard parent masking into a sequence modeling architecture, providing a bridge between structural causal models and Transformer-based anomaly detection.

### Approved Open Questions
- Joint Causal Discovery and Detection: Addressing this bottleneck is critical for deploying causal anomaly detection in dynamic, real-world industrial environments where static causal priors quickly become obsolete or inaccurate.

### Rejected Candidates
- [concept] Shadow Auxiliary Path (`shadow-auxiliary-path`) - subcomponent_of_broader_mechanism: This is a paper-local subcomponent/mechanism for blending residuals rather than a broad, independent framework.
- [dataset] ASD Benchmark (`asd`) - low_impact: Standard evaluation benchmark; lacks sufficient description for a standalone note in this archive.
- [dataset] SMD Benchmark (`smd`) - low_impact: Standard evaluation benchmark; lacks sufficient description for a standalone note in this archive.

## Links

- [Abstract](https://arxiv.org/abs/2604.17998)
- [PDF](https://arxiv.org/pdf/2604.17998)

