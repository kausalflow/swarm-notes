---
# CSL-compatible fields
title: "Co-evolution of bar and spiral arms in TNG50 simulations using Information Theory"
author:
  - literal: "Anagha A G"
  - literal: "A Banerjee"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16403"

# Custom fields
paper_id: "2606.16403"
paper_source: "openalex"
domain: "biology"
tags:
  - "dataset"
architectures:
  []
datasets:
  - "illustris-tng50"
concept_slugs:
  - "information-theoretic-causal-analysis-in-astrophysics"
dataset_slugs:
  - "illustris-tng50"
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:27:46Z"
created_at: "2026-06-17T09:27:46Z"
---

# Co-evolution of bar and spiral arms in TNG50 simulations using Information Theory

**Authors**: Anagha A G, A Banerjee
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16403](https://arxiv.org/abs/2606.16403)

## Summary

This paper investigates the coupled evolution of bar and spiral structures in barred-spiral galaxies using the TNG50 cosmological simulation. By applying Mutual Information and Transfer Entropy to time-series parameters of bar and spiral strength, the authors quantify the degree and direction of their interaction. The results suggest that these galactic components regulate one another on an equal footing, challenging the assumption of a singular driving force in their co-evolution.

## Key Contributions

- Demonstrates that bar-spiral galaxy co-evolution is characterized by a strong information-theoretic association with mutual information values between 0.4 and 0.8.
- Applies Transfer Entropy and Liang information flow to quantify causal directionality, revealing that bars and spiral arms mutually regulate their evolution.
- Identifies distinct evolutionary pathways based on whether bars or spirals form first, with time delays of up to 1.7 Gyrs in bar-late forming galaxies.

## Open Questions & Future Work

- [[dynamical-mechanisms-of-galactic-structure-coupling]]

## Key Concepts

- [[information-theoretic-causal-analysis-in-astrophysics]]: A framework for quantifying directional causal relationships in astrophysical time-series data using Transfer Entropy and related information-theoretic measures.

## Archivist Review

The review focuses on elevating the paper's contribution to a broader methodology for causal discovery in astrophysical time series. I rejected the local concept of 'Transfer Entropy for Galactic Dynamics' in favor of a more general concept that can handle various structures. I also approved the Illustris TNG50 dataset as it is a standard, highly cited reference in this domain. Finally, the open question was reframed to focus on the general challenge of linking information-theoretic findings to physical dynamics.

### Approved Concepts
- Information-Theoretic Causal Analysis in Astrophysics: This approach provides a generalized framework for identifying directional causal influence in complex, non-linear astrophysical dynamical systems where traditional observational correlations are insufficient.

### Approved Open Questions
- Mechanisms of Galactic Structure Coupling: Connecting abstract information-theoretic results to concrete astrophysical mechanisms is critical to bridging the gap between simulation-based data analytics and classical galactic dynamics.

### Rejected Candidates
- [concept] Transfer Entropy for Galactic Dynamics (`transfer-entropy-for-galactic-dynamics`) - subcomponent_of_broader_mechanism: This is a specific application of Transfer Entropy; the broader methodology is captured as a concept for the vault.

## Datasets

- [[illustris-tng50]]

## Links

- [Abstract](https://arxiv.org/abs/2606.16403)
- [PDF](https://arxiv.org/pdf/2606.16403)

