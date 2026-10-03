---
# CSL-compatible fields
title: "Activity Recognition from Smart Insole Sensor Data Using a Circular Dilated CNN"
author:
  - literal: "Yanhua Zhao"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2603.04477"

# Custom fields
paper_id: "2603.04477"
paper_source: "openalex"
domain: "time-series"
tags:
  - "convolutional-neural-network"
  - "cnn"
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:08:51Z"
created_at: "2026-10-03T10:08:51Z"
---

# Activity Recognition from Smart Insole Sensor Data Using a Circular Dilated CNN

**Authors**: Yanhua Zhao
**Date**: 2026-10-01
**Paper ID**: [openalex:2603.04477](https://arxiv.org/abs/2603.04477)

## Summary

This paper presents an activity classification system for smart insoles using a circular dilated convolutional neural network (CDCNN) to process multi-modal time-series data from pressure sensors, accelerometers, and gyroscopes. Operating on 160-frame windows with 24 channels, the model achieves 86.42% test accuracy on a subject-independent four-class task covering standing, walking, sitting, and tandem activities. Additionally, permutation feature importance is used to quantify the relative contributions of individual sensors to the classification performance.

## Key Contributions

- Proposes an activity classification system using a circular dilated convolutional neural network (CDCNN) for multi-modal smart insole time-series data.
- Processes 160-frame windows across 24 channels combining pressure, accelerometer, and gyroscope readings.
- Achieves 86.42% test accuracy in a subject-independent evaluation on a four-class activity recognition task (Standing, Walking, Sitting, Tandem).
- Analyzes feature importance using permutation feature importance to evaluate sensor contributions.

## Limitations

Evaluated on a four-class task with subject-independent evaluation achieving 86.42% accuracy, leaving room for broader activity sets and improved generalization.

## Archivist Review

Applied strict filtering standards, rejecting the single domain-specific open question as routine validation practice rather than a reusable research frontier. No concepts or datasets met the vault's threshold for permanence.

### Rejected Candidates
- [open_question] Subject-Independent Evaluation in Gait Recognition (`subject-independent-evaluation-gait`) - not_novel: This question touches on standard cross-subject validation principles common to sensor-based biometric and activity recognition without introducing a distinct theoretical bottleneck or algorithmic mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2603.04477)
- [PDF](https://arxiv.org/pdf/2603.04477)

