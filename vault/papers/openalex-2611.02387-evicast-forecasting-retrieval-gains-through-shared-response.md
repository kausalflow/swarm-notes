---
# CSL-compatible fields
title: "EviCast: Forecasting Retrieval Gains Through Shared Response Calibration"
author:
  - literal: "YiboWang"
  - literal: "JishengDang"
  - literal: "BimeiWang"
  - literal: "JiongpeiHou"
  - literal: "JingwenZhao"
  - literal: "WenjunMa"
  - literal: "FeiShen"
  - literal: "JunchengLi"
  - literal: "MengWang"
  - literal: "QiTian"
  - literal: "BinHu"
  - literal: "Tat-Seng Chua"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.02387"

# Custom fields
paper_id: "2611.02387"
paper_source: "openalex"
domain: "nlp"
tags:
  - "retrieval-augmented-generation"
  - "rag"
  - "language-model"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "evicast"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-05T12:52:08Z"
created_at: "2026-11-05T12:52:08Z"
---

# EviCast: Forecasting Retrieval Gains Through Shared Response Calibration

**Authors**: YiboWang, JishengDang, BimeiWang, JiongpeiHou, JingwenZhao, WenjunMa, FeiShen, JunchengLi, MengWang, QiTian, BinHu, Tat-Seng Chua
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.02387](https://arxiv.org/abs/2611.02387)

## Summary

EviCast is a novel framework for forecasting retrieval value in retrieval-augmented generation (RAG) pipelines without executing every candidate configuration. By combining a generator's shared response profile under controlled evidence states with offline evidence-state distributions, EviCast accurately predicts end-to-end net utility and confidence bounds. Experiments on HotpotQA and MuSiQue demonstrate high accuracy, significant reduction in diagnostic generation calls, and robust transfer capabilities.

## Key Contributions

- Introduces EviCast, a framework that forecasts retrieval value and net utility via interventional evidence-state decomposition and shared response calibration.
- Reduces diagnostic generation calls by 80% while correctly deciding all 14 HotpotQA retrieval configurations with a small forecast error of 2.75 F1 points.
- Proposes a topology-aware instantiation, EviCast-T, that captures evidence complementarity and correctly decides 16 out of 16 configurations on MuSiQue and HotpotQA, and 23 of 24 in prospective transfer.

## Limitations

None explicitly highlighted in the abstract.

## Open Questions & Future Work

- [[multimodal-iterative-rag-utility-forecasting]]

## Key Concepts

- [[evicast]]: A framework that forecasts retrieval value in retrieval-augmented generation through interventional evidence-state decomposition.

## Archivist Review

Approved EviCast as a reusable framework concept for RAG utility forecasting and the corresponding open question on extending it to iterative and multimodal setups. Routine dataset mentions were excluded to maintain vault scarcity.

### Approved Concepts
- EviCast: Core framework introduced for forecasting retrieval value in RAG pipelines without full execution.

### Approved Open Questions
- Utility Forecasting for Multimodal Iterative RAG: Expanding utility forecasting frameworks to dynamic, iterative, and multimodal RAG setups is critical for scaling deployment decision-making to complex reasoning tasks.

## Links

- [Abstract](https://arxiv.org/abs/2611.02387)
- [PDF](https://arxiv.org/pdf/2611.02387)

