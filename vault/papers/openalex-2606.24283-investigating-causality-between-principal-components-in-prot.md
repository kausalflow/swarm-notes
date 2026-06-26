---
# CSL-compatible fields
title: "Investigating causality between principal components in protein dynamics"
author:
  - literal: "Debarshi Banerjee"
  - literal: "Ali Hassanali"
  - literal: "Alessandro Laio"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.24283"

# Custom fields
paper_id: "2606.24283"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "causal-discovery-in-principal-component-dynamics"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:26:03Z"
created_at: "2026-06-26T08:26:03Z"
---

# Investigating causality between principal components in protein dynamics

**Authors**: Debarshi Banerjee, Ali Hassanali, Alessandro Laio
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.24283](https://arxiv.org/abs/2606.24283)

## Summary

This paper investigates causal relationships between principal components (PCs) in protein molecular dynamics simulations, which conventional PCA and TICA methods fail to capture. By utilizing a recently developed causal-discovery framework for high-dimensional time series, the authors infer putative causal asymmetries between collective protein motions. The approach generates directed influence networks, offering a new perspective on the hierarchical dynamical organization of proteins. This methodology provides a vital complement to standard statistical dimensionality reduction techniques.

## Key Contributions

- Introduces a causal inference framework to quantify directed asymmetries between principal components in protein molecular dynamics trajectories.
- Constructs directed dependency networks between collective protein motions that remain opaque to standard covariance-based methods like PCA or TICA.
- Demonstrates that directional causal relationships provide complementary insights into the dynamical organization of complex protein structural fluctuations.

## Open Questions & Future Work

- [[causal-confounder-distinction-in-high-dimensional-time-series]]

## Key Concepts

- [[causal-discovery-in-principal-component-dynamics]]: A framework for inferring directed causal asymmetries and influence networks between principal components of high-dimensional time-series data.

## Archivist Review

I approved the concept of causal discovery in PC dynamics because it bridges static feature decomposition with dynamical causal modeling, a persistent challenge in time-series analysis. The open question on confounder distinction was approved as a core theoretical bottleneck for causal inference in complex dynamical systems. Other candidates were rejected due to overly narrow scope or naming preferences.

### Approved Concepts
- Causal Discovery in Principal Component Dynamics: It provides a systematic method for extending standard static dimensionality reduction (PCA/TICA) to uncover directional causal influence in complex time-series systems.

### Approved Open Questions
- Causal confounder distinction: This is a fundamental challenge for the validity of causal inference in any complex dynamical system where confounding is present, which is common in molecular and physical simulations.

### Rejected Candidates
- [concept] causal-discovery-framework-for-principal-components (`causal-discovery-framework-for-principal-components`) - other: Renamed to a more descriptive and general slug for better vault organization.
- [open_question] Causal graph confounder identification (`causal-graph-confounder-identification`) - other: Renamed to a more standard and descriptive slug for better vault indexing.

## Links

- [Abstract](https://arxiv.org/abs/2606.24283)
- [PDF](https://arxiv.org/pdf/2606.24283)

