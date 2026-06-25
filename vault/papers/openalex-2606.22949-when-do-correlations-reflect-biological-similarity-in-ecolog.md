---
# CSL-compatible fields
title: "When do correlations reflect biological similarity in ecological dynamics?"
author:
  - literal: "Akiva Goldberg"
  - literal: "Nadav M. Shnerb"
issued:
  date-parts:
    - [2026, 6, 22]
url: "https://arxiv.org/abs/2606.22949"

# Custom fields
paper_id: "2606.22949"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:19:59Z"
created_at: "2026-06-25T08:19:59Z"
---

# When do correlations reflect biological similarity in ecological dynamics?

**Authors**: Akiva Goldberg, Nadav M. Shnerb
**Date**: 2026-06-22
**Paper ID**: [openalex:2606.22949](https://arxiv.org/abs/2606.22949)

## Summary

This paper critically evaluates the common practice of using abundance correlations in ecological time series as proxies for biological similarity and niche overlap. By analyzing stochastic community models, the authors prove that abundance correlations often fail to encode these biological quantities within the stochastic Lotka-Volterra framework. Furthermore, they demonstrate that in consumer-resource models, the interpretation of such correlations is highly sensitive to the specific stochastic forcing pathway. These results caution against the indiscriminate use of correlation-based inferences in ecological community dynamics.

## Key Contributions

- Demonstrates that the stochastic Lotka-Volterra framework inherently fails to consistently map biological similarity to abundance correlations.
- Establishes that in consumer-resource models, the pathway of stochastic forcing dictates whether abundance correlations reflect direct consumer dynamics or resource-mediated niche overlap.
- Provides a theoretical framework demonstrating that abundance correlations in community time series cannot serve as universal proxies for biological similarity or niche overlap.

## Open Questions & Future Work

- [[validity-of-biologically-grounded-noise-assumptions]]
- [[disentangling-noise-pathways-in-ecological-dynamics]]

## Archivist Review

The paper provides a strong theoretical critique of using abundance correlations in community time series as proxies for biological niche overlap. The approved open questions capture the core challenges identified: validating the link between noise structure and biology, and disentangling the distinct forcing pathways. No new concepts were approved as the analysis focused on existing theoretical models rather than proposing a new, reusable forecasting method.

### Approved Open Questions
- Validity of Biologically Grounded Noise Assumptions: Understanding whether environmental noise reflects biological similarity is fundamental to interpreting community abundance time-series as proxies for niche overlap. If the noise structure does not align with niche structure, current inference methods based on abundance correlations are fundamentally flawed.
- Disentangling Noise Pathways in Ecological Dynamics: Empirical data typically show a mix of direct and indirect environmental forcing. Without a way to distinguish these pathways, observers cannot correctly attribute the observed abundance correlations to either niche overlap or yield-depletion mismatch, leading to potentially incorrect biological conclusions.

## Links

- [Abstract](https://arxiv.org/abs/2606.22949)
- [PDF](https://arxiv.org/pdf/2606.22949)

