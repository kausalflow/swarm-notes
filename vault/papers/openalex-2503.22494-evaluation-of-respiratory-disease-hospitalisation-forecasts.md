---
# CSL-compatible fields
title: "Evaluation of respiratory disease hospitalisation forecasts using synthetic outbreak data"
author:
  - literal: "Grégoire Béchade"
  - literal: "Torjörn Lundh"
  - literal: "Philip Gerlee"
issued:
  date-parts:
    - [2026, 7, 29]
url: "https://arxiv.org/abs/2503.22494"

# Custom fields
paper_id: "2503.22494"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-01T07:22:36Z"
created_at: "2026-08-01T07:22:36Z"
---

# Evaluation of respiratory disease hospitalisation forecasts using synthetic outbreak data

**Authors**: Grégoire Béchade, Torjörn Lundh, Philip Gerlee
**Date**: 2026-07-29
**Paper ID**: [openalex:2503.22494](https://arxiv.org/abs/2503.22494)

## Summary

This paper evaluates respiratory disease hospitalisation forecasts using a generated synthetic dataset of 324 diverse outbreak time-series alongside COVID-19 pandemic data. The authors assess 14 component models and 6 ensembles, finding that mechanistic models gain relative accuracy over statistical ones at longer horizons (14 days vs. 7 days). Furthermore, they introduce an adaptive ensemble method that outperforms individual models and show that the coefficient of variation among component forecasts can effectively predict future ensemble error.

## Key Contributions

- Generated a diverse synthetic dataset of 324 hospitalisation time-series capturing various disease characteristics and public health responses for epidemic forecasting evaluation.
- Evaluated 14 component models and 6 ensembles, showing mechanistic models improve in relative accuracy over statistical models when moving from 7-day to 14-day horizons.
- Demonstrated that a novel adaptive ensemble method and a median ensemble outperform individual component models on synthetic outbreak data.
- Showed that the coefficient of variation among component forecasts is predictive of future ensemble error, enabling confidence assignment at prediction time.

## Open Questions & Future Work

- [[epidemic-ensemble-spread-skill-relationship]]
- [[generalizability-of-adaptive-ensembles]]

## Archivist Review

Adhered strictly to the scarcity policy and high selectivity criteria. The paper evaluates epidemiological forecasts using synthetic outbreaks and compares ensemble methods, but the specific adaptive ensemble and synthetic datasets are paper-local or incremental variants of standard ensemble weighting and generation techniques. Two open questions regarding ensemble spread-skill relationships and adaptive ensemble generalizability were evaluated; one was retained and the duplicate filtered against existing vault entries.

### Approved Open Questions
- Spread-Skill Relationship in Ensembles: Understanding the spread-skill relationship in epidemiological ensembles is vital for reliably quantifying prediction uncertainty and assigning confidence intervals to public health forecasts during active outbreaks.
- Generalizability of Adaptive Ensembles: Assessing the robustness and generalizability of adaptive weighting schemes ensures that public health decision support tools remain reliable when applied to emerging pathogens with different transmission characteristics.

### Rejected Candidates
- [open_question] Spread-Skill Relationship in Ensembles (`epidemic-ensemble-spread-skill-relationship`) - duplicate_existing: Duplicate of existing ensemble uncertainty/spread-skill concepts in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2503.22494)
- [PDF](https://arxiv.org/pdf/2503.22494)

