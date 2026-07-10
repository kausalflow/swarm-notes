---
# CSL-compatible fields
title: "A study of holes: Topological analysis reveals crowd dynamics regimes in a bidirectional corridor scenario"
author:
  - literal: "Sabrina Desiree Kern"
  - literal: "Gerta Köster"
issued:
  date-parts:
    - [2026, 7, 7]
url: "https://arxiv.org/abs/2607.06086"

# Custom fields
paper_id: "2607.06086"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "crocker"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-10T08:15:42Z"
created_at: "2026-07-10T08:15:42Z"
---

# A study of holes: Topological analysis reveals crowd dynamics regimes in a bidirectional corridor scenario

**Authors**: Sabrina Desiree Kern, Gerta Köster
**Date**: 2026-07-07
**Paper ID**: [openalex:2607.06086](https://arxiv.org/abs/2607.06086)

## Summary

This paper applies topological data analysis, specifically persistent homology, to identify regimes in crowd dynamics within simulated uni- and bidirectional corridor scenarios. By analyzing pedestrian proximity-based connectivity, the authors construct CROCKER matrices—a topological signature representation for time series. They show that principal component analysis on these matrices effectively separates different crowd movement configurations, offering a robust, assumption-free method for characterizing complex spatio-temporal dynamics.

## Key Contributions

- Introduces topological data analysis using persistent homology to characterize crowd dynamics in bidirectional corridors without prior spatio-temporal assumptions.
- Demonstrates that CROCKER matrices effectively capture and separate distinct crowd dynamic regimes when combined with PCA on time-delayed pedestrian positional data.
- Validates the utility of persistent homology for identifying phase transitions in pedestrian movement patterns based solely on proximity-based connectivity.

## Open Questions & Future Work

- [[topological-vs-classical-crowd-metrics]]

## Key Concepts

- [[crocker]]: A matrix representation of topological persistent homology signatures derived from time-series data for analysis and dimensionality reduction.

## Archivist Review

I approved the CROCKER concept because it provides a standardizable format for representing topological time-series data, which is a reusable technique across diverse spatiotemporal domains. I also approved the open question regarding the comparison between topological and classical metrics, as it addresses a fundamental, unresolved bottleneck in evaluating whether the complexity of topological data analysis is justified by superior performance over simpler, well-established physical metrics.

### Approved Concepts
- CROCKER (Contour of Persistence-based Regression): Provides a structured matrix representation for topological persistence signatures over time, making them compatible with standard machine learning dimensionality reduction techniques.

### Approved Open Questions
- Topological vs. Classical Metrics: Determining the specific informational value-add of topological descriptors is essential for moving beyond empirical proofs-of-concept toward practical utility in crowd management and safety applications.

## Links

- [Abstract](https://arxiv.org/abs/2607.06086)
- [PDF](https://arxiv.org/pdf/2607.06086)

