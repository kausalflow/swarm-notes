---
# CSL-compatible fields
title: "Decision-focused Conservation Voltage Reduction to Consider the Cascading Impact of Forecast Errors"
author:
  - literal: "Qintao Du"
  - literal: "Ran Li"
  - literal: "Weiyi Lv"
  - literal: "Huan Zhou"
  - literal: "M. Yu"
  - literal: "Jianzhe Liu"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.07106"

# Custom fields
paper_id: "2604.07106"
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
  - "decision-focused-forecasting-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:54:44Z"
created_at: "2026-04-11T05:54:44Z"
---

# Decision-focused Conservation Voltage Reduction to Consider the Cascading Impact of Forecast Errors

**Authors**: Qintao Du, Ran Li, Weiyi Lv, Huan Zhou, M. Yu, Jianzhe Liu
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.07106](https://arxiv.org/abs/2604.07106)

## Summary

This paper introduces a bi-level multi-timescale forecasting (Bi-MTF) framework to optimize Conservation Voltage Reduction (CVR) in hierarchical Volt-Var Control systems. By embedding multi-stage VVC optimization directly into the upstream forecasting model training, the approach explicitly addresses the cascading impacts of forecast errors that plague traditional sequential paradigms. A novel sensitivity-driven integer L-shaped method, utilizing hybrid gradient feedback, is developed to ensure the computational tractability of this bi-level optimization. Evaluations on a modified IEEE 33-bus system confirm that this decision-focused approach significantly outperforms conventional MSE-based methods in both energy savings and operational safety.

## Key Contributions

- Introduces a Bi-MTF framework that integrates multi-stage VVC optimization into forecasting model training to mitigate the cascading effects of forecast errors.
- Develops a modified sensitivity-driven integer L-shaped method that uses hybrid gradient feedback to ensure tractability in bi-level optimization.
- Achieves superior CVR efficiency, increasing energy savings from 1.50-1.76% (conventional MSE-based) to 2.74-3.41% on the modified IEEE 33-bus system.

## Key Concepts

- [[decision-focused-forecasting-framework]]: A training paradigm that integrates downstream multi-stage optimization objectives into upstream forecasting models to mitigate cascading forecast error impacts.

## Archivist Review

The paper's primary contribution is a shift from MSE-based forecasting to decision-focused forecasting within a hierarchical control loop. I have approved a generalized version of the proposed concept that aligns with existing research on integrating decision-making with predictive models. The specific term 'Bi-MTF' was rejected as a duplicate of this broader paradigm. No datasets or open questions were approved, as the system remains local to IEEE bus benchmarks and does not identify a fundamental open theoretical or empirical gap.

### Approved Concepts
- Decision-Focused Forecasting Framework: It addresses the critical problem of cascading errors in hierarchical control systems by aligning forecasting models directly with downstream decision objectives rather than proxy statistical metrics.

### Rejected Candidates
- [concept] Bi-level multi-timescale forecasting (Bi-MTF) (`bi-level-multi-timescale-forecasting-bi-mtf`) - duplicate_existing: The core contribution is better described by the more general 'Decision-Focused Forecasting Framework' which is already included in the vault as an approved concept.

## Links

- [Abstract](https://arxiv.org/abs/2604.07106)
- [PDF](https://arxiv.org/pdf/2604.07106)

