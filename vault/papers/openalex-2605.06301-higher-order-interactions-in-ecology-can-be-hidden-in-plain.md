---
# CSL-compatible fields
title: "Higher-order interactions in ecology can be hidden in plain sight"
author:
  - literal: "Violeta Calleja-Solanas"
  - literal: "Santiago Lamata-Otín"
  - literal: "Carlos Gómez-Ambrosi"
  - literal: "Jesús Gómez-Gardeñes"
  - literal: "Sandro Meloni"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.06301"

# Custom fields
paper_id: "2605.06301"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mechanistic-identifiability-problem"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:22:02Z"
created_at: "2026-05-10T07:22:02Z"
---

# Higher-order interactions in ecology can be hidden in plain sight

**Authors**: Violeta Calleja-Solanas, Santiago Lamata-Otín, Carlos Gómez-Ambrosi, Jesús Gómez-Gardeñes, Sandro Meloni
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.06301](https://arxiv.org/abs/2605.06301)

## Summary

This paper investigates the inherent limitations in inferring ecological interaction structures from abundance time-series data. The authors show that higher-order Lotka-Volterra dynamics often yield effective pairwise representations, creating a fundamental issue of mechanistic identifiability. Consequently, data-driven modeling can lead to highly accurate but physically misleading ecological interpretations. The findings emphasize that time series alone are insufficient for identifying interaction mechanisms, necessitating the inclusion of auxiliary ecological priors.

## Key Contributions

- Demonstrated that higher-order Lotka-Volterra dynamics can be statistically replicated by effective pairwise models, rendering them indistinguishable from time-series observations.
- Identified a fundamental mechanistic identifiability limit that prevents the unique inference of ecological interaction structures from abundance data.
- Argued for the necessity of incorporating non-time-series ecological constraints to resolve ambiguities in dynamical model selection.

## Open Questions & Future Work

- [[identifying-higher-order-interactions-beyond-timeseries]]

## Key Concepts

- [[mechanistic-identifiability-problem]]: A phenomenon where distinct dynamic mechanisms produce indistinguishable observational time series, rendering model identification ambiguous.

## Archivist Review

The paper introduces a significant challenge in dynamical systems and time-series modeling: the mechanistic identifiability problem where different underlying processes yield identical observational signatures. I have approved the concept and the corresponding open question as they address a fundamental limitation in time-series inference that extends beyond ecology into any field relying on dynamical modeling. No other candidates were provided.

### Approved Concepts
- Mechanistic Identifiability Problem: It highlights that time-series data alone is insufficient to recover underlying ecological models due to the observational equivalence of higher-order and pairwise models.

### Approved Open Questions
- Empirical Validation of Higher-Order Interactions: Misidentifying HOIs as pairwise (or vice-versa) can lead to failed predictions when communities are subjected to novel stressors or management interventions.

## Links

- [Abstract](https://arxiv.org/abs/2605.06301)
- [PDF](https://arxiv.org/pdf/2605.06301)

