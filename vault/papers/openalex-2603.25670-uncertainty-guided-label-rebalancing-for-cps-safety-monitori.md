---
# CSL-compatible fields
title: "Uncertainty-Guided Label Rebalancing for CPS Safety Monitoring"
author:
  - literal: "John Ayotunde"
  - literal: "Qinghua Xu"
  - literal: "Guancheng Wang"
  - literal: "Lionel C. Briand"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25670"

# Custom fields
paper_id: "2603.25670"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "safety-monitoring"
  - "evaluation"
  - "robustness"
  - "mlp"
architectures:
  - "mlp"
datasets:
  - "UAV benchmark"
concept_slugs:
  - "uncertainty-guided-label-rebalancing-ulnr"
  - "gatedmlp-behavioral-uncertainty-predictor"
dataset_slugs:
  - "uav-benchmark"
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:09:13Z"
created_at: "2026-03-29T06:09:13Z"
---

# Uncertainty-Guided Label Rebalancing for CPS Safety Monitoring

**Authors**: John Ayotunde, Qinghua Xu, Guancheng Wang, Lionel C. Briand
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25670](https://arxiv.org/abs/2603.25670)

## Summary

This paper addresses extreme class imbalance in time-series safety monitoring for Cyber-Physical Systems (CPSs) by proposing U-Balance. U-Balance first utilizes a novel GatedMLP-based uncertainty predictor to estimate the behavioral uncertainty associated with each telemetry window. The core contribution is the uncertainty-guided label rebalancing (uLNR) mechanism, which uses this score to probabilistically re-label highly uncertain 'safe' instances as 'unsafe', effectively augmenting the minority class with informative boundary samples. Evaluated on a large-scale UAV benchmark with a 46:1 imbalance, U-Balance achieved a significant F1 score improvement of 14.3 percentage points over baselines while maintaining inference efficiency.

## Key Contributions

- Proposed U-Balance, a supervised approach leveraging behavioral uncertainty to rebalance extremely imbalanced datasets for CPS safety monitoring.
- Introduced a GatedMLP-based uncertainty predictor to summarize telemetry windows into a distributional kinematic feature and output an uncertainty score.
- Developed the uncertainty-guided label rebalancing (uLNR) mechanism, which probabilistically relabels highly uncertain safe samples as unsafe, enriching the minority class without synthetic data generation.
- Achieved a 14.3 percentage point F1 score improvement over the strongest baseline (0.806 F1) on a large-scale UAV benchmark with a 46:1 imbalance ratio.

## Limitations

The paper relies on a large-scale UAV benchmark and the correlation between behavioral uncertainty and safety outcomes is only described as 'moderate' although significant. Further generalization to other CPS types is implied but not demonstrated.

## Open Questions & Future Work

- [[generalizability-across-cps-domains]]
- [[impact-of-uncertainty-estimation-techniques]]

## Key Concepts

- [[uncertainty-guided-label-rebalancing-ulnr]]: A mechanism that probabilistically relabels safe-labeled time-series windows with high behavioral uncertainty as unsafe to augment the minority class for safety monitoring.
- [[gatedmlp-behavioral-uncertainty-predictor]]: A GatedMLP model trained to summarize time-series telemetry into distributional kinematic features and output a single behavioral uncertainty score.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 2 concept(s), 2 open question(s), and 1 dataset(s), with 1 rejected candidate note(s).

### Approved Concepts
- Uncertainty-Guided Label Rebalancing (uLNR): It is the core novel technique used to address extreme class imbalance by re-labeling uncertain 'safe' examples as 'unsafe' to enrich the minority class.
- Behavioral Uncertainty Predictor (GatedMLP): This custom predictor is essential for quantifying the uncertainty that drives the label rebalancing, making the overall method functional.

### Approved Open Questions
- Evaluate U-Balance on other CPSs: Assessing generalizability across different CPS domains (e.g., submarines vs. UAVs) is crucial to confirm that the uncertainty-guided rebalancing technique is robust to varying sensor types and operational physics, rather than being overfit to UAV telemetry.
- Investigate alternative uncertainty estimation: Understanding the relationship between the fidelity of uncertainty estimation methods (like MC Dropout or Deep Ensembles) and the resulting data rebalancing effectiveness is important for optimizing the overall system pipeline, especially since the core contribution relies on high-quality uncertainty scores.

### Rejected Candidates
- [concept] Behavioral Uncertainty Definition (`behavioral-uncertainty-definition`) - generic: The definition of behavioral uncertainty is too generic/contextual to warrant its own archival note, as the core contribution lies in *using* the score, not the definition itself.

## Datasets

- [[uav-benchmark]]

## Links

- [Abstract](https://arxiv.org/abs/2603.25670)
- [PDF](https://arxiv.org/pdf/2603.25670)

