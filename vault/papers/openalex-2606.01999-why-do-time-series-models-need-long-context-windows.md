---
# CSL-compatible fields
title: "Why Do Time Series Models Need Long Context Windows?"
author:
  - literal: "Luca Butera"
  - literal: "Giovanni De Felice"
  - literal: "Andrea Cini"
  - literal: "Cesare Alippi"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.01999"

# Custom fields
paper_id: "2606.01999"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "generative-process-identification-gpi"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:42:53Z"
created_at: "2026-06-04T08:42:53Z"
---

# Why Do Time Series Models Need Long Context Windows?

**Authors**: Luca Butera, Giovanni De Felice, Andrea Cini, Cesare Alippi
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.01999](https://arxiv.org/abs/2606.01999)

## Summary

This paper provides a theoretical explanation for the performance gains observed in deep learning models using long time-series context windows. The authors argue that these windows serve to reduce uncertainty regarding the underlying data-generating process, formally decomposing the task into Generative Process Identification (GPI) and Conditional Forecasting (CF). Through analytical proofs and empirical validation, they demonstrate that capturing the memory length of the process is insufficient, as extra history is required to reach the minimum possible error. Furthermore, they introduce a strategy to decouple GPI and CF, offering a path toward more scalable and accurate forecasting architectures.

## Key Contributions

- Identifies that time-series forecasting fundamentally decomposes into Generative Process Identification (GPI) and Conditional Forecasting (CF).
- Proves theoretically that optimal forecasting requires an input window strictly larger than the underlying process memory length P to minimize predictive error.
- Proposes a decoupling of GPI and CF to achieve increased computational efficiency while maintaining forecasting accuracy.

## Open Questions & Future Work

- [[decoupling-gpi-cf-bottleneck]]

## Key Concepts

- [[generative-process-identification-gpi]]: The task of inferring the underlying stochastic process that generated a given input sequence of time series data as a prerequisite for conditional forecasting.

## Archivist Review

The paper provides a compelling theoretical framework for why long context windows are beneficial in time-series forecasting, moving beyond simple 'long-range dependency' claims to a rigorous distinction between latent model identification and predictive inference. I approved the Generative Process Identification concept and the associated decoupling open question as they represent foundational structural insights for time-series modeling. No datasets were approved as none met the strict criteria for standalone, reusable research artifacts.

### Approved Concepts
- Generative Process Identification (GPI): It establishes a theoretical foundation for the necessity of long context windows in time-series forecasting by framing them as an uncertainty-reduction mechanism regarding the data-generating process.

### Approved Open Questions
- Decoupling GPI and CF: This is a core architectural bottleneck for scaling time series foundation models, as decoupling could alleviate the need for uniformly long contexts and reduce computational overhead.

## Links

- [Abstract](https://arxiv.org/abs/2606.01999)
- [PDF](https://arxiv.org/pdf/2606.01999)

