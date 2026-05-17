---
# CSL-compatible fields
title: "NeuroAtlas: Benchmarking Foundation Models for Clinical EEG and Brain-Computer Interfaces"
author:
  - literal: "Konstantinos Kontras"
  - literal: "Trui Osselaer"
  - literal: "Stylianos G. Mouslech"
  - literal: "Angeliki-Ιlektra Karaiskou"
  - literal: "Guido Gagliardi"
  - literal: "Thomas Strypsteen"
  - literal: "Mohammad Hossein Badiei"
  - literal: "Anku Rani"
  - literal: "Maarten Vanmarcke"
  - literal: "Miguel Bhagubai"
  - literal: "Chanakya Ekbote"
  - literal: "Jaedong Hwang"
  - literal: "Christos Chatzichristos"
  - literal: "Paul Pu Liang"
  - literal: "Maarten De Vos"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14698"

# Custom fields
paper_id: "2605.14698"
paper_source: "openalex"
domain: "medicine"
tags:
  - "benchmark"
  - "llm"
  - "time-series"
  - "multimodal"
  - "language-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "neuroatlas"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:31:14Z"
created_at: "2026-05-17T07:31:14Z"
---

# NeuroAtlas: Benchmarking Foundation Models for Clinical EEG and Brain-Computer Interfaces

**Authors**: Konstantinos Kontras, Trui Osselaer, Stylianos G. Mouslech, Angeliki-Ιlektra Karaiskou, Guido Gagliardi, Thomas Strypsteen, Mohammad Hossein Badiei, Anku Rani, Maarten Vanmarcke, Miguel Bhagubai, Chanakya Ekbote, Jaedong Hwang, Christos Chatzichristos, Paul Pu Liang, Maarten De Vos
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14698](https://arxiv.org/abs/2605.14698)

## Summary

NeuroAtlas is a comprehensive benchmark designed to assess foundation models on clinical EEG and brain-computer interface (BCI) tasks, aggregating 42 datasets and 260k hours of data. The authors evaluate various EEG-specific and generic time-series foundation models, finding that neither group consistently outperforms the other. Furthermore, the study critiques standard ML metrics, advocating for clinically relevant measures such as event-level decision accuracy and brain-age estimation gaps to better reflect real-world utility. Results suggest that existing foundation models have yet to provide a robust, out-of-the-box unified EEG representation.

## Key Contributions

- Introduces NeuroAtlas, a large-scale benchmark comprising 42 datasets and 260k hours of EEG data to evaluate foundation model performance in clinical and BCI applications.
- Demonstrates that current EEG-specific foundation models do not consistently outperform generic time-series foundation models, highlighting a lack of specialized advantage.
- Proposes and demonstrates the use of clinically relevant evaluation metrics (e.g., event-level decision-making quality, hypnogram-derived features) over standard machine learning metrics to better assess clinical utility.

## Open Questions & Future Work

- [[eeg-fm-vs-ts-fm-utility]]

## Key Concepts

- [[neuroatlas]]: A comprehensive benchmarking suite for evaluating foundation models across 42 clinical EEG and brain-computer interface datasets.

## Archivist Review

NeuroAtlas provides a significant benchmarking contribution for clinical EEG and BCI, consolidating heterogeneous tasks under clinically meaningful metrics. I approved the benchmark concept and the central open question regarding the efficacy of specialized versus generalist temporal foundation models in neurophysiological domains. Other candidates were rejected to prioritize core architectural and evaluation bottlenecks.

### Approved Concepts
- NeuroAtlas: Establishes a standardized, massive-scale evaluation framework for EEG foundation models, addressing fragmentation in current clinical EEG research.

### Approved Open Questions
- Utility of EEG Pretraining: Crucial for guiding the development of the next generation of unified EEG foundation models and avoiding unnecessary data-intensive overhead.

## Links

- [Abstract](https://arxiv.org/abs/2605.14698)
- [PDF](https://arxiv.org/pdf/2605.14698)

