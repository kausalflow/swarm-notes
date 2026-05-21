---
# CSL-compatible fields
title: "Electric Vehicle Charging Profile Forecasting Using Hybrid Models"
author:
  - literal: "Riccardo Ramaschi"
  - literal: "Mario Paolone"
  - literal: "Sonia Leva"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.18443"

# Custom fields
paper_id: "2605.18443"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:34:06Z"
created_at: "2026-05-21T08:34:06Z"
---

# Electric Vehicle Charging Profile Forecasting Using Hybrid Models

**Authors**: Riccardo Ramaschi, Mario Paolone, Sonia Leva
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.18443](https://arxiv.org/abs/2605.18443)

## Summary

This paper addresses the challenge of forecasting individual electric vehicle (EV) fast-charging profiles, a task often overshadowed by aggregate-level modeling. The authors introduce a hybrid, lightweight model designed to estimate charging dynamics both pre-charge and during the ongoing process. Evaluation on public datasets demonstrates that the approach enables more granular scheduling and improved departure time estimation, while highlighting the sensitivity of predictions to the availability of temporal information.

## Key Contributions

- Proposes a hybrid and lightweight forecasting method for individual EV charging profiles that operates both before and during the charging process.
- Demonstrates the efficacy of the proposed model in capturing charging behavior at the individual charger level compared to existing aggregated forecasting approaches.
- Provides an empirical assessment of how varying levels of available temporal information influence the accuracy of the predicted charging profile.

## Open Questions & Future Work

- [[charging-profile-time-transposition-error-propagation]]

## Archivist Review

The paper focuses on an application-specific hybrid forecasting model, which I determined does not constitute a sufficiently general or reusable concept for the vault. However, the identified challenge regarding error propagation in time-transposition for charging profiles addresses a substantive bottleneck in time-series modeling for energy systems, deserving of a standalone note. No relevant public datasets were specified beyond general "public datasets," so none were approved.

### Approved Open Questions
- EV Charging Profile Time Transposition: Understanding error propagation in time-domain mappings is critical for the development of reliable energy management systems in electric vehicle infrastructure, as inaccurate projections lead to inefficient power scheduling and grid management.

### Rejected Candidates
- [concept] Hybrid and Lightweight Charging Forecasting Method (`hybrid-and-lightweight-charging-forecasting-method`) - not_reusable: This is a specific application-level methodology without enough generalizability to serve as a foundational concept in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2605.18443)
- [PDF](https://arxiv.org/pdf/2605.18443)

