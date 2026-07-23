---
# CSL-compatible fields
title: "Beyond the Edge of Chaos: Stability-Expressivity Transfer in Reservoir Forecasting"
author:
  - literal: "Yao Du"
  - literal: "Xingang Wang"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.17909"

# Custom fields
paper_id: "2607.17909"
paper_source: "openalex"
domain: "time-series"
tags:
  - "recurrent-neural-network"
  - "forecasting"
  - "dynamical-systems"
  - "chaos"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "stability-expressivity-transfer-index"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:26:57Z"
created_at: "2026-07-23T07:26:57Z"
---

# Beyond the Edge of Chaos: Stability-Expressivity Transfer in Reservoir Forecasting

**Authors**: Yao Du, Xingang Wang
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.17909](https://arxiv.org/abs/2607.17909)

## Summary

The authors investigate the limitations of the classic edge-of-chaos heuristic in reservoir computing and introduce a stability-expressivity transfer index to find the optimal spectral radius. By analyzing the collective dynamics of teacher-forced reservoirs, they show that target dynamics are captured by stable Lyapunov modes modulated by inputs. The proposed index accurately predicts the optimal spectral radius for autonomous forecasting across chaotic and quasiperiodic targets.

## Key Contributions

- Demonstrated that the optimal spectral radius for reservoir forecasting does not coincide with the traditional Lyapunov edge of chaos.
- Discovered that target dynamics are primarily represented by stable Lyapunov modes whose finite-time stability is modulated by the input.
- Proposed the stability-expressivity transfer index to accurately identify the optimal spectral radius across chaotic and quasiperiodic targets for autonomous forecasting.

## Open Questions & Future Work

- [[role-of-marginal-modes-in-reservoir-computing]]

## Key Concepts

- [[stability-expressivity-transfer-index]]: A metric that balances finite-time stability and expressivity of Lyapunov modes to determine the optimal spectral radius for reservoir forecasting.

## Archivist Review

Approved the core conceptual metric (stability-expressivity transfer index) for reservoir computing and the corresponding open question regarding marginal Lyapunov modes. Maintained strict scarcity and alignment with existing vault standards.

### Approved Concepts
- Stability-expressivity transfer index: It provides a novel metric that outperforms the traditional edge-of-chaos heuristic for tuning reservoir computing hyperparameters.

### Approved Open Questions
- Role of Marginal Modes in Reservoir Computing: Understanding marginal modes is critical for connecting microscopic network stability criteria to macroscopic reservoir forecasting capabilities and refining stability-expressivity measures.

## Links

- [Abstract](https://arxiv.org/abs/2607.17909)
- [PDF](https://arxiv.org/pdf/2607.17909)

