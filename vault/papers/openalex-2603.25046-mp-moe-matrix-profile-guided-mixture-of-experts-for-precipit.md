---
# CSL-compatible fields
title: "MP-MoE: Matrix Profile-Guided Mixture of Experts for Precipitation Forecasting"
author:
  - literal: "Huyen Ngoc Tran"
  - literal: "Dung Trung Tran"
  - literal: "Hong Nguyen"
  - literal: "Xuan-Vu Phan"
  - literal: "Nam-Phong Nguyen"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25046"

# Custom fields
paper_id: "2603.25046"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "mixture-of-experts"
  - "anomaly-detection"
  - "evaluation"
architectures:
  - "mixture-of-experts"
datasets:
  []
concept_slugs:
  - "mp-moe-matrix-profile-guided-mixture-of-experts"
  - "structural-aware-matrix-profile-objective"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:07:36Z"
created_at: "2026-03-29T06:07:36Z"
---

# MP-MoE: Matrix Profile-Guided Mixture of Experts for Precipitation Forecasting

**Authors**: Huyen Ngoc Tran, Dung Trung Tran, Hong Nguyen, Xuan-Vu Phan, Nam-Phong Nguyen
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25046](https://arxiv.org/abs/2603.25046)

## Summary

This paper introduces the Matrix Profile-guided Mixture of Experts (MP-MoE) framework to enhance precipitation forecasting in complex tropical regions by addressing the limitations of point-wise loss functions that suffer from the double penalty effect due to phase shifts. MP-MoE integrates a structural-aware Matrix Profile objective, which leverages subsequence-level similarity, to guide expert selection and mitigate errors caused by minor temporal misalignments. The method was tested on rainfall data across multiple horizons (1-hour to 48-hour accumulated) from Vietnamese river basins. Experimental results show that MP-MoE improves performance over baselines, particularly for heavy rainfall events as indicated by higher CSI-M scores and significantly lower Dynamic Time Warping (DTW) values, confirming its efficacy in capturing peak intensity and preserving event morphology.

## Key Contributions

- Proposed MP-MoE, a framework that integrates a structural-aware Matrix Profile objective with conventional intensity loss for precipitation forecasting.
- The Matrix Profile objective facilitates more reliable expert selection in the Mixture of Experts by leveraging subsequence-level similarity, mitigating issues from temporal misalignments.
- MP-MoE outperformed raw NWP and baseline learning methods on heavy rainfall events, as measured by CSI-M.
- The framework significantly reduced Dynamic Time Warping (DTW) values, demonstrating superior morphological integrity preservation of storm events.

## Limitations

The evaluation is focused on forecasting in tropical regions (Vietnam river basins), and its generalized performance across diverse climate zones remains to be fully explored.

## Open Questions & Future Work

- [[extending-to-spatiotemporal-domain-with-graph-dependencies]]
- [[adaptive-tuning-of-hyperparameters-via-online-learning]]

## Key Concepts

- [[mp-moe-matrix-profile-guided-mixture-of-experts]]: A Mixture of Experts framework for time-series forecasting guided by a structural-aware Matrix Profile objective to improve alignment resilience.
- [[structural-aware-matrix-profile-objective]]: A loss function for sequence modeling that utilizes the Matrix Profile to measure and optimize for similarity in temporal subsequences rather than just point-wise accuracy.

## Archivist Review

The primary contributions revolve around the novel MP-MoE architecture and the specific Structural-Aware Matrix Profile Objective used to guide expert selection against phase shifts. Both concepts were approved as reusable mechanisms. Two promising open questions regarding spatiotemporal extension and adaptive hyperparameter tuning were also approved due to their direct link to overcoming the current model's core limitations in generalization and robustness. The specific Vietnamese rainfall dataset was rejected as it is too localized for the vault.

### Approved Concepts
- Matrix Profile-Guided Mixture of Experts (MP-MoE): It is the central novel architecture proposed in the paper, integrating structural-aware loss into a MoE framework for improved time-series alignment in forecasting.
- Structural-Aware Matrix Profile Objective: This novel loss function shifts evaluation from point-wise errors to subsequence-level similarity, specifically addressing phase shifts common in precipitation forecasting.

### Approved Open Questions
- Extend to Spatiotemporal Domain: Moving from 1D to spatiotemporal modeling is critical for capturing large-scale atmospheric correlation and improving regional hazard forecasting consistency.
- Adaptive Hyperparameter Tuning: Adaptive tuning of hyperparameters like $\lambda$ and $\Delta$ is necessary to maintain forecast accuracy across the highly variable conditions of tropical monsoon regimes.

### Rejected Candidates
- [dataset] rainfall datasets from two major river basins in Vietnam (`rainfall-datasets-from-two-major-river-basins-in-vietnam`) - low_impact: The dataset is highly specific and not a commonly recognized benchmark; it is too local for general knowledge reuse.
- [concept] CSI-M (Mean Critical Success Index) (`csi-m-critical-success-index-for-heavy-rainfall`) - not_reusable: CSI-M is a standard meteorological evaluation metric, not a novel reusable methodological concept from this paper.
- [concept] Dynamic Time Warping (DTW) Reduction (`dtw-dynamic-time-warping-reduction`) - subcomponent_of_broader_mechanism: DTW is a general sequence similarity measure, and its reduction is the *result* of the novel method, not the novel method itself.

## Links

- [Abstract](https://arxiv.org/abs/2603.25046)
- [PDF](https://arxiv.org/pdf/2603.25046)

