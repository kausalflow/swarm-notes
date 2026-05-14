---
# CSL-compatible fields
title: "Set Prediction for Next-Day Active Fire Forecasting"
author:
  - literal: "Yuchen Bai"
  - literal: "Georgios Athanasiou"
  - literal: "Xin Yu"
  - literal: "Diogenis Antonopoulos"
  - literal: "Ioannis Papoutsis"
  - literal: "Stijn Hantson"
  - literal: "Nuno Carvalhais"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10298"

# Custom fields
paper_id: "2605.10298"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sparse-point-set-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:38:04Z"
created_at: "2026-05-14T07:38:04Z"
---

# Set Prediction for Next-Day Active Fire Forecasting

**Authors**: Yuchen Bai, Georgios Athanasiou, Xin Yu, Diogenis Antonopoulos, Ioannis Papoutsis, Stijn Hantson, Nuno Carvalhais
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10298](https://arxiv.org/abs/2605.10298)

## Summary

Wildfire Ignition Set Predictor (WISP) reformulates next-day active fire forecasting from traditional grid-based probability estimation into a sparse point-set prediction problem. Utilizing a query-based architecture trained with Hungarian matching, WISP predicts the locations of active fire cluster centers at 375m resolution based on multi-source covariates. An asymmetric classification-localization weighting loss is proposed to optimize the interaction between score assignment and cluster localization. Experimental results on a novel, globally distributed benchmark demonstrate that the framework effectively captures fire radiative power mass and provides high-precision localizations.

## Key Contributions

- Introduces Wildfire Ignition Set Predictor (WISP), a query-based model for next-day wildfire forecasting that treats the task as sparse point-set prediction rather than grid-based probability.
- Implements an asymmetric classification-localization weighting strategy within Hungarian matching to stabilize query-based training for wildfire cluster detection.
- Establishes a new globally distributed, hourly, multi-source wildfire benchmark, demonstrating a 38.2% AP and significant coverage of Fire Radiative Power (FRP) on held-out test data.

## Open Questions & Future Work

- [[set-prediction-assignment-instability]]

## Key Concepts

- [[sparse-point-set-forecasting]]: A forecasting paradigm that reformulates spatial-temporal event prediction as a sparse point-set detection task using query-based architectures.

## Archivist Review

I approved 'Sparse Point-Set Forecasting' as the overarching paradigm shift presented in the paper, rejecting the specific 'WISP' model name as a local instantiation. I also approved 'set-prediction-assignment-instability' as it is a well-known, foundational issue in this domain that remains a substantial bottleneck for future work. Other candidates were rejected as being either design-specific subcomponents of these ideas or as lacking the required level of abstraction for long-term vault utility.

### Approved Concepts
- Sparse Point-Set Forecasting: Shifts wildfire forecasting from traditional dense grid-based probability estimation to sparse, query-based point-set prediction, which is a significant paradigm change.

### Approved Open Questions
- Stabilizing Set Prediction Assignments: This is a fundamental challenge in DETR-style set prediction architectures, directly impacting model convergence and the reliability of learned spatial representations.

### Rejected Candidates
- [concept] Wildfire Ignition Set Predictor (WISP) (`wildfire-ignition-set-predictor-wisp`) - subcomponent_of_broader_mechanism: The model name WISP is a local implementation of the more general 'Sparse Point-Set Forecasting' concept.
- [open_question] Resolving Query Score Conflicts (`set-prediction-score-role-conflict`) - subcomponent_of_broader_mechanism: This conflict is a specific design consequence of query-based models that can be addressed as part of the broader study of set prediction stability.

## Links

- [Abstract](https://arxiv.org/abs/2605.10298)
- [PDF](https://arxiv.org/pdf/2605.10298)

