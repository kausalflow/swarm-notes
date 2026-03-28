---
# CSL-compatible fields
title: "Uncovering Memorization in Timeseries Imputation models: LBRM Membership Inference and its link to attribute Leakage"
author:
  - literal: "Faiz Taleb"
  - literal: "Ivan Gazeau"
  - literal: "Maryline Laurent"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24213"

# Custom fields
paper_id: "2603.24213"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "privacy"
  - "membership-inference"
  - "attribute-inference"
  - "attention-mechanism"
architectures:
  - "attention-mechanism"
datasets:
  []
concept_slugs:
  - "reference-model-membership-inference-timeseries"
  - "time-series-attribute-inference-attack"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:28:40Z"
created_at: "2026-03-28T05:28:40Z"
---

# Uncovering Memorization in Timeseries Imputation models: LBRM Membership Inference and its link to attribute Leakage

**Authors**: Faiz Taleb, Ivan Gazeau, Maryline Laurent
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24213](https://arxiv.org/abs/2603.24213)

## Summary

This work addresses critical privacy concerns in deep learning models for time series imputation by demonstrating vulnerability to black-box inference attacks. The authors propose a two-stage attack framework, beginning with a novel Membership Inference Attack (LBRM) that uses a reference model to achieve high detection accuracy even against models robust to standard overfitting attacks. Furthermore, they introduce the first Attribute Inference Attack designed to extract sensitive characteristics from the training data of imputation models. Experimental results confirm the effectiveness of the membership attack against attention-based and autoencoder architectures, showing a significant improvement over naive baselines, and establish a predictive link between membership leakage and attribute leakage success.

## Key Contributions

- Introduction of a novel two-stage membership inference attack (LBRM) based on a reference model, improving detection accuracy against imputation models robust to overfitting-based attacks.
- Development of the first attribute inference attack capable of predicting sensitive characteristics from a trained time series imputation model.
- Demonstration of significant training data retrieval by the membership attack (tpr@top25% higher than baseline) across attention-based and autoencoder architectures.
- Establishment of a link where the membership attack success predicts the viability of the subsequent attribute inference attack (90% precision).

## Limitations

The abstract focuses on the attack success and does not detail inherent limitations, though the evaluation covers trained-from-scratch and fine-tuned models. Future work likely involves developing robust defenses against these specific attacks.

## Key Concepts

- [[reference-model-membership-inference-timeseries]]: A two-stage membership inference attack framework for time series imputation models that utilizes a reference model to improve the detection of training data inclusion.
- [[time-series-attribute-inference-attack]]: An attack that infers sensitive characteristics about the original training set used to train a time series imputation model.

## Archivist Review

Two primary concepts were approved as they represent novel methodologies specifically tailored for privacy attacks on time series imputation models: a new membership inference technique (LBRM) and the first attribute inference attack for this domain. These contributions establish reusable attack patterns for sensitive time series data. No specific named datasets were provided in the analysis, and standard architectural components were rejected.

### Approved Concepts
- Reference Model Membership Inference (LBRM): It is a novel membership inference attack specifically tailored for time series imputation models, designed to work even when models are robust to traditional overfitting-based attacks.
- Time Series Attribute Inference Attack: It is the first reported attribute inference attack specifically targeting time series imputation models, exposing a new privacy vector beyond simple data memorization.

### Rejected Candidates
- [concept] attention-mechanism (`attention-mechanism`) - subcomponent_of_broader_mechanism: The mention of attention-based architectures is descriptive of the evaluated models rather than a novel reusable mechanism introduced by this paper for privacy analysis.

## Links

- [Abstract](https://arxiv.org/abs/2603.24213)
- [PDF](https://arxiv.org/pdf/2603.24213)

