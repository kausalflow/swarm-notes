---
# CSL-compatible fields
title: "ProtoX-AD: Self-Explainable Time Series Anomaly Detection and Characterization"
author:
  - literal: "Aitor Sánchez-Ferrera"
  - literal: "Elisabeth Wetzer"
  - literal: "Kristoffer Wickstrøm"
  - literal: "Michael Kampffmeyer"
  - literal: "Robert Jenssen"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13277"

# Custom fields
paper_id: "2606.13277"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
  - "self-supervised-learning"
  - "interpretability"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "protox-ad-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:37:25Z"
created_at: "2026-06-14T08:37:25Z"
---

# ProtoX-AD: Self-Explainable Time Series Anomaly Detection and Characterization

**Authors**: Aitor Sánchez-Ferrera, Elisabeth Wetzer, Kristoffer Wickstrøm, Michael Kampffmeyer, Robert Jenssen
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13277](https://arxiv.org/abs/2606.13277)

## Summary

ProtoX-AD is a self-explainable framework for time series anomaly detection that builds upon transformation-based self-supervised learning. By learning interpretable prototypes within a transformation-aware latent space, the model identifies anomalies while simultaneously providing characterizations of their specific patterns. Experiments show that ProtoX-AD maintains competitive detection performance against black-box methods while offering superior semantic consistency in its explanations.

## Key Contributions

- ProtoX-AD achieves anomaly detection performance comparable to black-box self-supervised baselines while providing semantically meaningful, prototype-based explanations.
- The framework learns transformation-aware latent representations alongside interpretable prototypes to enable characterization of anomalous profiles.
- Systematic analysis of transformation design impact on the trade-off between detection performance and explainability.

## Open Questions & Future Work

- [[adaptive-transformation-learning-tsad]]

## Key Concepts

- [[protox-ad-framework]]: A self-explainable framework for time series anomaly detection that utilizes learned prototypes to characterize anomalous profiles.

## Archivist Review

I approved the ProtoX-AD framework as a distinct architectural approach for incorporating prototype-based interpretability into self-supervised anomaly detection. The open question regarding adaptive transformation learning was approved because it addresses a fundamental trade-off between domain-specific knowledge and model generality in self-supervised learning for time series. No datasets were approved as none were highlighted as specific, novel, or unique contributions.

### Approved Concepts
- ProtoX-AD Framework: It introduces a novel paradigm of combining prototype-based interpretability with self-supervised transformation-based anomaly detection.

### Approved Open Questions
- Adaptive transformation learning strategies: The trade-off between domain-specific knowledge and model generality is a fundamental bottleneck in self-supervised anomaly detection, and solving it would expand model applicability.

### Rejected Candidates
- [concept] ProtoX-AD Framework (`protox-ad-framework-2`) - duplicate_existing: Duplicate concept candidate already approved.

## Links

- [Abstract](https://arxiv.org/abs/2606.13277)
- [PDF](https://arxiv.org/pdf/2606.13277)

