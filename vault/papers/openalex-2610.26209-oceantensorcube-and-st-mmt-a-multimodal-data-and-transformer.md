---
# CSL-compatible fields
title: "OceanTensorCube and ST-MMT: A Multimodal Data and Transformer System for Seven-Day Forecasting of Pyropia Bleaching"
author:
  - literal: "Gwangjin Kim"
  - literal: "cheolyoung 장철용Jang"
  - literal: "Yosep Jo"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26209"

# Custom fields
paper_id: "2610.26209"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "multi-head-attention"
  - "multimodal"
  - "time-series"
  - "forecasting"
  - "spatiotemporal"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:44:49Z"
created_at: "2026-10-22T09:44:49Z"
---

# OceanTensorCube and ST-MMT: A Multimodal Data and Transformer System for Seven-Day Forecasting of Pyropia Bleaching

**Authors**: Gwangjin Kim, cheolyoung 장철용Jang, Yosep Jo
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26209](https://arxiv.org/abs/2610.26209)

## Summary

This paper introduces OceanTensorCube, a multimodal data alignment system, and ST-MMT, a 9.2-million-parameter spatiotemporal transformer designed for seven-day ahead forecasting of Pyropia bleaching in seaweed farming. Operating on a 30 m grid with 32 channels, ST-MMT uses hub-style multi-head cross-attention between variable groups to map a 14-day history to a bleaching probability. Evaluations show that a six-seed ensemble achieves a false-alarm rate below 3.5% while capturing all reported positives, though single models underperform compared to simple LSTMs unless ensembled.

## Key Contributions

- Introduced OceanTensorCube, aligning 32 multi-source channels on a 30 m grid for marine forecasting.
- Proposed ST-MMT, a 9.2-million-parameter spatiotemporal transformer featuring hub-style multi-head cross-attention for seven-day Pyropia bleaching prediction.
- Demonstrated a false-alarm rate of at most 3.5% with a six-seed ensemble while detecting all reported positives on validation data.
- Identified key operational limitations, including a steep skill drop as nutrient survey data ages and superior performance of single-variable LSTM baselines over single ST-MMT models.

## Limitations

Forecasting skill drops significantly as the quarterly nutrient survey data ages (ROC-AUC 0.94 at 30 days vs. 0.53 at 129 days), and single ST-MMT models underperform compared to single LSTM baselines unless ensembled.

## Archivist Review

The paper presents OceanTensorCube and ST-MMT for forecasting Pyropia bleaching. Since the submitted open question focuses specifically on nutrient survey freshness in seaweed aquaculture, it is too domain-specific and paper-local for our general ML/time-series vault. No concepts or datasets were proposed or met our strict scarcity and reusability standards.

### Rejected Candidates
- [open_question] Nutrient Survey Freshness Thresholds (`nutrient-survey-freshness-thresholds`) - paper_local: The question of survey freshness thresholds is domain-specific to seaweed aquaculture and nutrient decay, making it too narrow for our general machine learning and time-series forecasting vault.

## Links

- [Abstract](https://arxiv.org/abs/2610.26209)
- [PDF](https://arxiv.org/pdf/2610.26209)

