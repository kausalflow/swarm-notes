---
# CSL-compatible fields
title: "LabelFusion-TS: Fusing Large Language Models, Transformer Encoders, and Financial Time Series for Monetary-Policy Stance Classification"
author:
  - literal: "Michael Schlee"
  - literal: "Fabian Lukassen"
  - literal: "Christoph Weisser"
issued:
  date-parts:
    - [2026, 8, 12]
url: "https://arxiv.org/abs/2608.11753"

# Custom fields
paper_id: "2608.11753"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "multimodal"
  - "text-classification"
  - "transformer"
  - "bert"
  - "fine-tuning"
  - "time-series"
architectures:
  - "encoder-only"
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-15T05:15:11Z"
created_at: "2026-08-15T05:15:11Z"
---

# LabelFusion-TS: Fusing Large Language Models, Transformer Encoders, and Financial Time Series for Monetary-Policy Stance Classification

**Authors**: Michael Schlee, Fabian Lukassen, Christoph Weisser
**Date**: 2026-08-12
**Paper ID**: [openalex:2608.11753](https://arxiv.org/abs/2608.11753)

## Summary

LabelFusion-TS is a multimodal financial text classification system that integrates fine-tuned RoBERTa encoders, prompted large language models, and time-series transformers to classify Federal Reserve communication as hawkish, dovish, or neutral. By combining textual features with preceding market time series through a voting network, the system achieves 70.2% weighted F1 on FOMC data from 2015-2022, outperforming text-only zero-shot LLMs. Furthermore, the approach demonstrates high sample efficiency, surpassing zero-shot performance with only 240 human labels.

## Key Contributions

- Proposes LabelFusion-TS, a multimodal architecture that fuses fine-tuned RoBERTa encoders, prompted LLMs, and time-series transformers to classify Federal Reserve monetary policy stances.
- Demonstrates that incorporating market time series alongside financial text improves classification performance, achieving 70.2% weighted F1 on FOMC communication from 2015-2022 compared to 64.1% for zero-shot LLMs.
- Shows data efficiency, proving that the fused multi-modal system can outperform zero-shot LLMs with as few as 240 human-labelled sentences by leveraging LLM-pre-trained text encoders.

## Limitations

Evaluated specifically on Federal Reserve (FOMC) communication and market series; broader applicability across different central banks and emerging markets remains to be explored.

## Archivist Review

The proposed concept describes a paper-specific system architecture (LabelFusion-TS) rather than a broadly reusable methodological primitive, and the open question is a standard application extension (testing the same idea on different financial tasks). Both are rejected to maintain strict vault selectivity.

### Rejected Candidates
- [concept] LabelFusion-TS (`labelfusion-ts`) - paper_local: This is a paper-specific system architecture combining specific modules (RoBERTa, LLM, time-series transformers) for a single NLP task, which lacks broader standalone conceptual reusability across machine learning research.
- [open_question] Multimodal Financial Text Classification Beyond Stance (`multimodal-financial-text-classification-beyond-stance`) - low_impact: This is a standard application-extension future work proposal rather than a foundational technical bottleneck or unresolved research mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2608.11753)
- [PDF](https://arxiv.org/pdf/2608.11753)

