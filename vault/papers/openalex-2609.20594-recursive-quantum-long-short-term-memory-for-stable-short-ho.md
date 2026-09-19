---
# CSL-compatible fields
title: "Recursive Quantum Long Short-Term Memory for Stable Short-Horizon Temperature Forecasting"
author:
  - literal: "Mu-En Lee"
  - literal: "Yen-Ku Liu"
  - literal: "Samuel Yen-Chi Chen"
  - literal: "Yun-Cheng Tsai"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.20594"

# Custom fields
paper_id: "2609.20594"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "recurrent-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-19T09:04:23Z"
created_at: "2026-09-19T09:04:23Z"
---

# Recursive Quantum Long Short-Term Memory for Stable Short-Horizon Temperature Forecasting

**Authors**: Mu-En Lee, Yen-Ku Liu, Samuel Yen-Chi Chen, Yun-Cheng Tsai
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.20594](https://arxiv.org/abs/2609.20594)

## Summary

This paper investigates a recursive quantum long short-term memory (QLSTM) architecture for short-horizon daily minimum and maximum temperature forecasting. Using weather data from Toronto across multiple input windows and 20 random seeds, the authors demonstrate that recursive quantum feature transformations achieve faster convergence, higher predictive accuracy (lower MAE and RMSE), and a smaller generalization gap than standard QLSTM models. These findings highlight the efficacy of recursive quantum-classical designs for stable time-series forecasting.

## Key Contributions

- Evaluates a recursive QLSTM architecture against standard QLSTM for one-step-ahead daily minimum and maximum temperature forecasting across input windows of 8, 16, and 32 days over 20 random seeds.
- Demonstrates that the recursive model consistently reaches near-optimal test loss earlier, reduces MAE and RMSE, and exhibits a smaller generalization gap compared to standard QLSTM.
- Shows that recursive quantum feature transformations improve stability and out-of-sample performance for compact hybrid quantum-classical temporal models using weather observations from Toronto.

## Limitations

Evaluated specifically on temperature forecasting with short-horizon input windows and compact hybrid architectures.

## Open Questions & Future Work

- [[evaluating-robustness-of-recursive-qlstm]]

## Archivist Review

The paper explores a recursive variant of Quantum LSTM for temperature forecasting. While it presents empirical evaluations across seeds and window sizes, the core technique is a paper-local modification of QLSTM rather than a broad, reusable forecasting mechanism. Therefore, concepts are rejected. One open question regarding the hardware and dataset robustness of recursive QLSTMs was evaluated; however, given the specialized and niche nature of hybrid quantum-classical architectures, we maintain high selectivity and reject it as well to avoid cluttering the vault with narrow hardware-dependent explorations.

### Approved Open Questions
- Evaluating Recursive QLSTM Robustness: Determining the scalability and robustness of hybrid quantum-classical sequential models across varied real-world operating conditions and hardware backends is essential to substantiate quantum advantage in machine learning.

### Rejected Candidates
- [open_question] Evaluating Recursive QLSTM Robustness (`evaluating-robustness-of-recursive-qlstm`) - low_impact: The proposed hybrid quantum LSTM architecture is too narrow and experimental to justify permanent vault entries under strict scarcity and novelty standards.

## Links

- [Abstract](https://arxiv.org/abs/2609.20594)
- [PDF](https://arxiv.org/pdf/2609.20594)

