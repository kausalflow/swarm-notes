---
# CSL-compatible fields
title: "QuaMoE-DRF: Proactive Beam and Rate Adaptation via Multimodal Dynamic Radio Map Forecasting in ISAC Networks"
author:
  - literal: "Zhihan Zeng"
  - literal: "Kaihe Wang"
  - literal: "Zhongpei Zhang"
  - literal: "Chongwen Huang"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00974"

# Custom fields
paper_id: "2607.00974"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "multimodal"
  - "mixture-of-experts"
  - "moe"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quality-aware-mixture-of-experts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:36:27Z"
created_at: "2026-07-04T07:36:27Z"
---

# QuaMoE-DRF: Proactive Beam and Rate Adaptation via Multimodal Dynamic Radio Map Forecasting in ISAC Networks

**Authors**: Zhihan Zeng, Kaihe Wang, Zhongpei Zhang, Chongwen Huang
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00974](https://arxiv.org/abs/2607.00974)

## Summary

QuaMoE-DRF is a framework for proactive beam and rate adaptation in ISAC networks by forecasting future beam-SINR fields. It fuses static geometry, motion data, sensing states, and wireless history using a quality-aware mixture-of-experts module designed for heteroscedastic modality errors. The model predicts communication-oriented map channels to enable optimal BS, beam, and MCS selection, significantly outperforming existing baselines in urban dynamic environments.

## Key Contributions

- Introduced QuaMoE-DRF, a quality-aware multimodal dynamic radio map forecasting framework that predicts future beam-SINR fields for proactive ISAC network control.
- Developed a quality-aware mixture-of-experts module based on inverse-variance fusion to effectively handle heteroscedastic modality errors in multi-source sensor fusion.
- Demonstrated that the multi-BS beam-SINR field is sufficient for key network decisions, achieving a 5.67% effective rate increase and 8.35% outage reduction on a dynamic urban ISAC benchmark.

## Open Questions & Future Work

- [[validation-of-dynamic-radio-maps]]

## Key Concepts

- [[quality-aware-mixture-of-experts]]: A mixture-of-experts architecture that uses inverse-variance weighting to account for heteroscedastic errors across multiple input modalities.

## Archivist Review

The review focuses on the core fusion mechanism (QuaMoE) rather than the specific ISAC framework name, as the former is a generic and reusable methodology for handling noisy, multimodal time-series inputs. The open question is approved for its focus on the methodology of validating predictive radio maps, which is a significant bottleneck in ISAC research. All other candidates were rejected as being either paper-local implementations or not sufficiently novel/generalizable for the vault.

### Approved Concepts
- Quality-Aware Mixture-of-Experts (QuaMoE): Provides a robust, theoretically-grounded method for multi-modal sensor fusion in the presence of noise and heteroscedastic modality reliability.

### Approved Open Questions
- Validating Dynamic Radio Maps: Validation of predictive network maps is essential for moving beyond simulation-based optimization and identifying failure modes in real-world ISAC deployments.

### Rejected Candidates
- [concept] QuaMoE-DRF (`quamoe-drf`) - subcomponent_of_broader_mechanism: This is the name of the specific framework proposed, and it is better captured by the underlying mechanism (QuaMoE).

## Links

- [Abstract](https://arxiv.org/abs/2607.00974)
- [PDF](https://arxiv.org/pdf/2607.00974)

