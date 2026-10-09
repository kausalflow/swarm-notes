---
# CSL-compatible fields
title: "ProtocolMatch: Protocol-Dependent Model Selection for Scientific Dynamics Forecasting"
author:
  - literal: "Lu Wei"
  - literal: "Yufeng Wang"
  - literal: "Haibin Ling"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.10239"

# Custom fields
paper_id: "2610.10239"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "protocolmatch"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:35:26Z"
created_at: "2026-10-09T11:35:26Z"
---

# ProtocolMatch: Protocol-Dependent Model Selection for Scientific Dynamics Forecasting

**Authors**: Lu Wei, Yufeng Wang, Haibin Ling
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.10239](https://arxiv.org/abs/2610.10239)

## Summary

This paper demonstrates that model selection for scientific dynamics forecasting depends heavily on evaluation protocols such as observed history, rollout feedback, compute budget, physical objectives, and test distribution, rather than architecture alone. To address this, the authors introduce ProtocolMatch, a compute-matched, validation-selected, and failure-preserving evaluation framework. Experiments on driven quantum-spin dynamics reveal that model rankings and error characteristics reverse or shift drastically depending on these protocol choices, highlighting the necessity of reporting accuracy, physical validity, and shifted-distribution reliability separately.

## Key Contributions

- Formulated protocol-dependent model selection for scientific dynamics forecasting, integrating observed history, rollout feedback, compute budget, physical objectives, and test distribution.
- Introduced ProtocolMatch, a compute-matched, validation-selected, and failure-preserving evaluation framework.
- Demonstrated through driven quantum-spin dynamics experiments that model rankings heavily depend on evaluation protocols, such as training set size, history length, closed-loop versus refreshed-loop rollout, and distribution shifts.

## Limitations

Evaluated specifically on driven quantum-spin dynamics; generalization to broader physical simulation domains remains to be fully explored.

## Open Questions & Future Work

- [[scaling-to-large-scale-open-systems]]

## Key Concepts

- [[protocolmatch]]: A compute-matched, validation-selected, and failure-preserving evaluation framework for scientific dynamics forecasting.

## Archivist Review

Approved the core evaluation framework 'ProtocolMatch' as a distinct, reusable methodology for scientific dynamics forecasting, along with its primary open scaling question. Rejected generic domain phrases.

### Approved Concepts
- ProtocolMatch: ProtocolMatch is the central framework introduced in the paper for protocol-dependent model selection in scientific dynamics forecasting.

### Approved Open Questions
- Scaling to Large-Scale Open Systems: Scaling model-selection protocols to large-scale, noisy, and open quantum systems is critical for understanding whether observed ranking reversals and failure-sensitivity findings persist in realistic physical deployment scenarios.

### Rejected Candidates
- [concept] Scientific Dynamics Forecasting (`scientific-dynamics-forecasting`) - subcomponent_of_broader_mechanism: Too broad and descriptive of the application domain rather than a specific algorithmic contribution.

## Links

- [Abstract](https://arxiv.org/abs/2610.10239)
- [PDF](https://arxiv.org/pdf/2610.10239)

