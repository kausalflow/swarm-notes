---
# CSL-compatible fields
title: "Towards Robust Time Series Learning via Capacity-Centric Modulation"
author:
  - literal: "Siru Zhong"
  - literal: "Senzhang Wang"
  - literal: "James Tin-Yau Kwok"
  - literal: "Yuxuan Liang"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.39489"

# Custom fields
paper_id: "2609.39489"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "regularization"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "capacity-centric-modulation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:07:38Z"
created_at: "2026-10-03T10:07:38Z"
---

# Towards Robust Time Series Learning via Capacity-Centric Modulation

**Authors**: Siru Zhong, Senzhang Wang, James Tin-Yau Kwok, Yuxuan Liang
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.39489](https://arxiv.org/abs/2609.39489)

## Summary

This paper introduces Capacity-Centric Modulation (CCM) and its instantiation SACM, a task-agnostic framework that addresses sample-level reliability heterogeneity in time series learning by exploiting spectral sparsity to assign sample-wise dropout probabilities along internal activation paths. SACM integrates seamlessly into existing backbones without architectural modification and maintains a deterministic inference pipeline with zero test-time overhead. Extensive evaluations across 301 dataset-backbone pairs for forecasting, classification, and anomaly detection demonstrate significant performance improvements over standard training baselines.

## Key Contributions

- Proposes Capacity-Centric Modulation (CCM) as a sample-adaptive regularization principle to handle sample-level reliability heterogeneity.
- Introduces SACM (Sample-Adaptive Capacity Modulation), a task-agnostic framework assigning sample-wise dropout probabilities along internal activation paths using spectral sparsity.
- Reduces forecasting MSE by 6.7% and improves classification accuracy and anomaly detection F1 by 3.04% and 17.05% respectively across 301 dataset-backbone pairs with zero test-time overhead.

## Open Questions & Future Work

- [[hybrid-time-frequency-filtering]]

## Key Concepts

- [[capacity-centric-modulation]]: A sample-adaptive regularization principle that modulates internal capacity based on spectral sparsity to handle sample-level reliability heterogeneity.

## Archivist Review

Approved the overarching regularization principle 'Capacity-Centric Modulation' and the open question regarding hybrid time-frequency filtering. Adhered strictly to the skill context and review guidelines by approving only high-impact, reusable concepts and non-trivial open questions while omitting routine datasets.

### Approved Concepts
- Capacity-Centric Modulation: CCM provides a novel sample-adaptive regularization principle that exploits spectral sparsity to modulate internal capacity via dropout probabilities.

### Approved Open Questions
- Hybrid Time-Frequency Filtering: Crucial for extending spectral-based modulation to non-harmonic and complex temporal signals without filtering out valid high-frequency phenomena.

## Links

- [Abstract](https://arxiv.org/abs/2609.39489)
- [PDF](https://arxiv.org/pdf/2609.39489)

