---
# CSL-compatible fields
title: "MoveBench: A Benchmark for Global-Scale Wildlife Movement Forecasting"
author:
  - literal: "Justin Kay"
  - literal: "Shir Bar"
  - literal: "Ellen O. Aikens"
  - literal: "Martin Becker"
  - literal: "Francesca Cagnacci"
  - literal: "Juliet Cohen"
  - literal: "Scott W. Forrest"
  - literal: "Jessica Kendall-Bar"
  - literal: "Madeleine Lucas"
  - literal: "Macon Overcast"
  - literal: "Meredith S. Palmer"
  - literal: "Will Rogers"
  - literal: "Nicholas J. Russo"
  - literal: "Christian Rutz"
  - literal: "Larissa T. Beumer"
  - literal: "Michael Brown"
  - literal: "Ying‐Chi Chan"
  - literal: "Sarah C. Davidson"
  - literal: "Diego Ellis Soto"
  - literal: "Anne G. Hertel"
  - literal: "Roland Kays"
  - literal: "Benjamin Koger"
  - literal: "Guram Mikaberidze"
  - literal: "Thomas Mueller"
  - literal: "Ruth Oliver"
  - literal: "Thorsten Papenbrock"
  - literal: "Robert Patchett"
  - literal: "Jared A. Stabach"
  - literal: "D.J. Taylor"
  - literal: "Scott W. Yanco"
  - literal: "Sara Beery"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15780"

# Custom fields
paper_id: "2609.15780"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  - "MoveBench"
concept_slugs:
  - "movebench"
dataset_slugs:
  - "movebench"
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:44:02Z"
created_at: "2026-09-17T09:44:02Z"
---

# MoveBench: A Benchmark for Global-Scale Wildlife Movement Forecasting

**Authors**: Justin Kay, Shir Bar, Ellen O. Aikens, Martin Becker, Francesca Cagnacci, Juliet Cohen, Scott W. Forrest, Jessica Kendall-Bar, Madeleine Lucas, Macon Overcast, Meredith S. Palmer, Will Rogers, Nicholas J. Russo, Christian Rutz, Larissa T. Beumer, Michael Brown, Ying‐Chi Chan, Sarah C. Davidson, Diego Ellis Soto, Anne G. Hertel, Roland Kays, Benjamin Koger, Guram Mikaberidze, Thomas Mueller, Ruth Oliver, Thorsten Papenbrock, Robert Patchett, Jared A. Stabach, D.J. Taylor, Scott W. Yanco, Sara Beery
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15780](https://arxiv.org/abs/2609.15780)

## Summary

Understanding and predicting wildlife movement is critical for ecology, but existing trajectory forecasting methods lack standardized evaluation on unconstrained, stochastic animal paths. To bridge this gap, the authors introduce MoveBench, a global-scale benchmark comprising 2.6M GPS locations across 110 species paired with 1.6B environmental raster tiles, along with a probabilistic evaluation protocol. Through comprehensive evaluation of four method families, the study reveals that current models generalize better to future timepoints than to unseen individuals, deep learning approaches do not universally surpass simpler baselines, and environmental covariates strongly impact performance.

## Key Contributions

- Introduced MoveBench, the first large-scale global benchmark for probabilistic wildlife movement forecasting spanning 2.6M GPS locations across 110 species and 127 countries paired with 1.6B environmental raster tiles.
- Proposed a probabilistic evaluation protocol designed specifically for stochastic wildlife trajectories to overcome the limitations of point-prediction metrics.
- Conducted a comprehensive empirical evaluation of four forecasting method families, revealing key insights regarding generalization to unseen individuals versus future timepoints and the impact of environmental covariate selection.

## Limitations

Existing predictive methods struggle to generalize to unseen individuals compared to future timepoints, and deep learning approaches do not consistently outperform simpler baselines on this stochastic task.

## Open Questions & Future Work

- [[cross-individual-generalization-wildlife-movement]]

## Key Concepts

- [[movebench]]: The first large-scale global benchmark for probabilistic wildlife movement forecasting containing millions of GPS locations and high-resolution environmental covariates.

## Archivist Review

Approved the core benchmark concept and dataset 'MoveBench' along with the open question regarding cross-individual generalization in wildlife forecasting, adhering strictly to the sparsity and novelty review policies.

### Approved Concepts
- MoveBench: It establishes the first standardized, large-scale global benchmark for probabilistic wildlife movement forecasting, encompassing diverse species, geographies, and high-resolution environmental covariates.

### Approved Open Questions
- Cross-Individual Generalization in Wildlife Movement: Understanding out-of-domain generalization across unseen individuals is crucial for deploying ecological forecasting models in conservation settings where target animal populations are unlabelled or unmonitored during training.

### Rejected Candidates
- [concept] Probabilistic Evaluation Protocol for Movement Trajectory Forecasts (`probabilistic-evaluation-protocol-for-movement`) - subcomponent_of_broader_mechanism: Standard probabilistic evaluation metrics and protocols are widely used across time series and trajectory forecasting, making this too specific to a benchmark wrapper rather than a distinct reusable ML technique.

## Datasets

- [[movebench]]

## Links

- [Abstract](https://arxiv.org/abs/2609.15780)
- [PDF](https://arxiv.org/pdf/2609.15780)

