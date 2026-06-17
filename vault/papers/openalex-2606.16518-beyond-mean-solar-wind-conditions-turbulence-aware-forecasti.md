---
# CSL-compatible fields
title: "Beyond Mean Solar Wind Conditions: Turbulence-Aware Forecasting of the AE Index"
author:
  - literal: "Cara L. Waters"
  - literal: "Christopher H. K. Chen"
  - literal: "Mathew J. Owens"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16518"

# Custom fields
paper_id: "2606.16518"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "turbulence-aware-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:26:23Z"
created_at: "2026-06-17T09:26:23Z"
---

# Beyond Mean Solar Wind Conditions: Turbulence-Aware Forecasting of the AE Index

**Authors**: Cara L. Waters, Christopher H. K. Chen, Mathew J. Owens
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16518](https://arxiv.org/abs/2606.16518)

## Summary

This study evaluates the impact of incorporating solar wind turbulence on the forecasting of the auroral electrojet (AE) index. By training gradient boosted decision tree (XGBoost) models, the authors compare a baseline relying on mean solar wind parameters against a turbulence-aware model enriched with measures of intermittency and Alfvenic structure. Results indicate that the turbulence-aware model maintains superior skill and economic value at longer lead times and across higher activity thresholds, providing robust operational utility for space weather monitoring.

## Key Contributions

- Developed an XGBoost-based turbulence-aware AE index forecasting model that incorporates solar wind fluctuation amplitude, intermittency, and Alfvenic structure.
- Demonstrated that turbulence-aware models show reduced forecast skill degradation at 60-90 minute horizons compared to baseline models utilizing only mean parameters.
- Showed through cost-loss analysis that turbulence-aware features provide stable economic value across extreme AE index thresholds, whereas baseline performance degrades at higher activity levels.

## Open Questions & Future Work

- [[magnetospheric-state-integration-forecasting]]

## Key Concepts

- [[turbulence-aware-forecasting]]: A forecasting framework that integrates physical turbulence metrics to improve long-horizon stability and robustness during extreme events.

## Archivist Review

The paper effectively identifies how domain-specific physical features (turbulence metrics) can improve the robustness and economic utility of time series forecasting in extreme event scenarios. I have approved the framework for turbulence-aware forecasting and the associated open question regarding magnetospheric state integration, as these provide a reusable methodology for physical time series forecasting and identify a critical research bottleneck in space weather prediction. No datasets were approved as the source data was implicitly handled as general solar wind observations without a specific benchmark name for the dataset.

### Approved Concepts
- Turbulence-aware forecasting: Demonstrates that incorporating turbulence-related features (amplitude, intermittency, Alfvenic structure) provides complementary information that significantly enhances forecast stability for high-impact geomagnetic events.

### Approved Open Questions
- Integrating Magnetospheric State Variables: This direction addresses the fundamental upper bound of solar wind-driven predictability by proposing a more holistic representation of magnetospheric states.

## Links

- [Abstract](https://arxiv.org/abs/2606.16518)
- [PDF](https://arxiv.org/pdf/2606.16518)

