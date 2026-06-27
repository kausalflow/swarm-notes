---
# CSL-compatible fields
title: "Geometrically convex return risk measures on AM-algebras"
author:
  - literal: "Christian Laudagé"
issued:
  date-parts:
    - [2026, 6, 24]
url: "https://arxiv.org/abs/2606.26031"

# Custom fields
paper_id: "2606.26031"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "risk-management"
architectures:
  []
datasets:
  []
concept_slugs:
  - "return-risk-measures"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-27T07:43:21Z"
created_at: "2026-06-27T07:43:21Z"
---

# Geometrically convex return risk measures on AM-algebras

**Authors**: Christian Laudagé
**Date**: 2026-06-24
**Paper ID**: [openalex:2606.26031](https://arxiv.org/abs/2606.26031)

## Summary

This paper provides a rigorous mathematical extension of Return Risk Measures (RRMs) beyond standard random variables to general ordered vector spaces and AM-algebras. By characterizing positive homogeneity through geometric epigraphs, the work establishes theoretical foundations for return-based risk assessment in higher-dimensional contexts. The study further introduces new classes of systemic and vector-valued RRMs, establishing key properties such as continuity, finiteness, and duality representations.

## Key Contributions

- Extends the axiomatic foundation of Return Risk Measures (RRMs) from random variables to general ordered vector spaces and AM-algebras.
- Characterizes positive homogeneity for RRMs using the geometric epigraph property.
- Introduces novel classes of systemic and vector-valued return risk measures suitable for multidimensional financial analysis.

## Open Questions & Future Work

- [[rrm-domain-generalization]]

## Key Concepts

- [[return-risk-measures]]: An axiomatic framework for assessing risk in time series using logarithmic returns on ordered vector spaces.

## Archivist Review

I approved the concept of Return Risk Measures as the central theoretical framework of the paper. I also approved one open question regarding the domain generalization of these measures, reformulating its slug to be more descriptive and distinct from existing entries. The 'Systemic and Vector-Valued' candidate was rejected as a subcomponent of the broader RRM framework.

### Approved Concepts
- Return Risk Measures: Provides the necessary axiomatic generalization for risk assessment in multidimensional finance and time series analysis.

### Approved Open Questions
- Generalizing RRM Domain Domains: Critical for applying RRM theory to financial datasets characterized by heavy tails and varying integrability requirements.

### Rejected Candidates
- [concept] Systemic and Vector-Valued RRMs (`systemic-and-vector-valued-rrms`) - subcomponent_of_broader_mechanism: This represents a classification within the RRM framework rather than a novel methodology; the concept of RRMs itself is sufficiently broad to encompass these variants.
- [open_question] Extending RRMs to f-algebras (`rrm-beyond-am-algebras`) - other: The proposed question was technically sound but required a more descriptive, thematic slug to align with the vault's taxonomy.

## Links

- [Abstract](https://arxiv.org/abs/2606.26031)
- [PDF](https://arxiv.org/pdf/2606.26031)

