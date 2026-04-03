---
# CSL-compatible fields
title: "IMPACT: Influence Modeling for Open-Set Time Series Anomaly Detection"
author:
  - literal: "Xiaohui Zhou"
  - literal: "Yijie Wang"
  - literal: "Hongzuo Xu"
  - literal: "Weixuan Liang"
  - literal: "Xiaoli Li"
  - literal: "Guansong Pang"
issued:
  date-parts:
    - [2026, 3, 31]
url: "https://arxiv.org/abs/2603.29183"

# Custom fields
paper_id: "2603.29183"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "influence-based-anomaly-generation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-03T06:06:40Z"
created_at: "2026-04-03T06:06:40Z"
---

# IMPACT: Influence Modeling for Open-Set Time Series Anomaly Detection

**Authors**: Xiaohui Zhou, Yijie Wang, Hongzuo Xu, Weixuan Liang, Xiaoli Li, Guansong Pang
**Date**: 2026-03-31
**Paper ID**: [openalex:2603.29183](https://arxiv.org/abs/2603.29183)

## Summary

IMPACT is a framework designed for open-set time series anomaly detection that addresses the failure of current augmentation techniques to maintain temporal coherence. By learning influence functions, the model identifies the impact of training samples, enabling the generation of realistic unseen anomalies and the decontamination of training sets from unlabeled noise. Extensive evaluation confirms that IMPACT consistently outperforms state-of-the-art baselines under various OSAD settings and contamination levels.

## Key Contributions

- Introduces IMPACT, a framework that utilizes influence functions to estimate the importance of training samples for time-series anomaly detection.
- Leverages influence scores to generate semantically divergent and realistic unseen anomalies, overcoming the limitations of standard time-series data augmentation.
- Develops a method to repurpose highly influential samples for supervised anomaly decontamination, effectively mitigating the impact of training data contamination.

## Open Questions & Future Work

- [[generating-high-quality-pseudo-anomalies]]
- [[proactive-anomaly-decontamination]]

## Key Concepts

- [[influence-based-anomaly-generation]]: An anomaly generation technique that uses influence scores to synthesize realistic and semantically diverse anomalies for open-set time series anomaly detection.

## Archivist Review

I approved the core mechanism of influence-based anomaly generation rather than the framework itself to ensure reusability. I also approved two high-impact open questions regarding the generation of diverse pseudo-anomalies and proactive contamination mitigation, both of which are central challenges in open-set anomaly detection beyond this specific paper. No datasets were approved as none were specifically named as primary, novel benchmarks.

### Approved Concepts
- Influence-based Anomaly Generation: Shifts anomaly generation from heuristic/rule-based approaches to a data-driven process using influence functions, which is more robust for time series temporal dynamics.

### Approved Open Questions
- Generating High-Quality Pseudo Anomalies: The quality and diversity of pseudo-anomalies determine the generalization capability of open-set models to unseen failure modes.
- Proactive Training Data Decontamination: Proactive decontamination is essential for robust model training in real-world scenarios where perfectly clean datasets are unavailable.

### Rejected Candidates
- [concept] IMPACT (Influence Modeling for Open-Set Time Series Anomaly Detection) (`impact-influence-modeling-for-open-set-time-series-anomaly-detection`) - subcomponent_of_broader_mechanism: The name is a specific framework title; the underlying mechanism of influence-based generation is more reusable and appropriate for the vault.

## Links

- [Abstract](https://arxiv.org/abs/2603.29183)
- [PDF](https://arxiv.org/pdf/2603.29183)

