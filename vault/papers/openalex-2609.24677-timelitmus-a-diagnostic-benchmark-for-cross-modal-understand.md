---
# CSL-compatible fields
title: "TimeLitmus: A Diagnostic Benchmark for Cross-Modal Understanding and Explanation Faithfulness in Event-Conditioned Time-Series Prediction"
author:
  - literal: "Jie Gong"
  - literal: "Maowei Jiang"
  - literal: "Zhiwei Liu"
  - literal: "Yankai Chen"
  - literal: "Guojun Xiong"
  - literal: "Xue Liu"
  - literal: "Min Peng"
  - literal: "Qianqian Xie"
  - literal: "Sophia Ananiadou"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24677"

# Custom fields
paper_id: "2609.24677"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "llm"
  - "language-model"
  - "benchmark"
  - "evaluation"
  - "interpretability"
  - "explainability"
  - "robustness"
architectures:
  []
datasets:
  - "timelitmus-dataset"
concept_slugs:
  - "timelitmus"
dataset_slugs:
  - "timelitmus-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:38:34Z"
created_at: "2026-09-24T09:38:34Z"
---

# TimeLitmus: A Diagnostic Benchmark for Cross-Modal Understanding and Explanation Faithfulness in Event-Conditioned Time-Series Prediction

**Authors**: Jie Gong, Maowei Jiang, Zhiwei Liu, Yankai Chen, Guojun Xiong, Xue Liu, Min Peng, Qianqian Xie, Sophia Ananiadou
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24677](https://arxiv.org/abs/2609.24677)

## Summary

The paper introduces TimeLitmus, a diagnostic benchmark designed to evaluate cross-modal understanding and explanation faithfulness in LLMs performing event-conditioned time-series prediction. Comprising 4,856 records across Finance and Traffic with controlled counterfactuals, contrastive interventions, and shortcut controls, the evaluation reveals that standard prediction accuracy drastically overstates models' true cross-modal reasoning capabilities and explanation faithfulness. Furthermore, human annotators significantly outperform LLMs on these rigorous diagnostics, highlighting persistent limitations in current multimodal forecasting models.

## Key Contributions

- Introduced TimeLitmus, a diagnostic benchmark comprising 4,856 evaluation records across Finance and Traffic featuring counterfactual interventions and explanation faithfulness tests.
- Demonstrated that standard prediction accuracy heavily overstates reliable cross-modal understanding, with Hard Paired Contrast correctness peaking at only 19.2% in Finance and 11.7% in Traffic across ten LLMs.
- Revealed severe explanation unfaithfulness, where models frequently cite manipulated temporal factors while their behavioral support remains below 22%.
- Showed that human annotators significantly outperform LLMs on controlled and hard-pair diagnostics, and that natural-only adaptation fails to yield consistent gains in controlled behavior.

## Limitations

The study focuses on evaluating current LLMs without providing a universal architectural remedy for unfaithful explanations or cross-modal reasoning failures.

## Open Questions & Future Work

- [[explanation-faithfulness-gap]]

## Key Concepts

- [[timelitmus]]: A diagnostic benchmark evaluating cross-modal understanding and explanation faithfulness in event-conditioned time-series prediction.

## Archivist Review

Approved the core benchmark concept 'TimeLitmus', the dataset 'timelitmus-dataset', and the open question on explanation faithfulness. Generic terms and broad subsets were rejected to maintain high vault standards.

### Approved Concepts
- TimeLitmus: It is the central methodological and evaluation contribution of the paper, providing controlled counterfactuals, contrastive interventions, and explanation faithfulness tests for event-conditioned time series.

### Approved Open Questions
- Bridging Explanation Faithfulness Gaps: Crucial for high-stakes domains where unfaithful or deceptive explanations create false confidence and can lead to severe real-world consequences.

## Datasets

- [[timelitmus-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2609.24677)
- [PDF](https://arxiv.org/pdf/2609.24677)

