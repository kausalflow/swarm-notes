---
# CSL-compatible fields
title: "The Stanford EDGAR Filings Dataset: Reconstructing U.S. Corporate and Financial Disclosures into Layout-Faithful and Token-Efficient Pretraining Data"
author:
  - literal: "Nick Bettencourt"
  - literal: "Xiaowei Ding"
  - literal: "Kay Giesecke"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.18192"

# Custom fields
paper_id: "2606.18192"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "pre-training"
  - "long-context"
  - "benchmark"
  - "dataset"
  - "finance"
architectures:
  []
datasets:
  - "SEFD-v1"
concept_slugs:
  - "stanford-edgar-filings-dataset-sefd"
  - "edgar-forecast-benchmark"
dataset_slugs:
  - "sefd-v1"
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:24:59Z"
created_at: "2026-06-19T09:24:59Z"
---

# The Stanford EDGAR Filings Dataset: Reconstructing U.S. Corporate and Financial Disclosures into Layout-Faithful and Token-Efficient Pretraining Data

**Authors**: Nick Bettencourt, Xiaowei Ding, Kay Giesecke
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.18192](https://arxiv.org/abs/2606.18192)

## Summary

The Stanford EDGAR Filings Dataset (SEFD) addresses the scarcity of high-quality, long-context pretraining data by providing an open-source, layout-faithful reconstruction of SEC filings in MultiMarkdown. This corpus, consisting of 152B tokens in its initial snapshot, is optimized for financial language modeling and document understanding, exhibiting minimal overlap with traditional web corpora. The paper also introduces two specialized benchmarks, EDGAR-Forecast and EDGAR-OCR, to evaluate numerical forecasting grounded in financial documents and the transcription of complex financial tables, respectively.

## Key Contributions

- Introduces the Stanford EDGAR Filings Dataset (SEFD), a 152B-token open-source corpus of layout-faithful MultiMarkdown SEC filings.
- Demonstrates that SEFD provides high-quality, token-efficient long-context pretraining data with minimal overlap (<0.1%) with Common Crawl.
- Provides the EDGAR-Forecast benchmark for filing-grounded numerical forecasting and the EDGAR-OCR benchmark for complex financial table transcription.

## Open Questions & Future Work

- [[parsing-complex-evolving-edgar-filings]]

## Key Concepts

- [[stanford-edgar-filings-dataset-sefd]]: A large-scale, layout-faithful MultiMarkdown dataset of SEC filings designed for financial language modeling and document understanding.
- [[edgar-forecast-benchmark]]: A benchmark for evaluating filing-grounded numerical forecasting capabilities in language models.

## Archivist Review

I have approved the core dataset (SEFD-v1) and its corresponding dataset/benchmark concepts. I reframed the open question to be more general and professional, focusing on the broader challenge of parsing complex, evolving filing structures in financial archives rather than focusing solely on 'rare XML branches' as an internal limitation of this specific parser. The approved items provide a foundational resource for long-context financial language modeling and forecasting.

### Approved Concepts
- Stanford EDGAR Filings Dataset (SEFD): It provides a large-scale, open-source, layout-faithful corpus specifically designed for long-context financial language modeling and evaluation.
- EDGAR-Forecast Benchmark: It establishes a structured task for evaluating a model's ability to perform numerical reasoning and forecasting based on specific financial filing data.

### Approved Open Questions
- Parsing Complex Evolving Filings: As the EDGAR archive continues to grow, incomplete coverage of rare or atypical XML structures limits the utility of the data for tasks requiring full financial disclosure integrity.

## Datasets

- [[sefd-v1]]

## Links

- [Abstract](https://arxiv.org/abs/2606.18192)
- [PDF](https://arxiv.org/pdf/2606.18192)

