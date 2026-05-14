---
# CSL-compatible fields
title: "Estimating Consensus Epidemic Trajectories via a Constrained Power Fréchet Mean with Functional Registration"
author:
  - literal: "Yui Tomo"
  - literal: "Shu Tamano"
  - literal: "Daisuke Yoneoka"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10069"

# Custom fields
paper_id: "2605.10069"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "constrained-power-frechet-mean"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:39:10Z"
created_at: "2026-05-14T07:39:10Z"
---

# Estimating Consensus Epidemic Trajectories via a Constrained Power Fréchet Mean with Functional Registration

**Authors**: Yui Tomo, Shu Tamano, Daisuke Yoneoka
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10069](https://arxiv.org/abs/2605.10069)

## Summary

The paper introduces a method for aggregating multiple epidemiological model outputs by computing a constrained power Fréchet mean with functional registration. By framing SEIR-type compartmental dynamics within a Hilbert space, the authors maintain mechanistic interpretability through explicit differential equation and population constraints during the optimization process. An efficient block-optimization algorithm is provided to estimate these consensus trajectories, offering a robust framework for ensemble model averaging in infectious disease forecasting.

## Key Contributions

- Introduces a constrained power Fréchet mean approach to aggregate multiple SEIR compartmental model solutions into a single consensus trajectory.
- Incorporates differential equation and population-level constraints into the functional estimation to preserve mechanistic interpretability.
- Develops an efficient block-optimization algorithm for performing functional registration and mean estimation in this constrained space.

## Open Questions & Future Work

- [[full-seir-dynamics-integration]]

## Key Concepts

- [[constrained-power-frechet-mean]]: A functional data analysis technique that computes a mean trajectory across multiple model solutions while satisfying mechanistic differential equation and population constraints.

## Archivist Review

The paper contributes a specialized yet reusable framework for ensemble averaging of functional model outputs under structural constraints. I approved the concept as it provides a principled approach to a common problem in scientific forecasting. The open question is approved for its focus on the fundamental trade-off between computational feasibility and physical fidelity in mechanistic modeling.

### Approved Concepts
- Constrained Power Fréchet Mean: This method provides a principled way to perform ensemble averaging of functional model outputs while strictly adhering to system dynamics constraints, offering a bridge between data-driven summarization and mechanistic modeling.

### Approved Open Questions
- Mechanistic Fidelity in Ensembles: Achieving full mechanistic consistency in ensemble forecasting is essential for improving the reliability and physical interpretability of epidemic predictions.

### Rejected Candidates
- [open_question] Integrating Full SEIR Dynamics (`full-seir-dynamics-integration`) - duplicate_existing: Duplicate of the approved item after renaming for better clarity.

## Links

- [Abstract](https://arxiv.org/abs/2605.10069)
- [PDF](https://arxiv.org/pdf/2605.10069)

