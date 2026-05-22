---
# CSL-compatible fields
title: "BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics"
author:
  - literal: "Siddharth Viswanath"
  - literal: "Panayiotis Ketonis"
  - literal: "Chen Liu"
  - literal: "Michael Perlmutter"
  - literal: "Dhananjay Bhaskar"
  - literal: "Smita Krishnaswamy"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.19324"

# Custom fields
paper_id: "2605.19324"
paper_source: "openalex"
domain: "biology"
tags:
  - "neural-architecture-search"
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "braindyn"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:18:14Z"
created_at: "2026-05-22T08:18:14Z"
---

# BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics

**Authors**: Siddharth Viswanath, Panayiotis Ketonis, Chen Liu, Michael Perlmutter, Dhananjay Bhaskar, Smita Krishnaswamy
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.19324](https://arxiv.org/abs/2605.19324)

## Summary

BrainDyn is a generative model designed to simulate brain-like dynamic activity by combining sheaf theory with neural ordinary differential equations (neural ODEs). By projecting historical regional activity into stalks and using sheaf Laplacians to regulate message passing, the model captures complex, anatomically-aligned brain dynamics. It demonstrates high efficacy in forecasting across heterogeneous modalities, including resting-state fMRI, epileptic EEG, and simulated spiking networks, while supporting downstream perturbation analysis.

## Key Contributions

- Introduces BrainDyn, a sheaf-theoretic neural ODE model that incorporates anatomical brain structure into continuous-time dynamic modeling.
- Utilizes LSTM-based stalk projections and sheaf Laplacians to enable expressive message passing between brain regions.
- Demonstrates superior forecasting performance on fMRI (PNC), scalp EEG (TUSZ), and synthetic NEST data compared to non-structural baselines.
- Enables in silico perturbation prediction by learning the underlying generative dynamics of neuronal activity.

## Open Questions & Future Work

- [[generalizing-to-stimulus-driven-dynamics]]

## Key Concepts

- [[braindyn]]: A sheaf neural ODE architecture that captures continuous-time brain activity dynamics by incorporating structural brain graph constraints through sheaf Laplacians.

## Archivist Review

The paper introduces a compelling synthesis of sheaf theory and neural ODEs for dynamic modeling on structured graphs, which I have approved as a core architectural concept. I also approved the identified open question regarding stimulus-driven generalization, as it addresses a substantive architectural limitation relevant to generative modeling beyond this domain. Other candidates were rejected to adhere to the scarcity policy and avoid domain-specific dataset entries.

### Approved Concepts
- BrainDyn: Central architecture integrating sheaf theory with neural ODEs for modeling brain dynamics.

### Approved Open Questions
- Generalizing to stimulus-driven dynamics: The transition from modeling intrinsic resting-state activity to modeling stimulus-evoked or task-related dynamics is essential for creating a truly versatile virtual brain model. This is a critical next step for researchers seeking to use these generative frameworks for cognitive or task-based neuroscience applications.

## Links

- [Abstract](https://arxiv.org/abs/2605.19324)
- [PDF](https://arxiv.org/pdf/2605.19324)

