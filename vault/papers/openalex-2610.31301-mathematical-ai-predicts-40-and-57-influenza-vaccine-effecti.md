---
# CSL-compatible fields
title: "Mathematical AI Predicts 40% and 57% Influenza Vaccine Effectiveness Against H1N1 and H3N2, Respectively, for the 2026--2027 U.S. Season"
author:
  - literal: "Xiang Xiang Wang"
  - literal: "Guo-Wei Wei"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.31301"

# Custom fields
paper_id: "2610.31301"
paper_source: "openalex"
domain: "biology"
tags:
  - "forecasting"
  - "dataset"
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
processed_at: "2026-10-25T09:29:44Z"
created_at: "2026-10-25T09:29:44Z"
---

# Mathematical AI Predicts 40% and 57% Influenza Vaccine Effectiveness Against H1N1 and H3N2, Respectively, for the 2026--2027 U.S. Season

**Authors**: Xiang Xiang Wang, Guo-Wei Wei
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.31301](https://arxiv.org/abs/2610.31301)

## Summary

This paper presents a mathematical AI approach to forecast preseason clinical influenza vaccine effectiveness (VE) using hemagglutinin sequence data from GISAID. By computing topological and geometric distances between circulating strains and vaccine targets across historical seasons (2010-2025), the authors fitted regression models to predict VE. Applying this model to sequences from August-September 2026, they forecasted VE values of 40.3% for H1N1 and 56.9% for H3N2 for the 2026-2027 U.S. influenza season.

## Key Contributions

- Forecasted influenza vaccine effectiveness for the 2026-2027 U.S. season using mathematical AI and hemagglutinin sequence distances, predicting 40.3% against H1N1 and 56.9% against H3N2.
- Evaluated topological and geometric models on 26 historical observations across 13 seasons, demonstrating negative association between virus-vaccine sequence distances and clinical vaccine effectiveness.
- Established a methodology leveraging pre-season GISAID hemagglutinin sequences (August-September) to enable timely preseason forecasting of clinical influenza vaccine effectiveness.

## Open Questions & Future Work

- [[prospective-validation-influenza-ve-ai]]

## Archivist Review

Applied strict selection criteria to maintain vault hygiene. No reusable architectural or conceptual innovations were identified, but the open question regarding prospective validation of epidemiological vaccine effectiveness models addresses a distinct methodological bottleneck in public health forecasting.

### Approved Open Questions
- Prospective Validation of Influenza VE Forecasts: Crucial for determining whether mathematical AI models can transition from retrospective analysis to operationally reliable, prospective tools for public health planning and resource allocation.

### Rejected Candidates
- [dataset] GISAID (`gisaid`) - not_reusable: GISAID is a broad genomic database repository rather than a dedicated benchmark dataset or corpus.

## Links

- [Abstract](https://arxiv.org/abs/2610.31301)
- [PDF](https://arxiv.org/pdf/2610.31301)

