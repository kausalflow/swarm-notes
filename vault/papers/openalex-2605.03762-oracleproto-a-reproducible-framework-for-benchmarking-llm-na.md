---
# CSL-compatible fields
title: "OracleProto: A Reproducible Framework for Benchmarking LLM Native Forecasting via Knowledge Cutoff and Temporal Masking"
author:
  - literal: "Yiding Ma"
  - literal: "Chengyun Ruan"
  - literal: "Kaibo Huang"
  - literal: "Zhongliang Yang"
  - literal: "Linna Zhou"
issued:
  date-parts:
    - [2026, 5, 5]
url: "https://arxiv.org/abs/2605.03762"

# Custom fields
paper_id: "2605.03762"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "forecasting"
  - "benchmark"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  - "futurex-past"
concept_slugs:
  - "oracleproto"
dataset_slugs:
  - "futurex-past"
skill: "TimeSeriesSkill"
processed_at: "2026-05-08T06:27:24Z"
created_at: "2026-05-08T06:27:24Z"
---

# OracleProto: A Reproducible Framework for Benchmarking LLM Native Forecasting via Knowledge Cutoff and Temporal Masking

**Authors**: Yiding Ma, Chengyun Ruan, Kaibo Huang, Zhongliang Yang, Linna Zhou
**Date**: 2026-05-05
**Paper ID**: [openalex:2605.03762](https://arxiv.org/abs/2605.03762)

## Summary

OracleProto is a reproducible framework designed to evaluate the forecasting capabilities of LLMs while mitigating knowledge leakage from pretraining data. By utilizing knowledge-cutoff-aligned sample admission, temporal masking, and hierarchical scoring, the framework enables rigorous, auditable forecasting benchmarks. Experimental results on the FutureX-Past dataset demonstrate that OracleProto effectively separates genuine predictive reasoning from memorized facts, offering a standardized approach for cross-model comparison and downstream model alignment.

## Key Contributions

- Introduced OracleProto, a reproducible benchmarking framework for LLM native forecasting that systematically mitigates knowledge leakage.
- Demonstrated that OracleProto reduces residual leakage to the 1% level, significantly outperforming existing tool-only temporal filtering methods.
- Validated the framework on the FutureX-Past dataset across six contemporary LLMs, establishing a standard for evaluating forecasting quality, stability, and efficiency.

## Key Concepts

- [[oracleproto]]: A reproducible evaluation framework for LLM native forecasting that enforces strict knowledge boundaries through temporal masking and cutoff-aligned sample reconstruction.

## Archivist Review

The submission proposes a robust methodology (OracleProto) for addressing the critical problem of pretraining data leakage in LLM forecasting evaluation. I have approved this framework as a permanent concept due to its potential to standardize and improve reproducibility in model-based forecasting benchmarks. The FutureX-Past dataset was approved as it serves as the primary empirical basis for validating the proposed framework.

### Approved Concepts
- OracleProto: Provides a systematic, auditable method to address knowledge leakage in LLM forecasting benchmarks, shifting evaluation from ad-hoc trials to structured, reproducible experiments.

## Datasets

- [[futurex-past]]

## Links

- [Abstract](https://arxiv.org/abs/2605.03762)
- [PDF](https://arxiv.org/pdf/2605.03762)

