---
# CSL-compatible fields
title: "A Search for Wide-orbit Planets Around M-dwarfs using Deep MIRI 15-micron Images"
author:
  - literal: "Yihan Li"
  - literal: "Yifan Zhou"
  - literal: "Rachel Bowens-Rubin"
  - literal: "Mary Anne Limbach"
  - literal: "Hannah Diamond-Lowe"
  - literal: "Cassidy Walker"
  - literal: "Kevin B. Stevenson"
  - literal: "Andrew Vanderburg"
  - literal: "G. Strampelli"
  - literal: "Gregory J. Herczeg"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2604.07703"

# Custom fields
paper_id: "2604.07703"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:19:52Z"
created_at: "2026-04-12T06:19:52Z"
---

# A Search for Wide-orbit Planets Around M-dwarfs using Deep MIRI 15-micron Images

**Authors**: Yihan Li, Yifan Zhou, Rachel Bowens-Rubin, Mary Anne Limbach, Hannah Diamond-Lowe, Cassidy Walker, Kevin B. Stevenson, Andrew Vanderburg, G. Strampelli, Gregory J. Herczeg
**Date**: 2026-04-09
**Paper ID**: [openalex:2604.07703](https://arxiv.org/abs/2604.07703)

## Summary

This paper investigates the population of wide-orbit gas giant planets around M-dwarf stars using archival JWST MIRI 15-micron time-series imaging. By applying reference differential imaging (RDI) for precise PSF subtraction, the authors achieve deep contrast sensitivities capable of detecting Jupiter-sized, cool (170 K) planets at separations beyond 35 AU. The study provides detection probability maps as a function of planet mass and semimajor axis, demonstrating the utility of repurposing transit survey data for exoplanetary companion characterization.

## Key Contributions

- Demonstrates that JWST MIRI time-series imaging enables high-sensitivity searches for wide-orbit gas giants around M-dwarf systems.
- Achieves median 5σ contrast sensitivities of 8.9e-4 to 6.2e-3 at 1 arcsecond, enabling detection of Jupiter-mass planets at separations >35 AU.
- Establishes a methodology for leveraging archival MIRI transit observation data for wide-orbit companion identification via reference differential imaging (RDI).

## Open Questions & Future Work

- [[evolutionary-models-for-old-low-mass-planets]]

## Archivist Review

This paper focuses on astronomical observational techniques and exoplanet detection, which fall outside the scope of core machine learning research methodology. No novel ML concepts were identified. One open question regarding the need for better planetary evolution models was approved, as it represents a significant bottleneck for the domain-specific interpretation of direct imaging data.

### Approved Open Questions
- Evolutionary Models for Old Planets: Without these models, direct imaging surveys are unable to interpret non-detections or define reliable mass-sensitivity limits for the oldest planetary systems, which represent a significant fraction of the M-dwarf population.

### Rejected Candidates
- [concept] Reference Differential Imaging (RDI) (`reference-differential-imaging`) - not_novel: RDI is a long-standing, established technique in observational astronomy and is not a novel machine learning concept.

## Links

- [Abstract](https://arxiv.org/abs/2604.07703)
- [PDF](https://arxiv.org/pdf/2604.07703)

