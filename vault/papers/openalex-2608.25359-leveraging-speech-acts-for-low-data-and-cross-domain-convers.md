---
# CSL-compatible fields
title: "Leveraging Speech Acts for Low-Data and Cross-Domain Conversation Derailment Forecasting"
author:
  - literal: "Anran Yuan"
  - literal: "Christine De Kock"
  - literal: "Christopher Leckie"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.25359"

# Custom fields
paper_id: "2608.25359"
paper_source: "openalex"
domain: "nlp"
tags:
  - "language-model"
  - "text-classification"
  - "forecasting"
  - "robustness"
  - "dataset"
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
processed_at: "2026-08-28T16:59:52Z"
created_at: "2026-08-28T16:59:52Z"
---

# Leveraging Speech Acts for Low-Data and Cross-Domain Conversation Derailment Forecasting

**Authors**: Anran Yuan, Christine De Kock, Christopher Leckie
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.25359](https://arxiv.org/abs/2608.25359)

## Summary

Conversational derailment forecasting aims to predict when online discussions will escalate into hostility, but existing approaches struggle in low-data and cross-domain settings. This paper proposes modeling pragmatic representations of conversations by incorporating speech act information as an auxiliary learning signal alongside textual semantics. Experiments across three datasets demonstrate that this approach reduces lexical noise and improves forecasting performance, particularly under low-data and cross-domain conditions.

## Key Contributions

- Proposes modeling pragmatic representations of conversations using speech act information to reduce lexical noise and improve generalizability in conversational derailment forecasting.
- Utilizes speech act information as an auxiliary learning signal alongside textual semantics for dialogue moderation.
- Demonstrates improved performance across three datasets, particularly in low-data and cross-domain settings.

## Archivist Review

The paper investigates leveraging speech acts as auxiliary learning signals for conversational derailment forecasting in low-data and cross-domain settings. The proposed open questions are low-impact, paper-local future work directions regarding feature extraction costs and annotation quality rather than fundamental methodological bottlenecks. No permanent vaulted notes are warranted.

### Rejected Candidates
- [open_question] Cost-Effective Speech Act Extraction (`cost-effective-speech-act-extraction`) - low_impact: Paper-local future work direction on computational efficiency of LLM feature extraction.
- [open_question] Ground-Truth Speech Acts for Nuanced Intents (`ground-truth-speech-acts-nuanced-intents`) - low_impact: Paper-local empirical question about manual annotation quality vs LLM extraction.

## Links

- [Abstract](https://arxiv.org/abs/2608.25359)
- [PDF](https://arxiv.org/pdf/2608.25359)

