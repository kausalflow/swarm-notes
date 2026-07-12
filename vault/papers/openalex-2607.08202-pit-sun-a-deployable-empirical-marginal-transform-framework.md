---
# CSL-compatible fields
title: "PIT-SUN: A Deployable Empirical Marginal Transform Framework with Expectation-Consistent Recovery for Regression in Recommender Systems"
author:
  - literal: "Mingyu Zhao"
  - literal: "Zhaohan Li"
  - literal: "Zhenxiong Miao"
  - literal: "Xu Zhang"
  - literal: "Dewei Leng"
  - literal: "Yanan Niu"
  - literal: "Kun Gai"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08202"

# Custom fields
paper_id: "2607.08202"
paper_source: "openalex"
domain: "nlp"
tags:
  - "recommendation-system"
  - "regression"
architectures:
  []
datasets:
  []
concept_slugs:
  - "pit-sun-recovery-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:28:19Z"
created_at: "2026-07-12T07:28:19Z"
---

# PIT-SUN: A Deployable Empirical Marginal Transform Framework with Expectation-Consistent Recovery for Regression in Recommender Systems

**Authors**: Mingyu Zhao, Zhaohan Li, Zhenxiong Miao, Xu Zhang, Dewei Leng, Yanan Niu, Kun Gai
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08202](https://arxiv.org/abs/2607.08202)

## Summary

This paper addresses the instability and lack of expectation consistency when applying target transformations to complex regression targets like dwell time or GMV in recommender systems. The authors propose PIT-SUN, an empirical marginal recovery framework that estimates original-space expectations using multiplicative SUN recovery rather than naive inverse transformation. By leveraging empirical marginal tables for bounded normal-score coordinates and variance-controlled recovery, the method achieves robust performance on heavy-tailed and zero-inflated data. Empirical evaluations on various scales confirm significant improvements in both prediction accuracy and ranking quality with minimal deployment overhead.

## Key Contributions

- Introduces PIT-SUN, a framework that recovers the original-space conditional expectation after nonlinear marginal transformation without losing consistency.
- Demonstrates that PIT-SUN resolves the mean collapse and tail shrinkage issues prevalent in standard MSE regression for heavy-tailed and multimodal targets.
- Achieves superior point accuracy, calibration, and ranking quality across synthetic, public, and large-scale industrial recommender system datasets.

## Open Questions & Future Work

- [[empirical-marginal-recovery-closure-bottleneck]]

## Key Concepts

- [[pit-sun-recovery-framework]]: A framework that uses empirical marginal tables and multiplicative recovery to maintain expectation consistency when performing regression with nonlinear target transforms.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 1 concept(s), 1 open question(s), and 0 dataset(s), with 1 rejected candidate note(s).

### Approved Concepts
- Probability-Integral-Transformed Unbiased recovery (PIT-SUN): It solves the fundamental regression problem of achieving expectation-consistent estimation when using non-linear target transformations for heavy-tailed or zero-inflated data.

### Approved Open Questions
- Empirical Marginal Recovery Closure: This bottleneck determines the reliability and stability of regression-based forecasting in industrial recommender systems, where target distributions often exhibit extreme multimodality and zero-inflation.

### Rejected Candidates
- [open_question] Optimal Empirical Marginal Recovery Closure (`empirical-marginal-recovery-heterogeneity`) - duplicate_existing: Duplicate of the approved question; re-titled for clarity and consistency.

## Links

- [Abstract](https://arxiv.org/abs/2607.08202)
- [PDF](https://arxiv.org/pdf/2607.08202)

