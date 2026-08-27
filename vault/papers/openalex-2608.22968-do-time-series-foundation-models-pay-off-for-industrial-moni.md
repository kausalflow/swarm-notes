---
# CSL-compatible fields
title: "Do Time-Series Foundation Models Pay Off for Industrial Monitoring? A Cost-Aware Empirical Study"
author:
  - literal: "Guan-Hua Wen"
  - literal: "Kuan-Yu Chen"
issued:
  date-parts:
    - [2026, 8, 24]
url: "https://arxiv.org/abs/2608.22968"

# Custom fields
paper_id: "2608.22968"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "evaluation"
  - "benchmark"
  - "model-compression"
architectures:
  []
datasets:
  - "c-mapss"
  - "mimii"
concept_slugs:
  []
dataset_slugs:
  - "c-mapss"
  - "mimii"
skill: "TimeSeriesSkill"
processed_at: "2026-08-27T15:58:11Z"
created_at: "2026-08-27T15:58:11Z"
---

# Do Time-Series Foundation Models Pay Off for Industrial Monitoring? A Cost-Aware Empirical Study

**Authors**: Guan-Hua Wen, Kuan-Yu Chen
**Date**: 2026-08-24
**Paper ID**: [openalex:2608.22968](https://arxiv.org/abs/2608.22968)

## Summary

This paper presents a cost-aware empirical evaluation comparing time-series foundation models (TSFMs) with classical and lightweight neural models across diverse industrial monitoring tasks including degradation-risk proxy detection, anomalous-sound detection, and forecasting-residual diagnostics. The findings show that lightweight fitted models like TCN-AE and OCSVM often outperform zero-shot or frozen TSFMs while incurring significantly lower computational and storage footprints. Consequently, TSFMs serve as task-dependent options rather than default replacements for localized industrial monitoring architectures.

## Key Contributions

- Provides a protocol-aware empirical assessment comparing time-series foundation models (MOMENT-small, Chronos-T5, TimesFM 2.5) against classical and lightweight neural baselines (TCN-AE, OCSVM) across industrial monitoring tasks.
- Shows that lightweight models such as TCN-AE achieve superior anomaly ranking (AUROC/AUPRC 0.9570/0.8960 vs 0.7310/0.3080 for MOMENT reconstruction) on C-MAPSS degradation-risk tasks.
- Demonstrates that TSFMs incur higher deployment overhead in latency, peak VRAM, and storage than lightweight fitted autoencoders while performing competitively only under specific data and perturbation regimes.

## Limitations

Evaluated under specific frozen and zero-shot deployment configurations; deployment trade-offs may vary with full fine-tuning or specialized downstream adaptation.

## Open Questions & Future Work

- [[tsfm-fine-tuning-vs-frozen-adaptation]]

## Archivist Review

The paper is an empirical evaluation of time-series foundation models versus lightweight fitted models in industrial monitoring. No novel architectural concepts or reusable forecasting mechanisms are introduced that warrant permanent standalone vault notes. The canonical C-MAPSS dataset is already in the vault, and MIMII is approved as a core dataset. The open question was rejected as a standard empirical extension.

### Approved Open Questions
- Fine-Tuning vs. Frozen TSFMs: Understanding whether full fine-tuning or specialized domain adaptation can bridge the performance gap between TSFMs and fitted lightweight models is crucial for cost-aware industrial deployments.

### Rejected Candidates
- [open_question] Fine-Tuning vs. Frozen TSFMs (`tsfm-fine-tuning-vs-frozen-adaptation`) - low_impact: The open question is a straightforward empirical evaluation extension rather than an unresolved theoretical bottleneck or structural limitation.

## Datasets

- [[c-mapss]]
- [[mimii]]

## Links

- [Abstract](https://arxiv.org/abs/2608.22968)
- [PDF](https://arxiv.org/pdf/2608.22968)

