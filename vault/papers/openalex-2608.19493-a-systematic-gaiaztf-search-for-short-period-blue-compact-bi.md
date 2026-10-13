---
# CSL-compatible fields
title: "A Systematic Gaia–ZTF Search for Short-period Blue Compact-binary Candidates"
author:
  - literal: "Jiamao Lin"
  - literal: "Liangliang Ren"
  - literal: "Yilong Li"
  - literal: "Bo Ma"
  - literal: "Di-Chang Chen"
  - literal: "Ziheng Yu"
  - literal: "Sen Yang"
  - literal: "S. Huang"
  - literal: "Yi-Ming Hu"
  - literal: "Chengyuan Li"
issued:
  date-parts:
    - [2026, 10, 12]
url: "https://arxiv.org/abs/2608.19493"

# Custom fields
paper_id: "2608.19493"
paper_source: "openalex"
domain: "astronomy"
tags:
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  - "ztf-dr23"
concept_slugs:
  []
dataset_slugs:
  - "ztf-dr23"
skill: "GeneralMLSkill"
processed_at: "2026-10-13T12:17:11Z"
created_at: "2026-10-13T12:17:11Z"
---

# A Systematic Gaia–ZTF Search for Short-period Blue Compact-binary Candidates

**Authors**: Jiamao Lin, Liangliang Ren, Yilong Li, Bo Ma, Di-Chang Chen, Ziheng Yu, Sen Yang, S. Huang, Yi-Ming Hu, Chengyuan Li
**Date**: 2026-10-12
**Paper ID**: [openalex:2608.19493](https://arxiv.org/abs/2608.19493)

## Summary

The authors combine Gaia DR3 and ZTF DR23 data with machine learning morphology ranking to assemble a catalog of 147 short-period blue compact-binary candidates, comprising 111 new classifications. Multi-wavelength analysis using DESI, GALEX, and AllWISE reveals an intrinsically heterogeneous sample spanning white-dwarf and hot-subdwarf loci. Furthermore, the study highlights that observed modulation amplitudes for many candidates exceed ellipsoidal signals by orders of magnitude, suggesting competing single-star interpretations that require further time-resolved follow-up.

## Key Contributions

- Assembled a catalog of 147 short-period blue compact-binary candidates (10.34–106.46 minutes) by combining Gaia DR3 and ZTF DR23 data using machine learning morphology ranking and ZTF period searches.
- Identified 111 candidates without previous compact-binary classifications, including a prioritized set of new white-dwarf-locus candidates with periods below 40 minutes.
- Demonstrated through multi-wavelength data (DESI DR1, GALEX, AllWISE) and follow-up considerations that the sample is intrinsically heterogeneous, with observed modulation amplitudes exceeding ellipsoidal signals by orders of magnitude for the compact majority, pointing to magnetic or chemically inhomogeneous single white dwarfs as competing interpretations.

## Limitations

ZTF photometry alone cannot conclusively distinguish between binary orbital modulation and rotating magnetic or chemically inhomogeneous single white dwarf interpretations for the majority of the candidates.

## Open Questions & Future Work

- [[binary-versus-rotational-variability]]

## Archivist Review

Approved one open question regarding photometric vs rotational variability ambiguity and one dataset (ZTF DR23) while rejecting domain-specific survey scaling questions and already indexed datasets like Gaia DR3.

### Approved Open Questions
- Binary Versus Rotational Variability: Critical for correctly interpreting photometric variability signatures, avoiding contamination in gravitational-wave source catalogs, and accurately identifying true compact binaries.

### Rejected Candidates
- [open_question] Scalable Survey Selection Vetting (`survey-selection-and-vetting-scalability`) - low_impact: Too general and domain-specific to astronomy survey processing rather than a broad ML bottleneck.
- [dataset] Gaia DR3 (`gaia-dr3`) - duplicate_existing: Gaia DR3 is already a widely known external astronomical survey catalog and dataset.

## Datasets

- [[ztf-dr23]]

## Links

- [Abstract](https://arxiv.org/abs/2608.19493)
- [PDF](https://arxiv.org/pdf/2608.19493)

