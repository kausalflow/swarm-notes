---
# CSL-compatible fields
title: "Parameter-Efficient Adaptation of Time Series Foundation Models for Electrical Load Forecasting"
author:
  - literal: "Aliullah"
  - literal: "Julian Oelhaf"
  - literal: "Edouard Fouché"
  - literal: "Jessica Deuschel"
  - literal: "Christian Bergler"
  - literal: "Andreas Maier"
  - literal: "Siming Bayer"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.28200"

# Custom fields
paper_id: "2610.28200"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "language-model"
  - "pre-training"
  - "fine-tuning"
  - "lora"
  - "parameter-efficient-fine-tuning"
  - "peft"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:39:28Z"
created_at: "2026-10-23T09:39:28Z"
---

# Parameter-Efficient Adaptation of Time Series Foundation Models for Electrical Load Forecasting

**Authors**: Aliullah, Julian Oelhaf, Edouard Fouché, Jessica Deuschel, Christian Bergler, Andreas Maier, Siming Bayer
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.28200](https://arxiv.org/abs/2610.28200)

## Summary

This paper evaluates parameter-efficient adaptation strategies—specifically Low-Rank Adaptation (LoRA)—for adapting time series foundation models (MOIRAI 1.0 Large and Chronos-2) to electrical load forecasting across four aggregation levels. The study demonstrates that rank-16 LoRA achieves an average 7.5% reduction in normalized mean absolute error on MOIRAI while updating only 1% of the model parameters, capturing most of the performance gains of full fine-tuning. Furthermore, the findings highlight that while pretrained TSFMs outperform traditional baselines (seasonal naive, XGBoost), adaptation benefits are highly dependent on the target aggregation level and distribution shift settings.

## Key Contributions

- Compares pretrained inference, full fine-tuning, and LoRA across four electrical load aggregation levels using MOIRAI 1.0 Large and Chronos-2.
- Demonstrates that rank-16 LoRA on MOIRAI Large reduces normalized mean absolute error (NMAE) by 7.5% on average while updating only 1% of the model parameters.
- Shows that pretrained foundation models consistently outperform seasonal naive and XGBoost baselines across evaluated aggregation levels.
- Evaluates in-distribution and out-of-distribution performance to reveal that adaptation benefits vary by target series type.

## Limitations

Adaptation benefits vary by target, with the clearest gains observed for local-area series and several buildings rather than uniformly across all OOD settings.

## Open Questions & Future Work

- [[conditions-for-peft-in-tsfms]]

## Archivist Review

Approved the open question regarding the conditions and trade-offs for PEFT in time series foundation models, as it addresses a distinct unresolved methodological bottleneck in applying foundation models to hierarchical electrical load forecasting. Rejected concept candidates since the core technique (LoRA applied to time series models) is well-established and the paper focuses on an empirical evaluation rather than introducing a reusable foundational algorithm.

### Approved Open Questions
- Conditions for PEFT in TSFMs: Understanding the boundaries of when adaptation is beneficial prevents unnecessary computational overhead and guides optimal deployment strategies for time series foundation models across diverse power system hierarchies.

### Rejected Candidates
- [concept] Parameter-Efficient Adaptation of Time Series Foundation Models for Electrical Load Forecasting (`parameter-efficient-adaptation-electrical-load-forecasting`) - not_novel: Applying existing LoRA techniques to electrical load forecasting using pretrained models like MOIRAI and Chronos-2 is an application study rather than a novel standalone concept note.

## Links

- [Abstract](https://arxiv.org/abs/2610.28200)
- [PDF](https://arxiv.org/pdf/2610.28200)

