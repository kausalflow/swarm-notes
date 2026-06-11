---
# CSL-compatible fields
title: "Bayesian Selective Latent Inference for Wastewater-First Influenza Monitoring"
author:
  - literal: "Yixuan Zhang"
  - literal: "Yang Song"
  - literal: "H Y Wang"
  - literal: "Samir Bhatt"
  - literal: "Hengguan Huang"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.09433"

# Custom fields
paper_id: "2606.09433"
paper_source: "openalex"
domain: "biology"
tags:
  - "forecasting"
  - "bayesian-inference"
  - "decision-making"
  - "uncertainty-estimation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "bayesian-selective-latent-inference-bsli"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:08:29Z"
created_at: "2026-06-11T09:08:29Z"
---

# Bayesian Selective Latent Inference for Wastewater-First Influenza Monitoring

**Authors**: Yixuan Zhang, Yang Song, H Y Wang, Samir Bhatt, Hengguan Huang
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.09433](https://arxiv.org/abs/2606.09433)

## Summary

Wastewater influenza surveillance often struggles with source ambiguity and the high cost of querying additional official data streams. To address this, the paper introduces Bayesian Selective Latent Inference (BSLI), which treats surveillance as a selective decision process rather than a static estimation task. By maintaining a posterior over latent disease burden and using explicit scientific gates for answerability, the model dynamically determines when additional data acquisition is warranted. BSLI achieves superior cost-performance trade-offs on a large public-data influenza benchmark while robustly abstaining from predictions under high uncertainty.

## Key Contributions

- Introduced Bayesian Selective Latent Inference (BSLI) to model wastewater monitoring as an evidence-selective decision problem.
- Implemented an exact cost-calibrated Bellman policy that integrates scientific gates for certifying answerability and managing source ambiguity.
- Demonstrated improved cost-performance frontiers on a 5,933-episode forecasting benchmark compared to traditional fixed-evidence wastewater models.

## Open Questions & Future Work

- [[generalizing-selective-surveillance-to-dynamic-environments]]

## Key Concepts

- [[bayesian-selective-latent-inference-bsli]]: A Bayesian framework for selective evidence acquisition in wastewater monitoring that optimizes information gathering under cost and ambiguity constraints.

## Archivist Review

I approved the BSLI framework for its novel formulation of sensor-fusion as a cost-calibrated selective decision problem. The open question was approved for articulating the substantial leap required to move from static public-health benchmarks to real-world, nonstationary surveillance deployments. No datasets were approved as none were presented as novel, reusable entities distinct from general wastewater surveillance literature.

### Approved Concepts
- Bayesian Selective Latent Inference (BSLI): The paper's core methodology, which addresses the novel challenge of selective evidence acquisition in monitoring by certifying answerability via Bayesian gates and cost-calibrated policies.

### Approved Open Questions
- Generalizing Selective Surveillance Systems: Establishing how selective inference systems adapt to evolving public health reporting environments and diverse pathogen characteristics is essential for moving beyond static, benchmark-constrained evaluations to robust, scalable deployments.

## Links

- [Abstract](https://arxiv.org/abs/2606.09433)
- [PDF](https://arxiv.org/pdf/2606.09433)

