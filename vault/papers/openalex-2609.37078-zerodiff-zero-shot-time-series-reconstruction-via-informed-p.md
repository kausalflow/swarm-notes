---
# CSL-compatible fields
title: "ZeroDiff: Zero-Shot Time Series Reconstruction via Informed-Prior Diffusion"
author:
  - literal: "Yingda Fan"
  - literal: "Dan Lu"
  - literal: "Xiaowei Jia"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.37078"

# Custom fields
paper_id: "2609.37078"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "diffusion-model"
  - "zero-shot-learning"
  - "forecasting"
  - "robustness"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "zerodiff"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:15:17Z"
created_at: "2026-10-01T11:15:17Z"
---

# ZeroDiff: Zero-Shot Time Series Reconstruction via Informed-Prior Diffusion

**Authors**: Yingda Fan, Dan Lu, Xiaowei Jia
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.37078](https://arxiv.org/abs/2609.37078)

## Summary

The paper introduces zero-shot time series reconstruction, a task aiming to predict target measurements at unobserved locations using available exogenous inputs. To address the smoothing and underestimation issues of naive mapping, the authors propose ZeroDiff, a framework that builds an informed prior from exogenous variables and leverages diffusion models to calibrate reconstruction errors by training on observed locations and generalizing to unobserved ones. Extensive experiments on real-world datasets demonstrate substantial performance gains over existing methods.

## Key Contributions

- Introduces the zero-shot time series reconstruction task to estimate target measurements at unobserved locations using only exogenous inputs.
- Proposes ZeroDiff, which constructs an informed prior from exogenous variables and calibrates reconstruction errors via a diffusion model trained on observed locations.
- Demonstrates significant improvements over existing baseline approaches across diverse real-world datasets.

## Open Questions & Future Work

- [[joint-optimization-co-adaptation-zero-shot-diffusion]]

## Key Concepts

- [[zerodiff]]: A zero-shot time series reconstruction framework that builds an informed prior from exogenous variables and calibrates reconstruction errors via diffusion.

## Archivist Review

Approved the core framework concept 'ZeroDiff' and the open question concerning joint optimization and co-adaptation in prior-informed diffusion models, adhering to strict scarcity and relevance criteria.

### Approved Concepts
- ZeroDiff: It introduces a novel zero-shot time series reconstruction framework combining informed priors from exogenous variables with diffusion-based error calibration.

### Approved Open Questions
- Joint Optimization and Co-Adaptation in Diffusion: Understanding how to jointly optimize modularized prior-informed diffusion pipelines without hurting out-of-domain transferability is a core architectural problem for robust generative reconstruction.

## Links

- [Abstract](https://arxiv.org/abs/2609.37078)
- [PDF](https://arxiv.org/pdf/2609.37078)

