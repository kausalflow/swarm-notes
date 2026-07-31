---
# CSL-compatible fields
title: "Visibility graph-based characterization of extreme values in time series"
author:
  - literal: "Juliane T. Moraes"
  - literal: "Lucas Lacasa"
  - literal: "Cristina Masoller"
issued:
  date-parts:
    - [2026, 7, 28]
url: "https://arxiv.org/abs/2607.25214"

# Custom fields
paper_id: "2607.25214"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-31T07:43:51Z"
created_at: "2026-07-31T07:43:51Z"
---

# Visibility graph-based characterization of extreme values in time series

**Authors**: Juliane T. Moraes, Lucas Lacasa, Cristina Masoller
**Date**: 2026-07-28
**Paper ID**: [openalex:2607.25214](https://arxiv.org/abs/2607.25214)

## Summary

This paper introduces a visibility graph-based approach for characterizing extreme values in time series without relying on external thresholds or parameters. By mapping time series into networks, the method utilizes the monotonic and nonlinear relationship between node degree and data values to amplify large fluctuations and suppress noise. Validated on synthetic and climatological datasets, the approach enhances traditional extreme-value detection in stationary processes and provides a robust alternative for nonstationary processes where conventional methods fail.

## Key Contributions

- Proposes a parameter-free, visibility graph-based characterization method for identifying extreme values in both stationary and nonstationary time series.
- Leverages the nonlinear and monotonic relationship between node degree and data value in visibility graphs to amplify large values and suppress noise.
- Demonstrates the effectiveness of the method using synthetic time series and real climatological data, showing improvements in stationary series and a robust alternative for ill-posed nonstationary cases.

## Open Questions & Future Work

- [[vg-extreme-values-regime-shifts]]

## Archivist Review

I approved the open question regarding the connection between visibility-graph-based extreme value detection and regime shifts because it addresses an unresolved methodological frontier in complex systems. I rejected the concept candidate as visibility graphs are already a well-established time-series mapping technique, making the specific application an incremental extension rather than a foundational vault primitive.

### Approved Open Questions
- Visibility Graphs for Regime Shifts: Connecting network-based extreme value detection directly to physical regime shifts and dynamical tipping points bridges abstract topological time-series features with concrete mechanistic insights in complex systems.

### Rejected Candidates
- [concept] Visibility graph-based extreme value characterization (`visibility-graph-extreme-value-characterization`) - not_novel: Visibility graphs are a standard existing concept in time-series analysis; applying them to extreme value detection is a domain-specific application rather than a new standalone conceptual primitive.

## Links

- [Abstract](https://arxiv.org/abs/2607.25214)
- [PDF](https://arxiv.org/pdf/2607.25214)

