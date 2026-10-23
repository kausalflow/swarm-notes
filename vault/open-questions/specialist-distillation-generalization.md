---
created_at: '2026-10-23T09:39:48Z'
source_papers:
- '[[openalex-2610.28602-turning-ts2vec-into-a-foundation-model-for-time-series-class]]'
title: Generalization of Specialist Distillation
---

**Background:** Time series foundation models typically rely on specialized architectures and multi-view tokenizers to capture both normalized shape and absolute amplitude information.

**Question / Future Work:** Investigate whether specialist distillation frameworks can effectively generalize to alternative backbone architectures and tokenizer designs beyond convolutional networks for time series foundation models.

**Why It Matters:** Determining whether specialist distillation is architecture-agnostic helps establish it as a universal pre-training paradigm for time series representation learning.

**Evidence:** Evaluation is limited to UCR and UEA, and whether specialist distillation generalizes to other backbones and tokenizer designs remains open.