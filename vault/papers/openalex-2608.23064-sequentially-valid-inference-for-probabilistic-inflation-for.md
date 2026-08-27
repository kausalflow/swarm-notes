---
# CSL-compatible fields
title: "Sequentially valid inference for probabilistic inflation forecasts"
author:
  - literal: "Amadeo Grob"
  - literal: "Maurizio Daniele"
  - literal: "Johanna Ziegel"
issued:
  date-parts:
    - [2026, 8, 24]
url: "https://arxiv.org/abs/2608.23064"

# Custom fields
paper_id: "2608.23064"
paper_source: "openalex"
domain: "finance"
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
processed_at: "2026-08-27T15:58:32Z"
created_at: "2026-08-27T15:58:32Z"
---

# Sequentially valid inference for probabilistic inflation forecasts

**Authors**: Amadeo Grob, Maurizio Daniele, Johanna Ziegel
**Date**: 2026-08-24
**Paper ID**: [openalex:2608.23064](https://arxiv.org/abs/2608.23064)

## Summary

Traditional statistical tests struggle with the sequential evaluation of probabilistic forecast calibration. This paper applies an e-value-based sequential testing method to macroeconomic forecasting, enabling anytime-valid inference that allows practitioners to test calibration continuously. Applied to probabilistic inflation forecasts for the US, Euro Area, and Switzerland, the sequential approach uncovers detailed insights into forecast misspecification, particularly during major structural breaks missed by static full-sample tests.

## Key Contributions

- Introduces a sequential testing method based on e-values for evaluating probabilistic forecast calibration in macroeconomic forecasting.
- Enables anytime-valid inference for continuous calibration testing without invalidating statistical guarantees.
- Demonstrates the practical value of the sequential framework on probabilistic inflation forecasts for the United States, the Euro Area, and Switzerland.
- Reveals that sequential testing uncovers forecast misspecification and evidence against calibration during major structural breaks that static, full-sample tests miss.

## Open Questions & Future Work

- [[sequentially-valid-inference-multistep-forecasts]]

## Archivist Review

Approved the open question regarding sequentially valid multi-step inference because it identifies a concrete theoretical bottleneck in extending e-value testing to multi-step horizon forecasting. No concepts or datasets met the strict novelty and reusability criteria for vault inclusion.

### Approved Open Questions
- Sequentially Valid Multi-Step Inference: Multi-step macroeconomic forecasting inherently involves overlapping information sets, making the development of powerful and non-conservative anytime-valid testing procedures critical for real-time central bank monitoring.

### Rejected Candidates
- [open_question] Sequentially Valid Multi-Step Inference (`sequentially-valid-inference-multistep-forecasts`) - other: The open question is already appropriate and approved.

## Links

- [Abstract](https://arxiv.org/abs/2608.23064)
- [PDF](https://arxiv.org/pdf/2608.23064)

