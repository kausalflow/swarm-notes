---
# CSL-compatible fields
title: "ARFBench: Benchmarking Time Series Question Answering Ability for Software Incident Response"
author:
  - literal: "Stephan Xie"
  - literal: "Ben Cohen"
  - literal: "Mononito Goswami"
  - literal: "Jun-Hong Shen"
  - literal: "Emaad Khwaja"
  - literal: "Chenghao Liu"
  - literal: "David Asker"
  - literal: "Othmane Abou-Amal"
  - literal: "Ameet Talwalkar"
issued:
  date-parts:
    - [2026, 4, 23]
url: "https://arxiv.org/abs/2604.21199"

# Custom fields
paper_id: "2604.21199"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "multimodal"
  - "vision-language-model"
  - "benchmark"
  - "dataset"
  - "question-answering"
  - "time-series"
architectures:
  []
datasets:
  - "ARFBench"
concept_slugs:
  - "time-series-question-answering-tsqa"
dataset_slugs:
  - "arfbench"
skill: "TimeSeriesSkill"
processed_at: "2026-04-26T06:54:13Z"
created_at: "2026-04-26T06:54:13Z"
---

# ARFBench: Benchmarking Time Series Question Answering Ability for Software Incident Response

**Authors**: Stephan Xie, Ben Cohen, Mononito Goswami, Jun-Hong Shen, Emaad Khwaja, Chenghao Liu, David Asker, Othmane Abou-Amal, Ameet Talwalkar
**Date**: 2026-04-23
**Paper ID**: [openalex:2604.21199](https://arxiv.org/abs/2604.21199)

## Summary

This paper introduces ARFBench, a novel benchmark designed to evaluate Time Series Question-Answering (TSQA) capabilities of multimodal foundation models in the context of software incident response. The study assesses various LLMs, VLMs, and time series foundation models, revealing that frontier VLMs currently outperform dedicated time series approaches. The authors further propose a hybrid TSFM-VLM model and demonstrate that human-AI collaboration can reach superhuman performance levels on incident telemetry analysis.

## Key Contributions

- Introduces ARFBench, a new TSQA benchmark containing 750 questions over 142 time series from 63 production software incidents.
- Demonstrates that frontier vision-language models (VLMs) significantly outperform existing time series foundation model baselines on TSQA tasks.
- Presents a TSFM + VLM hybrid architecture that achieves performance comparable to frontier models via post-training on small synthetic and real-world datasets.
- Establishes a 'model-expert oracle' framework, showing that model-human collaboration achieves 87.2% accuracy, significantly higher than individual model performance.

## Key Concepts

- [[time-series-question-answering-tsqa]]: A paradigm where natural language queries are used to reason about and infer properties from time series data.

## Archivist Review

I approved Time Series Question-Answering (TSQA) as a new concept because it captures the emerging task paradigm introduced in the paper. I approved ARFBench as a dataset rather than a concept to adhere to the policy of not creating duplicate entries. No open questions were approved as the candidates provided were insufficient.

### Approved Concepts
- Time Series Question-Answering (TSQA): It defines an emerging paradigm at the intersection of multimodal foundation models and time series analysis.

### Rejected Candidates
- [concept] ARFBench (`arfbench`) - duplicate_existing: This is already being approved as a dataset; it does not need to be a concept entry as well.

## Datasets

- [[arfbench]]

## Links

- [Abstract](https://arxiv.org/abs/2604.21199)
- [PDF](https://arxiv.org/pdf/2604.21199)

