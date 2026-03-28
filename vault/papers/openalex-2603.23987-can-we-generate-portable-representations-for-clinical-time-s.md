---
# CSL-compatible fields
title: "Can we generate portable representations for clinical time series data using LLMs?"
author:
  - literal: "Zongliang Ji"
  - literal: "Yifei Sun"
  - literal: "André Carlos Kajdacsy-Balla Amaral"
  - literal: "Anna Goldenberg"
  - literal: "Rahul G. Krishnan"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.23987"

# Custom fields
paper_id: "2603.23987"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "time-series"
  - "few-shot-learning"
  - "embedding"
  - "forecasting"
  - "robustness"
  - "language-model"
architectures:
  []
datasets:
  - "MIMIC-IV"
  - "HIRID"
  - "PPICU"
concept_slugs:
  - "llm-generated-portable-clinical-embeddings"
  - "structured-prompting-for-embedding-variance-reduction"
dataset_slugs:
  - "mimic-iv"
  - "hirid"
  - "ppicu"
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:28:46Z"
created_at: "2026-03-28T05:28:46Z"
---

# Can we generate portable representations for clinical time series data using LLMs?

**Authors**: Zongliang Ji, Yifei Sun, André Carlos Kajdacsy-Balla Amaral, Anna Goldenberg, Rahul G. Krishnan
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.23987](https://arxiv.org/abs/2603.23987)

## Summary

This work addresses the deployment brittleness of clinical ML models across different hospitals by investigating the creation of portable patient embeddings using Large Language Models (LLMs). The proposed method involves using a frozen LLM to translate irregular ICU time series data into concise natural language summaries, which are then converted into fixed-length vectors using a frozen text embedding model. Evaluated across forecasting and classification tasks on three cohorts (MIMIC-IV, HIRID, PPICU), this approach achieves competitive in-distribution performance while showing superior robustness to cross-hospital distribution shifts compared to imputation and time series foundation models. A key finding is that structured prompting significantly reduces the variance in the final predictive model performance. The resulting representations facilitate few-shot learning, suggesting a path toward reducing engineering overhead for scalable clinical deployment.

## Key Contributions

- Proposing a method to create portable patient embeddings for clinical ML by mapping irregular ICU time series to text summaries using a frozen LLM, followed by text embedding.
- Demonstrating that these portable representations achieve competitive in-distribution performance and exhibit smaller relative performance drops when transferring between distinct hospital cohorts (MIMIC-IV, HIRID, PPICU).
- Identifying that structured prompt design is crucial for reducing the variance of downstream predictive models derived from these embeddings without sacrificing mean accuracy.
- Showing the approach enables few-shot learning capability and does not increase demographic information recoverability compared to baseline representations.

## Limitations

The study focuses on three specific cohorts; generalizability across a wider range of clinical settings or data types remains to be fully established.

## Key Concepts

- [[llm-generated-portable-clinical-embeddings]]: Generating fixed-length, transferrable patient vector representations by first summarizing irregular ICU time series data into natural language using a frozen LLM, and then embedding the text summary.
- [[structured-prompting-for-embedding-variance-reduction]]: The use of specially structured natural language prompts when converting time series data to text for embedding significantly reduces the variance in downstream predictive model performance without significantly changing the mean accuracy.

## Archivist Review

Two core concepts were approved: the main mechanism of creating portable embeddings via LLM summarization of clinical time series, and the critical finding regarding structured prompting's role in stabilizing embedding quality (reducing variance). The three clinical datasets used for evaluation were approved as they anchor the main cross-site generalization claims. No new open questions were identified as the candidates were either conclusions or dependent benefits of the main approach.

### Approved Concepts
- Portable Patient Embeddings via LLM Summarization: This is the core novel technique proposed to address the portability problem in clinical ML deployment.
- Structured Prompting for Reduced Predictive Variance: This identifies a critical hyperparameter/design choice (prompt structure) that affects the reliability (variance) of the resulting embeddings, which is a key finding for practical use.

### Rejected Candidates
- [concept] Few-Shot Learning enabled by Portable Embeddings (`few-shot-learning-for-portable-embeddings`) - subcomponent_of_broader_mechanism: The paper discusses that the representations *improve* few-shot learning, but this is a general benefit of the representation, not a novel reusable mechanism distinct from the core embedding method.
- [concept] LLMs as Tools to Enable Scalable Clinical Deployment (`llm-for-clinical-ml-deployment-bottleneck-reduction`) - low_impact: This is a high-level conclusion about the impact of the work, not a specific reusable mechanism or technical artifact.

## Datasets

- [[mimic-iv]]
- [[hirid]]
- [[ppicu]]

## Links

- [Abstract](https://arxiv.org/abs/2603.23987)
- [PDF](https://arxiv.org/pdf/2603.23987)

