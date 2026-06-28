---
# CSL-compatible fields
title: "End-to-end probabilistic hierarchical forecasting of large hierarchies via probabilistic top-down"
author:
  - literal: "Lorenzo Zambon"
  - literal: "Dario Azzimonti"
  - literal: "Giorgio Corani"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.26774"

# Custom fields
paper_id: "2606.26774"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  - "m5-competition"
  - "favorita-dataset"
concept_slugs:
  - "e2etd"
dataset_slugs:
  - "m5-competition"
  - "favorita-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:15:46Z"
created_at: "2026-06-28T08:15:46Z"
---

# End-to-end probabilistic hierarchical forecasting of large hierarchies via probabilistic top-down

**Authors**: Lorenzo Zambon, Dario Azzimonti, Giorgio Corani
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.26774](https://arxiv.org/abs/2606.26774)

## Summary

e2eTD is a scalable framework for hierarchical probabilistic forecasting that avoids the computational burden of end-to-end neural reconciliation by forecasting only a small subset of aggregate series. It utilizes a novel top-down sampling algorithm that treats historical disaggregation proportions as joint distributions to derive coherent bottom-level samples. Experiments on the M5 and Favorita datasets demonstrate that the method achieves superior probabilistic accuracy and extreme computational efficiency, processing hundreds of thousands of series on standard hardware in minutes.

## Key Contributions

- Introduces e2eTD, a computationally efficient framework for probabilistic coherent hierarchical forecasting that scales to hundreds of thousands of time series on standard hardware.
- Develops a probabilistic top-down sampling algorithm that models historical disaggregation proportions as joint distributions to ensure bottom-level coherence.
- Achieves state-of-the-art performance on the M5 and Favorita benchmarks while significantly reducing operational runtime compared to existing neural and reconciliation-based models.

## Open Questions & Future Work

- [[automated-subhierarchy-selection]]
- [[dynamic-disaggregation-proportions]]

## Key Concepts

- [[e2etd]]: A scalable probabilistic hierarchical forecasting framework that generates coherent bottom-level samples by propagating aggregate-level forecasts through top-down sampling based on joint historical proportions.

## Archivist Review

I have approved the e2eTD framework as a distinct and reusable architectural paradigm for hierarchical forecasting. I also approved two research bottlenecks regarding subhierarchy selection and dynamic proportion modeling, as these address fundamental scalability and adaptability challenges in hierarchical time series. M5 and Favorita datasets were approved as they are canonical, high-impact benchmarks central to the method's evaluation.

### Approved Concepts
- e2eTD: Provides a highly scalable, computationally efficient alternative to traditional two-step reconciliation for very large retail hierarchies by focusing on aggregate-level forecasting and top-down sampling.

### Approved Open Questions
- Automated subhierarchy selection criteria: This is a critical bottleneck for deploying hierarchical forecasting models at scale, as the choice of sub-hierarchy directly dictates both the computational cost and the upper bound of achievable accuracy.
- Modeling dynamic disaggregation proportions: The current assumption of near-stationarity limits the method's ability to adapt to non-stationary environments, which are common in retail and supply chain contexts where demand patterns shift significantly over time.

## Datasets

- [[m5-competition]]
- [[favorita-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2606.26774)
- [PDF](https://arxiv.org/pdf/2606.26774)

