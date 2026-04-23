---
# CSL-compatible fields
title: "Recurrence analysis of quantum many-body dynamics"
author:
  - literal: "Tomasz Szołdra"
  - literal: "Matheus S. Palmero"
  - literal: "Peter Schmelcher"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.18446"

# Custom fields
paper_id: "2604.18446"
paper_source: "openalex"
domain: "physics"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "recurrence-quantification-analysis-for-quantum-dynamics"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:56:33Z"
created_at: "2026-04-23T06:56:33Z"
---

# Recurrence analysis of quantum many-body dynamics

**Authors**: Tomasz Szołdra, Matheus S. Palmero, Peter Schmelcher
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.18446](https://arxiv.org/abs/2604.18446)

## Summary

This paper introduces recurrence analysis, a technique traditionally used in classical nonlinear dynamics, to the study of out-of-equilibrium quantum many-body systems. By applying recurrence plots and recurrence quantification analysis to two-site correlations in the 1D transverse-field Ising model, the authors demonstrate the framework's ability to capture complex temporal structures and phase transitions. This methodology allows for the unsupervised detection of critical field strengths, offering a model-agnostic approach to analyzing high-dimensional quantum dynamics.

## Key Contributions

- Adapts recurrence quantification analysis (RQA) as a nonlinear time-series tool for characterizing out-of-equilibrium quantum many-body observables.
- Demonstrates the capability to identify the critical field strength in the 1D transverse-field Ising model without prior model knowledge.
- Provides a qualitative and quantitative framework for the unsupervised detection of quantum phase transitions via recurrence plot fingerprints.

## Open Questions & Future Work

- [[recurrence-analysis-for-non-ergodicity]]

## Key Concepts

- [[recurrence-quantification-analysis-for-quantum-dynamics]]: A nonlinear time-series analysis framework adapted for extracting numerical descriptors from correlated quantum many-body observables to detect phase transitions.

## Archivist Review

I approved the concept of applying RQA to quantum dynamics as it represents a novel cross-domain methodology (nonlinear time-series for physics) likely to be reusable. The open question regarding its application to non-ergodicity and scarring is also high-impact, providing a clear research trajectory. I adjusted the slug to be slightly more general to ensure better utility as a permanent record.

### Approved Concepts
- Recurrence Quantification Analysis for Quantum Dynamics: Provides a model-agnostic, unsupervised approach to characterizing complex quantum out-of-equilibrium dynamics and phase transitions using nonlinear time-series techniques.

### Approved Open Questions
- Recurrence analysis for non-ergodicity: This is technically significant because RQA provides a potential unsupervised method to distinguish complex phases of matter that are currently difficult to characterize in the time domain.

### Rejected Candidates
- [concept] Recurrence Quantification Analysis for Quantum Many-Body Systems (`recurrence-quantification-analysis-for-quantum-many-body-systems`) - duplicate_existing: This is a duplicate of the approved concept, simplified to a more general slug for better reusability.

## Links

- [Abstract](https://arxiv.org/abs/2604.18446)
- [PDF](https://arxiv.org/pdf/2604.18446)

