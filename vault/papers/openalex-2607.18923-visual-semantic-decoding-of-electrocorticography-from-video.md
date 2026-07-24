---
# CSL-compatible fields
title: "Visual Semantic Decoding of Electrocorticography from Video Stimuli using End-to-End Deep Learning"
author:
  - literal: "Stella Ho"
  - literal: "Joel Villalobos"
  - literal: "Joseph West"
  - literal: "JingYang Liu"
  - literal: "Weijie Qi"
  - literal: "Haruhiko Kishima"
  - literal: "Ryohei Fukuma"
  - literal: "Takufumi Yanagisawa"
  - literal: "Sam E. John"
  - literal: "David B. Grayden"
issued:
  date-parts:
    - [2026, 7, 21]
url: "https://arxiv.org/abs/2607.18923"

# Custom fields
paper_id: "2607.18923"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "transformer"
  - "attention-mechanism"
  - "multimodal"
  - "time-series"
  - "interpretability"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-24T07:25:43Z"
created_at: "2026-07-24T07:25:43Z"
---

# Visual Semantic Decoding of Electrocorticography from Video Stimuli using End-to-End Deep Learning

**Authors**: Stella Ho, Joel Villalobos, Joseph West, JingYang Liu, Weijie Qi, Haruhiko Kishima, Ryohei Fukuma, Takufumi Yanagisawa, Sam E. John, David B. Grayden
**Date**: 2026-07-21
**Paper ID**: [openalex:2607.18923](https://arxiv.org/abs/2607.18923)

## Summary

This study investigates ECoG-based visual semantic decoding to predict visual categories from video stimuli using an end-to-end deep learning framework. Evaluating various neural network architectures and frequency bands, the authors find that a Transformer-based encoder with high-gamma inputs and mixup augmentation achieves robust performance despite having fewer than 50 training samples per category. Interpretability analyses reveal that the model leverages spectral, temporal, and cortical regions (e.g., early visual cortex, ventral stream, MT+ complex) aligned with known neuroscientific principles.

## Key Contributions

- Demonstrates an end-to-end deep learning framework for ECoG-based visual semantic decoding from dynamic video stimuli without handcrafted features.
- Identifies that a Transformer-based encoder utilizing high-gamma (80-150 Hz) inputs and mixup augmentation achieves effective decoding performance with fewer than 50 training samples per visual category.
- Shows through post-hoc analysis that the model relies on spectral, temporal, and cortical dimensions (such as early visual cortex, ventral stream, MT+ complex, and lateral temporal cortex) consistent with established neuroscience.

## Limitations

Evaluated on a limited dataset of 17 participants with drug-resistant epilepsy and fewer than 50 training samples per visual category.

## Archivist Review

The candidate open question focuses on multi-band fusion strategies in ECoG decoding, which represents standard incremental future work rather than an enduring technical bottleneck. No concepts or datasets qualified under the strict reusability criteria.

### Rejected Candidates
- [open_question] Advanced Multi-Band Fusion Strategies (`advanced-multi-band-fusion-strategies`) - low_impact: Standard future work suggestion regarding multi-band feature combination in neural decoding without a concrete methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.18923)
- [PDF](https://arxiv.org/pdf/2607.18923)

