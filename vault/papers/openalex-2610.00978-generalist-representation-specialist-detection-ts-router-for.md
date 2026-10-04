---
# CSL-compatible fields
title: "Generalist Representation, Specialist Detection: TS-Router for Time-Series Anomaly Detection"
author:
  - literal: "Tian Lan"
  - literal: "Yifei Gao"
  - literal: "Yimeng Lu"
  - literal: "Xuming An"
  - literal: "Meng Wang"
  - literal: "Yue Pan"
  - literal: "Wenjun He"
  - literal: "Chenghao Liu"
  - literal: "Chen Zhang"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.00978"

# Custom fields
paper_id: "2610.00978"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "foundation-model"
  - "pre-training"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:48:30Z"
created_at: "2026-10-04T10:48:30Z"
---

# Generalist Representation, Specialist Detection: TS-Router for Time-Series Anomaly Detection

**Authors**: Tian Lan, Yifei Gao, Yimeng Lu, Xuming An, Meng Wang, Yue Pan, Wenjun He, Chenghao Liu, Chen Zhang
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.00978](https://arxiv.org/abs/2610.00978)

## Summary

Time-series anomaly detection struggles to generalize across heterogeneous temporal dynamics when coupled with fixed scoring mechanisms. To address this, the authors propose TS-Router, a framework that uses pretrained foundation model representations to estimate the relative competence of different anomaly detectors and dynamically select suitable specialists. By leveraging soft supervision derived from simulated tasks, TS-Router performs routing without target anomaly labels and achieves top overall performance across 16 real-world benchmarks.

## Key Contributions

- Proposes TS-Router, a generalist-representation specialist-detection framework that uses time-series foundation models to route and coordinate heterogeneous anomaly detectors based on estimated relative competence.
- Derives soft competence supervision from specialists' relative performance on labeled simulated tasks to eliminate the need for target task labels.
- Achieves the best overall average rank across 16 real-world time-series anomaly detection benchmarks using four complementary evaluation metrics.

## Archivist Review

No concepts or open questions met the strict novelty and reusability standards required for the permanent vault.

### Rejected Candidates
- [open_question] Cross-Domain Competence Transfer Limits (`cross-domain-transfer-limits-tsad`) - duplicate_existing: Too broad and similar to general sim-to-real transfer questions already covered in the vault.
- [open_question] Multivariate Cross-Variable Interaction Modeling (`multivariate-cross-variable-interactions-routing`) - not_novel: Standard future work extension for multivariate handling in time-series anomaly detection.

## Links

- [Abstract](https://arxiv.org/abs/2610.00978)
- [PDF](https://arxiv.org/pdf/2610.00978)

