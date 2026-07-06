---
# CSL-compatible fields
title: "Information-theoretic grid topology reconstruction using low-precision smart meter data"
author:
  - literal: "Daniel T. Speckhard"
issued:
  date-parts:
    - [2026, 7, 3]
url: "https://arxiv.org/abs/2505.11517"

# Custom fields
paper_id: "2505.11517"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "information-extraction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "information-theoretic-grid-topology-reconstruction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-06T08:54:54Z"
created_at: "2026-07-06T08:54:54Z"
---

# Information-theoretic grid topology reconstruction using low-precision smart meter data

**Authors**: Daniel T. Speckhard
**Date**: 2026-07-03
**Paper ID**: [openalex:2505.11517](https://arxiv.org/abs/2505.11517)

## Summary

This paper presents a comprehensive sensitivity analysis of the data fidelity requirements for reconstructing distribution grid topologies using voltage measurements. By applying the Chow-Liu algorithm to estimate maximum spanning trees, the study evaluates how quantization, bit-depth, and sampling frequency impact structural inference. Findings demonstrate that high-precision instrumentation is not strictly required, as successful recovery is possible with low-precision data, provided sampling intervals remain under 20 minutes. The work establishes a theoretical baseline for assessing data quality in practical smart meter deployments.

## Key Contributions

- Establishes that grid topology can be accurately reconstructed using low-precision 8-bit data or millivolt-level quantization.
- Identifies critical data fidelity bounds, showing significant reconstruction performance degradation when downsampling intervals exceed 20 minutes.
- Provides a systematic sensitivity analysis of measurement data (bit-depth, truncation, time-window length) on the accuracy of Chow-Liu-based topology inference.

## Open Questions & Future Work

- [[meshed-grid-topology-reconstruction]]

## Key Concepts

- [[information-theoretic-grid-topology-reconstruction]]: A systematic framework for evaluating the minimum measurement fidelity (bit-depth, sampling, precision) required to recover distribution grid topologies using mutual information.

## Archivist Review

I approved the concept of information-theoretic grid topology reconstruction as it frames a systematic approach to data fidelity analysis in smart power grids, which is distinct and re-usable. I also approved the open question regarding meshed topology reconstruction because current information-theoretic methods in this domain are bottlenecked by radial assumptions. The simulation environments were rejected as they are standard tools rather than specific datasets.

### Approved Concepts
- Information-theoretic grid topology reconstruction: Provides a formal, rigorous baseline for the feasibility of using low-precision, low-sampling data for grid structure inference, shifting focus from algorithm design to data fidelity requirements.

### Approved Open Questions
- Reconstructing Meshed Grid Topologies: As power distribution systems evolve to incorporate more meshing for reliability, existing tree-based topology reconstruction algorithms will become insufficient for accurate grid modeling. Developing information-theoretic methods capable of reconstructing cyclic graphs is critical for the scalability and applicability of data-driven topology inference.

### Rejected Candidates
- [dataset] GridLAB-D (`GridLAB-D`) - paper_local: Routine simulation environment rather than a specific benchmark dataset for evaluation.
- [dataset] MATPOWER (`MATPOWER`) - paper_local: Standard simulation toolbox/benchmark case generator rather than a reusable dataset.

## Links

- [Abstract](https://arxiv.org/abs/2505.11517)
- [PDF](https://arxiv.org/pdf/2505.11517)

