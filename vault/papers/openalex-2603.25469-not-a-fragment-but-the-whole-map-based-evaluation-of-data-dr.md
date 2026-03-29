---
# CSL-compatible fields
title: "Not a fragment, but the whole: Map-based evaluation of data-driven Fire Danger Index models"
author:
  - literal: "Shahbaz Alvi"
  - literal: "Italo Epicoco"
  - literal: "José María Costa-Saura"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25469"

# Custom fields
paper_id: "2603.25469"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "evaluation"
  - "anomaly-detection"
  - "safety-critical"
architectures:
  []
datasets:
  []
concept_slugs:
  - "map-based-fdi-evaluation"
  - "ensemble-fire-forecasting-improvement"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:07:56Z"
created_at: "2026-03-29T06:07:56Z"
---

# Not a fragment, but the whole: Map-based evaluation of data-driven Fire Danger Index models

**Authors**: Shahbaz Alvi, Italo Epicoco, José María Costa-Saura
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25469](https://arxiv.org/abs/2603.25469)

## Summary

This paper addresses the limitations of standard classification metrics in evaluating operational Fire Danger Index (FDI) forecasting models, which often neglect the high cost associated with false positive predictions. The authors introduce a novel, map-based evaluation paradigm designed to directly align model performance with real-world decision-making in forest fire management. The methodology systematically analyzes a model's ability to accurately forecast fire events while rigorously accounting for false alarms. Furthermore, the research empirically shows that employing an ensemble of machine learning models is an effective strategy for simultaneously enhancing fire identification accuracy and minimizing the false positive rate.

## Key Contributions

- Proposed a novel, map-based evaluation method for daily Fire Danger Index (FDI) models that aligns performance assessment with real-world operational decision-making requirements.
- Systematically assessed model performance focusing on the critical trade-off between accurately predicting fire activity and controlling the rate of false positives (false alarms).
- Demonstrated that the application of an ensemble of machine learning models leads to improvements in both fire identification capability and the reduction of false positive rates compared to individual models.

## Limitations

The abstract does not explicitly detail the datasets used for the map-based evaluation or the specific ML model architectures tested within the ensemble.

## Open Questions & Future Work

- [[optimal-cnn-depth-for-false-positive-rejection]]
- [[ensemble-recall-function-equivalence]]
- [[future-work-full-map-evaluation-standard]]

## Key Concepts

- [[map-based-fdi-evaluation]]: A novel evaluation methodology for Fire Danger Index (FDI) models that incorporates spatial information and accounts for the operational impact of false positives.
- [[ensemble-fire-forecasting-improvement]]: Using an ensemble of machine learning models specifically designed to simultaneously improve fire identification accuracy and decrease the rate of false alarms in Fire Danger Index forecasting.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 2 concept(s), 3 open question(s), and 0 dataset(s), with 0 rejected candidate note(s).

### Approved Concepts
- Map-based Fire Danger Index Evaluation: This proposes a new evaluation paradigm for a specific applied ML task (fire forecasting) that directly ties to operational relevance, moving beyond standard classification metrics.
- Ensemble Improvement for Fire Forecasting: The finding that ensembling specifically targets both recall (identification) and precision (false positives) reduction in this context is a valuable, specific result.

### Approved Open Questions
- Optimal CNN depth for no-fire confidence: Identifying the optimal complexity (depth) is crucial for engineering the most operationally useful model, where correctly classifying 'no-fire' areas with high confidence (low noise) is as important as detecting actual fires.
- Ensemble recall function equivalence: Understanding this relationship is key to rigorously validating the performance gains of ensemble averaging over individual model predictions when evaluation relies on a non-linear metric like recall.
- Standardizing full-map evaluation method: Establishing a clear standard for operational evaluation methods is essential for translating research advances into reliable real-world decision support systems.

## Links

- [Abstract](https://arxiv.org/abs/2603.25469)
- [PDF](https://arxiv.org/pdf/2603.25469)

