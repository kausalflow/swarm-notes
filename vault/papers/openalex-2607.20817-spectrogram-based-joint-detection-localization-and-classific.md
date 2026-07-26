---
# CSL-compatible fields
title: "Spectrogram-Based Joint Detection, Localization, and Classification of Events in Continuously Recorded IBR Waveforms"
author:
  - literal: "Shivanshu Tripathi"
  - literal: "Maziar Raissi"
  - literal: "Hamed Mohsenian‐Rad"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2607.20817"

# Custom fields
paper_id: "2607.20817"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-26T07:30:03Z"
created_at: "2026-07-26T07:30:03Z"
---

# Spectrogram-Based Joint Detection, Localization, and Classification of Events in Continuously Recorded IBR Waveforms

**Authors**: Shivanshu Tripathi, Maziar Raissi, Hamed Mohsenian‐Rad
**Date**: 2026-07-23
**Paper ID**: [openalex:2607.20817](https://arxiv.org/abs/2607.20817)

## Summary

This paper proposes a spectrogram-based framework for jointly detecting, localizing, and classifying power system events in continuously recorded high-resolution waveforms from Inverter-Based Resources (IBRs). By transforming time-series measurements into stacked per-channel spectrograms using the short-time Fourier transform, the problem is cast as temporal object detection. Experiments on single-phase disturbances and three-phase faults show that this spectrogram-based approach improves performance over raw time-series baselines.

## Key Contributions

- Developed a spectrogram-based framework to jointly detect, localize, and classify events in continuously recorded high-resolution waveform measurements from Inverter-Based Resources (IBRs).
- Recast the event identification problem as a temporal object detection task on stacked per-channel spectrogram images derived via the short-time Fourier transform.
- Demonstrated through experiments on single-phase disturbances and three-phase faults that the spectrogram approach consistently outperforms raw time-series baselines.

## Archivist Review

The proposed open questions represent standard application-level future work (streaming inference and finer-grained classification) rather than fundamental, structurally reusable research bottlenecks. No concepts or datasets met the strict vault standards.

### Rejected Candidates
- [open_question] Real-Time Streaming Waveform Monitoring (`real-time-streaming-waveform-monitoring`) - low_impact: Standard future work regarding streaming deployment without a specific methodological bottleneck.
- [open_question] Fine-Grained Event Type Discrimination (`fine-grained-event-type-discrimination`) - low_impact: Generic classification accuracy improvement request rather than an enduring structural research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.20817)
- [PDF](https://arxiv.org/pdf/2607.20817)

