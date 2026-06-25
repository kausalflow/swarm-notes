---
# CSL-compatible fields
title: "Temporal-Spectral Alignment with Frequency Adaptation for Source-Free Time-Series Adaptation"
author:
  - literal: "Shichang Meng"
  - literal: "Linquan Wu"
  - literal: "Xuan Ai"
  - literal: "Linqi Song"
issued:
  date-parts:
    - [2026, 6, 22]
url: "https://arxiv.org/abs/2606.23120"

# Custom fields
paper_id: "2606.23120"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "domain-adaptation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "temporal-spectral-alignment-with-frequency-adaptation-safa"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:16:53Z"
created_at: "2026-06-25T08:16:53Z"
---

# Temporal-Spectral Alignment with Frequency Adaptation for Source-Free Time-Series Adaptation

**Authors**: Shichang Meng, Linquan Wu, Xuan Ai, Linqi Song
**Date**: 2026-06-22
**Paper ID**: [openalex:2606.23120](https://arxiv.org/abs/2606.23120)

## Summary

This paper addresses the challenge of source-free domain adaptation (SFDA) for time-series data, where source data is unavailable for adaptation. The authors introduce Temporal-Spectral Alignment with Frequency Adaptation (SAFA), which explicitly tackles spectral shifts alongside traditional temporal drifts. By employing a frequency adaptation module that dynamically modulates the phase and amplitude of target signals, SAFA effectively aligns the target domain with the pre-trained source distribution. Empirical evaluations confirm that the proposed approach improves robustness and adaptation performance on benchmark time-series tasks.

## Key Contributions

- Introduces the SAFA framework, which jointly models source temporal dependencies and spectral characteristics.
- Proposes a frequency adaptation module to bridge domain gaps by modulating phase and amplitude, overcoming feature shift and temporal drift without access to source data.
- Demonstrates superior performance and robustness of SAFA compared to state-of-the-art methods on multiple time-series benchmark datasets.

## Open Questions & Future Work

- [[spectral-shift-generalization-sfda]]

## Key Concepts

- [[temporal-spectral-alignment-with-frequency-adaptation-safa]]: A source-free time-series domain adaptation framework that aligns target signals with source distributions by modulating phase and amplitude in the frequency domain.

## Archivist Review

I approved the SAFA framework as a distinct approach to frequency-domain alignment for source-free adaptation, and the open question regarding spectral shift generalization as it identifies a substantive, non-trivial research gap in the field of time-series domain adaptation. I rejected other candidates or sub-components as they were either already covered by broader mechanisms or were too local to the paper's specific implementation. The review adhered to the selective requirements by focusing on mechanisms and unresolved structural bottlenecks rather than generic performance claims.

### Approved Concepts
- Temporal-Spectral Alignment with Frequency Adaptation (SAFA): It provides a novel mechanism for addressing spectral shifts alongside temporal drift in source-free settings, which is a neglected but critical aspect of time-series adaptation.

### Approved Open Questions
- Addressing Spectral Shifts in SFDA: Spectral shifts are a fundamental, often overlooked component of time-series domain shift, and robustifying SFDA against these variations is critical for sensor-based applications.

## Links

- [Abstract](https://arxiv.org/abs/2606.23120)
- [PDF](https://arxiv.org/pdf/2606.23120)

