---
# CSL-compatible fields
title: "Importance of Aggregated DER Installed Capacity in Distribution Networks"
author:
  - literal: "Alexandre Gouveia"
  - literal: "Md. Umar Hashmi"
  - literal: "Reinhilde D'hulst"
  - literal: "Dirk Van Hertem"
issued:
  date-parts:
    - [2026, 4, 15]
url: "https://arxiv.org/abs/2604.13926"

# Custom fields
paper_id: "2604.13926"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-18T06:07:18Z"
created_at: "2026-04-18T06:07:18Z"
---

# Importance of Aggregated DER Installed Capacity in Distribution Networks

**Authors**: Alexandre Gouveia, Md. Umar Hashmi, Reinhilde D'hulst, Dirk Van Hertem
**Date**: 2026-04-15
**Paper ID**: [openalex:2604.13926](https://arxiv.org/abs/2604.13926)

## Summary

This paper addresses the observability challenges faced by Distribution System Operators due to the rapid growth of distributed energy resources (DERs) in low-voltage networks. The authors propose estimating aggregated DER installed capacity at LV substation levels using only standard measurements, circumventing the need for granular customer data. This approach is positioned as a foundational requirement to improve operational tasks such as hosting capacity assessment, congestion management, and DER-aware forecasting. By leveraging existing infrastructure measurements, the proposed framework offers a practical and scalable solution for modernizing distribution network visibility.

## Key Contributions

- Proposes aggregated DER installed capacity estimation at LV substations as a scalable alternative to customer-level monitoring for observability.
- Formulates the DER capacity estimation problem based on commonly available substation and feeder measurements.
- Demonstrates how aggregated DER capacity estimates improve downstream tasks including hosting capacity assessment, congestion management, and DER-aware forecasting.

## Open Questions & Future Work

- [[refining-der-capacity-estimation-and-impact-quantification]]

## Archivist Review

I approved the open question regarding DER capacity estimation refinement as it identifies a clear, unresolved methodological bottleneck in grid observability. The proposed concept of 'Aggregated DER Installed Capacity Estimation' was rejected because it represents an application-specific framing of a measurement problem rather than a distinct, reusable algorithmic technique or forecasting representation that would benefit the long-term knowledge vault.

### Approved Open Questions
- Refining DER Capacity Estimation: Quantifying the impact of metadata-aware methods is critical for DSOs to justify investments in better monitoring infrastructure and to validate the theoretical benefits of DER metadata on grid stability and planning efficiency.

### Rejected Candidates
- [concept] Aggregated DER Installed Capacity Estimation (`aggregated-der-installed-capacity-estimation`) - not_reusable: This is an application-specific problem formulation rather than a reusable methodological mechanism or representation technique.

## Links

- [Abstract](https://arxiv.org/abs/2604.13926)
- [PDF](https://arxiv.org/pdf/2604.13926)

