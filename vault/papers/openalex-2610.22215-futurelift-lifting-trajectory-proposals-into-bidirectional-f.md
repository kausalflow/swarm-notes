---
# CSL-compatible fields
title: "FutureLift: Lifting Trajectory Proposals into Bidirectional Future Graphs for Motion Forecasting"
author:
  - literal: "Daniel Grimm"
  - literal: "J. Marius Zöllner"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.22215"

# Custom fields
paper_id: "2610.22215"
paper_source: "openalex"
domain: "robotics"
tags:
  - "autonomous-agent"
  - "planning"
  - "robustness"
  - "multimodal"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "futurelift"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:13:00Z"
created_at: "2026-10-18T09:13:00Z"
---

# FutureLift: Lifting Trajectory Proposals into Bidirectional Future Graphs for Motion Forecasting

**Authors**: Daniel Grimm, J. Marius Zöllner
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.22215](https://arxiv.org/abs/2610.22215)

## Summary

FutureLift is a backbone-agnostic motion refiner for autonomous driving that represents multimodal trajectory proposals as heterogeneous future graphs. By connecting spatially grounded temporal nodes to agent histories, map elements, alternative modes, and other agents' future trajectories via bidirectional temporal edges, it allows holistic residual corrections in a single pass. Evaluated on Argoverse2 and the Waymo Open Motion Dataset, FutureLift consistently improves frozen proposals, ranking first in minADE and minFDE on the WOMD leaderboard among standard-input methods.

## Key Contributions

- Introduces FutureLift, a backbone-agnostic motion refiner that represents multimodal trajectory proposals as heterogeneous future graphs.
- Employs bidirectional temporal edges enabling later evidence to revise earlier segments in a single pass.
- Achieves state-of-the-art performance on the Waymo Open Motion Dataset leaderboard, ranking first in minADE (0.5049m) and minFDE (0.9942m) among compared standard-input methods without LiDAR or ensembling.

## Open Questions & Future Work

- [[future-graph-lifting-unstructured-environments-and-planning]]

## Key Concepts

- [[futurelift]]: A backbone-agnostic motion refiner that represents multimodal trajectory proposals as heterogeneous future graphs with bidirectional temporal edges for residual correction.

## Archivist Review

Approved the central backbone-agnostic motion refinement framework (FutureLift) and an open question exploring future-graph lifting for planning and unstructured environments. Rejected datasets as they already exist in the vault.

### Approved Concepts
- FutureLift: It introduces a novel framework for motion forecasting that lifts trajectory proposals into bidirectional future graphs to capture relational context across agent histories, maps, alternative modes, and joint agent trajectories.

### Approved Open Questions
- Future-Graph Lifting for Planning: Extending motion forecasting refiners to closed-loop planning and unstructured environments addresses the current limitation of open-loop metrics and static HD maps.

### Rejected Candidates
- [dataset] Argoverse2 (`argoverse-2`) - duplicate_existing: Argoverse 2 is already present in the vault under existing canonical names.
- [dataset] Waymo Open Motion Dataset (`waymo-open-motion-dataset`) - duplicate_existing: Waymo Open Motion Dataset is already present in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2610.22215)
- [PDF](https://arxiv.org/pdf/2610.22215)

