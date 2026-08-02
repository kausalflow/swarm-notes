---
# CSL-compatible fields
title: "Complementary Matrix-Gated QKAN Fast-Weight Programmers for Quantum Dynamics Forecasting"
author:
  - literal: "K. C. Peng"
  - literal: "Samuel Yen-Chi Chen"
  - literal: "Jiun-Cheng Jiang"
  - literal: "Chen-Yu Liu"
  - literal: "En-Jui Kuo"
  - literal: "Yun-Yuan Wang"
  - literal: "Tzung-Chi Huang"
  - literal: "Prayag Tiwari"
  - literal: "Chi-Sheng Chen"
  - literal: "Chun-Hua Lin"
  - literal: "Yu‐Chao Hsu"
  - literal: "Tai-Yue Li"
  - literal: "Saif Al-Kuwari"
  - literal: "Simon See"
  - literal: "Kuan-Cheng Chen"
  - literal: "Nan-Yow Chen"
  - literal: "Hsi-Sheng Goan"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.27945"

# Custom fields
paper_id: "2607.27945"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
  - "sequence-modeling"
  - "quantum-dynamics"
architectures:
  []
datasets:
  []
concept_slugs:
  - "complementary-matrix-gating"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:27:02Z"
created_at: "2026-08-02T07:27:02Z"
---

# Complementary Matrix-Gated QKAN Fast-Weight Programmers for Quantum Dynamics Forecasting

**Authors**: K. C. Peng, Samuel Yen-Chi Chen, Jiun-Cheng Jiang, Chen-Yu Liu, En-Jui Kuo, Yun-Yuan Wang, Tzung-Chi Huang, Prayag Tiwari, Chi-Sheng Chen, Chun-Hua Lin, Yu‐Chao Hsu, Tai-Yue Li, Saif Al-Kuwari, Simon See, Kuan-Cheng Chen, Nan-Yow Chen, Hsi-Sheng Goan
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.27945](https://arxiv.org/abs/2607.27945)

## Summary

This paper introduces Self-Modulating Quantum-inspired Kolmogorov-Arnold Network (QKAN) Fast-Weight Programmers (FWPs) equipped with Complementary Matrix Gating (CMG) to overcome the limitations of scalar retention-write balances in sequence modeling. By using a sigmoid matrix gate for retaining the old state and its complement for writing new proposals, CMG enables coordinate-wise memory control while preserving the affine prefix-scan structure. Evaluations on quantum dynamics forecasting (Jaynes-Cummings and transmon-resonator systems) and single-step benchmarks show that CMG models reduce mean-squared error by at least 91.2% compared to scalar-gated counterparts.

## Key Contributions

- Introduced Self-Modulating QKAN-based Fast-Weight Programmers (FWPs) using low-rank element-wise modulation to overcome scalar gating limitations.
- Proposed Complementary Matrix Gating (CMG), using a sigmoid matrix gate and its complement to provide coordinate-wise memory control while retaining parallel prefix-scan properties.
- Demonstrated consistent forecasting improvements across seven single-step benchmarks and five sequence lengths for QKAN-based FWP architectures.
- Achieved low mean-squared errors on the order of 0.001 or lower in direct multi-step forecasting of Jaynes-Cummings and transmon-resonator quantum dynamics, outperforming scalar-gated baselines by at least 91.2%.

## Limitations

Limited to architectures incorporating quantum-inspired Kolmogorov-Arnold networks and evaluated specifically on simulated quantum dynamics and standard time-series forecasting benchmarks.

## Open Questions & Future Work

- [[spatiotemporal-complementary-matrix-gating]]

## Key Concepts

- [[complementary-matrix-gating]]: A matrix-gated update mechanism for fast-weight programmers that uses a sigmoid matrix gate and its complement for coordinate-wise retention and write control.

## Archivist Review

Approved the central matrix-gating mechanism and its spatio-temporal open question while pruning the architecture-specific variant to maintain high selectivity in the vault.

### Approved Concepts
- Complementary Matrix Gating: Introduces coordinate-wise memory control for fast-weight programmers while preserving bounded convex updates and parallelizable prefix-scan structure.

### Approved Open Questions
- Spatiotemporal Complementary Matrix Gating: Extends the applicability of QKAN fast-weight programmers from univariate time-series to complex multi-variable spatiotemporal quantum systems.

### Rejected Candidates
- [concept] Self-Modulating QKAN-based FWPs (`self-modulating-qkan-based-fwps`) - subcomponent_of_broader_mechanism: Subcomponent of broader mechanism or specialized derivative heavily tied to QKAN architectures rather than a standalone general concept.

## Links

- [Abstract](https://arxiv.org/abs/2607.27945)
- [PDF](https://arxiv.org/pdf/2607.27945)

