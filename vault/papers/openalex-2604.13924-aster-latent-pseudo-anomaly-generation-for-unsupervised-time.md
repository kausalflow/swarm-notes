---
# CSL-compatible fields
title: "ASTER: Latent Pseudo-Anomaly Generation for Unsupervised Time-Series Anomaly Detection"
author:
  - literal: "Romain Hermary"
  - literal: "Samet Hiçsönmez"
  - literal: "Dan Pineau"
  - literal: "Abd El Rahman Shabayek"
  - literal: "Djamila Aouada"
issued:
  date-parts:
    - [2026, 4, 15]
url: "https://arxiv.org/abs/2604.13924"

# Custom fields
paper_id: "2604.13924"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "transformer"
  - "llm"
  - "language-model"
  - "unsupervised-learning"
architectures:
  - "transformer"
datasets:
  []
concept_slugs:
  - "latent-pseudo-anomaly-generation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-18T06:06:29Z"
created_at: "2026-04-18T06:06:29Z"
---

# ASTER: Latent Pseudo-Anomaly Generation for Unsupervised Time-Series Anomaly Detection

**Authors**: Romain Hermary, Samet Hiçsönmez, Dan Pineau, Abd El Rahman Shabayek, Djamila Aouada
**Date**: 2026-04-15
**Paper ID**: [openalex:2604.13924](https://arxiv.org/abs/2604.13924)

## Summary

Time-series anomaly detection (TSAD) is hampered by data scarcity and the difficulty of defining complex, heterogeneous anomalies. ASTER addresses these challenges by generating pseudo-anomalies directly in the latent space, using a decoder to train a Transformer-based classifier without manual intervention. Furthermore, the framework integrates pre-trained LLMs to enrich the latent space with superior temporal and contextual information. Experimental results demonstrate that ASTER outperforms existing state-of-the-art methods across multiple benchmarks.

## Key Contributions

- Introduces ASTER, a latent-space pseudo-anomaly generation framework that eliminates the need for handcrafted anomaly injection or domain-specific expertise.
- Leverages pre-trained LLMs to enhance temporal and contextual latent representations for anomaly classification.
- Achieves state-of-the-art performance on three standard time-series anomaly detection benchmarks, establishing a new baseline for LLM-integrated TSAD.

## Open Questions & Future Work

- [[enhancing-latent-pseudo-anomaly-diversity]]

## Key Concepts

- [[latent-pseudo-anomaly-generation]]: A technique for unsupervised anomaly detection where pseudo-anomalies are synthesized directly within the latent representation space rather than by modifying input time series.

## Archivist Review

I approved the latent pseudo-anomaly generation technique as it represents a core paradigm shift in unsupervised TSAD, moving away from input-space injections. I rejected the 'ASTER' framework name in favor of this conceptual description to maintain a cleaner, mechanism-focused vault. The open question regarding pseudo-anomaly diversity addresses a fundamental bottleneck in the effectiveness of latent-space generation methods.

### Approved Concepts
- Latent Pseudo-Anomaly Generation: It shifts anomaly detection from raw space manipulation to latent space transformation, potentially decoupling anomaly generation from raw data characteristics.

### Approved Open Questions
- Enhancing latent pseudo-anomaly diversity: Limited pseudo-anomaly diversity restricts model robustness and prevents generalization to the highly heterogeneous anomalies found in real-world time-series datasets.

### Rejected Candidates
- [concept] ASTER Framework (`aster-framework`) - subcomponent_of_broader_mechanism: Replaced by the more descriptive and reusable 'Latent Pseudo-Anomaly Generation' which captures the core innovation.

## Links

- [Abstract](https://arxiv.org/abs/2604.13924)
- [PDF](https://arxiv.org/pdf/2604.13924)

