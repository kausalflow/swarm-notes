---
# CSL-compatible fields
title: "Reconstructing OPC UA Address Spaces from Time-Series Databases"
author:
  - literal: "Lukas Lürzer"
  - literal: "Hannes Unger"
  - literal: "Stefan Huber"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10663"

# Custom fields
paper_id: "2606.10663"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "information-extraction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "opcua-ts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:53:17Z"
created_at: "2026-06-12T08:53:17Z"
---

# Reconstructing OPC UA Address Spaces from Time-Series Databases

**Authors**: Lukas Lürzer, Hannes Unger, Stefan Huber
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10663](https://arxiv.org/abs/2606.10663)

## Summary

This paper addresses the loss of semantic metadata (such as node hierarchies and type definitions) when OPC UA telemetry is archived in standard time-series databases. The authors introduce opcua-ts, an architecture that maintains this metadata alongside telemetry using lifecycle-stable join keys to allow for consistent reconstruction of the original address space. By mapping these persistent records to a live OPC UA endpoint, the system resolves issues related to session-local namespace indices and cross-source identifier collisions. Evaluation using a boiler-simulator setup demonstrates the feasibility and sound reconstruction of complex OPC UA address spaces.

## Key Contributions

- Introduces opcua-ts, an architecture to persist semantic OPC UA metadata alongside telemetry in time-series databases using a lifecycle-stable join key.
- Enables the reconstruction of source OPC UA address spaces as live endpoints from database records, addressing namespace index instability and identifier collisions.
- Provides a formal characterization of sound reconstruction conditions for multi-source deployments and validates results via NodeSet2 XML round-trips.

## Open Questions & Future Work

- [[opcua-type-hierarchy-preservation]]

## Key Concepts

- [[opcua-ts]]: An architecture that persists semantic OPC UA metadata with telemetry for address space reconstruction.

## Archivist Review

The paper introduces a structured approach to metadata preservation for OPC UA systems, which is highly relevant for industrial digital twin fidelity. I approved the core architecture (opcua-ts) and a substantial open research problem regarding semantic type hierarchy preservation. I rejected the subscription-driven metadata crawling question as it pertains more to system engineering/operational implementation than to core research in temporal modeling.

### Approved Concepts
- opcua-ts: It provides a novel mechanism to preserve semantic OPC UA metadata within time-series databases, enabling reconstruction of address spaces.

### Approved Open Questions
- Preserving custom type hierarchies: Preserving type hierarchies is essential for maintaining the semantic fidelity and interoperability of industrial digital twins.

### Rejected Candidates
- [open_question] Subscription-driven metadata updates (`subscription-driven-metadata-crawling`) - low_impact: The problem of dynamic metadata updates is an implementation/engineering challenge rather than a fundamental open question in time-series modeling.

## Links

- [Abstract](https://arxiv.org/abs/2606.10663)
- [PDF](https://arxiv.org/pdf/2606.10663)

