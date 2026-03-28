---
# CSL-compatible fields
title: "GARP-EFM: Improving Foundation Models with Revealed Preference Structure"
author:
  - literal: "Victor H. Aguiar"
  - literal: "Nail Kashaev"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.23993"

# Custom fields
paper_id: "2603.23993"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "language-model"
  - "fine-tuning"
  - "llm"
  - "transformer"
  - "forecasting"
  - "reasoning"
  - "emergent-abilities"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "garp-fine-tuning-for-forecasting"
  - "rationality-constrained-forecasting-prior"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:29:36Z"
created_at: "2026-03-28T05:29:36Z"
---

# GARP-EFM: Improving Foundation Models with Revealed Preference Structure

**Authors**: Victor H. Aguiar, Nail Kashaev
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.23993](https://arxiv.org/abs/2603.23993)

## Summary

This work introduces GARP-EFM to improve time-series foundation models for economic forecasting by incorporating established economic logic. The authors fine-tuned the transformer-based Amazon Chronos-2 model using synthetic time-series data generated from utility-maximizing agents, ensuring these synthetic histories satisfy the Generalized Axiom of Revealed Preference (GARP) via Afriat's theorem. This process creates a rationality-constrained forecasting prior that learns price-quantity relations consistent with economic theory. Experimental results show that this fine-tuning substantially improves prediction accuracy relative to the zero-shot foundation model across all tested forecast horizons. The paper suggests that injecting domain axioms via structured synthetic data is an effective technique for enhancing foundation model performance in specialized applications.

## Key Contributions

- Demonstrated that fine-tuning a time-series foundation model (Chronos-2) on synthetic data generated from utility-maximizing agents significantly improves prediction accuracy across all forecast horizons.
- Proposed leveraging Afriat's theorem and the Generalized Axiom of Revealed Preference (GARP) to generate structured, economically consistent synthetic data for fine-tuning.
- Introduced the concept of a "rationality-constrained forecasting prior," where economic theory dictates the synthetic training distribution to enhance model generalization for demand prediction.

## Limitations

The study relies on synthetic data generation based on a specific economic model (utility maximization subject to budget constraints), which may not capture all real-world consumer behaviors or market complexities.

## Key Concepts

- [[garp-fine-tuning-for-forecasting]]: A fine-tuning paradigm that integrates the Generalized Axiom of Revealed Preference (GARP) structure, derived from utility maximization theory, into time-series foundation models to improve economic forecasting by ensuring learned patterns are rationality-consistent.
- [[rationality-constrained-forecasting-prior]]: A time-series forecasting model, derived from fine-tuning a large foundation model on economically structured synthetic data, whose outputs are guaranteed to satisfy specific behavioral axioms like GARP.

## Archivist Review

Two central concepts were approved, both related to the core methodological contribution: using the GARP axiom to structure synthetic data for fine-tuning, and the resulting constrained model itself, termed the 'rationality-constrained forecasting prior'. The existing concept 'chronos-2' makes the explicit mention of the model name as a dataset candidate a duplicate. No new open questions were proposed that meet the high bar for inclusion.

### Approved Concepts
- Generalized Axiom of Revealed Preference (GARP) Fine-Tuning: The paper introduces and leverages the GARP axiom, derived from economic theory, as a structural constraint for fine-tuning time-series foundation models.
- Rationality-Constrained Forecasting Prior: This term defines the resulting model: a foundation model whose predictions are inherently constrained by a set of desired economic rational behaviors learned from synthetic data.

### Rejected Candidates
- [dataset] Amazon Chronos-2 (`amazon-chronos-2`) - duplicate_existing: Amazon Chronos-2 is a model/framework, not a dataset, and is already in the vault as an existing concept (chronos-2).

## Links

- [Abstract](https://arxiv.org/abs/2603.23993)
- [PDF](https://arxiv.org/pdf/2603.23993)

