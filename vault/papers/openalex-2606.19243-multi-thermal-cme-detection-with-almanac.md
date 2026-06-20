---
# CSL-compatible fields
title: "Multi-Thermal CME Detection with ALMANAC"
author:
  - literal: "Thomas Williams"
  - literal: "Christopher Prior"
  - literal: "David MacTaggart"
  - literal: "Huw Morgan"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.19243"

# Custom fields
paper_id: "2606.19243"
paper_source: "openalex"
domain: "space-weather"
tags:
  - "anomaly-detection"
  - "time-series"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "almanac-algorithm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:18:27Z"
created_at: "2026-06-20T08:18:27Z"
---

# Multi-Thermal CME Detection with ALMANAC

**Authors**: Thomas Williams, Christopher Prior, David MacTaggart, Huw Morgan
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.19243](https://arxiv.org/abs/2606.19243)

## Summary

This paper introduces a re-engineered, multi-thermal implementation of the ALMANAC algorithm to improve the detection of low-coronal CME origins in EUV observations. By integrating multi-wavelength data with a spatiotemporal clustering scheme, the framework enhances event discrimination, reduces signal fragmentation, and improves localization consistency. Furthermore, the authors demonstrate that integrating these coronal intensity diagnostics with photospheric magnetic topology allows for the identification of recurrent pre-eruptive precursors, offering a more effective pathway for space weather early warning systems.

## Key Contributions

- Re-engineered a multi-thermal version of the ALMANAC algorithm for robust detection of eruptive signatures across multiple EUV wavelengths.
- Introduced a spatiotemporal clustering scheme that merges multi-channel detections to reduce event bifurcation and improve detection coherence.
- Demonstrated that multi-wavelength kurtosis time-series combined with magnetic helicity metrics provide reliable pre-eruptive precursors for solar activity.

## Open Questions & Future Work

- [[autonomous-spurious-detection-filtering]]

## Key Concepts

- [[almanac-algorithm]]: A multi-thermal framework for detecting eruptive coronal mass ejection signatures across multiple EUV wavelengths.

## Archivist Review

The review focused on the core algorithmic contribution to multi-thermal eruption detection and the fundamental bottleneck preventing the automation of operational space-weather warnings. The ALMANAC algorithm is approved for its distinct methodological fusion approach, and the open question regarding autonomous filtering is approved as a critical, high-impact research challenge in the field. Routine benchmark usage (CDAW) was rejected to maintain vault focus on novel methodological research components.

### Approved Concepts
- ALMANAC Algorithm: Central algorithm for space-weather eruption detection from multi-wavelength EUV observations.

### Approved Open Questions
- Autonomous Spurious Detection Filtering: This is a primary bottleneck for scaling research-level solar detection algorithms into autonomous operational early-warning systems.

### Rejected Candidates
- [dataset] CDAW (`CDAW`) - not_novel: This is a well-established standard catalog for CMEs rather than a novel or highly specific research dataset that requires a standalone vault note for this paper.

## Links

- [Abstract](https://arxiv.org/abs/2606.19243)
- [PDF](https://arxiv.org/pdf/2606.19243)

