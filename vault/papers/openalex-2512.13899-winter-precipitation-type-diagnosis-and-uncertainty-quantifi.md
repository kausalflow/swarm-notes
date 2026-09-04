---
# CSL-compatible fields
title: "Winter Precipitation Type Diagnosis and Uncertainty Quantification with a Physically Consistent Machine Learning Method"
author:
  - literal: "Charles Becker"
  - literal: "David John Gagne"
  - literal: "Julie L. Demuth"
  - literal: "John S. Schreck"
  - literal: "Jacob Radford"
  - literal: "Gabrielle Gantos"
  - literal: "Eliot Kim"
  - literal: "Dhamma Kimpara"
  - literal: "S Reiner"
  - literal: "Justin Willson"
  - literal: "Christopher D. Wirz"
issued:
  date-parts:
    - [2026, 9, 2]
url: "https://arxiv.org/abs/2512.13899"

# Custom fields
paper_id: "2512.13899"
paper_source: "openalex"
domain: "time-series"
tags:
  - "uncertainty-quantification"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-04T09:11:29Z"
created_at: "2026-09-04T09:11:29Z"
---

# Winter Precipitation Type Diagnosis and Uncertainty Quantification with a Physically Consistent Machine Learning Method

**Authors**: Charles Becker, David John Gagne, Julie L. Demuth, John S. Schreck, Jacob Radford, Gabrielle Gantos, Eliot Kim, Dhamma Kimpara, S Reiner, Justin Willson, Christopher D. Wirz
**Date**: 2026-09-02
**Paper ID**: [openalex:2512.13899](https://arxiv.org/abs/2512.13899)

## Summary

This paper introduces an evidential neural network for winter precipitation type diagnosis that outputs calibrated probabilities and epistemic uncertainty from a single model run. Trained on curated crowd-sourced mPING observations and NOAA Rapid Refresh thermodynamic profiles, the model effectively identifies precipitation transitions while capturing thermodynamic ambiguity. Evaluations and case studies demonstrate superior operational utility and physical consistency compared to traditional deterministic methods.

## Key Contributions

- Developed an evidential neural network that predicts calibrated multi-class probabilities and epistemic uncertainty for winter precipitation types at standard neural network computational cost.
- Trained and evaluated on quality-controlled crowd-sourced mPING observations paired with NOAA Rapid Refresh vertical thermodynamic profiles.
- Demonstrated superior or comparable success ratios compared to area-based deterministic methods, especially for freezing rain and ice pellets.
- Showed that model prediction errors are physically structured in interpretable diagnostic spaces corresponding to thermodynamic ambiguity.

## Archivist Review

After careful review, no concepts, datasets, or open questions met the strict reusability and impact standards required for permanent vault inclusion. The proposed open question is too application-specific and lacks broader cross-domain methodological weight.

### Rejected Candidates
- [open_question] Multi-label Evidential Neural Networks (`multi-label-evidential-neural-networks-for-mixed-precipitation`) - low_impact: Future work proposing a multi-label extension for precipitation classification is paper-internal and specific to a niche meteorological application.

## Links

- [Abstract](https://arxiv.org/abs/2512.13899)
- [PDF](https://arxiv.org/pdf/2512.13899)

