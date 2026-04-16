---
# CSL-compatible fields
title: "Data Poisoning Attacks on Informativity for Observability: Invariance-Based Synthesis"
author:
  - literal: "Iori Takaki"
  - literal: "Ahmet Cetinkaya"
  - literal: "Hideaki Ishii"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11657"

# Custom fields
paper_id: "2604.11657"
paper_source: "openalex"
domain: "control-theory"
tags:
  - "time-series"
  - "robustness"
  - "adversarial-examples"
architectures:
  []
datasets:
  []
concept_slugs:
  - "informativity-based-data-poisoning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:29:04Z"
created_at: "2026-04-16T06:29:04Z"
---

# Data Poisoning Attacks on Informativity for Observability: Invariance-Based Synthesis

**Authors**: Iori Takaki, Ahmet Cetinkaya, Hideaki Ishii
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11657](https://arxiv.org/abs/2604.11657)

## Summary

This paper investigates cyber-attacks against informativity-based analysis in data-driven control systems. The authors demonstrate that an adversary can use invertible linear transformations on time-series data matrices to embed malicious states into the underlying system's invariant subspace. A constructive method is provided to derive these transformations, accompanied by an optimization framework that computes the minimum data distortion required to destroy informativity certificates. Numerical experiments confirm that even small, structured modifications can effectively undermine data-driven observability analysis.

## Key Contributions

- Formalized an adversarial model for data-driven control using invertible linear transformations on data matrices to compromise informativity.
- Derived existence and feasibility conditions for embedding malicious states into the invariant subspace of transformed datasets.
- Formulated a minimum-norm optimization objective to calculate the smallest data distortion necessary to invalidate system informativity certificates.

## Key Concepts

- [[informativity-based-data-poisoning]]: A method for attacking data-driven control informativity using linear data transformation to embed malicious states.

## Archivist Review

The paper introduces a novel adversarial framework targeting the integrity of data-driven control systems by exploiting the informativity of data matrices. I have approved 'Informativity-based Data Poisoning' as a central concept, as it establishes a specific threat model for an important area of robust control theory. No datasets or open questions met the stringent criteria for permanent vault inclusion in this instance.

### Approved Concepts
- Informativity-based Data Poisoning: It introduces a novel threat model for data-driven control systems specifically targeting informativity analysis, which is critical for system reliability.

### Rejected Candidates
- [concept] Informativity-based Data Poisoning (`informativity-based-data-poisoning`) - generic: This is a robust concept for the vault. (Wait, I just approved it, so this entry should not be here. Correction: the logic is to only list rejected items here. Removing this from rejected list.)

## Links

- [Abstract](https://arxiv.org/abs/2604.11657)
- [PDF](https://arxiv.org/pdf/2604.11657)

