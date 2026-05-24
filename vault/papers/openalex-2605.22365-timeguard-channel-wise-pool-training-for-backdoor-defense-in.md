---
# CSL-compatible fields
title: "TimeGuard: Channel-wise Pool Training for Backdoor Defense in Time Series Forecasting"
author:
  - literal: "Quang Duc Nguyen"
  - literal: "Siyuan Liang"
  - literal: "Yiming Li"
  - literal: "Fushuo Huo"
  - literal: "Dacheng Tao"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22365"

# Custom fields
paper_id: "2605.22365"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "adversarial-examples"
architectures:
  []
datasets:
  []
concept_slugs:
  - "timeguard-backdoor-defense"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:45:20Z"
created_at: "2026-05-24T07:45:20Z"
---

# TimeGuard: Channel-wise Pool Training for Backdoor Defense in Time Series Forecasting

**Authors**: Quang Duc Nguyen, Siyuan Liang, Yiming Li, Fushuo Huo, Dacheng Tao
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22365](https://arxiv.org/abs/2605.22365)

## Summary

Time series forecasting models face significant security risks from backdoor attacks, which are exacerbated by challenges like channel data entanglement and task-formulation shifts. This paper systematically evaluates existing defenses and introduces TimeGuard, a novel training-time backdoor defense strategy. TimeGuard employs channel-wise pool training and a time-aware confidence mechanism to effectively filter poisoned data, significantly improving model robustness against backdoor triggers without compromising forecasting accuracy on clean data.

## Key Contributions

- Systematically analyzed 13 representative backdoor defenses in the TSF life cycle, identifying signal dilution due to data entanglement and loss degeneration due to task-formulation shift as primary failure modes.
- Proposed TimeGuard, a training-time defense utilizing channel-wise pool training and time-aware confidence criteria to filter backdoor-polluted data.
- Introduced distance-regularized loss selection to dynamically manage and expand the reliable training pool, mitigating the impact of poison-injected windows.
- Demonstrated that TimeGuard improves MAE_P by 1.96x over leading baselines while maintaining clean performance degradation within 5%.

## Key Concepts

- [[timeguard-backdoor-defense]]: A training-time backdoor defense for time series forecasting that uses channel-wise pool training and time-aware confidence criteria to isolate poisoned signals.

## Archivist Review

I approved the TimeGuard backdoor defense mechanism as it introduces a specialized strategy for mitigating unique TSF vulnerabilities like channel data entanglement. Other potential candidates were either subcomponents (like distance-regularized loss selection) or lacked sufficient uniqueness to merit permanent standalone status. The review applied strict criteria to ensure only foundational, reusable security paradigms are added to the vault.

### Approved Concepts
- TimeGuard Backdoor Defense: It addresses fundamental vulnerabilities in time-series forecasting (data entanglement and task-formulation shift) during training.

### Rejected Candidates
- [concept] TimeGuard (`timeguard-backdoor-defense`) - other: The title 'TimeGuard' is slightly redundant with the slug; 'TimeGuard Backdoor Defense' is a more descriptive conceptual name.

## Links

- [Abstract](https://arxiv.org/abs/2605.22365)
- [PDF](https://arxiv.org/pdf/2605.22365)

