---
# CSL-compatible fields
title: "EMG-FM-Bench: A Comprehensive Benchmark for Foundation Model Transfer and Adaptation on Electromyography"
author:
  - literal: "TianhaoWu"
  - literal: "XuWu"
  - literal: "AmirmohammadRadmehr"
  - literal: "JiaweiYu"
  - literal: "YiWu"
  - literal: "PhucNguyen"
  - literal: "JianLiu"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.06450"

# Custom fields
paper_id: "2610.06450"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "few-shot-learning"
  - "fine-tuning"
  - "pre-training"
  - "multimodal"
architectures:
  []
datasets:
  - "EMG-FM-Bench"
concept_slugs:
  - "emg-fm-bench"
dataset_slugs:
  - "emg-fm-bench"
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:41:44Z"
created_at: "2026-10-08T11:41:44Z"
---

# EMG-FM-Bench: A Comprehensive Benchmark for Foundation Model Transfer and Adaptation on Electromyography

**Authors**: TianhaoWu, XuWu, AmirmohammadRadmehr, JiaweiYu, YiWu, PhucNguyen, JianLiu
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.06450](https://arxiv.org/abs/2610.06450)

## Summary

This paper introduces EMG-FM-Bench, a comprehensive benchmark unifying 20 public datasets and over 1 million electromyography (EMG) segments to evaluate the transferability and adaptation of nine pretrained time-series foundation models. The study investigates frozen versus full fine-tuning, pretraining versus training from scratch, few-shot user adaptation, and cross-task generalization. Findings reveal that pretraining benefits are non-universal, cross-user generalization remains challenging even with few-shot adaptation, and performance is highly correlated across limb and continuous decoding tasks.

## Key Contributions

- Introduces EMG-FM-Bench, a systematic benchmark unifying 20 public datasets with over 1 million electromyography segments.
- Evaluates nine pretrained foundation models across freezing, full fine-tuning, training from scratch, few-shot user generalization, and multi-task transfer.
- Shows that pretraining benefits vary substantially across models and are not universal for electromyography data.
- Demonstrates that five-shot adaptation improves macro-F1 in 70.2% of combinations but only partially recovers inter-user performance drops.

## Limitations

Future work involves expanding architectures and exploring more advanced domain adaptation techniques to bridge the cross-user performance gap.

## Open Questions & Future Work

- [[continuous-emg-decoding-generalization]]

## Key Concepts

- [[emg-fm-bench]]: A systematic benchmark unifying 20 public datasets to study foundation model transfer and adaptation on electromyography.

## Archivist Review

Approved the EMG-FM-Bench benchmark and its corresponding dataset, along with an open question on continuous EMG decoding generalization, adhering strictly to the policy of keeping only high-impact, reusable evaluation artifacts.

### Approved Concepts
- EMG-FM-Bench: It provides the first comprehensive benchmark unifying 20 public datasets to evaluate foundation model transferability and adaptation on electromyography signals.

### Approved Open Questions
- Generalization to Continuous EMG Decoding: Crucial for establishing whether task-consistency findings in foundation model adaptation hold universally across all types of continuous neuromuscular decoding or if they are restricted to specific task formulations.

### Rejected Candidates
- [concept] Electromyography Transfer Learning (`electromyography-transfer-learning`) - not_novel: Too broad and standard as a machine learning concept.

## Datasets

- [[emg-fm-bench]]

## Links

- [Abstract](https://arxiv.org/abs/2610.06450)
- [PDF](https://arxiv.org/pdf/2610.06450)

