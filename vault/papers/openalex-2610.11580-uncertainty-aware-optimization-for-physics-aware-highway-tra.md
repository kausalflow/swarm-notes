---
# CSL-compatible fields
title: "Uncertainty-Aware Optimization for Physics-Aware Highway Trajectory Prediction"
author:
  - literal: "Aanchal Rajesh Chugh"
  - literal: "Sebastian Dörn"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11580"

# Custom fields
paper_id: "2610.11580"
paper_source: "openalex"
domain: "robotics"
tags:
  - "autonomous-agent"
  - "robustness"
  - "uncertainty-quantification"
  - "conformal-prediction"
  - "trajectory-prediction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "x-track"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-11T11:05:42Z"
created_at: "2026-10-11T11:05:42Z"
---

# Uncertainty-Aware Optimization for Physics-Aware Highway Trajectory Prediction

**Authors**: Aanchal Rajesh Chugh, Sebastian Dörn
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11580](https://arxiv.org/abs/2610.11580)

## Summary

This paper proposes uncertainty-aware extensions of the physics-aware trajectory prediction framework X-TRACK, named X-TRACK-DE and X-TRACK-MCD, which model both aleatoric and epistemic uncertainties by propagating motion space uncertainty into trajectory space. Additionally, conformal prediction is applied to the trajectory predictive covariance to guarantee a desired marginal coverage level. Evaluations on the highD dataset show that these variants improve prediction accuracy over the deterministic baseline while providing well-calibrated predictive uncertainty.

## Key Contributions

- Proposed uncertainty-aware extensions of X-TRACK (X-TRACK-DE and X-TRACK-MCD) that model aleatoric and epistemic uncertainties by propagating motion space uncertainty to trajectory space.
- Applied conformal prediction to the trajectory space predictive covariance to construct uncertainty regions targeting a desired marginal coverage level.
- Evaluated on the highD dataset, demonstrating improved trajectory prediction accuracy over the deterministic baseline and effective conformal calibration of predictive uncertainty.

## Open Questions & Future Work

- [[diverse-scenarios-conformal-calibration]]

## Key Concepts

- [[x-track]]: A physics-aware trajectory prediction framework extended to model aleatoric and epistemic uncertainties.

## Archivist Review

Approved the core physics-aware trajectory prediction framework (X-TRACK) and the open question regarding conformal calibration across diverse scenarios. Rejected the highD dataset as it is a standard existing benchmark dataset.

### Approved Concepts
- X-TRACK: Central physics-aware trajectory prediction framework extended for uncertainty quantification.

### Approved Open Questions
- Diverse Scenarios and Conformal Calibration: Important for verifying the generalizability and robustness of physics-aware uncertainty propagation and conformal calibration beyond standard datasets like highD.

### Rejected Candidates
- [dataset] highD (`highd`) - duplicate_existing: highD is a standard public dataset already well-established in the autonomous driving literature and does not require a standalone vault entry.

## Links

- [Abstract](https://arxiv.org/abs/2610.11580)
- [PDF](https://arxiv.org/pdf/2610.11580)

