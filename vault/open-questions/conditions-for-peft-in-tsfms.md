---
created_at: '2026-10-23T09:39:28Z'
source_papers:
- '[[openalex-2610.28200-parameter-efficient-adaptation-of-time-series-foundation-mod]]'
title: Conditions for PEFT in TSFMs
---

**Background:** Time series foundation models provide strong zero-shot forecasting capabilities across diverse domains, but the precise conditions and trade-offs regarding when downstream adaptation or parameter-efficient fine-tuning is necessary remain unclear across electrical load aggregation levels and out-of-distribution transfer settings.

**Question / Future Work:** Investigate the exact conditions, target characteristics, and aggregation levels under which parameter-efficient fine-tuning (such as LoRA) or full fine-tuning outperforms strong pretrained zero-shot inference for time series foundation models, particularly in out-of-distribution transfer and complex building energy profiles.

**Why It Matters:** Understanding the boundaries of when adaptation is beneficial prevents unnecessary computational overhead and guides optimal deployment strategies for time series foundation models across diverse power system hierarchies.

**Evidence:** However, it remains unclear when PEFT is preferable to pretrained inference or full fine-tuning across electrical load aggregation levels, and whether adaptation gains transfer to unseen systems and buildings.