---
# CSL-compatible fields
title: "Primary creep encodes time to failure across laboratory and natural systems"
author:
  - literal: "Qinghua Lei"
  - literal: "Didier Sornette"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24081"

# Custom fields
paper_id: "2603.24081"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "primary-creep-time-to-failure-scaling"
  - "creep-phase-rupture-forecasting-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:29:55Z"
created_at: "2026-03-28T05:29:55Z"
---

# Primary creep encodes time to failure across laboratory and natural systems

**Authors**: Qinghua Lei, Didier Sornette
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24081](https://arxiv.org/abs/2603.24081)

## Summary

This paper investigates progressive creep dynamics in geomaterials, compiling laboratory and field data spanning rocks, composites, and natural hazards like landslides. The core finding is a nearly linear correlation between the duration of the initial decelerating (primary) creep phase and the total time to catastrophic failure, holding across five orders of magnitude. This unified scaling law suggests that early-time creep dynamics inherently contain information about the entire failure process. The authors introduce this as a simple, robust framework for forecasting rupture across diverse material and natural systems.

## Key Contributions

- Established a nearly linear scaling relationship between the duration of the early-stage (primary) creep and the total time to rupture across five orders of magnitude.
- Demonstrated the validity of this unified scaling law by compiling and analyzing creep data from diverse laboratory systems (rocks, composites, papers, glasses) and natural systems (landslides, rockfalls, glaciers).
- Proposed a simple and robust framework for forecasting rupture time by focusing only on the dynamics of the initial, decelerating creep phase.

## Limitations

The abstract focuses on the compilation and finding of the scaling law, but potential limitations regarding measurement precision in natural systems or the precise physical mechanisms underlying the linear correlation are not detailed.

## Key Concepts

- [[primary-creep-time-to-failure-scaling]]: A newly discovered linear correlation between the duration of the early-stage decelerating creep phase and the total time to catastrophic failure in geomaterials.
- [[creep-phase-rupture-forecasting-framework]]: A robust forecasting framework for catastrophic failure based on analyzing the transitions between the decelerating, steady-state, and accelerating phases of progressive creep.

## Archivist Review

Two concepts were approved as they represent a fundamentally unified, physics-based scaling law and the associated robust forecasting framework derived from analyzing progressive creep dynamics. The framework concept was deemed potentially redundant but kept as it frames the analysis methodology. No datasets or open questions were proposed or approved as the paper focused on a new empirical finding rather than a general technical bottleneck.

### Approved Concepts
- Primary Creep Scaling Law: The finding establishes a universal, unified predictive framework for rupture time based solely on the initial, decelerating creep phase dynamics, which is highly novel across different material systems.
- Creep Phase-Based Rupture Forecasting: The paper proposes a new conceptual framework for failure prediction that systematically utilizes the sequence of physical creep phases (decelerating, quasi-stationary, accelerating).

### Rejected Candidates
- [concept] Creep Phase-Based Rupture Forecasting (`creep-phase-rupture-forecasting-framework`) - subcomponent_of_broader_mechanism: The candidate 'Creep Phase-Based Rupture Forecasting' is too closely related to the core concept 'Primary Creep Scaling Law'; the scaling law itself is the central, reusable contribution.

## Links

- [Abstract](https://arxiv.org/abs/2603.24081)
- [PDF](https://arxiv.org/pdf/2603.24081)

