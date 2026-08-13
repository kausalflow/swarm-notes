---
# CSL-compatible fields
title: "A Resource-centric Analysis and Optimization of NoSQL Workloads using Distressed Resource Volume Metric"
author:
  - literal: "Gunika Verma"
  - literal: "A"
  - literal: "Aashutosh"
  - literal: "V"
  - literal: "Pooja Srinivas"
  - literal: "Yogesh Simmhan"
  - literal: "Ayush Choure"
  - literal: "Harshit Shah"
  - literal: "Mayukh Das"
  - literal: "Prashant Sasatte"
  - literal: "Chetan Bansal"
  - literal: "Abhijit Pai"
  - literal: "Suraj Dixit"
  - literal: "Achint Agrawal"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09173"

# Custom fields
paper_id: "2608.09173"
paper_source: "openalex"
domain: "nlp"
tags:
  - "benchmark"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:09:45Z"
created_at: "2026-08-13T06:09:45Z"
---

# A Resource-centric Analysis and Optimization of NoSQL Workloads using Distressed Resource Volume Metric

**Authors**: Gunika Verma, A, Aashutosh, V, Pooja Srinivas, Yogesh Simmhan, Ayush Choure, Harshit Shah, Mayukh Das, Prashant Sasatte, Chetan Bansal, Abhijit Pai, Suraj Dixit, Achint Agrawal
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09173](https://arxiv.org/abs/2608.09173)

## Summary

This paper investigates resource optimization and reliability for large-scale managed cloud NoSQL databases using production traces from Microsoft Cosmos DB. The authors introduce the Distressed Resource Volume (DRV) metric to capture end-user quality of service and propose LoadStar, an open-source policy simulation framework. They further develop the Luna load forecasting model and the Orbit packing and migration (PAM) algorithm, achieving up to a 35% reduction in resources and significant tail-error improvements in production deployments.

## Key Contributions

- Proposed open-source NoSQL workloads derived from real Microsoft Cosmos DB production clusters to overcome the lack of public cloud database traces.
- Introduced the Distressed Resource Volume (DRV) reliability metric and the LoadStar policy simulation framework for resource-centric NoSQL workload validation.
- Developed the Luna load forecasting model and the Orbit packing and migration algorithm to optimize replica placement and reduce tail-errors.
- Demonstrated up to 35% reduction in cloud resources and lower error rates in production deployment, yielding substantial annual savings.

## Archivist Review

Applied strict scarcity and domain filtering. The paper focuses on systems infrastructure, cloud database workloads, packing, and migration policies (Cosmos DB, LoadStar, DRV), which are outside the scope of reusable machine learning forecasting primitives. Therefore, no concepts or open questions were approved.

### Rejected Candidates
- [open_question] NoSQL Workload Validation and Dynamic Forecasting (`nosql-workload-validation-and-dynamic-forecasting`) - low_impact: The question is specific to cloud database resource management and migration policies rather than being a central, reusable bottleneck in machine learning time series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2608.09173)
- [PDF](https://arxiv.org/pdf/2608.09173)

