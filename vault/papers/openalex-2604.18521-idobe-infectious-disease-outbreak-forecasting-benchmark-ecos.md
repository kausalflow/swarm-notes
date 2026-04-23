---
# CSL-compatible fields
title: "IDOBE: Infectious Disease Outbreak forecasting Benchmark Ecosystem"
author:
  - literal: "Aniruddha Adiga"
  - literal: "Jingyuan Chou"
  - literal: "Anshul Chiranth"
  - literal: "Bryan Lewis"
  - literal: "Ana I. Bento"
  - literal: "Shaun Truelove, Geoffrey Fox"
  - literal: "Madhav Marathe"
  - literal: "Harry Hochheiser"
  - literal: "Srini Venkatramanan"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.18521"

# Custom fields
paper_id: "2604.18521"
paper_source: "openalex"
domain: "nlp"
tags:
  - "benchmark"
  - "dataset"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  - "IDOBE"
concept_slugs:
  - "idobe-benchmark"
dataset_slugs:
  - "idobe"
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:55:19Z"
created_at: "2026-04-23T06:55:19Z"
---

# IDOBE: Infectious Disease Outbreak forecasting Benchmark Ecosystem

**Authors**: Aniruddha Adiga, Jingyuan Chou, Anshul Chiranth, Bryan Lewis, Ana I. Bento, Shaun Truelove, Geoffrey Fox, Madhav Marathe, Harry Hochheiser, Srini Venkatramanan
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.18521](https://arxiv.org/abs/2604.18521)

## Summary

IDOBE addresses the lack of standardized evaluation tools in infectious disease forecasting by providing a curated, large-scale benchmark ecosystem. The collection compiles over a century of surveillance data, segmented into 10,000+ outbreaks across 13 diseases to support multi-horizon forecasting research. The authors evaluate 11 baseline models using point-forecast and probabilistic scoring metrics, establishing a performance baseline that highlights the comparative strengths of MLP-based and statistical models. This resource aims to foster reproducible research in epidemiological modeling by offering a unified framework for benchmarking novel outbreak responses.

## Key Contributions

- Introduces IDOBE, a standardized benchmark ecosystem containing over 10,000 outbreak segments for 13 infectious diseases, covering cases and hospitalizations across global locations.
- Quantifies epidemiological diversity using information-theoretic and distributional measures to ensure robust evaluation of forecasting models.
- Provides a comprehensive performance evaluation of 11 baseline models for 1- to 4-week-ahead forecasting, establishing that MLP-based methods are most robust while statistical models perform well pre-peak.

## Open Questions & Future Work

- [[complex-outbreak-segmentation]]
- [[multivariate-mechanistic-integration]]

## Key Concepts

- [[idobe-benchmark]]: A large-scale curated benchmark ecosystem of over 10,000 epidemiological outbreak time series designed for standardized forecasting evaluation.

## Archivist Review

The IDOBE benchmark is approved as a central contribution to the field of epidemiological time-series forecasting, providing a much-needed standardized evaluation ecosystem. The approved open questions identify key structural limitations in current outbreak forecasting research: the need for better multi-wave segmentation and the integration of multivariate, mechanistic data. Standard review policies were applied to reject overly specific implementation details while retaining high-impact research directions.

### Approved Concepts
- IDOBE: Provides a standardized, large-scale ecosystem specifically designed for infectious disease outbreak forecasting across multiple outcomes and diseases, filling a significant gap in epidemiological benchmarks.

### Approved Open Questions
- Complex Outbreak Segmentation Methods: This is a core methodological bottleneck in transitioning from single-wave forecasting benchmarks to real-world, multi-pathogen epidemiological environments.
- Multivariate and Mechanistic Forecasting: This represents a critical gap in advancing beyond black-box time-series forecasting toward scientifically robust, mechanistic public health decision support.

## Datasets

- [[idobe]]

## Links

- [Abstract](https://arxiv.org/abs/2604.18521)
- [PDF](https://arxiv.org/pdf/2604.18521)

