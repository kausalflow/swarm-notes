---
# CSL-compatible fields
title: "ViTs: Teaching Machines to See Time Series Anomalies Like Human Experts"
author:
  - literal: "Zexin Wang"
  - literal: "Changhua Pei"
  - literal: "Yang Liu"
  - literal: "Haonan Jiang"
  - literal: "Quan Zhou"
  - literal: "Haotian Si"
  - literal: "Huijuan Cui"
  - literal: "Jianhui Li"
  - literal: "Gaogang Xie"
  - literal: "Jingjing Li"
  - literal: "Dan Pei"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2510.04710"

# Custom fields
paper_id: "2510.04710"
paper_source: "openalex"
domain: "nlp"
tags:
  - "vlm"
  - "vision-language-model"
  - "anomaly-detection"
  - "time-series"
  - "zero-shot-learning"
  - "instruction-tuning"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "visual-time-series-representation-learning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:18:18Z"
created_at: "2026-04-12T06:18:18Z"
---

# ViTs: Teaching Machines to See Time Series Anomalies Like Human Experts

**Authors**: Zexin Wang, Changhua Pei, Yang Liu, Haonan Jiang, Quan Zhou, Haotian Si, Huijuan Cui, Jianhui Li, Gaogang Xie, Jingjing Li, Dan Pei
**Date**: 2026-04-09
**Paper ID**: [openalex:2510.04710](https://arxiv.org/abs/2510.04710)

## Summary

ViTs is a novel Vision-Language Model (VLM)-based framework that addresses the context-length limitations of LLMs in time series anomaly detection by converting KPI curves into visual representations. This approach preserves temporal dependencies while allowing for arbitrary inference lengths without retraining. To overcome the lack of aligned data, the authors use an evolutionary algorithm to generate training pairs and implement a systematic three-stage training pipeline. Results show that ViTs effectively leverages VLM capabilities for superior zero-shot anomaly detection and reasoning.

## Key Contributions

- Introduced ViTs, a VLM-based framework that enables 'train once, infer across scenarios' for time series anomaly detection by converting curves into visual representations.
- Developed a three-stage training pipeline (knowledge injection, anomaly detection, reasoning) to adapt VLMs for time series tasks.
- Employed an evolutionary algorithm to automatically synthesize high-quality image-text alignment data for time series anomaly detection.

## Open Questions & Future Work

- [[synthetic-to-real-tsad-generalization-gap]]

## Key Concepts

- [[visual-time-series-representation-learning]]: A paradigm where time series are converted into image data to leverage vision-based models for temporal analysis, effectively bypassing token context limits.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 1 concept(s), 1 open question(s), and 0 dataset(s), with 1 rejected candidate note(s).

### Approved Concepts
- Visual Time Series Representation Learning: It enables vision-language models to bypass sequence-length limitations by encoding temporal patterns into spatial structures, providing a distinct alternative to standard tokenization or sliding-window methods.

### Approved Open Questions
- Synthetic to Real TSAD Generalization: Relying on synthetic training data is a common strategy to circumvent data scarcity, but verifying and bridging the gap to real-world deployment is essential for reliable anomaly detection.

### Rejected Candidates
- [concept] ViTs Framework (`vits-framework`) - other: Renamed to a more descriptive concept name ('Visual Time Series Representation Learning') to emphasize the underlying mechanism rather than the specific paper-local framework name.

## Links

- [Abstract](https://arxiv.org/abs/2510.04710)
- [PDF](https://arxiv.org/pdf/2510.04710)

