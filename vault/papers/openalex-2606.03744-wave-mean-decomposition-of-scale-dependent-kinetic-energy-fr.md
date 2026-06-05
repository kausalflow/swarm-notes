---
# CSL-compatible fields
title: "Wave-mean decomposition of scale-dependent kinetic energy from surface drifters"
author:
  - literal: "Han Wang"
  - literal: "Dhruv Balwada"
  - literal: "Jin-Han Xie"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03744"

# Custom fields
paper_id: "2606.03744"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "generalized-lagrangian-mean-filtering"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:40:17Z"
created_at: "2026-06-05T08:40:17Z"
---

# Wave-mean decomposition of scale-dependent kinetic energy from surface drifters

**Authors**: Han Wang, Dhruv Balwada, Jin-Han Xie
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03744](https://arxiv.org/abs/2606.03744)

## Summary

This paper introduces a Lagrangian filtering approach using the Generalized Lagrangian Mean (GLM) framework to decompose surface kinetic energy into wave and mean-flow components from surface drifter time series. By applying this method to Gulf of Mexico data, the authors demonstrate that standard Helmholtz decomposition of unfiltered velocity structure functions is insufficient for identifying dynamical wave-mean contributions. The study provides new insights into seasonal ocean dynamics, showing that winter mean flows are more active than summer flows at 500m-10km scales, and identifies a scale-dependent equipartition of motion components.

## Key Contributions

- Demonstrates that Lagrangian filtering effectively separates wave and mean-flow contributions in surface drifter observations.
- Proves that Helmholtz decomposition of unfiltered structure functions fails to provide accurate wave-mean dynamical decomposition.
- Reveals that surface mean flows at scales <1 km exhibit equipartition between divergent and rotational components, implying potential vertical exchange.

## Open Questions & Future Work

- [[dynamical-origin-rotational-divergent-equipartition]]

## Key Concepts

- [[generalized-lagrangian-mean-filtering]]: A filtering framework for decomposing Lagrangian velocities into physically meaningful wave and mean flow components by attributing velocities to mean rather than particle positions.

## Archivist Review

The paper is approved for its methodological advancement in Lagrangian ocean dynamics. I have approved the GLM-based filtering framework as it provides a distinct, physically-informed approach to time-series decomposition that improves upon standard Helmholtz methods. The open question regarding the dynamical origin of rotational-divergent equipartition is tracked as it represents a significant, unresolved submesoscale phenomenon in oceanography. No datasets were approved, as the Gulf of Mexico drifter data is a routine regional observation set.

### Approved Concepts
- Generalized Lagrangian Mean (GLM) Filtering: Provides a physically rigorous foundation for separating wave and mean flow components in Lagrangian trajectories, correcting for the limitations of standard Helmholtz decomposition in dynamic settings.

### Approved Open Questions
- Dynamical origin of rotational-divergent equipartition: Understanding submesoscale vertical transport is critical for oceanographic climate modeling; identifying if this equipartition represents significant vertical energy exchange or analytical noise is essential for robust parameterization.

## Links

- [Abstract](https://arxiv.org/abs/2606.03744)
- [PDF](https://arxiv.org/pdf/2606.03744)

