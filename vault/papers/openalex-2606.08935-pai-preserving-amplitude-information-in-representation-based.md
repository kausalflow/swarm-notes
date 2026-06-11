---
# CSL-compatible fields
title: "PAI: Preserving Amplitude Information in Representation-Based Time-Series Anomaly Detection"
author:
  - literal: "Kang Zhang"
  - literal: "Wei Jian Lau"
  - literal: "Shoushou Ren"
  - literal: "Dong Lin"
  - literal: "Joon Son Chung"
  - literal: "Chuanhao Sun"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.08935"

# Custom fields
paper_id: "2606.08935"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  - "TSB-AD-U-Eva"
  - "TAB UV"
concept_slugs:
  - "pai-preserving-amplitude-information"
dataset_slugs:
  - "tsb-ad-u-eva"
  - "tab-uv"
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:07:24Z"
created_at: "2026-06-11T09:07:24Z"
---

# PAI: Preserving Amplitude Information in Representation-Based Time-Series Anomaly Detection

**Authors**: Kang Zhang, Wei Jian Lau, Shoushou Ren, Dong Lin, Joon Son Chung, Chuanhao Sun
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.08935](https://arxiv.org/abs/2606.08935)

## Summary

Representation-based time-series anomaly detection methods often overlook critical amplitude information, leading to degraded performance on amplitude-sensitive anomalies. The authors introduce PAI, an anomaly scoring scheme that augments these methods with a diagnostic module and a point-wise score fusion function to explicitly recover and utilize amplitude data. Evaluations on standard benchmarks demonstrate that PAI consistently improves various representation-based baselines, with PaAno+PAI outperforming previous state-of-the-art methods by 15%.

## Key Contributions

- Identifies that existing representation-based time-series anomaly detection methods suffer from amplitude-agnostic learned embeddings.
- Proposes PAI, a two-module scoring scheme (diagnostic and augmentation) to explicitly retain amplitude information.
- Demonstrates significant performance gains across diverse baselines, achieving VUS-PR improvements of 98.4% and 36.8% on TSB-AD-U-Eva and TAB UV datasets, respectively.

## Open Questions & Future Work

- [[multivariate-pai-extension]]

## Key Concepts

- [[pai-preserving-amplitude-information]]: An anomaly scoring scheme that combines a diagnostic module and score augmentation to explicitly incorporate amplitude information into representation-based anomaly detectors.

## Archivist Review

I have approved the PAI scoring scheme as a reusable plug-and-play augmentation method for time-series anomaly detection and the identified limitation regarding its univariate restriction in multivariate contexts. The TSB-AD-U-Eva and TAB UV datasets are approved as they serve as the primary evaluation benchmarks for this framework. Other candidate ideas were rejected as they represent local implementation details or are redundant.

### Approved Concepts
- PAI (Preserving Amplitude Information): Addresses a systemic limitation in representation-based anomaly detection where learned embeddings are often amplitude-agnostic.

### Approved Open Questions
- Multivariate PAI Extension: Most real-world anomaly detection applications involve multivariate data; therefore, a method limited to univariate series has significant practical constraints.

### Rejected Candidates
- [dataset] TSB-AD-U-Eva Dataset (`tsb-ad-u-eva-dataset`) - duplicate_existing: The dataset is already captured in the approved list; no separate note needed for the dataset label.

## Datasets

- [[tsb-ad-u-eva]]
- [[tab-uv]]

## Links

- [Abstract](https://arxiv.org/abs/2606.08935)
- [PDF](https://arxiv.org/pdf/2606.08935)

