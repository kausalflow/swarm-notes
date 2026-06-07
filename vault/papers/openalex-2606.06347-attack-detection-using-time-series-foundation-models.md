---
# CSL-compatible fields
title: "Attack Detection using Time Series Foundation Models"
author:
  - literal: "S.C. Anand"
  - literal: "Anh Tung Nguyen"
  - literal: "George J. Pappas"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06347"

# Custom fields
paper_id: "2606.06347"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "language-model"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:18:58Z"
created_at: "2026-06-07T08:18:58Z"
---

# Attack Detection using Time Series Foundation Models

**Authors**: S.C. Anand, Anh Tung Nguyen, George J. Pappas
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06347](https://arxiv.org/abs/2606.06347)

## Summary

This paper presents a model-structure-free approach to attack detection in cyber-physical systems by utilizing the TimesFM foundation model. The authors analytically derive optimal stealthy attack policies for both linear and nonlinear systems and evaluate a zero-shot TimesFM-based detector on the IEEE 14-bus power system. Results show that this framework effectively identifies both replay and model-based stealthy attacks, while also enabling the mitigation of corrupted sensor data through predictive imputation.

## Key Contributions

- Formulates closed-form optimal stealthy attack policies for both linear and nonlinear systems against chi-squared detectors.
- Introduces a model-structure-free attack detection framework leveraging TimesFM as a zero-shot surrogate residual generator.
- Demonstrates that time-series foundation model predictions provide effective sensor data imputation in the presence of malicious network corruption.

## Open Questions & Future Work

- [[foundation-model-attack-detection-robustness]]

## Archivist Review

The paper explores using a pre-trained time-series foundation model as a surrogate for anomaly detection in cyber-physical systems. While interesting, no new standalone concepts were identified that merit permanent addition to the vault, as the primary mechanism is the application of an existing model (TimesFM) to a new domain. I approved the open question regarding the theoretical robustness of such detectors against adaptive adversaries, as it poses a significant long-term challenge for using foundation models in security-critical applications.

### Approved Open Questions
- Robustness of Foundation-Model-Based Detectors: This is technically crucial because relying solely on empirical success against standard attacks may lead to a false sense of security; understanding the theoretical limits of foundation-model-based detection against adaptive threats is essential for developing resilient cyber-physical security architectures.

### Rejected Candidates
- [dataset] IEEE 14-bus power system (`ieee-14-bus-power-system`) - low_impact: The IEEE 14-bus system is a standard synthetic test case, not a uniquely novel or critical dataset that requires a standalone archive note.

## Links

- [Abstract](https://arxiv.org/abs/2606.06347)
- [PDF](https://arxiv.org/pdf/2606.06347)

