---
# CSL-compatible fields
title: "SpiroLLM: Finetuning pretrained LLMs to understand spirogram time series with clinical validation in COPD reporting"
author:
  - literal: "Shuhao Mei"
  - literal: "Yao Long"
  - literal: "Xiaoyu Xiao"
  - literal: "Shan Cao"
  - literal: "Xiaobo Han"
  - literal: "Shijia Geng"
  - literal: "Jian‐Sheng Sun"
  - literal: "Yuxi Zhou"
  - literal: "Shenda Hong"
issued:
  date-parts:
    - [2026, 3, 24]
url: "https://arxiv.org/abs/2507.16145"

# Custom fields
paper_id: "2507.16145"
paper_source: "openalex"
domain: "medicine"
tags:
  - "multimodal"
  - "language-model"
  - "time-series"
  - "llm"
  - "medicine"
  - "decoder-only"
  - "evaluation"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "spiro-encoder"
  - "spiro-projector"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T15:43:46Z"
created_at: "2026-03-27T15:43:46Z"
---

# SpiroLLM: Finetuning pretrained LLMs to understand spirogram time series with clinical validation in COPD reporting

**Authors**: Shuhao Mei, Yao Long, Xiaoyu Xiao, Shan Cao, Xiaobo Han, Shijia Geng, Jian‐Sheng Sun, Yuxi Zhou, Shenda Hong
**Date**: 2026-03-24
**Paper ID**: [openalex:2507.16145](https://arxiv.org/abs/2507.16145)

## Summary

SpiroLLM is introduced as the first multimodal Large Language Model designed to interpret respiratory spirogram time series for Chronic Obstructive Pulmonary Disease (COPD) diagnosis and reporting. The model utilizes a novel framework where a SpiroEncoder extracts morphological features from the time series, which are then aligned with standard Pulmonary Function Test (PFT) numerical values via a SpiroProjector into a unified latent space consumable by an LLM backbone. Experiments on the UK Biobank dataset show SpiroLLM achieves a diagnostic AUROC of 0.8977 and exhibits significantly higher robustness when core data is missing compared to text-only baselines. This work establishes a new paradigm for creating interpretable and reliable clinical decision support systems by deeply integrating physiological signals with generative language models.

## Key Contributions

- Development of SpiroLLM, the first multimodal large language model capable of understanding and reasoning about respiratory spirogram time series data.
- Introduction of the SpiroEncoder and SpiroProjector to extract morphological features and align them with PFT numerical values in a unified latent space.
- Achieving a diagnostic AUROC of 0.8977 on COPD classification using spirogram analysis, demonstrating strong clinical performance.
- Demonstration of superior robustness against missing core data compared to text-only models, maintaining a 100% valid response rate.

## Limitations

The paper focuses specifically on COPD reporting; generalization to other respiratory diseases or medical time-series requires further testing. Clinical deployment requires rigorous prospective validation beyond the reported retrospective analysis.

## Open Questions & Future Work

- [[spiro-llm-demographic-generalization]]
- [[spiro-llm-prospective-clinical-assessment]]

## Key Concepts

- [[spiro-encoder]]: A dedicated component used to extract morphological features from spirogram time series data to enable LLM understanding.
- [[spiro-projector]]: A projection layer that aligns the morphological features extracted from the SpiroEncoder with standard PFT numerical values into a shared latent representation space.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 2 concept(s), 2 open question(s), and 0 dataset(s), with 1 rejected candidate note(s).

### Approved Concepts
- SpiroEncoder: It is the core component responsible for extracting meaningful morphological features from the spirogram time series data, which is essential for the multimodal integration.
- SpiroProjector: This module bridges the gap between the extracted time-series features and the LLM's input space, making the fusion of modalities explicit and unified.

### Approved Open Questions
- Verify demographic generalization: Lack of demographic diversity in training data limits the model's applicability and fairness across global populations, a critical consideration for clinical tools.
- Conduct prospective clinical pilot studies},{background:: Assessing the model's real-world impact on clinical efficiency and report utility via prospective testing is necessary to move from technical demonstration to validated clinical integration.

### Rejected Candidates
- [dataset] UK Biobank (UKB) (`uk-biobank-ukb`) - low_impact: The dataset is a standard, large-scale resource commonly used in biomedical research and does not possess unique methodological significance warranting a standalone vault entry.

## Links

- [Abstract](https://arxiv.org/abs/2507.16145)
- [PDF](https://arxiv.org/pdf/2507.16145)

