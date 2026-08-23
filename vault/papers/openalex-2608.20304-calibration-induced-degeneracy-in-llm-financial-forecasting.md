---
# CSL-compatible fields
title: "Calibration-Induced Degeneracy in LLM Financial Forecasting: An Audit-Trailed Case Study on Next-Day Market Risk"
author:
  - literal: "Arin Mohanty"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.20304"

# Custom fields
paper_id: "2608.20304"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "language-model"
  - "forecasting"
  - "financial"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "calibration-induced-degeneracy"
  - "calibration-viability-checkpoint"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:19:46Z"
created_at: "2026-08-23T05:19:46Z"
---

# Calibration-Induced Degeneracy in LLM Financial Forecasting: An Audit-Trailed Case Study on Next-Day Market Risk

**Authors**: Arin Mohanty
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.20304](https://arxiv.org/abs/2608.20304)

## Summary

This paper investigates a failure link in LLM financial forecasting termed calibration-induced degeneracy, where calibration sets all LLM feature weights to zero and nullifies subsequent scoring. The author demonstrates that simple, near-zero-cost baselines outperform the expensive LLM setups and proposes a calibration-viability checkpoint to audit feature responsiveness prior to incurring holdout acquisition costs.

## Key Contributions

- Identifies calibration-induced degeneracy, where post-hoc calibration sets all LLM feature weights to zero and nullifies subsequent scoring.
- Demonstrates that allowing signed weights reactivates mappings, but none improve forecasts after familywise correction.
- Shows that a near-zero-cost headline count baseline outperforms the LLM setup, reducing SPY variance-forecast loss.
- Proposes a calibration-viability checkpoint to test forecast responsiveness and prevent unnecessary paid inference costs.

## Limitations

Limited to a next-day market risk study of two broad-market funds using full-history scoring and 2022 calibration.

## Open Questions & Future Work

- [[calibration-induced-degeneracy-llm-forecasting]]

## Key Concepts

- [[calibration-induced-degeneracy]]: A failure mode where model calibration collapses feature weights to zero, rendering expensive downstream scoring ineffective.
- [[calibration-viability-checkpoint]]: A diagnostic checkpoint that tests if calibration parameters permit meaningful feature response before acquiring costly holdout features.

## Archivist Review

Approved two concepts capturing the novel failure mode of calibration-induced degeneracy and its audit protocol (calibration-viability checkpoint), alongside one open question concerning its broader generalization across LLM architectures and horizons.

### Approved Concepts
- Calibration-Induced Degeneracy: Identifies a novel failure mode where post-hoc calibration zeroes out expensive model features, rendering subsequent scoring ineffective.
- Calibration-Viability Checkpoint: Introduces a pre-acquisition audit mechanism to test if features can meaningfully affect forecasts before incurring inference costs.

### Approved Open Questions
- Calibration-Induced Degeneracy in LLM Forecasting: Preventing wasted computational and financial resources during large-scale inference by ensuring that calibrated models retain a non-degenerate pathway for newly acquired features is a critical operational requirement for automated ML pipelines.

## Links

- [Abstract](https://arxiv.org/abs/2608.20304)
- [PDF](https://arxiv.org/pdf/2608.20304)

