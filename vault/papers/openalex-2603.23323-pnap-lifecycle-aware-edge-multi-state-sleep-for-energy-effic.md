---
# CSL-compatible fields
title: "PNap: Lifecycle-aware Edge Multi-state sleep for Energy Efficient MEC"
author:
  - literal: "Federico Giarrè"
  - literal: "Holger Karl"
issued:
  date-parts:
    - [2026, 3, 24]
url: "https://arxiv.org/abs/2603.23323"

# Custom fields
paper_id: "2603.23323"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "time-series"
  - "anomaly-detection"
  - "resource-management"
architectures:
  []
datasets:
  []
concept_slugs:
  - "power-nap-lifecycle-aware-orchestration"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T15:44:26Z"
created_at: "2026-03-27T15:44:26Z"
---

# PNap: Lifecycle-aware Edge Multi-state sleep for Energy Efficient MEC

**Authors**: Federico Giarrè, Holger Karl
**Date**: 2026-03-24
**Paper ID**: [openalex:2603.23323](https://arxiv.org/abs/2603.23323)

## Summary

This paper addresses the high energy consumption in Multi-access Edge Computing (MEC) systems caused by keeping servers active during low-load phases. The authors introduce PowerNap (PNap), a novel orchestration framework that jointly manages server power-saving sleep states and the dependent service lifecycle states. PNap utilizes traffic forecasting to make coordinated decisions that minimize active servers while ensuring service continuity and low latency. Evaluations show that PNap achieves up to a 14.9% reduction in energy consumption compared to state-of-the-art methods while preserving service availability metrics.

## Key Contributions

- Introduction of PowerNap (PNap), a lifecycle-aware orchestration framework for MEC that jointly manages server sleep states and service lifecycle states.
- PNap leverages traffic forecasting to jointly minimize the number of active edge servers and service disruptions.
- Demonstration of PNap reducing energy consumption by up to 14.9% compared to a state-of-the-art solution while maintaining service availability.

## Limitations

The abstract does not explicitly detail limitations, but the coupling of energy saving with service continuity implies trade-offs with wake-up delays.

## Open Questions & Future Work

- [[distributed-pnap-for-mec-orchestration]]
- [[refined-request-scheduling-policies-mec]]

## Key Concepts

- [[power-nap-lifecycle-aware-orchestration]]: A lifecycle-aware orchestration framework for Multi-access Edge Computing (MEC) that jointly manages server sleep states and service lifecycle states by leveraging traffic forecasting.

## Archivist Review

The central contribution, PowerNap (PNap) Lifecycle-aware Orchestration, was approved as a novel, reusable mechanism for energy management in MEC that jointly handles power and service states. Two open questions were approved: one focusing on the necessary distributed scaling of the centralized orchestrator, and another on refining the request scheduling policies beyond the basic preemptive discipline used. No other candidates were present or qualified for vaulting.

### Approved Concepts
- PowerNap (PNap) Lifecycle-aware Orchestration: PNap is the central novel framework for jointly managing server sleep states and service lifecycle states to minimize energy consumption while maintaining service continuity.

### Approved Open Questions
- Distributed PNap Orchestration: Developing a distributed version is crucial for the practical scalability of lifecycle-aware energy-saving orchestration in large-scale MEC deployments.
- Refined Request Scheduling Policies: Exploring refined, non-preemptive, or alternative priority scheduling policies may yield better performance trade-offs between service continuity and immediate user response times than the adopted preemptive discipline.

### Rejected Candidates
- [open_question] Distributed PNap Orchestration (`distributed-pnap-for-mec-orchestration`) - other: Approved as a substantial future work direction regarding scalability.
- [open_question] Refined Request Scheduling Policies (`refined-request-scheduling-policies-mec`) - other: Approved as a specific unresolved mechanism question regarding optimal scheduling rules.

## Links

- [Abstract](https://arxiv.org/abs/2603.23323)
- [PDF](https://arxiv.org/pdf/2603.23323)

