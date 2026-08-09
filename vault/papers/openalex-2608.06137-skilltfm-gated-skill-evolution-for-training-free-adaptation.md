---
# CSL-compatible fields
title: "SkillTFM: Gated Skill Evolution for Training-Free Adaptation of Tabular Foundation Models"
author:
  - literal: "Yi He"
  - literal: "Zhengkang Guan"
  - literal: "Anpeng Wu"
  - literal: "Peng Cui"
  - literal: "Fei Wu"
  - literal: "Kun Kuang"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.06137"

# Custom fields
paper_id: "2608.06137"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "pre-training"
  - "fine-tuning"
  - "agent"
  - "autonomous-agent"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:41:42Z"
created_at: "2026-08-09T05:41:42Z"
---

# SkillTFM: Gated Skill Evolution for Training-Free Adaptation of Tabular Foundation Models

**Authors**: Yi He, Zhengkang Guan, Anpeng Wu, Peng Cui, Fei Wu, Kun Kuang
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.06137](https://arxiv.org/abs/2608.06137)

## Summary

Tabular foundation models (TFMs) struggle with distribution shifts and heterogeneous feature semantics without costly fine-tuning. To address this, the authors propose SkillTFM, a training-free adaptation system that replaces parameter updates with the gated evolution of agentic skills. SkillTFM utilizes a verifiable skill bank coupling boundary evidence identification with gated skill evolution to retrieve and extend reusable skills. Experiments on simulated boundaries and electricity-price forecasting show substantial improvements in AUC and generalization across TFM backbones.

## Key Contributions

- Proposes SkillTFM, a training-free adaptation framework for tabular foundation models via gated evolution of agentic skills.
- Implements a verifiable and extensible skill bank coupling boundary evidence identification with gated skill evolution.
- Improves AUC by 0.128--0.142 and raises nonlinear-boundary AUC from 0.699 to 0.898 on electricity-price forecasting and simulated settings.

## Limitations

Evaluated primarily on boundary settings and electricity-price forecasting tasks.

## Archivist Review

Evaluated SkillTFM as a paper-specific system framework rather than a generalizable temporal or foundational ML mechanism. Adhering to strict scarcity and novelty standards, no concepts, open questions, or datasets were approved for the permanent knowledge vault.

### Rejected Candidates
- [concept] SkillTFM (`skilltfm`) - paper_local: Represents a paper-specific system name and implementation rather than a broadly reusable methodological primitive for the vault.

## Links

- [Abstract](https://arxiv.org/abs/2608.06137)
- [PDF](https://arxiv.org/pdf/2608.06137)

