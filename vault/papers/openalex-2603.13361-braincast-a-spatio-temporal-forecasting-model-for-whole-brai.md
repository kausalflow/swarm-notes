---
# CSL-compatible fields
title: "BrainCast: A Spatio-Temporal Forecasting Model for Whole-Brain fMRI Time Series Prediction"
author:
  - literal: "Yunlong Gao"
  - literal: "Jinbo Yang"
  - literal: "Li Xiao"
  - literal: "Haiye Huo"
  - literal: "Yang Ji"
  - literal: "Hao Wang"
  - literal: "Aiying Zhang"
  - literal: "Yu-Ping Wang"
issued:
  date-parts:
    - [2026, 3, 9]
url: "https://arxiv.org/abs/2603.13361"

# Custom fields
paper_id: "2603.13361"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "neural-signal-processing"
  - "multivariate-time-series"
  - "self-supervised-learning"
architectures:
  []
datasets:
  - "Human Connectome Project"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:08:33Z"
created_at: "2026-03-27T14:08:33Z"
---

# BrainCast: A Spatio-Temporal Forecasting Model for Whole-Brain fMRI Time Series Prediction

**Authors**: Yunlong Gao, Jinbo Yang, Li Xiao, Haiye Huo, Yang Ji, Hao Wang, Aiying Zhang, Yu-Ping Wang
**Date**: 2026-03-09
**Paper ID**: [openalex:2603.13361](https://arxiv.org/abs/2603.13361)

## Summary

BrainCast is a novel spatio-temporal forecasting framework proposed to extend whole-brain fMRI time series data, mitigating issues arising from short clinical scan durations. The model treats fMRI forecasting as a multivariate time series problem, integrating three key modules: Spatial Interaction Awareness for inter-ROI dependencies via tokenized ROI series, Temporal Feature Refinement for capturing internal dynamics through energy component enhancement, and Spatio-temporal Pattern Alignment to merge the representations. Experimental validation on Human Connectome Project datasets shows BrainCast surpasses existing time series baselines, and the generated data proves beneficial for downstream tasks like cognitive ability prediction.

## Key Contributions

- Introduction of BrainCast, a novel spatio-temporal forecasting framework for extending informative whole-brain fMRI time series data by treating it as a multivariate time series prediction task.
- Design of a Spatial Interaction Awareness module that tokenizes ROI time series to explicitly model inter-ROI dependencies.
- Development of a Temporal Feature Refinement module that captures intrinsic neural dynamics by selectively enhancing low- and high-energy temporal components within each ROI.
- Demonstration that BrainCast outperforms state-of-the-art time series forecasting baselines on resting-state and task fMRI datasets, and that extended data improves downstream cognitive ability prediction.

## Limitations

The abstract does not explicitly state limitations, but the core task is constrained by the quality and complexity of fMRI data, which inherently limits generalization to unseen brain states or scanner conditions.

## Open Questions & Future Work

- [[subject-specific-variability-fmri-forecasting]]
- [[multi-modal-data-fusion-fmri-forecasting]]
- [[clinical-validation-neurological-applications]]

## Key Concepts

- [BrainCast Framework](../concepts/braincast-forecasting-framework.md): A spatio-temporal forecasting framework designed to extend whole-brain fMRI time series by jointly modeling temporal dynamics within and spatial interactions across Regions of Interest (ROIs).

## Datasets

- [Human Connectome Project](../datasets/human-connectome-project.md)

## Limitations

The abstract does not explicitly state limitations, but the core task is constrained by the quality and complexity of fMRI data, which inherently limits generalization to unseen brain states or scanner conditions.

## Links

- [Abstract](https://arxiv.org/abs/2603.13361)
- [PDF](https://arxiv.org/pdf/2603.13361)

