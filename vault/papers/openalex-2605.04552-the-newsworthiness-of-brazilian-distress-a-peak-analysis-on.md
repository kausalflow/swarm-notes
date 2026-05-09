---
# CSL-compatible fields
title: "The Newsworthiness of Brazilian Distress: A Peak Analysis on Time Series of International Media Attention to Disasters in Brazil"
author:
  - literal: "Brielen Madureira"
  - literal: "Andreas Niekler"
  - literal: "Marc Keuschnigg"
  - literal: "Mariana Madruga de Brito"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2605.04552"

# Custom fields
paper_id: "2605.04552"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:02:14Z"
created_at: "2026-05-09T07:02:14Z"
---

# The Newsworthiness of Brazilian Distress: A Peak Analysis on Time Series of International Media Attention to Disasters in Brazil

**Authors**: Brielen Madureira, Andreas Niekler, Marc Keuschnigg, Mariana Madruga de Brito
**Date**: 2026-05-06
**Paper ID**: [openalex:2605.04552](https://arxiv.org/abs/2605.04552)

## Summary

This paper investigates the determinants of international media attention toward localized disasters in Brazil by analyzing 2,000 German news articles covering fires and landslides from 2000 to 2024. The authors employ time series segmentation to detect significant peaks in media coverage and assess their temporal correlation with established disaster databases. The study highlights the gap in systematic understanding of international media attention drivers and provides a methodology for evaluating news-event alignment.

## Key Contributions

- Constructed a representative, validated, and country-specific news dataset comprising 2,000 articles on Brazilian fires and landslides in German newspapers (2000–2024).
- Developed a time series peak analysis methodology using segmentation to identify and characterize international news attention spikes.
- Evaluated the temporal alignment between detected media attention peaks and recorded disaster events in national and global databases to assess the drivers of newsworthiness.

## Open Questions & Future Work

- [[temporal-alignment-news-disaster-databases]]

## Archivist Review

The paper provides a niche empirical study on media attention, which does not introduce novel, reusable ML methodology or concepts. I have approved the open question regarding temporal alignment of heterogeneous data sources (media vs. event databases) as it captures a non-trivial, domain-agnostic bottleneck in time series analysis.

### Approved Open Questions
- Temporal Alignment of Media and Disaster Data: Temporal misalignment hinders the automated validation of news datasets against authoritative disaster records, limiting the ability to draw reliable conclusions about how specific disaster characteristics drive international media attention.

### Rejected Candidates
- [concept] News Peak Segmentation Methodology (`news-peak-segmentation-methodology`) - not_novel: This is a generic application of time series segmentation to news data, lacking the novelty required for a permanent research concept.
- [dataset] Brazilian Fires and Landslides Dataset (`brazilian-fires-and-landslides-dataset`) - low_impact: This is a niche, small-scale dataset that does not meet the standard for a critical, widely applicable research dataset in the ML vault.

## Links

- [Abstract](https://arxiv.org/abs/2605.04552)
- [PDF](https://arxiv.org/pdf/2605.04552)

