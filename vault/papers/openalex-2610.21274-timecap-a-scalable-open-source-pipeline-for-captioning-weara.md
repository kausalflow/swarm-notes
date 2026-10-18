---
# CSL-compatible fields
title: "TimeCap: A Scalable Open-Source Pipeline for Captioning Wearable Health Time-Series Data"
author:
  - literal: "Max Rosenblattl"
  - literal: "Milana Gurbanova"
  - literal: "Karl Aurel Deck"
  - literal: "Narayan Schuetz"
  - literal: "Thomas Kaar"
  - literal: "Manuel Milling"
  - literal: "Nicolas Zumarraga"
  - literal: "Ning Wang"
  - literal: "Kelly W. Zhang"
  - literal: "Anders Johnson"
  - literal: "Robert Jakob"
  - literal: "Björn W. Schuller"
  - literal: "Elgar Fleisch"
  - literal: "Daniel Seung Kim"
  - literal: "Allan Lawrie"
  - literal: "Patrick Langer"
  - literal: "Maxwell A. Xu"
  - literal: "Euan Ashley"
  - literal: "Paul Schmiedmayer"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.21274"

# Custom fields
paper_id: "2610.21274"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "multimodal"
  - "language-model"
  - "dataset"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "timecap"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:12:49Z"
created_at: "2026-10-18T09:12:49Z"
---

# TimeCap: A Scalable Open-Source Pipeline for Captioning Wearable Health Time-Series Data

**Authors**: Max Rosenblattl, Milana Gurbanova, Karl Aurel Deck, Narayan Schuetz, Thomas Kaar, Manuel Milling, Nicolas Zumarraga, Ning Wang, Kelly W. Zhang, Anders Johnson, Robert Jakob, Björn W. Schuller, Elgar Fleisch, Daniel Seung Kim, Allan Lawrie, Patrick Langer, Maxwell A. Xu, Euan Ashley, Paul Schmiedmayer
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.21274](https://arxiv.org/abs/2610.21274)

## Summary

Time-Series Language Models (TSLMs) struggle due to a lack of reproducible, signal-grounded, text-annotated time-series corpora. To address this, the authors introduce TimeCap, an open deterministic captioning pipeline operating without language models to generate reproducible annotations. Applying TimeCap to the OpenMHC wearable dataset yields MHCap, a large open caption corpus covering millions of person-days. Training OpenTSLM on MHCap demonstrates improved performance on health-outcome prediction tasks compared to label-only baselines.

## Key Contributions

- Introduces TimeCap, an open deterministic captioning pipeline that operates directly on signals without large language models to ensure reproducibility.
- Releases MHCap, the largest open caption layer for multimodal wearable time-series data, spanning over 7 million captions across 908,944 person-days.
- Trains OpenTSLM on MHCap, demonstrating superior health-outcome prediction performance, outperforming a label-only baseline on 29 of 32 binary evaluations.

## Limitations

Evaluated primarily on wearable health time-series data and health-outcome prediction tasks; generalizability to non-health industrial or environmental time-series requires further demonstration.

## Key Concepts

- [[timecap]]: An open deterministic captioning pipeline for generating signal-grounded text-annotated wearable health time-series data without relying on language models.

## Archivist Review

Approved the central methodological concept TimeCap because it introduces a reproducible, non-LLM deterministic captioning mechanism for time-series data. Rejected the dataset MHCap and the open question as either paper-local or overly broad.

### Approved Concepts
- TimeCap: Provides a deterministic, language-model-free open captioning pipeline for generating reproducible text-annotated wearable health time-series datasets.

### Rejected Candidates
- [open_question] Grounded Post-Processing and Imbalanced Clinical Tasks (`grounded-nlg-postprocessing-class-imbalance`) - generic: The question combines multiple distinct goals (readability, determinism, class imbalance handling) into a broad future work statement rather than a focused unresolved mechanism.
- [dataset] MHCap (`mhcap`) - not_reusable: A domain-specific derivative dataset that duplicates or extends existing wearable health corpora without establishing broad cross-domain benchmark utility.

## Links

- [Abstract](https://arxiv.org/abs/2610.21274)
- [PDF](https://arxiv.org/pdf/2610.21274)

