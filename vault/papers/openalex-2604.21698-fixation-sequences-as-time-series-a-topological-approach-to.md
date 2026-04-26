---
# CSL-compatible fields
title: "Fixation Sequences as Time Series: A Topological Approach to Dyslexia Detection"
author:
  - literal: "Marius Huber"
  - literal: "David R. Reich"
  - literal: "Lena A. Jäger"
issued:
  date-parts:
    - [2026, 4, 23]
url: "https://arxiv.org/abs/2604.21698"

# Custom fields
paper_id: "2604.21698"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "interpretability"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "copenhagen-corpus"
concept_slugs:
  - "topological-eye-tracking-analysis"
dataset_slugs:
  - "copenhagen-corpus"
skill: "TimeSeriesSkill"
processed_at: "2026-04-26T06:54:07Z"
created_at: "2026-04-26T06:54:07Z"
---

# Fixation Sequences as Time Series: A Topological Approach to Dyslexia Detection

**Authors**: Marius Huber, David R. Reich, Lena A. Jäger
**Date**: 2026-04-23
**Paper ID**: [openalex:2604.21698](https://arxiv.org/abs/2604.21698)

## Summary

This paper proposes a topological approach for dyslexia detection by treating eye-tracking fixation sequences as time series and applying persistent homology. By developing novel filtrations, the authors extract multi-scale topological features that, when combined with traditional statistical eye-movement metrics in a hybrid model, yield superior performance over baseline methods. The approach is evaluated on the Copenhagen Corpus and demonstrates that topological analysis captures distinct, non-redundant information useful for clinical classification tasks.

## Key Contributions

- Develops novel filtrations for persistent homology specifically designed for time-series-interpreted eye-tracking data.
- Introduces a hybrid modeling framework that concatenates topological features with statistical eye-movement features to improve classification performance.
- Achieves state-of-the-art results for dyslexia detection on the Copenhagen Corpus, demonstrating that topological features capture complementary discriminative information.

## Open Questions & Future Work

- [[optimal-aggregation-dyslexia-detection]]
- [[interpreting-topological-reading-features]]

## Key Concepts

- [[topological-eye-tracking-analysis]]: A method for analyzing eye-tracking fixation sequences by treating them as time series and applying persistent homology via custom filtrations.

## Archivist Review

I approved the core topological analysis concept and the dataset as they are central to the study's novel contribution to dyslexia detection. The two open questions were approved for their clear focus on the challenges of aggregation and model interpretability in clinical topological time-series analysis. No other concepts or datasets met the strict novelty or reusability criteria for permanent vault inclusion.

### Approved Concepts
- Topological Eye-Tracking Analysis: Represents a novel integration of TDA into oculomotor research for diagnostic tasks.

### Approved Open Questions
- Optimal Aggregation for Dyslexia Detection: Understanding the optimal level of data aggregation is essential for moving topological dyslexia detection from a research setting to a reliable clinical screening tool.
- Interpreting Topological Reading Features: Bridging the gap between high-dimensional topological representations and cognitive mechanisms is critical for the clinical adoption and interpretability of these models.

## Datasets

- [[copenhagen-corpus]]

## Links

- [Abstract](https://arxiv.org/abs/2604.21698)
- [PDF](https://arxiv.org/pdf/2604.21698)

