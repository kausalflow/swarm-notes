---
# CSL-compatible fields
title: "JanusBM: A Dual-Fidelity Multi-Zone White-Box Building Modeling Framework"
author:
  - literal: "Hung Cheng"
  - literal: "Hüseyin K. Çakmak"
  - literal: "Veit Hagenmeyer"
issued:
  date-parts:
    - [2026, 3, 24]
url: "https://arxiv.org/abs/2603.23015"

# Custom fields
paper_id: "2603.23015"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "model-compression"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "janusbm-dual-fidelity-modeling"
  - "ideal-load-surrogate-modeling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T15:44:35Z"
created_at: "2026-03-27T15:44:35Z"
---

# JanusBM: A Dual-Fidelity Multi-Zone White-Box Building Modeling Framework

**Authors**: Hung Cheng, Hüseyin K. Çakmak, Veit Hagenmeyer
**Date**: 2026-03-24
**Paper ID**: [openalex:2603.23015](https://arxiv.org/abs/2603.23015)

## Summary

This paper introduces JanusBM, a dual-fidelity modeling framework for building energy systems that combines a high-fidelity (HiFi) hydronic model with a low-fidelity (LoFi) ideal-load surrogate to balance simulation speed and accuracy across different timescales. The framework is built using the RoomFlex6D tool, with the LoFi component explicitly removing hydronic states to enable rapid annual assessments. A two-stage hybrid calibration process validates the framework against the IEA EBC Annex 60 benchmark for energy scale and uses real-world measurements for calibrating dynamic accuracy. Results confirm the LoFi model achieves fast simulation speeds while maintaining energy consistency, with the calibration workflow robustly improving loop-level and zone-level temperature transients. The work establishes the trade-off where the HiFi model remains necessary only for accurately capturing limitations arising from distribution and control during peak or transient events.

## Key Contributions

- Proposal of JanusBM, a dual-fidelity, multi-zone white-box building modeling framework coupling a HiFi hydronic model with a LoFi ideal-load surrogate derived via RoomFlex6D.
- Introduction of a two-stage hybrid validation and calibration pipeline using both energy-scale data (Annex 60) and measurement-scale data (real-world transients) for rigorous cross-scale consistency.
- Demonstration that the LoFi models achieve energy-scale consistency with benchmarks while offering orders-of-magnitude faster simulation speeds compared to the HiFi model.
- Validation that the calibration workflow successfully improves critical transient dynamics, specifically loop-level return water temperature and zone-level temperature fluctuations.

## Limitations

The need for the HiFi model remains necessary when distribution/control limitations cause a significant mismatch between required and delivered heat, particularly during transient or peak load assessments.

## Open Questions & Future Work

- [[lolo-model-transient-peak-capability]]
- [[hifi-calibration-envelope-uncertainties]]
- [[model-generation-interoperability-standards]]

## Key Concepts

- [[janusbm-dual-fidelity-modeling]]: A dual-fidelity, multi-zone white-box building modeling framework that couples a high-fidelity hydronic model with a low-fidelity ideal-load surrogate.
- [[ideal-load-surrogate-modeling]]: A low-fidelity model component designed to represent building energy demand by abstracting away explicit hydronic states, used to accelerate annual simulations.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 2 concept(s), 3 open question(s), and 0 dataset(s), with 3 rejected candidate note(s).

### Approved Concepts
- JanusBM Framework: This framework directly addresses the trade-off between simulation speed and fidelity in building energy modeling by combining two distinct fidelity levels.
- Ideal-Load Surrogate Modeling: This surrogate is the core innovation enabling the low-fidelity representation by abstracting away complex hydronic dynamics while maintaining necessary fidelity characteristics.

### Approved Open Questions
- Extend LoFi model transient capability: Accurate peak load prediction is crucial for system-level studies in sector-coupled energy systems, which rely on the computationally efficient LoFi models for large-scale analysis.
- Extend HiFi calibration to envelope: A fully calibrated model that accounts for both thermal distribution and envelope physics is necessary for robust digital twin applications and high-fidelity dynamic analysis.
- Integrate GIS/BIM standards: Integrating standardized formats is essential for broader adoption and seamless integration with existing building data workflows (e.g., BIM).

### Rejected Candidates
- [dataset] IEA EBC Annex 60 benchmark (`iea-ebc-annex-60-benchmark`) - low_impact: This is a standard benchmark dataset/protocol for building energy modeling, not a novel, reusable dataset worthy of a vault entry.
- [concept] RoomFlex6D Tool (`roomflex6d-modeling-tool`) - paper_local: This is a specific, proprietary tool used for implementation, not a reusable modeling concept or method itself.
- [concept] Two-Stage Hybrid Validation and Calibration Pipeline (`hybrid-validation-calibration-pipeline`) - paper_local: This pipeline is a specific procedural artifact tailored to validating the dual-fidelity approach using two different data scales, making it too procedural and paper-local for a reusable concept.

## Links

- [Abstract](https://arxiv.org/abs/2603.23015)
- [PDF](https://arxiv.org/pdf/2603.23015)

