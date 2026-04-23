---
# CSL-compatible fields
title: "Forecasting Ionospheric Irregularities on GNSS Lines of Sight Using Dynamic Graphs with Ephemeris Conditioning"
author:
  - literal: "Mert Can Turkmen"
  - literal: "Eng Leong Tan"
  - literal: "Yee Hui Lee"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.18379"

# Custom fields
paper_id: "2604.18379"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "graph-neural-network"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ephemeris-conditioning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:55:27Z"
created_at: "2026-04-23T06:55:27Z"
---

# Forecasting Ionospheric Irregularities on GNSS Lines of Sight Using Dynamic Graphs with Ephemeris Conditioning

**Authors**: Mert Can Turkmen, Eng Leong Tan, Yee Hui Lee
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.18379](https://arxiv.org/abs/2604.18379)

## Summary

IonoDGNN is a dynamic graph-based forecasting model that treats the ionosphere as an evolving set of pierce points rather than a fixed grid. By incorporating ephemeris conditioning, the model leverages predictable satellite trajectories to maintain high accuracy on lines of sight that appear mid-forecast. Evaluated on multi-GNSS data from Singapore, IonoDGNN significantly outperforms baseline methods and exhibits strong robustness to coverage dropout through spatial message passing.

## Key Contributions

- Introduces IonoDGNN, a dynamic graph neural network for forecasting ionospheric irregularities directly on satellite lines of sight.
- Implements ephemeris conditioning to allow predictions for lines of sight that emerge during the forecast horizon, yielding a significant improvement in predictive performance.
- Demonstrates robust performance on multi-GNSS data, outperforming persistence benchmarks by 35% in Brier Skill Score and 52% in PR-AUC.

## Open Questions & Future Work

- [[physics-informed-graph-topology]]

## Key Concepts

- [[ephemeris-conditioning]]: A forecasting technique that conditions predictions on the pre-calculable, time-evolving graph topology of predictable movement patterns.

## Archivist Review

I approved 'Ephemeris Conditioning' as it represents a novel and reusable methodological contribution for any spatiotemporal forecasting task where graph topology is driven by deterministic trajectories. I also approved 'Physics-Informed Graph Topology' as a high-impact research question regarding the limitation of geometric graph constructions in physics-constrained spatiotemporal forecasting. I rejected the 'Heterogeneous Sensor Integration' candidate as it is a common scalability challenge rather than a unique, foundational bottleneck in the context of the current vault's focus on modeling techniques.

### Approved Concepts
- Ephemeris Conditioning: It is the core innovation enabling the model to predict on lines of sight that appear only during the forecast horizon.

### Approved Open Questions
- Physics-Informed Graph Topology: Moving beyond purely geometric graph constructions is essential for improving the physical realism and long-term predictive skill of GNNs in space weather, where plasma structures are inherently constrained by the Earth's magnetic field.

## Links

- [Abstract](https://arxiv.org/abs/2604.18379)
- [PDF](https://arxiv.org/pdf/2604.18379)

