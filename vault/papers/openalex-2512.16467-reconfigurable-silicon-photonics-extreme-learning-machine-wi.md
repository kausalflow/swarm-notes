---
# CSL-compatible fields
title: "Reconfigurable silicon photonics extreme learning machine with random non-linearities as neural processor and physical unclonable function"
author:
  - literal: "George Sarantoglou"
  - literal: "Georgios Aias Karydis"
  - literal: "Adonis Bogris"
  - literal: "Charis Mesaritakis"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2512.16467"

# Custom fields
paper_id: "2512.16467"
paper_source: "openalex"
domain: "nlp"
tags:
  - "machine-learning"
  - "photonic-computing"
  - "neuromorphic-computing"
  - "time-series"
  - "benchmark"
architectures:
  []
datasets:
  - "santa-fe-chaotic-time-series-benchmark"
concept_slugs:
  - "rn-elm"
dataset_slugs:
  - "santa-fe-chaotic-time-series-benchmark"
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:10:45Z"
created_at: "2026-07-17T07:10:45Z"
---

# Reconfigurable silicon photonics extreme learning machine with random non-linearities as neural processor and physical unclonable function

**Authors**: George Sarantoglou, Georgios Aias Karydis, Adonis Bogris, Charis Mesaritakis
**Date**: 2026-07-14
**Paper ID**: [openalex:2512.16467](https://arxiv.org/abs/2512.16467)

## Summary

The paper introduces RN-ELM, a silicon-photonic Extreme Learning Machine that utilizes heterogeneous random non-linearities from an array of passive optical filters instead of conventional uniform activation functions. By mapping non-linear synapses to the physical frequency-to-power response of micro-ring resonators, the model achieves competitive accuracy on the Santa-Fe chaotic time-series benchmark with significantly fewer parameters than traditional photonic reservoirs. Furthermore, the architecture leverages intrinsic hardware imperfections to function as a Physical Unclonable Function (PUF) for secure authentication.

## Key Contributions

- Proposed RN-ELM, a hybrid analog-digital architecture that replaces uniform activation functions with heterogeneous random non-linearities via silicon-photonic filters.
- Achieved 0.053 normalized mean squared error on the Santa-Fe chaotic time-series benchmark using only five optical filters, demonstrating high parameter efficiency.
- Demonstrated dual-use capability as a Physical Unclonable Function (PUF), utilizing fabrication-induced imperfections as an entropy source with a cloning probability of 10^-15.

## Key Concepts

- [[rn-elm]]: A hybrid analog-digital extreme learning machine that replaces conventional uniform activation functions with an array of fixed random non-linear synapses realized via silicon-photonic optical filters.

## Archivist Review

I have approved the core RN-ELM architecture as it presents a novel hybrid approach to extreme learning machines using passive hardware non-linearities, which is a highly reusable design concept for neuromorphic computing. I also approved the Santa-Fe chaotic time-series benchmark as it is a standard, distinct dataset frequently used in the literature to evaluate such temporal forecasting models. Other candidates were rejected for being specific hardware-level applications rather than generalizable ML mechanisms.

### Approved Concepts
- RN-ELM: Introduces a hybrid analog-digital architecture that leverages heterogeneous hardware-based non-linearities, challenging the reliance on uniform activation functions in traditional extreme learning machines.

### Rejected Candidates
- [concept] Physical Unclonable Function (PUF) in Silicon Photonics (`silicon-photonic-puf`) - subcomponent_of_broader_mechanism: This is a specific application/hardware feature rather than a core machine learning concept.

## Datasets

- [[santa-fe-chaotic-time-series-benchmark]]

## Links

- [Abstract](https://arxiv.org/abs/2512.16467)
- [PDF](https://arxiv.org/pdf/2512.16467)

