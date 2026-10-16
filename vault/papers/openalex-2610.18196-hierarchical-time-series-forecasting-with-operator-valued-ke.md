---
# CSL-compatible fields
title: "Hierarchical Time Series Forecasting with Operator-Valued Kernels"
author:
  - literal: "Junjie Yang"
  - literal: "Adeline Fermanian"
  - literal: "Claire Boyer"
  - literal: "Gérard Biau"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.18196"

# Custom fields
paper_id: "2610.18196"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hierarchical-forecasting-with-operator-valued-kernels"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:22:44Z"
created_at: "2026-10-16T09:22:44Z"
---

# Hierarchical Time Series Forecasting with Operator-Valued Kernels

**Authors**: Junjie Yang, Adeline Fermanian, Claire Boyer, Gérard Biau
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.18196](https://arxiv.org/abs/2610.18196)

## Summary

This paper introduces a unified framework for hierarchical time series forecasting by casting it as a multivariate regression problem in a vector-valued reproducing kernel Hilbert space. By employing structured operator-valued kernels, the proposed approach enforces hierarchical coherence by construction within the hypothesis space, avoiding post-hoc reconciliation or unconstrained end-to-end pipelines. Theoretical guarantees are established via excess risk bounds, and empirical evaluations on synthetic and real-world benchmarks demonstrate its effectiveness.

## Key Contributions

- Formulates hierarchical time series forecasting as a multivariate regression problem within a vector-valued reproducing kernel Hilbert space (RKHS).
- Introduces structured operator-valued kernel constructions that enforce coherence across multiple levels of aggregation directly by construction within the hypothesis space.
- Derives theoretical excess risk bounds that characterize the generalization performance of the proposed kernel-based hierarchical forecasting framework.
- Demonstrates empirical relevance and effectiveness on synthetic and real-world hierarchical forecasting datasets.

## Key Concepts

- [[hierarchical-forecasting-with-operator-valued-kernels]]: A unified hierarchical forecasting framework that formulates multivariate regression in a vector-valued reproducing kernel Hilbert space using structured operator-valued kernels.

## Archivist Review

Approved the central methodological concept of operator-valued kernels for hierarchical time series forecasting, as it represents a distinct, reusable theoretical formulation with clear generalization bounds. No datasets or open questions met the rigorous standalone criteria, so they were left empty.

### Approved Concepts
- Hierarchical Forecasting with Operator-Valued Kernels: Provides a rigorous mathematical formulation and principled approach for hierarchical time series forecasting using operator-valued kernels.

## Links

- [Abstract](https://arxiv.org/abs/2610.18196)
- [PDF](https://arxiv.org/pdf/2610.18196)

