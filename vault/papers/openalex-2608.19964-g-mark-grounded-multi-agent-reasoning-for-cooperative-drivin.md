---
# CSL-compatible fields
title: "G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs"
author:
  - literal: "Bhavya Gupta"
  - literal: "Onat Güngör"
  - literal: "Tajana Rosing"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.19964"

# Custom fields
paper_id: "2608.19964"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multi-agent"
  - "autonomous-agent"
  - "knowledge-graph"
  - "robotics"
architectures:
  []
datasets:
  []
concept_slugs:
  - "g-mark"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:20:11Z"
created_at: "2026-08-23T05:20:11Z"
---

# G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs

**Authors**: Bhavya Gupta, Onat Güngör, Tajana Rosing
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.19964](https://arxiv.org/abs/2608.19964)

## Summary

Autonomous driving systems face partial observability due to occlusions, which can be mitigated via vehicle-to-vehicle cooperation. Existing methods compress multi-agent evidence into opaque latent features, obscuring object provenance and conflict resolution. The authors propose G-MARK, a framework that transforms cooperative object observations into explicit provenance-aware knowledge graphs that track source attribution, visibility, and uncertainty, improving occlusion reasoning accuracy by 42.2% and reducing communication payloads by 25.6x.

## Key Contributions

- Proposes G-MARK, a grounded multi-agent reasoning framework converting cooperative object observations into provenance-aware knowledge graphs preserving source attribution, visibility, uncertainty, and conflicts.
- Improves occlusion reasoning accuracy by 42.2% compared to state-of-the-art latent-feature-based multi-agent baselines.
- Reduces control-selection error by 13.1% while achieving comparable trajectory-planning accuracy with a 25.6x smaller structured communication payload.

## Key Concepts

- [[g-mark]]: A grounded multi-agent reasoning framework that converts cooperative object-centric observations into explicit provenance-aware knowledge graphs to handle partial observability and uncertainty in autonomous driving.

## Archivist Review

Approved G-MARK as a central concept representing provenance-aware knowledge graphs for multi-agent cooperative perception. No datasets or open questions met the stringent reusability and novelty criteria.

### Approved Concepts
- G-MARK: Introduces a provenance-aware knowledge graph framework for multi-agent cooperative autonomous driving, replacing opaque latent feature communication with explicit graph-based source attribution.

## Links

- [Abstract](https://arxiv.org/abs/2608.19964)
- [PDF](https://arxiv.org/pdf/2608.19964)

