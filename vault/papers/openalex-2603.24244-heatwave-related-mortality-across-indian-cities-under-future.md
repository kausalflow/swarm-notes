---
# CSL-compatible fields
title: "Heatwave-Related Mortality Across Indian Cities Under Future Climate Scenarios"
author:
  - literal: "Ingita Dey Munshi"
  - literal: "Abbinav Sankar Kailasam"
  - literal: "Sudeep Shukla"
  - literal: "K. Shuvo Bakar"
  - literal: "Anirban Chakraborti"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24244"

# Custom fields
paper_id: "2603.24244"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "climate-change"
architectures:
  []
datasets:
  - "CMIP6 climate projections"
concept_slugs:
  - "climate-mitigation-health-burden-quantification"
  - "multidimensional-scaling-mortality-clustering"
dataset_slugs:
  - "cmip6-climate-projections"
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:29:46Z"
created_at: "2026-03-28T05:29:46Z"
---

# Heatwave-Related Mortality Across Indian Cities Under Future Climate Scenarios

**Authors**: Ingita Dey Munshi, Abbinav Sankar Kailasam, Sudeep Shukla, K. Shuvo Bakar, Anirban Chakraborti
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24244](https://arxiv.org/abs/2603.24244)

## Summary

This study integrates historical heat-related mortality data from 1970-2023 with bias-corrected CMIP6 climate projections (SSP2-4.5 and SSP5-8.5) to forecast mortality trends across 67 Indian cities until the end of the century. A time-series forecasting framework was employed, using summer mean temperature as the core climate driver to model future health burdens. The results project a significant increase in mortality, particularly under the high-emission scenario, which also exacerbates regional inequality in health outcomes. The findings strongly support that climate mitigation policies can effectively reduce the scale and uneven distribution of future urban heat-health vulnerability.

## Key Contributions

- Quantified future heatwave-related mortality across 67 Indian cities through the end of the 21st century using integrated long-term mortality records (1970-2023) and CMIP6 climate projections.
- Projected multi-fold amplification of mortality under the high-emission SSP5-8.5 scenario compared to the intermediate SSP2-4.5 scenario, demonstrating high sensitivity to emission pathways.
- Identified increasing regional divergence in mortality growth, with the Deccan Plateau and western/eastern India showing disproportionately higher impacts under extreme warming.
- Demonstrated that climate mitigation (SSP2-4.5) substantially reduces both the magnitude and inequality of future urban heat-health burdens.

## Limitations

The framework uses summer mean temperature as the primary climate driver, which may simplify the complex relationship between heatwave characteristics and mortality.

## Open Questions & Future Work

- [[optimal-climate-driver-for-heat-mortality-forecasting]]

## Key Concepts

- [[climate-mitigation-health-burden-quantification]]: The application of integrated climate projections and epidemiological data to quantify the differential magnitude and inequality of future public health burdens based on chosen emissions pathways.
- [[multidimensional-scaling-mortality-clustering]]: A technique used to visualize and cluster regional mortality responses based on their sensitivity to extreme climate change scenarios, revealing emergent structural dependencies.

## Archivist Review

Two reusable concepts were approved: one concerning the policy-relevant quantification of climate mitigation impact on health disparities, and another regarding the use of Multidimensional Scaling for behavioral clustering under extreme stress. The paper's core methodology relies on standard time-series forecasting, which is too generic for a concept note, though the input data (CMIP6) was approved. One open question was approved, focusing on the critical choice of climate drivers (aggregate vs. event-based) for improving future epidemiological forecasting fidelity.

### Approved Concepts
- Climate Mitigation Impact Quantification on Health Burdens: The core finding demonstrates the differential impact of various climate scenarios (SSP2-4.5 vs. SSP5-8.5) on public health metrics (mortality), providing a reusable framework for policy analysis connecting climate mitigation strategy directly to quantifiable social benefit.
- Multidimensional Scaling for Mortality Behavior Clustering: The use of Multidimensional Scaling (MDS) to reveal emerging structural clustering of state-level mortality response under extreme warming conditions is a reusable technique for summarizing complex, high-dimensional regional dependency structures in climate impact studies.

### Approved Open Questions
- Climate Driver Choice Fidelity: Understanding the optimal choice of climate driver—simple aggregates vs. complex event metrics—is crucial for improving the fidelity and interpretability of future climate-health impact assessments.

### Rejected Candidates
- [concept] time-series forecasting framework (`time-series-forecasting-framework`) - generic: This phrase is too generic; the specific framework applied is not detailed enough to warrant a vault entry without further definition.
- [concept] summer mean temperature as the primary climate driver (`summer-mean-temperature-as-driver`) - generic: Using a simple climatic aggregate like mean temperature as a driver is a common practice in basic climate impact modeling and not a novel, reusable technical mechanism.
- [concept] regional divergence in mortality (`regional-divergence-in-mortality`) - paper_local: This is a finding/observation derived from the modeling, not a reusable modeling concept, technique, or architecture itself.
- [concept] Heatwave-Related Mortality Forecasting (`heatwave-related-mortality-forecasting`) - low_impact: This is a problem domain, not a novel, reusable concept or technique introduced by the paper. The reusable concept is the *method* of quantifying mitigation impact or the *clustering* method.

## Datasets

- [[cmip6-climate-projections]]

## Links

- [Abstract](https://arxiv.org/abs/2603.24244)
- [PDF](https://arxiv.org/pdf/2603.24244)

