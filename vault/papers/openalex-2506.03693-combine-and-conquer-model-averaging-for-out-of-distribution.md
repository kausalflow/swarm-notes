---
# CSL-compatible fields
title: "Combine and conquer: Model averaging for out-of-distribution forecasting"
author:
  - literal: "Stephane Hess"
  - literal: "Sander van Cranenburgh"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2506.03693"

# Custom fields
paper_id: "2506.03693"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:26:48Z"
created_at: "2026-08-02T07:26:48Z"
---

# Combine and conquer: Model averaging for out-of-distribution forecasting

**Authors**: Stephane Hess, Sander van Cranenburgh
**Date**: 2026-07-30
**Paper ID**: [openalex:2506.03693](https://arxiv.org/abs/2506.03693)

## Summary

This paper investigates the out-of-distribution (OOD) forecasting performance of diverse travel behaviour models, spanning traditional econometrics, mathematical psychology, and machine learning. The authors demonstrate that while data-driven models excel in-distribution, their reliability degrades out-of-distribution. To address this, they introduce a distance-weighted model averaging technique that dynamically assigns weights based on how far prediction characteristics deviate from the estimation data, favoring robust behavioral and econometric structures under severe OOD conditions.

## Key Contributions

- Demonstrates that while data-driven machine learning models excel for in-distribution mode choice forecasting, their out-of-distribution performance degrades significantly.
- Proposes a distance-weighted model averaging approach that adaptively allocates weights between econometric, mathematical psychology, and data-driven models based on out-of-distribution severity.
- Shows that the proposed model averaging strategy assigns higher weights to models with strong behavioral and econometric underpinnings as predictions move further outside the training distribution range.
- Extends the out-of-distribution quantification framework to a multivariate setting using a Gower distance metric.

## Limitations

Evaluated primarily on travel behaviour and mode choice case studies focusing on trip distance.

## Open Questions & Future Work

- [[multivariate-ood-model-averaging]]

## Archivist Review

The paper presents a distance-weighted model averaging technique for out-of-distribution travel behavior forecasting. The proposed concept of distance-weighted model averaging is standard in statistical literature, so it was rejected for novelty. However, the open question concerning multivariate out-of-distribution model averaging across multi-attribute feature spaces is retained as a valuable research direction.

### Approved Open Questions
- Multivariate Out-of-Distribution Model Averaging: Understanding how model averaging and behavioural versus machine learning models perform across multidimensional and socio-economic out-of-distribution settings is crucial for expanding practical transport demand forecasting methodologies.

### Rejected Candidates
- [concept] Distance-Weighted Model Averaging for Out-of-Distribution Forecasting (`distance-weighted-model-averaging`) - not_novel: Model averaging based on covariate distance or domain divergence is a standard statistical concept, making the specific application to trip distance insufficiently novel as a standalone vault note.

## Links

- [Abstract](https://arxiv.org/abs/2506.03693)
- [PDF](https://arxiv.org/pdf/2506.03693)

