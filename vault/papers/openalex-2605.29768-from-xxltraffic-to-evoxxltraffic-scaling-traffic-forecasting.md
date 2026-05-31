---
# CSL-compatible fields
title: "From XXLTraffic to EvoXXLTraffic: Scaling Traffic Forecasting to Sensor-Evolving Networks"
author:
  - literal: "Du Yin"
  - literal: "Hao Xue"
  - literal: "Arian Prabowo"
  - literal: "Shuang Ao"
  - literal: "Flora Salim"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29768"

# Custom fields
paper_id: "2605.29768"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "continual-learning"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "evoxxltraffic-dataset"
concept_slugs:
  - "evoxxltraffic-dataset"
dataset_slugs:
  - "evoxxltraffic-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:09:33Z"
created_at: "2026-05-31T08:09:33Z"
---

# From XXLTraffic to EvoXXLTraffic: Scaling Traffic Forecasting to Sensor-Evolving Networks

**Authors**: Du Yin, Hao Xue, Arian Prabowo, Shuang Ao, Flora Salim
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29768](https://arxiv.org/abs/2605.29768)

## Summary

This paper introduces XXLTraffic and its extension, EvoXXLTraffic, the first traffic forecasting benchmarks that explicitly account for long-term, real-world sensor network evolution. By spanning 27 years of data with growth rates exceeding 10,000%, the dataset enables research into continual forecasting under dynamic graph topologies. The authors establish a yearly streaming protocol and demonstrate that existing static state-of-the-art models often fail to capture the challenges of evolving road-sensor networks.

## Key Contributions

- Introduced XXLTraffic and EvoXXLTraffic, a 27-year dataset family facilitating ultra-long-horizon and sensor-evolving traffic forecasting.
- Defined a yearly streaming forecasting protocol to benchmark spatio-temporal models on continual, non-stationary network growth tasks.
- Demonstrated that many SOTA static spatio-temporal GNNs struggle to generalize to the massive, realistic network expansions observed in EvoXXLTraffic.

## Open Questions & Future Work

- [[evolving-graph-cold-start-bottleneck]]

## Key Concepts

- [[evoxxltraffic-dataset]]: A large-scale, sensor-evolving traffic forecasting benchmark that tracks road-sensor network growth over up to 27 years.

## Archivist Review

The paper proposes a novel benchmark, EvoXXLTraffic, which shifts the paradigm from fixed-topology traffic forecasting to sensor-evolving continual learning. I have approved the dataset and the accompanying concept for their significance in evaluating non-stationary graph growth, as well as an open question that identifies a critical limitation in current cold-start inductive biases within this domain.

### Approved Concepts
- EvoXXLTraffic Dataset: Addresses the limitation of fixed-sensor benchmarks by providing a multi-year, evolving network structure for traffic forecasting.

### Approved Open Questions
- Evolving Graph Cold-Start Bottleneck: This identifies a fundamental bottleneck where standard continual learning assumptions for graph-based models (e.g., small, incremental changes) fail in real-world infrastructure growth scenarios, which is crucial for scalable intelligent transportation systems.

## Datasets

- [[evoxxltraffic-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2605.29768)
- [PDF](https://arxiv.org/pdf/2605.29768)

