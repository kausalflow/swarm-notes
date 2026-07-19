---
# CSL-compatible fields
title: "Post Hoc Inference for Component Attribution in Multivariate Change-Point Detection"
author:
  - literal: "Dhia-Elhaq Ouerfelli"
  - literal: "Sylvain Arlot"
  - literal: "Kevin Bleakley"
  - literal: "Patrick Pamphile"
issued:
  date-parts:
    - [2026, 7, 16]
url: "https://arxiv.org/abs/2607.14814"

# Custom fields
paper_id: "2607.14814"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "post-hoc-component-attribution"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-19T07:24:41Z"
created_at: "2026-07-19T07:24:41Z"
---

# Post Hoc Inference for Component Attribution in Multivariate Change-Point Detection

**Authors**: Dhia-Elhaq Ouerfelli, Sylvain Arlot, Kevin Bleakley, Patrick Pamphile
**Date**: 2026-07-16
**Paper ID**: [openalex:2607.14814](https://arxiv.org/abs/2607.14814)

## Summary

This paper addresses the interpretability challenge in multivariate time series analysis by proposing a post hoc inference framework to identify which coordinates contribute to a detected change-point. By partitioning the multivariate space into predefined blocks, the method utilizes nonparametric two-sample tests to statistically confirm the presence of changes within those specific components. The approach provides formal Type I error guarantees, ensuring reliability in downstream diagnostic applications. Empirical results confirm the method's effectiveness in pinpointing change sources in both synthetic and real-world multivariate datasets.

## Key Contributions

- Introduces a post hoc statistical framework for attributing change-points in multivariate time series to specific coordinate blocks.
- Provides a rigorous theoretical guarantee for Type I error control using nonparametric two-sample testing procedures.
- Demonstrates superior performance and accuracy in coordinate block identification through extensive simulation and real-data validation.

## Open Questions & Future Work

- [[power-guarantees-attribution-tests]]
- [[attribution-with-unknown-changepoints]]

## Key Concepts

- [[post-hoc-component-attribution]]: A statistical procedure to identify which coordinate blocks in a multivariate time series are responsible for a detected change-point.

## Archivist Review

The paper provides a modular, statistically rigorous approach to the problem of change-point attribution. I have approved the overarching concept of Post Hoc Component Attribution and two central open questions regarding the theoretical power and robustness of such methods to downstream estimation errors. No datasets were approved as none were cited as reusable benchmarks or novel contributions.

### Approved Concepts
- Post Hoc Component Attribution: It provides a generic interpretability framework for complex multivariate change-point detection tasks by isolating responsible coordinate blocks.

### Approved Open Questions
- Power guarantees for attribution tests: Understanding the power of attribution methods is essential to ensure they do not produce excessive false negatives in decision-critical applications like process control or clinical monitoring.
- Attribution with unknown change-points: Since true change-point counts are rarely known a priori, attribution methods that do not account for the uncertainty of the detection phase may lead to unreliable interpretations.

## Links

- [Abstract](https://arxiv.org/abs/2607.14814)
- [PDF](https://arxiv.org/pdf/2607.14814)

