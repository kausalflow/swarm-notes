---
# CSL-compatible fields
title: "Gaia DR3 variable white dwarfs vetted by ZTF"
author:
  - literal: "Timour Jestin"
  - literal: "Thịnh Hữu Nguyễn"
  - literal: "L. Eyer"
  - literal: "L. Rimoldini"
  - literal: "Ashish Mahabal"
  - literal: "M. Audard"
  - literal: "P. García-Lario"
  - literal: "P. Gavras"
  - literal: "K. Nienartowicz"
issued:
  date-parts:
    - [2026, 7, 13]
url: "https://arxiv.org/abs/2509.15133"

# Custom fields
paper_id: "2509.15133"
paper_source: "openalex"
domain: "nlp"
tags:
  - "dataset"
  - "evaluation"
  - "time-series"
architectures:
  []
datasets:
  - "gaia-dr3"
  - "ztf-dr23"
concept_slugs:
  []
dataset_slugs:
  - "gaia-dr3"
  - "ztf-dr23"
skill: "TimeSeriesSkill"
processed_at: "2026-07-16T07:14:41Z"
created_at: "2026-07-16T07:14:41Z"
---

# Gaia DR3 variable white dwarfs vetted by ZTF

**Authors**: Timour Jestin, Thịnh Hữu Nguyễn, L. Eyer, L. Rimoldini, Ashish Mahabal, M. Audard, P. García-Lario, P. Gavras, K. Nienartowicz
**Date**: 2026-07-13
**Paper ID**: [openalex:2509.15133](https://arxiv.org/abs/2509.15133)

## Summary

This paper presents a new catalog of candidate variable white dwarfs identified by cross-matching Gaia DR3 data with ZTF DR23 time-series photometry. The authors applied a multi-band Lomb-Scargle periodogram analysis to detect periodicity, identifying 141 confirmed periodic variables. Using unsupervised clustering, these objects were categorized into known white dwarf variability classes, with 67 of the periodic stars being newly identified.

## Key Contributions

- Constructed a catalogue of 1423 candidate variable white dwarfs using Gaia DR3 astrometric and photometric data.
- Combined Gaia DR3 data with ZTF DR23 time series to identify and classify 141 periodic variable white dwarfs.
- Classified detected periodic sources into known categories including ZZ Ceti stars, V777 Her stars, and white dwarf–main sequence (WD–MS) binaries.

## Open Questions & Future Work

- [[robust-detection-high-freq-pulsating-wd]]

## Archivist Review

The paper focuses on cataloguing white dwarf variability through cross-matching existing astronomical surveys. I approved the two primary astronomical datasets as they are essential, standardized references for stellar variability research. The open question regarding high-frequency detection in white dwarfs is approved because it identifies a clear, non-trivial limitation in current frequency-domain analysis methods for astronomical time series.

### Approved Open Questions
- Robust High-Frequency WD Detection: The current inability to consistently detect these variables limits the completeness of white dwarf variability surveys, which are essential for mapping the crystallization sequence and understanding stellar evolution.

## Datasets

- [[gaia-dr3]]
- [[ztf-dr23]]

## Links

- [Abstract](https://arxiv.org/abs/2509.15133)
- [PDF](https://arxiv.org/pdf/2509.15133)

