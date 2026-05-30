---
# CSL-compatible fields
title: "A Road-Conditioned Traffic Movie Prediction Network with Spatiotemporal and Structure-Consistent Learning"
author:
  - literal: "Joshua Kofi Asamoah"
  - literal: "Blessing Agyei Kyem"
  - literal: "Armstrong Aboah"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.27884"

# Custom fields
paper_id: "2605.27884"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "spatiotemporal-learning"
  - "traffic-prediction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "topology-guided-future-state-generation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:36:37Z"
created_at: "2026-05-30T07:36:37Z"
---

# A Road-Conditioned Traffic Movie Prediction Network with Spatiotemporal and Structure-Consistent Learning

**Authors**: Joshua Kofi Asamoah, Blessing Agyei Kyem, Armstrong Aboah
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.27884](https://arxiv.org/abs/2605.27884)

## Summary

RCSNet addresses the limitations of treating city-wide traffic movie prediction as standard image reconstruction by incorporating static road map topology as a conditioning factor. By aligning directional traffic dynamics with urban road structures, the model generates temporally consistent and spatially stable future traffic maps. The approach shows strong generalization, achieving consistent improvements in both same-city and cross-city forecasting benchmarks without requiring target-specific fine-tuning.

## Key Contributions

- Proposes RCSNet, a road-conditioned spatiotemporal network that reformulates traffic movie prediction as topology-guided future-state generation.
- Implements a structure-consistent learning objective that ensures generated traffic maps align with underlying road geometry and connectivity.
- Demonstrates significant performance gains, reducing RMSE by up to 11.5% in same-city tasks and over 10% in cross-city transfer scenarios without target-city fine-tuning.

## Open Questions & Future Work

- [[integrating-granular-road-attributes-in-traffic-forecasting]]

## Key Concepts

- [[topology-guided-future-state-generation]]: A framework that constraints traffic movie prediction by enforcing alignment with underlying urban road network topology and connectivity.

## Archivist Review

I have approved 'Topology-Guided Future-State Generation' as the core conceptual contribution and rejected the model-specific name 'RCSNet'. The open question regarding granular road attributes was approved as a substantial, unresolved challenge in spatiotemporal modeling that extends beyond the specific implementation proposed. All specific cities mentioned (Berlin, Chicago, etc.) were rejected as they function as routine benchmark instances rather than critical, reusable datasets.

### Approved Concepts
- Topology-Guided Future-State Generation: It represents a shift from treating traffic forecasting as pixel-level image reconstruction to a topology-constrained, physically grounded generation problem.

### Approved Open Questions
- Incorporating Granular Road Attributes: This addresses a core bottleneck in traffic modeling: how to move beyond generic spatial masks to leverage structured urban regulatory data for more physically and logically sound forecasts.

### Rejected Candidates
- [concept] RCSNet (`rcsnet`) - paper_local: This is the name of the specific model proposed, which is a paper-local instance of the broader topology-guided generation mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2605.27884)
- [PDF](https://arxiv.org/pdf/2605.27884)

