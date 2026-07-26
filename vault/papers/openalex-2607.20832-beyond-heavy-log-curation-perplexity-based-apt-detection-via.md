---
# CSL-compatible fields
title: "Beyond Heavy Log Curation: Perplexity-Based APT Detection via Unsupervised, Context-Augmented Language Models"
author:
  - literal: "Shoya Otsu"
  - literal: "Kei Suzuki"
  - literal: "Toshiaki Koike-Akino"
  - literal: "Jing Liu"
  - literal: "Ye Wang"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2607.20832"

# Custom fields
paper_id: "2607.20832"
paper_source: "openalex"
domain: "nlp"
tags:
  - "language-model"
  - "pre-training"
  - "anomaly-detection"
  - "unsupervised-learning"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-26T07:30:33Z"
created_at: "2026-07-26T07:30:33Z"
---

# Beyond Heavy Log Curation: Perplexity-Based APT Detection via Unsupervised, Context-Augmented Language Models

**Authors**: Shoya Otsu, Kei Suzuki, Toshiaki Koike-Akino, Jing Liu, Ye Wang
**Date**: 2026-07-23
**Paper ID**: [openalex:2607.20832](https://arxiv.org/abs/2607.20832)

## Summary

The authors propose CAPTAIN, an unsupervised, perplexity-based Advanced Persistent Threat (APT) detector that leverages pre-trained language models with minimal preprocessing. CAPTAIN encodes recent log history via an encoder and a Q-Former-style bridge, injecting compact context tokens into the decoder to ensure perplexity reflects temporal context while applying smoothing filters for stability. Across APT benchmarks, CAPTAIN matches strong baselines while drastically reducing the engineering costs associated with heavily curated preprocessing pipelines.

## Key Contributions

- Proposes CAPTAIN, an unsupervised, perplexity-based Advanced Persistent Threat (APT) detector using pre-trained language models with domain-agnostic preprocessing.
- Leverages an encoder model and a Q-Former-style bridge to encode recent history and inject compact context tokens into the decoder input for context-aware perplexity scoring.
- Applies smoothing filters to the perplexity time series to improve detection stability.
- Demonstrates competitive performance against strong existing baselines across APT-oriented benchmarks while requiring significantly less curated inputs.

## Archivist Review

The proposed concept (CAPTAIN) and open question are primarily focused on domain-specific security log analysis and APT detection rather than general machine learning, forecasting, or time series methodology. Therefore, both candidates are rejected to maintain strict vault quality and reusability standards.

### Rejected Candidates
- [concept] CAPTAIN (Context-Augmented Perplexity-based Threat Activity log detectIoN) (`captain`) - paper_local: Paper-local system architecture for log-based security threat detection rather than a general, broadly reusable machine learning primitive.
- [open_question] Adaptive Context Selection Strategies (`adaptive-context-selection-log-detection`) - low_impact: Domain-specific engineering question focused on log analysis and security systems rather than a core theoretical limitation in time series or general machine learning.

## Links

- [Abstract](https://arxiv.org/abs/2607.20832)
- [PDF](https://arxiv.org/pdf/2607.20832)

