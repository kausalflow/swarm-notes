---
# CSL-compatible fields
title: "FALLNEST: Dual-Domain Dataset Condensation of Imbalanced IMU Data for Wearable Fall Detection"
author:
  - literal: "Rashi Niyas P"
  - literal: "Ritika Jain"
  - literal: "Hitika Tiwari"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.18260"

# Custom fields
paper_id: "2610.18260"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "dataset"
  - "robustness"
  - "imbalance"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fallnest"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:25:26Z"
created_at: "2026-10-16T09:25:26Z"
---

# FALLNEST: Dual-Domain Dataset Condensation of Imbalanced IMU Data for Wearable Fall Detection

**Authors**: Rashi Niyas P, Ritika Jain, Hitika Tiwari
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.18260](https://arxiv.org/abs/2610.18260)

## Summary

Wearable fall detection suffers from rare fall events, severe class imbalance, and high data acquisition and training costs. To address this, the authors propose FALLNEST, a dual-domain time-series dataset condensation approach that distills large imbalanced IMU datasets into compact, class-balanced synthetic training sets. By leveraging normalized gradient matching, MMD embedding alignment, and a 7-channel fall-specific input representation, a TinyCNN trained on just 1% of the original training data achieves high accuracy and PR-AUC across SisFall, KFall, and MobiFall.

## Key Contributions

- Proposes FALLNEST, a dual-domain dataset condensation framework that distills large, imbalanced IMU datasets into tiny, class-balanced synthetic training sets.
- Incorporates a fall-specific 7-channel input representation, class-balanced K-Means initialization, normalized gradient matching with gradient clipping, and MMD-based embedding alignment.
- Demonstrates that training a 102K-parameter TinyCNN on only 1% of synthetic training windows achieves 93.5-95.8% mean accuracy and 0.89-0.98 PR-AUC on SisFall, KFall, and MobiFall datasets.

## Limitations

Future work could explore scaling dataset condensation to broader multi-modal sensor streams and real-time edge streaming environments.

## Key Concepts

- [[fallnest]]: A dual-domain dataset condensation framework for distilling large, imbalanced IMU datasets into compact class-balanced synthetic training sets.

## Archivist Review

Approved the core 'FALLNEST' concept because it introduces a distinct dual-domain dataset condensation mechanism for imbalanced IMU time-series data. Rejected both open questions as routine hardware deployment and downstream application future work. No datasets were approved as they represent standard domain benchmark corpora.

### Approved Concepts
- FALLNEST: Introduces a dual-domain dataset condensation technique specifically tailored for imbalanced IMU data in wearable fall detection.

### Rejected Candidates
- [open_question] False-Alarm Analysis on Free-Living Data (`false-alarm-analysis-free-living`) - low_impact: Boilerplate future work assessing deployment performance rather than an unresolved methodological limitation.
- [open_question] Microcontroller Deployment of Wearable Models (`microcontroller-deployment-wearable-ai`) - low_impact: Standard hardware implementation evaluation rather than a conceptual or theoretical research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.18260)
- [PDF](https://arxiv.org/pdf/2610.18260)

