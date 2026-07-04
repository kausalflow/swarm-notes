---
# CSL-compatible fields
title: "When Context Compensates for Sparse Event History: AlphaEarth for Spatio-Temporal Point-Process Forecasting"
author:
  - literal: "Yahya Aalaila"
  - literal: "Mouad Elhamdi"
  - literal: "Gerrit Großmann"
  - literal: "Daniel Jenson"
  - literal: "Elizaveta Semenova"
  - literal: "Sebastian Vollmer"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.01082"

# Custom fields
paper_id: "2607.01082"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "alphaearth-embeddings"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:36:21Z"
created_at: "2026-07-04T07:36:21Z"
---

# When Context Compensates for Sparse Event History: AlphaEarth for Spatio-Temporal Point-Process Forecasting

**Authors**: Yahya Aalaila, Mouad Elhamdi, Gerrit Großmann, Daniel Jenson, Elizaveta Semenova, Sebastian Vollmer
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.01082](https://arxiv.org/abs/2607.01082)

## Summary

This paper investigates the role of exogenous spatial context in enhancing spatio-temporal point-process models, particularly when local event history is sparse. By augmenting a log-Gaussian Cox process backbone with AlphaEarth embeddings, the authors demonstrate significant improvements in out-of-region predictive performance for emergency medical services (EMS) forecasting. The approach shows that incorporating external spatial data provides stability and performance gains that are most pronounced in data-scarce regimes, where history is limited to just 1-2 weeks.

## Key Contributions

- Introduces AlphaEarth embeddings as an exogenous spatial context provider for spatio-temporal point-process models.
- Demonstrates that contextual information significantly stabilizes out-of-region point-process forecasts under data-scarce conditions.
- Achieves 2-6x performance improvements in forecasting accuracy in regimes with limited event history (1-2 weeks) compared to event-only baselines.

## Open Questions & Future Work

- [[flexible-stpp-context-integration]]

## Key Concepts

- [[alphaearth-embeddings]]: A method for augmenting spatio-temporal point-process models with pre-computed exogenous spatial embeddings to improve forecasting in data-sparse regions.

## Archivist Review

The paper provides a clean, well-motivated approach for using exogenous spatial context to stabilize spatio-temporal point processes under extreme data scarcity. The approved concept and open question represent the core methodological contribution and the natural research extension, respectively, adhering to the standard of high reusability and impact within the time-series forecasting domain.

### Approved Concepts
- AlphaEarth Embeddings: These embeddings provide a formal, reusable mechanism for injecting exogenous spatial information into point processes, specifically to address the cold-start or sparsity problem in out-of-region forecasting.

### Approved Open Questions
- Flexible Integration of Contextual Fields: Moving beyond linear integration of spatial context is essential for scaling STPPs to more complex real-world datasets where simple priors are insufficient.

### Rejected Candidates
- [concept] No other candidates proposed. (`none`) - other: No additional relevant candidates were provided for consideration.

## Links

- [Abstract](https://arxiv.org/abs/2607.01082)
- [PDF](https://arxiv.org/pdf/2607.01082)

