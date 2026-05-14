---
# CSL-compatible fields
title: "A Taxonomy of Event-Linked Perpetual Futures: Variant Designs Beyond the Single-Market Binary Case"
author:
  - literal: "Maksym Nechepurenko"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10428"

# Custom fields
paper_id: "2605.10428"
paper_source: "openalex"
domain: "finance"
tags:
  - "finance"
architectures:
  []
datasets:
  []
concept_slugs:
  - "event-linked-perpetual-futures-taxonomy"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:39:28Z"
created_at: "2026-05-14T07:39:28Z"
---

# A Taxonomy of Event-Linked Perpetual Futures: Variant Designs Beyond the Single-Market Binary Case

**Authors**: Maksym Nechepurenko
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10428](https://arxiv.org/abs/2605.10428)

## Summary

This paper extends a risk-design framework for event-linked perpetual futures by categorizing seven canonical instrument variants beyond the basic single-market binary contract. The author defines these variants along four orthogonal design axes—underlying geometry, temporal structure, settlement structure, and venue composition—and evaluates their specific design constraints and microstructure properties. By analyzing theoretical payoffs and inheritance maps, the work provides a structured foundation for evaluating complex derivative instruments on prediction market processes.

## Key Contributions

- Proposes a formal taxonomy of seven canonical event-linked perpetual futures variants beyond simple binary contracts.
- Organizes contract design along four orthogonal axes: underlying geometry, temporal structure, settlement structure, and venue composition.
- Identifies critical design trade-offs, such as denominator instability in conditional variants and the need for multi-period jump-aware margin in basket variants.

## Open Questions & Future Work

- [[conditional-denominator-instability]]
- [[multi-leg-margin-aggregation]]

## Key Concepts

- [[event-linked-perpetual-futures-taxonomy]]: A structured taxonomy classifying event-linked perpetual futures into seven canonical variants based on underlying geometry, temporal structure, settlement structure, and venue composition.

## Archivist Review

The taxonomy of event-linked perpetuals is approved as a foundational framework for a growing class of financial derivatives. The two open questions address fundamental structural stability and risk management challenges (denominator singularity and multi-period margin aggregation) in these novel instruments. The PMXT v2 dataset is rejected as a paper-local archive.

### Approved Concepts
- Event-Linked Perpetual Futures Taxonomy: It provides the foundational framework for classifying and designing non-binary event-linked perpetual financial instruments.

### Approved Open Questions
- Conditional Denominator Instability: This represents a fundamental structural failure mode for the specific instrument variant that is currently theoretically conjectured but lacks a deployed or formally specified solution.
- Multi-leg Margin Aggregation: Proper margin calibration is the primary mechanism for preventing bad debt in binary prediction-market perpetuals, and the aggregation of multiple jump-risk channels in complex variants is a critical, unresolved risk-engineering bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2605.10428)
- [PDF](https://arxiv.org/pdf/2605.10428)

