---
# CSL-compatible fields
title: "MarsCast: Transfer Learning of AI Weather Foundation Models to Planetary Atmospheres"
author:
  - literal: "M.L. Carroll"
  - literal: "J. Li"
  - literal: "S. D. Guzewich"
  - literal: "G. Villanueva"
  - literal: "J.A. Caraballo-Vega"
  - literal: "M. J. Frost"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.05054"

# Custom fields
paper_id: "2608.05054"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "forecasting"
  - "robustness"
  - "fine-tuning"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-08T05:35:02Z"
created_at: "2026-08-08T05:35:02Z"
---

# MarsCast: Transfer Learning of AI Weather Foundation Models to Planetary Atmospheres

**Authors**: M.L. Carroll, J. Li, S. D. Guzewich, G. Villanueva, J.A. Caraballo-Vega, M. J. Frost
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.05054](https://arxiv.org/abs/2608.05054)

## Summary

This paper investigates the transferability of Earth weather foundation models to planetary atmospheres by adapting GraphCast to Mars using data from the Mars Climate Database. While zero-shot forecasts capture baseline conditions, they fail to capture diurnal variability without fine-tuning. By fine-tuning with top-of-atmosphere solar radiation forcing, the adapted model rapidly learns Martian thermal variability within 10 epochs and successfully forecasts seasonal and vertical temperature structures up to 10 days ahead.

## Key Contributions

- Demonstrates that Earth-trained weather foundation models like GraphCast can be transferred and fine-tuned for Martian atmospheric forecasting.
- Shows that zero-shot application captures broad conditions but fails on diurnal cycles, whereas fine-tuning with solar radiation forcing enables rapid learning of Martian thermal variability within 10 epochs.
- Proves that 10-day forecasts successfully reproduce seasonal and vertical temperature structures, supporting planetary mission operations and dust storm risk mitigation.

## Limitations

Zero-shot forecasts fail to capture diurnal variability and decay toward climatological means without planetary-specific fine-tuning and solar radiation forcing.

## Archivist Review

Reviewed the candidate concept (MarsCast) and determined it is primarily a domain-specific application of transfer learning to Martian atmospheric simulation rather than a broadly recurring general-purpose machine learning concept. Adhering to strict vault curation and scarcity policies, no concepts, open questions, or datasets were approved.

### Rejected Candidates
- [concept] MarsCast (`marscast`) - paper_local: MarsCast is a domain-specific application of fine-tuning an existing terrestrial weather model (GraphCast) to Mars rather than a reusable core forecasting mechanism or architectural vault concept.

## Links

- [Abstract](https://arxiv.org/abs/2608.05054)
- [PDF](https://arxiv.org/pdf/2608.05054)

