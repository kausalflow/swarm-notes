---
# CSL-compatible fields
title: "One Index for Subsumption and Roll-up across Time, Geography, and Ontology"
author:
  - literal: "Madhulatha Mandarapu"
  - literal: "Sandeep Kunkunuru"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.24677"

# Custom fields
paper_id: "2606.24677"
paper_source: "openalex"
domain: "nlp"
tags:
  - "information-extraction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "oeh-index"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:26:28Z"
created_at: "2026-06-26T08:26:28Z"
---

# One Index for Subsumption and Roll-up across Time, Geography, and Ontology

**Authors**: Madhulatha Mandarapu, Sandeep Kunkunuru
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.24677](https://arxiv.org/abs/2606.24677)

## Summary

This paper introduces OEH, a unified indexing framework that treats time-series, geospatial, and ontological hierarchies as subsumption posets. By representing hierarchies as either nested-set order-embeddings or chain decompositions, the index efficiently performs both subsumption testing and hierarchical monoid aggregation. OEH provides superior space efficiency and construction speed compared to traditional 2-hop indexes while matching the query latency of existing continuous aggregation solutions.

## Key Contributions

- Introduces OEH, a unified indexing framework that encodes various hierarchies (temporal, geospatial, and ontological) as either nested-set order-embeddings or chain decompositions.
- Enables simultaneous subsumption testing and index-resident monoid roll-up queries within a single structure, outperforming standard 2-hop indexing in space efficiency and build time.
- Demonstrates performance parity with continuous aggregates on benchmark systems like TimescaleDB while providing additional support for subsumption queries.

## Open Questions & Future Work

- [[dynamic-maintenance-of-hierarchy-indexes]]

## Key Concepts

- [[oeh-index]]: A unified indexing structure that uses nested-set order-embeddings or chain decompositions to enable both subsumption testing and index-resident monoid aggregation.

## Archivist Review

I approved the OEH Index because it presents a general-purpose, unified framework for managing hierarchy-dependent tasks (subsumption and roll-up) that transcends traditional domain-specific silos. The open question regarding dynamic maintenance was approved because it addresses a fundamental limitation in adopting such sophisticated indexing techniques for modern, high-velocity streaming data systems. Standardized datasets were rejected per the policy to prioritize research-specific benchmarks.

### Approved Concepts
- OEH Index: It provides a unified indexing approach that supports both subsumption and monoid roll-up queries across heterogeneous hierarchical data types, outperforming traditional 2-hop indexing.

### Approved Open Questions
- Dynamic Maintenance of Hierarchy Indexes: Real-world data systems (e.g., knowledge graphs, temporal versioning) are highly dynamic; current static-only limitations hinder the adoption of unified indexing primitives in streaming applications.

### Rejected Candidates
- [dataset] NCBI Taxonomy (`ncbi-taxonomy`) - not_novel: This is a widely available standard taxonomic dataset rather than a novel or highly specialized ML benchmark.
- [dataset] Gene Ontology (`gene-ontology`) - not_novel: This is a standardized domain database, not a specific reusable research benchmark for time-series or ML tasks.
- [dataset] GeoNames (`geonames`) - not_novel: GeoNames is a standard geospatial database used for lookups and is not a novel ML research dataset.

## Links

- [Abstract](https://arxiv.org/abs/2606.24677)
- [PDF](https://arxiv.org/pdf/2606.24677)

