---
# CSL-compatible fields
title: "Predicting the Progression of Adolescent Idiopathic Scoliosis"
author:
  - literal: "Owen Pullen"
  - literal: "Amir Jamaludin"
  - literal: "Andrew Zisserman"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.28434"

# Custom fields
paper_id: "2609.28434"
paper_source: "openalex"
domain: "biology"
tags:
  - "transformer"
  - "time-series"
  - "fine-tuning"
  - "synthetic-data"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-26T09:38:03Z"
created_at: "2026-09-26T09:38:03Z"
---

# Predicting the Progression of Adolescent Idiopathic Scoliosis

**Authors**: Owen Pullen, Amir Jamaludin, Andrew Zisserman
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.28434](https://arxiv.org/abs/2609.28434)

## Summary

This paper proposes a transformer model to predict the longitudinal progression of Adolescent Idiopathic Scoliosis across a temporal sequence from ages 9 to 24 using Dual X-ray Absorptiometry (DXA) scans. The model is initially pre-trained on a large-scale synthetic dataset encompassing diverse curve types and progression trajectories, and is subsequently evaluated on real DXA scan sequences. Results show that the model effectively generalizes to real data, with fine-tuning further boosting predictive performance on both scoliosis and normal cases.

## Key Contributions

- Proposes a transformer-based model to predict the temporal progression of Adolescent Idiopathic Scoliosis from ages 9 to 24 using DXA scans.
- Utilizes a large-scale synthetic dataset of spine curves and time series covering diverse curve types and progression patterns for pre-training.
- Demonstrates effective generalization from synthetic to real clinical DXA scan sequences, with fine-tuning yielding substantial performance improvements.

## Archivist Review

The paper applies standard transformer modeling and synthetic pre-training to clinical spine progression data without introducing a broadly reusable time-series or forecasting mechanism. The open questions merely suggest standard clinical validation steps and metadata extensions.

### Rejected Candidates
- [open_question] Incorporating Contextual Metadata for Scoliosis Prediction (`incorporating-contextual-metadata-scoliosis`) - low_impact: Standard future work proposing the addition of auxiliary clinical metadata.
- [open_question] Cross-Institute Testing for Scoliosis Progression (`cross-institute-testing-scoliosis-progression`) - low_impact: Routine call for external validation across clinical sites without a distinct methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.28434)
- [PDF](https://arxiv.org/pdf/2609.28434)

