---
# CSL-compatible fields
title: "Pre-localization of Massive Black Hole Binaries in the Millihertz Band"
author:
  - literal: "Xue-Ting Zhang"
  - literal: "Jonathan Gair"
  - literal: "Chris Messenger"
  - literal: "Natalia Korsakova"
  - literal: "Yi-Ming Hu"
  - literal: "Hong-Yu Chen"
issued:
  date-parts:
    - [2026, 4, 27]
url: "https://arxiv.org/abs/2604.24330"

# Custom fields
paper_id: "2604.24330"
paper_source: "openalex"
domain: "nlp,physics"
tags:
  - "multimodal"
  - "embedding"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "amortized-neural-bayesian-inference"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-30T07:25:24Z"
created_at: "2026-04-30T07:25:24Z"
---

# Pre-localization of Massive Black Hole Binaries in the Millihertz Band

**Authors**: Xue-Ting Zhang, Jonathan Gair, Chris Messenger, Natalia Korsakova, Yi-Ming Hu, Hong-Yu Chen
**Date**: 2026-04-27
**Paper ID**: [openalex:2604.24330](https://arxiv.org/abs/2604.24330)

## Summary

This paper presents a fast, normalizing flow-based Bayesian inference pipeline for the early-warning analysis of massive black hole binaries (MBHBs) in space-borne gravitational-wave detector configurations like TianQin. By combining learned time-series embeddings with a neural spline flow, the pipeline achieves amortized parameter estimation and sky localization in approximately one minute. Results demonstrate that the method provides performance comparable to traditional parallel-tempered MCMC while enabling pre-merger trigger windows suitable for electromagnetic follow-up.

## Key Contributions

- Developed a normalizing flow-based pipeline for real-time MBHB signal parameter estimation.
- Achieved ~20 deg^2 sky localization accuracy for pre-merger MBHBs in ~1 minute.
- Validated performance parity with traditional parallel-tempered Markov chain Monte Carlo (PTMCMC) methods.

## Open Questions & Future Work

- [[balancing-amortized-inference-and-sampling-accuracy]]

## Key Concepts

- [[amortized-neural-bayesian-inference]]: A signal processing approach that replaces iterative Bayesian sampling with a pre-trained neural network flow for low-latency parameter estimation.

## Archivist Review

I approved the overarching mechanism of 'Amortized Neural Bayesian Inference' as it reflects the shift from iterative to amortized modeling, which is highly reusable. I also approved a broader open question regarding the trade-off between amortization speed and sampling accuracy, as this is a fundamental bottleneck in real-time scientific signal processing. Other candidates were rejected either as application-specific instances or for being duplicative of broader research directions.

### Approved Concepts
- Amortized Neural Bayesian Inference: The paper demonstrates a shift from traditional iterative MCMC sampling to amortized flow-based inference for real-time signal analysis.

### Approved Open Questions
- Balancing Amortization and Sampling Accuracy: Bridging the gap between speed and exactness is critical for high-stakes, low-latency scientific discovery where parameter errors have direct consequences for follow-up observation strategies.

### Rejected Candidates
- [concept] Neural Spline Flow Inference Pipeline (`neural-spline-flow-inference-pipeline`) - subcomponent_of_broader_mechanism: The concept is essentially an application-specific instance of amortized inference; the proposed term 'Amortized Neural Bayesian Inference' captures the reusable methodological core.
- [open_question] Improving NSF Posterior Precision (`improving-nsf-posterior-precision`) - duplicate_existing: The question is overly specific to the model type; 'Balancing Amortization and Sampling Accuracy' is a broader, more canonical research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2604.24330)
- [PDF](https://arxiv.org/pdf/2604.24330)

