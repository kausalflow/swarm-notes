---
# CSL-compatible fields
title: "Learning Temporal Patterns in Financial Time Series: A Comparative Study of Quantum LSTM and Quantum Reservoir Computing"
author:
  - literal: "Danyal Maheshwari"
  - literal: "Gerhard Hellstern"
  - literal: "Martin Zaefferer"
  - literal: "Martin Braun"
  - literal: "Tanja Döhler"
issued:
  date-parts:
    - [2026, 5, 4]
url: "https://arxiv.org/abs/2605.02656"

# Custom fields
paper_id: "2605.02656"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "quantum-reservoir-computing"
  - "finance"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-07T07:37:13Z"
created_at: "2026-05-07T07:37:13Z"
---

# Learning Temporal Patterns in Financial Time Series: A Comparative Study of Quantum LSTM and Quantum Reservoir Computing

**Authors**: Danyal Maheshwari, Gerhard Hellstern, Martin Zaefferer, Martin Braun, Tanja Döhler
**Date**: 2026-05-04
**Paper ID**: [openalex:2605.02656](https://arxiv.org/abs/2605.02656)

## Summary

This paper investigates the performance of quantum-classical hybrid models—specifically Quantum Long Short-Term Memory (QLSTM) and Quantum Reservoir Computing (QRC)—for financial time-series forecasting. By employing amplitude encoding for lag structures, the authors evaluate these quantum-enhanced architectures against classical baselines under constrained qubit settings. The results indicate that while quantum models match classical performance on univariate data, they exhibit superior predictive capability in multivariate scenarios with correlated inputs.

## Key Contributions

- Conducted a comparative evaluation of QLSTM and QRC against classical counterparts for financial time-series forecasting.
- Demonstrated that quantum-enhanced architectures reach parity with classical baselines in univariate settings.
- Identified that quantum models offer performance advantages over classical models in multivariate regimes with correlated inputs when utilizing expressive amplitude encoding.

## Open Questions & Future Work

- [[quantum-recurrent-scaling-advantage]]

## Archivist Review

The paper conducts a comparative analysis of quantum-enhanced architectures in time-series forecasting. 'Quantum Reservoir Computing' is already represented in the vault, so it was not approved as a new concept. The open question regarding quantum recurrent scaling was approved as it provides a clear, technically grounded research trajectory for hybrid time-series modeling.

### Approved Open Questions
- Scalability and Advantage of Quantum Recurrent Models: The lack of a clear, universal quantum advantage in time-series forecasting necessitates a deeper understanding of the trade-offs between quantum architectural complexity and classical computational efficiency, particularly as hardware capabilities evolve. Identifying the specific conditions for competitive advantage is essential for guiding future developments in quantum machine learning.

### Rejected Candidates
- [concept] Quantum Reservoir Computing (QRC) (`quantum-reservoir-computing-qrc`) - duplicate_existing: This concept is already present in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2605.02656)
- [PDF](https://arxiv.org/pdf/2605.02656)

