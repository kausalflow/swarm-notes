---
# CSL-compatible fields
title: "Efficient and Interpretable Body-Based Emotion Recognition with Lightweight Temporal Convolutional Networks"
author:
  - literal: "Christian Arzate Cruz"
  - literal: "Stefanos Gkikas"
  - literal: "Houshyar Asadi"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2607.20820"

# Custom fields
paper_id: "2607.20820"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "convolutional-neural-network"
  - "emotion-analysis"
  - "interpretability"
  - "efficient-transformer"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-26T07:30:36Z"
created_at: "2026-07-26T07:30:36Z"
---

# Efficient and Interpretable Body-Based Emotion Recognition with Lightweight Temporal Convolutional Networks

**Authors**: Christian Arzate Cruz, Stefanos Gkikas, Houshyar Asadi
**Date**: 2026-07-23
**Paper ID**: [openalex:2607.20820](https://arxiv.org/abs/2607.20820)

## Summary

This paper investigates whether lightweight temporal convolutional networks (TCNs) can replace computationally heavy graph-based models for body-based emotion recognition. Evaluating models on the DIEM-A dataset, the authors find that a base TCN achieves comparable accuracy and macro-F1 to a graph-based baseline while offering significantly reduced parameter count and a 12.5x speedup in inference latency. Furthermore, region-specific ablation and saliency analyses reveal that upper-body motion dominates emotion cues, with utility varying across distinct emotional states.

## Key Contributions

- Demonstrated that lightweight TCNs achieve competitive body-based emotion recognition performance (within 1.58 accuracy points and 1.25 macro-F1 of a G-TSG baseline) while using 79.18% fewer parameters and 12.5x lower inference latency.
- Evaluated model behavior and interpretability across body regions using region-specific TCN models, zero-based occlusion, and gradient saliency.
- Identified that upper-body motion provides the strongest standalone regional cue for emotion classification, and that regional utility varies by emotion category.

## Archivist Review

Applied strict selectivity filters. The paper investigates temporal convolutional networks for body-based emotion recognition on a specific dataset (DIEM-A). No novel reusable forecasting or time-series modeling concepts qualified for vault admission, and the proposed open question is standard fairness/robustness future work boilerplate.

### Rejected Candidates
- [open_question] Cross-Cultural Robustness and Demographic Fairness (`cross-cultural-robustness-and-demographic-fairness-in-body-based-emotion-recognition`) - weak_evidence: Standard future-work boilerplate regarding fairness and demographic generalization without a specific methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.20820)
- [PDF](https://arxiv.org/pdf/2607.20820)

