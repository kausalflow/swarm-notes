---
# CSL-compatible fields
title: "Probabilistic analysis of scalogram ridges in signal processing"
author:
  - literal: "G Liu"
  - literal: "Yuan-Chung Sheu"
  - literal: "Hau‐Tieng Wu"
issued:
  date-parts:
    - [2026, 4, 14]
url: "https://arxiv.org/abs/2501.00270"

# Custom fields
paper_id: "2501.00270"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-17T06:29:57Z"
created_at: "2026-04-17T06:29:57Z"
---

# Probabilistic analysis of scalogram ridges in signal processing

**Authors**: G Liu, Yuan-Chung Sheu, Hau‐Tieng Wu
**Date**: 2026-04-14
**Paper ID**: [openalex:2501.00270](https://arxiv.org/abs/2501.00270)

## Summary

This paper provides a mathematical framework for understanding scalogram ridges of nonstationary signals under additive Gaussian noise. The authors model these ridges as random processes and prove formal properties such as uniqueness and upper hemicontinuity. By applying maximal inequalities for complex modulus nonstationary Gaussian processes, the study derives probabilistic bounds on ridge deviations, offering a theoretical basis for signal analysis in noisy environments.

## Key Contributions

- Provides a rigorous theoretical foundation for scalogram ridges in nonstationary time series by modeling them as set-valued random processes.
- Establishes the uniqueness of ridge points at individual time instances and proves the upper hemicontinuity of the ridge random process under stationary Gaussian noise.
- Derives explicit probability bounds for ridge deviations between noisy and clean signals based on the signal-to-noise ratio, utilizing maximal inequalities for nonstationary Gaussian processes.

## Open Questions & Future Work

- [[scalogram-ridge-stability-under-spectral-interference]]

## Archivist Review

The paper provides a significant mathematical grounding for a standard signal processing tool, but it does not propose a new, broadly reusable computational architecture or method that warrants a permanent 'concept' note. I have approved one high-level, well-defined open question regarding the stability of these mathematical structures under realistic signal interference, as this is a fundamental research challenge in nonstationary time series analysis.

### Approved Open Questions
- Scalogram ridge stability under spectral interference: These questions represent the primary bottlenecks for applying rigorous scalogram ridge analysis to real-world signals where components often interfere or cross, moving beyond theoretical isolation.

### Rejected Candidates
- [open_question] Ridge extraction and spectral interference (`ridge-extraction-and-spectral-interference`) - other: The title was improved for clarity and to better align with existing vault terminology.

## Links

- [Abstract](https://arxiv.org/abs/2501.00270)
- [PDF](https://arxiv.org/pdf/2501.00270)

