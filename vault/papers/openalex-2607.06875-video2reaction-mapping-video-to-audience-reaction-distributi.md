---
# CSL-compatible fields
title: "Video2Reaction: Mapping Video to Audience Reaction Distribution in the Wild"
author:
  - literal: "Trang Nguyen"
  - literal: "Sidong Zhang"
  - literal: "Shiv Shankar"
  - literal: "Gauri Jagatap"
  - literal: "Deepak Chandran"
  - literal: "Andrea Fanelli"
  - literal: "Madalina Fiterau"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.06875"

# Custom fields
paper_id: "2607.06875"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "vision-language-model"
  - "benchmark"
  - "dataset"
  - "llm"
  - "fine-tuning"
  - "zero-shot-learning"
architectures:
  []
datasets:
  - "video2reaction-dataset"
concept_slugs:
  - "two-stage-multi-agent-annotation-pipeline"
dataset_slugs:
  - "video2reaction-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:06:20Z"
created_at: "2026-07-11T07:06:20Z"
---

# Video2Reaction: Mapping Video to Audience Reaction Distribution in the Wild

**Authors**: Trang Nguyen, Sidong Zhang, Shiv Shankar, Gauri Jagatap, Deepak Chandran, Andrea Fanelli, Madalina Fiterau
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.06875](https://arxiv.org/abs/2607.06875)

## Summary

Video2Reaction is a new multimodal benchmark that maps movie segments to induced audience emotion distributions captured from social media. To address the challenge of labeling noisy, subjective emotional data at scale, the authors propose a two-stage multi-agent annotation pipeline leveraging open-source LLMs. Evaluation demonstrates that while standard foundation models underperform in zero-shot settings, fine-tuning enables state-of-the-art prediction of both dominant and full reaction distributions, though significant modeling gaps persist.

## Key Contributions

- Introduced Video2Reaction, a multimodal dataset of 10,000+ video segments mapped to audience emotional response distributions.
- Developed a two-stage multi-agent LLM pipeline that achieves 86% correctness in labeling subjective audience reactions.
- Established a baseline showing that foundation models require fine-tuning to accurately predict reaction distributions, with a residual 23% gap in Top-3 F1 performance.

## Limitations

The task remains challenging, with top-performing methods like LLaVA-Next achieving only 77% Top-3 F1, suggesting significant difficulty in capturing collective human emotional responses.

## Open Questions & Future Work

- [[long-tail-audience-reaction-prediction]]
- [[transfer-learning-affective-computing]]

## Key Concepts

- [[two-stage-multi-agent-annotation-pipeline]]: A multi-agent annotation framework using LLMs to transform subjective, noisy feedback into structured labels for audience reaction prediction.

## Archivist Review

I approved the multi-agent annotation pipeline as a reusable methodological contribution for labeling subjective data, and the dataset itself as a benchmark. I also approved two research questions that address the common bottleneck of class imbalance (long-tail) and the need for more systematic transfer learning strategies in affective computing, which are critical for the field. Other candidates were either duplicates or were incorporated into the approved items.

### Approved Concepts
- Two-stage multi-agent annotation pipeline: Demonstrates a cost-effective, high-accuracy method for generating structured ground-truth labels from subjective, noisy social media data using LLM agents.

### Approved Open Questions
- Addressing long-tail reaction distribution: Effective affective computing must move beyond dominant response prediction to capture the full spectrum of collective audience reactions.
- Optimizing foundation model transfer: Optimizing transfer learning reduces reliance on large-scale, human-annotated datasets for novel affective computing tasks.

### Rejected Candidates
- [dataset] Video2Reaction Dataset (`video2reaction-dataset`) - duplicate_existing: This dataset is approved in the approved_datasets field.

## Datasets

- [[video2reaction-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2607.06875)
- [PDF](https://arxiv.org/pdf/2607.06875)

