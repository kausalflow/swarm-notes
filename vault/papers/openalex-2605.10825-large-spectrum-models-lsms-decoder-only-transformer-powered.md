---
# CSL-compatible fields
title: "Large Spectrum Models (LSMs): Decoder-Only Transformer-Powered Spectrum Activity Forecasting via Tokenized RF Data"
author:
  - literal: "Mohammad Mosiur Lunar"
  - literal: "Mehmet C. Vuran"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10825"

# Custom fields
paper_id: "2605.10825"
paper_source: "openalex"
domain: "speech"
tags:
  - "llm"
  - "transformer"
  - "forecasting"
  - "time-series"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "rf-tokenizer"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:38:26Z"
created_at: "2026-05-14T07:38:26Z"
---

# Large Spectrum Models (LSMs): Decoder-Only Transformer-Powered Spectrum Activity Forecasting via Tokenized RF Data

**Authors**: Mohammad Mosiur Lunar, Mehmet C. Vuran
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10825](https://arxiv.org/abs/2605.10825)

## Summary

This paper explores the potential of Large Spectrum Models (LSMs) by adapting decoder-only transformer architectures for short-term RF spectrum activity forecasting. The authors introduce a novel RF tokenizer that converts raw IQ measurements into structured token sequences, facilitating the training of foundation models on radio frequency data. By training five well-known LLMs on a massive 22 TB custom-collected dataset, the study demonstrates that LSMs achieve highly accurate forecasting and exhibit robust generalization capabilities across different geographical locations. These findings highlight the efficacy of leveraging existing language model scaling paradigms for physical layer wireless tasks.

## Key Contributions

- Introduces Large Spectrum Models (LSMs), demonstrating that off-the-shelf decoder-only transformers can be repurposed for RF spectrum forecasting.
- Develops a novel RF tokenizer to transform raw IQ measurements into structured sequences suitable for transformer input.
- Curates an 8.4B token, 22 TB raw spectrum dataset across 33 sub-GHz bands to evaluate LSM performance and scaling.
- LSM-Mistral achieves a 3.25 dB RMSE across test bands, with 97% of predictions maintaining a mean absolute error below 5 dB.

## Open Questions & Future Work

- [[spectrum-foundation-model-adaptability]]

## Key Concepts

- [[rf-tokenizer]]: A method for converting raw IQ measurements into token sequences for transformer models by encoding power-spectral density, gain, frequency, FFT bin, and timestamp information.

## Archivist Review

I approved the RF tokenizer as a reusable concept for bridging raw signal data and transformers. I approved one open question concerning the adaptability of foundation models to RF data, focusing on the broader paradigm shift rather than just this paper's specific implementation. I rejected the dataset because it is a proprietary, paper-specific collection that does not yet function as a community-standardized benchmark.

### Approved Concepts
- RF Tokenizer: It enables the application of LLM architectures to raw RF signal data, serving as the core bridge between physical radio frequency measurements and transformer-based sequence processing.

### Approved Open Questions
- Spectrum Foundation Model Adaptability: This is critical because establishing how foundation models can be systematically adapted for RF data could enable a paradigm shift towards general-purpose, scalable wireless signal intelligence systems for 6G and beyond.

### Rejected Candidates
- [dataset] Outdoor Wireless Testbed Dataset (`outdoor-wireless-testbed-dataset`) - other: This dataset is described as a custom, proprietary collection rather than an established public benchmark with a standard name and widespread community use.

## Links

- [Abstract](https://arxiv.org/abs/2605.10825)
- [PDF](https://arxiv.org/pdf/2605.10825)

