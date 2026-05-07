---
# CSL-compatible fields
title: "Period-conscious Time-series Reconstruction under Local Differential Privacy"
author:
  - literal: "Yaxuan Wang"
  - literal: "Tianxin Li"
  - literal: "Enji Liang"
  - literal: "Yue Fu"
  - literal: "Yanran Wang"
issued:
  date-parts:
    - [2026, 5, 4]
url: "https://arxiv.org/abs/2605.02724"

# Custom fields
paper_id: "2605.02724"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "differential-privacy"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cpr-cycle-and-phase-recovery"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-07T07:36:58Z"
created_at: "2026-05-07T07:36:58Z"
---

# Period-conscious Time-series Reconstruction under Local Differential Privacy

**Authors**: Yaxuan Wang, Tianxin Li, Enji Liang, Yue Fu, Yanran Wang
**Date**: 2026-05-04
**Paper ID**: [openalex:2605.02724](https://arxiv.org/abs/2605.02724)

## Summary

This paper introduces CPR (Cycle and Phase Recovery), a framework designed to reconstruct periodic time series protected by local differential privacy (LDP). By utilizing multi-scale period probing and multi-consensus selection, the method effectively mitigates noise-induced spectral interference and phase drift. Further refinement via EM-based denoising and kernel density estimation enables high-fidelity signal recovery, even when privacy constraints are stringent. Experimental results confirm that CPR outperforms current LDP-based reconstruction techniques in preserving periodic structures.

## Key Contributions

- Proposes CPR, a novel period-aware reconstruction framework that performs multi-scale period probing and multi-consensus selection to suppress LDP noise.
- Integrates phase-matched aggregation with EM-based denoising and kernel density estimation to recover per-phase values.
- Demonstrates superior reconstruction accuracy over standard LDP baselines on periodic datasets, particularly under tight privacy budgets (low-epsilon).

## Open Questions & Future Work

- [[non-stationary-periodic-ldp-reconstruction]]

## Key Concepts

- [[cpr-cycle-and-phase-recovery]]: A period-aware reconstruction framework for periodic time-series data under local differential privacy.

## Archivist Review

The paper offers a novel framework, CPR, which explicitly addresses the unique challenge of reconstructing periodic structures under LDP constraints by combining multi-scale probing and phase-matched aggregation. I approved the CPR framework and the corresponding open question regarding non-stationary signals, as these provide a clear, reusable approach for privacy-preserving time-series analysis and identify a significant gap in the current literature. Other potential candidates were rejected for being subcomponents or generic descriptions.

### Approved Concepts
- Cycle and Phase Recovery (CPR): This framework provides a specialized approach to signal reconstruction by explicitly leveraging phase-matched aggregation and consensus mechanisms, which is a departure from standard LDP noise-reduction techniques.

### Approved Open Questions
- Handling non-stationary periodic signals: This is a fundamental bottleneck for deploying privacy-preserving signal processing in real-world, non-static environments where signal periodicity is dynamic.

## Links

- [Abstract](https://arxiv.org/abs/2605.02724)
- [PDF](https://arxiv.org/pdf/2605.02724)

