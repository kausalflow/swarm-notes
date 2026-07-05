---
created_at: '2026-07-05T07:51:57Z'
source_papers:
- '[[openalex-2607.01918-zeus-towards-tuning-free-foundation-model-for-time-series-an]]'
title: Granularity vs. Scalability Dilemma
---

**Background:** Time series foundation models currently face challenges in effectively balancing fine-grained point-level temporal information with long-sequence computational scalability.

**Question / Future Work:** There is a need to develop more efficient architectures or tokenization schemes that maintain high-resolution point-level temporal fidelity without incurring the prohibitive computational costs typically associated with point-wise processing in Transformer-based models for very long sequences.

**Why It Matters:** This is a fundamental architectural bottleneck that limits the universal applicability of time series foundation models to reconstruction-oriented tasks while maintaining long-range modeling capabilities.

**Evidence:** However, this design inevitably sacrifices point-level temporal details, hindering its effectiveness on reconstruction-based tasks like imputation and anomaly detection... In contrast, point-wise tokenization preserves fine-grained structure but suffers from low information density and prohibitive computational overhead on long sequences.