---
# CSL-compatible fields
title: "What LLM Forecasters Know but Don't Say: Probing Internal Representations for Calibration and Faithfulness"
author:
  - literal: "Raphaël Sarfati"
  - literal: "Pratyush Ranjan Tiwari"
  - literal: "Siddharth Boppana"
  - literal: "Christopher J. Earls"
  - literal: "Srikar Varadaraj"
  - literal: "Eric Ho"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08046"

# Custom fields
paper_id: "2607.08046"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "forecasting"
  - "chain-of-thought"
  - "interpretability"
  - "faithfulness"
  - "calibration"
architectures:
  []
datasets:
  - "openforesight"
concept_slugs:
  - "representation-pooling-probes"
dataset_slugs:
  - "openforesight"
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:24:37Z"
created_at: "2026-07-12T07:24:37Z"
---

# What LLM Forecasters Know but Don't Say: Probing Internal Representations for Calibration and Faithfulness

**Authors**: Raphaël Sarfati, Pratyush Ranjan Tiwari, Siddharth Boppana, Christopher J. Earls, Srikar Varadaraj, Eric Ho
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08046](https://arxiv.org/abs/2607.08046)

## Summary

This paper investigates the discrepancy between the accuracy and faithfulness of LLM-based forecasters, finding that verbalized chain-of-thought reasoning often fails to mirror the actual decision-making process. By training representation-pooling probes on intermediate activations, the authors show that internal states contain more calibrated and accurate information than the generated text. Their findings further reveal that these internal representations reliably detect when reasoning traces are decoupled from the underlying forecast, and that forecasting decisions are largely fixed prior to the reasoning phase, allowing for significant computational efficiency gains.

## Key Contributions

- Introduces representation-pooling probes that achieve superior calibration in LLM forecasters compared to standard CoT outputs.
- Demonstrates that internal activations act as reliable 'lie detectors' for CoT faithfulness, accurately tracking behavioral shifts despite misleading reasoning traces.
- Shows that LLM forecasts are determined before CoT generation, enabling a token-routing mechanism that reduces generation cost by 30-47% without accuracy loss.

## Key Concepts

- [[representation-pooling-probes]]: A probing technique applied to intermediate model activations that extracts more calibrated and faithful forecasting information than chain-of-thought traces.

## Archivist Review

I approved the representation-pooling probes as a robust concept for auditing model-internal reasoning, as this technique addresses the growing problem of faithfulness in LLM-based forecasting. I also approved OpenForesight as a specific, named dataset. Other candidates were rejected to maintain the vault's high bar for novelty and domain-specific impact.

### Approved Concepts
- Representation-Pooling Probes: Provides a novel, model-agnostic method to extract calibrated forecasts directly from model internal activations rather than relying on unreliable verbalized reasoning traces.

## Datasets

- [[openforesight]]

## Links

- [Abstract](https://arxiv.org/abs/2607.08046)
- [PDF](https://arxiv.org/pdf/2607.08046)

