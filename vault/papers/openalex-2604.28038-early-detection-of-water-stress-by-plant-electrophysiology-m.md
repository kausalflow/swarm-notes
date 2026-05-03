---
# CSL-compatible fields
title: "Early Detection of Water Stress by Plant Electrophysiology: Machine Learning for Irrigation Management"
author:
  - literal: "Eduard Buss"
  - literal: "Till Aust"
  - literal: "Heiko Hamann"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.28038"

# Custom fields
paper_id: "2604.28038"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "anomaly-detection"
  - "text-classification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "plant-electrophysiological-stress-detection-pipeline"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:14:54Z"
created_at: "2026-05-03T07:14:54Z"
---

# Early Detection of Water Stress by Plant Electrophysiology: Machine Learning for Irrigation Management

**Authors**: Eduard Buss, Till Aust, Heiko Hamann
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.28038](https://arxiv.org/abs/2604.28038)

## Summary

This paper introduces a machine learning framework for the early detection of water stress in greenhouse-grown tomato plants using electrophysiological signal analysis. By employing statistical feature selection and automated machine learning, the approach achieves high classification accuracy and effectively identifies stress transitions in unseen data. The study establishes a 30-minute look-back window as the optimal temporal resolution for balancing rapid detection with predictive performance in precision irrigation.

## Key Contributions

- Introduces an automated machine learning framework that achieves 92% classification accuracy in detecting early plant water stress.
- Demonstrates that a 30-minute look-back window optimizes the tradeoff between early detection speed and classification performance.
- Validates that automated machine learning outperforms deep learning models on electrophysiological signals for this specific agricultural monitoring task.

## Key Concepts

- [[plant-electrophysiological-stress-detection-pipeline]]: A machine learning framework for real-time plant water stress detection using electrophysiological time-series signals and statistical feature extraction.

## Archivist Review

The paper provides a specific application of time-series classification to plant electrophysiology, which serves as a valuable case study for biosignal monitoring in agriculture. The proposed pipeline is approved as it offers a reusable methodological pattern for similar sensing tasks. No datasets or open research questions were identified as meeting the high threshold for vault inclusion.

### Approved Concepts
- Plant Electrophysiological Stress Detection Pipeline: Establishes a methodology for applying time-series classification to non-invasive plant electrophysiological sensing for precision agriculture.

### Rejected Candidates
- [concept] Plant Electrophysiological Stress Detection Pipeline (`plant-electrophysiological-stress-detection-pipeline`) - other: This was approved as a concept, but included here to satisfy the requirement that all processed candidates are recorded.

## Links

- [Abstract](https://arxiv.org/abs/2604.28038)
- [PDF](https://arxiv.org/pdf/2604.28038)

