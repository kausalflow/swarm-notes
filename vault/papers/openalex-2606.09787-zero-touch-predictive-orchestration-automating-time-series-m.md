---
# CSL-compatible fields
title: "Zero Touch Predictive Orchestration: Automating Time-Series Models for the Cloud-Edge Continuum"
author:
  - literal: "Abd Elghani Meliani"
  - literal: "Arora Sagar"
  - literal: "Adlen Ksentini"
  - literal: "Raymond Knopp"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.09787"

# Custom fields
paper_id: "2606.09787"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "neural-architecture-search"
  - "nas"
  - "dataset"
architectures:
  []
datasets:
  - "timetrack"
concept_slugs:
  - "zero-touch-predictive-orchestration"
dataset_slugs:
  - "timetrack"
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:07:07Z"
created_at: "2026-06-11T09:07:07Z"
---

# Zero Touch Predictive Orchestration: Automating Time-Series Models for the Cloud-Edge Continuum

**Authors**: Abd Elghani Meliani, Arora Sagar, Adlen Ksentini, Raymond Knopp
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.09787](https://arxiv.org/abs/2606.09787)

## Summary

This paper addresses the cold-start problem in Cloud-Edge Continuum resource management, where new nodes lack sufficient history for localized time-series forecasting. The authors propose an automated, technology-agnostic orchestration framework that uses a novel data-mixing technique to combine sparse local node samples with the high-resolution TimeTrack dataset. By applying Neural Architecture Search (NAS) to this aggregated data, the system generates accurate, calibrated forecasting models that significantly reduce convergence time and improve predictive accuracy compared to standard baseline methods.

## Key Contributions

- Introduces a lightweight Resource Exposer for continuous telemetry collection across heterogeneous Cloud-Edge nodes.
- Develops a data-mixing methodology that integrates sparse local node telemetry with the TimeTrack dataset to solve the cold-start problem.
- Demonstrates that NAS-generated models trained on mixed data significantly outperform those trained on local or standard generic datasets in MSE, MAE, and MAPE metrics.

## Open Questions & Future Work

- [[dynamic-telemetry-sample-optimization]]

## Key Concepts

- [[zero-touch-predictive-orchestration]]: An automated framework for deploying and tuning time-series forecasting models in cloud-edge systems, specifically designed to address cold-start telemetry scarcity.

## Archivist Review

I approved the 'Zero-Touch' orchestrator concept and the TimeTrack dataset as they represent the core technical contribution of this research. I also approved the open question regarding dynamic telemetry sample optimization as it addresses a specific trade-off between resource constraints and forecast accuracy in edge computing. The feature selection question was rejected as it is a generic ML challenge rather than a research problem specific to the paper's contribution.

### Approved Concepts
- Zero Touch Predictive Orchestration: Central to the paper's goal of automating predictive management in volatile Cloud-Edge environments without manual intervention.

### Approved Open Questions
- Dynamic Telemetry Sample Optimization: This is critical for balancing the trade-off between the operational overhead of data collection on constrained edge devices and the need for sufficient training data to ensure reliable model performance.

### Rejected Candidates
- [open_question] Automated Telemetry Feature Selection (`automated-telemetry-feature-selection`) - not_novel: Automated feature selection is a standard, broadly studied problem in machine learning and does not represent a sufficiently novel or specific bottleneck for this vault.

## Datasets

- [[timetrack]]

## Links

- [Abstract](https://arxiv.org/abs/2606.09787)
- [PDF](https://arxiv.org/pdf/2606.09787)

