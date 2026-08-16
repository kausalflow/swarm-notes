---
# CSL-compatible fields
title: "CoMedBench: A Multi-Source Benchmark of Synthetic Medical Data Fidelity and Downstream Utility"
author:
  - literal: "Akanta Das"
  - literal: "Al Amin Farhad"
  - literal: "Mrinmoy Sarkar Anto"
  - literal: "David Rehkopf"
  - literal: "Ayin Vala"
  - literal: "Tanmoy Sarkar Pias"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.12805"

# Custom fields
paper_id: "2608.12805"
paper_source: "openalex"
domain: "medicine"
tags:
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "tabular"
  - "time-series"
  - "healthcare"
architectures:
  []
datasets:
  - "nhanes"
concept_slugs:
  []
dataset_slugs:
  - "nhanes"
skill: "TimeSeriesSkill"
processed_at: "2026-08-16T05:21:16Z"
created_at: "2026-08-16T05:21:16Z"
---

# CoMedBench: A Multi-Source Benchmark of Synthetic Medical Data Fidelity and Downstream Utility

**Authors**: Akanta Das, Al Amin Farhad, Mrinmoy Sarkar Anto, David Rehkopf, Ayin Vala, Tanmoy Sarkar Pias
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.12805](https://arxiv.org/abs/2608.12805)

## Summary

This paper introduces CoMedBench, a comprehensive and reproducible benchmark evaluating synthetic medical data fidelity and downstream utility across 37 dataset-task pairs (comprising static tabular and temporal ICU time-series). Drawing from seven public clinical sources such as MIMIC-III, MIMIC-IV, eICU, and NHANES, the benchmark assesses both statistical fidelity and task utility. Results show that models trained on synthetic data preserve robust downstream performance, with CoMed-TVAE achieving up to 97.3% relative AUROC on tabular tasks and ~95% on temporal ICU tasks, though performance drops under imbalance-sensitive metrics like AUPRC.

## Key Contributions

- Introduces CoMedBench, a reproducible benchmark spanning 37 dataset-task pairs across static tabular and temporal ICU time-series to evaluate synthetic medical data fidelity and downstream utility.
- Evaluates synthetic data generation across seven public clinical data sources, including MIMIC-III, MIMIC-IV, eICU, CDC BRFSS, NHANES, and pycox survival datasets.
- Demonstrates that stronger reference generators like CoMed-TVAE retain high utility (~97.3% AUROC on tabular tasks and ~95% on temporal ICU tasks), whereas imbalance-sensitive metrics like AUPRC reveal greater vulnerability on complex temporal data.

## Open Questions & Future Work

- [[sequence-native-generators-and-privacy-integration]]

## Archivist Review

Evaluated the paper according to strict vault standards. No standalone concepts met the threshold for vault inclusion. The open question regarding sequence-native generation and privacy integration in medical data benchmarks is insightful and reusable, so it was approved. The NHANES dataset was rejected because it is already present in the vault.

### Approved Open Questions
- Sequence-Native Generation and Privacy Integration: Extending benchmarks from tabular feature vectors to sequence-native generators and integrating formal privacy guarantees are crucial for real-world clinical deployment where fine-grained patient trajectories and patient re-identification risks are primary concerns.

### Rejected Candidates
- [dataset] NHANES (`nhanes`) - duplicate_existing: Dataset is already present in the vault.

## Datasets

- [[nhanes]]

## Links

- [Abstract](https://arxiv.org/abs/2608.12805)
- [PDF](https://arxiv.org/pdf/2608.12805)

