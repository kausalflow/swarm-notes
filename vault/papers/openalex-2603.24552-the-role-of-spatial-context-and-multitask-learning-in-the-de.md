---
# CSL-compatible fields
title: "The role of spatial context and multitask learning in the detection of organic and conventional farming systems based on Sentinel-2 time series"
author:
  - literal: "Jan Hemmerling"
  - literal: "Marcel Schwieder"
  - literal: "Philippe Rufin"
  - literal: "Leon-Friedrich Thomas"
  - literal: "Mirela G. Tulbure"
  - literal: "Patrick Hostert"
  - literal: "Stefan Erasmi"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24552"

# Custom fields
paper_id: "2603.24552"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "vision-transformer"
  - "multitask"
  - "remote-sensing"
  - "time-series"
  - "image-classification"
  - "patch-size"
  - "spatial-context"
architectures:
  - "vision-transformer"
datasets:
  []
concept_slugs:
  - "temporo-spatial-vision-transformer"
  - "multitask-farming-system-classification"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:29:11Z"
created_at: "2026-03-28T05:29:11Z"
---

# The role of spatial context and multitask learning in the detection of organic and conventional farming systems based on Sentinel-2 time series

**Authors**: Jan Hemmerling, Marcel Schwieder, Philippe Rufin, Leon-Friedrich Thomas, Mirela G. Tulbure, Patrick Hostert, Stefan Erasmi
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24552](https://arxiv.org/abs/2603.24552)

## Summary

This study proposes an approach using a modified Temporo-Spatial Vision Transformer (TSViT) to classify organic versus conventional farming systems based on Sentinel-2 time series data. The research specifically examines the impact of incorporating crop type prediction via multitask learning and varying the input spatial context (patch size). While classification of farming systems is shown to be feasible for certain crops (e.g., winter rye), performance is poor for others like permanent grassland. The findings indicate that incorporating wider spatial context significantly boosts accuracy for both classification tasks, whereas joint learning of crop type offered minimal benefit.

## Key Contributions

- Demonstrated the feasibility of discriminating between organic and conventional farming systems using intra-annual Sentinel-2 time series data.
- Investigated the influence of spatial context (patch size) on classification accuracy, finding that wider context improves performance for both farming system and crop type tasks.
- Showed that incorporating crop type prediction as a concurrent task (multitask learning) provided only limited additional benefit over single-task learning for farming system detection.
- Achieved high classification performance (F1 >= 0.8) for specific crops like winter rye, but struggled with others like permanent grassland (F1 <= 0.4).

## Limitations

Classification performance varies substantially across crop types, with several agricultural land use classes failing to be reliably distinguished.

## Key Concepts

- [[temporo-spatial-vision-transformer]]: A Vision Transformer model designed to process and integrate both spatial and temporal dimensions of image-based data, here applied to time series.
- [[multitask-farming-system-classification]]: A joint learning framework where a model simultaneously predicts both the farming system (organic vs. conventional) and the specific crop type from satellite imagery time series.

## Archivist Review

Two concepts were approved: the core architectural foundation, the Temporo-Spatial Vision Transformer (TSViT) adapted for this spatio-temporal data, and the specific methodology of Multitask Farming System Classification, which explores coupling related prediction tasks. No datasets or open questions were deemed central or novel enough for permanent vault entries. The review focused on identifying reusable mechanisms rather than paper-specific results or routine methodological variations like patch size exploration.

### Approved Concepts
- Temporo-Spatial Vision Transformer: It serves as the foundational architecture modified and adapted for handling spatio-temporal remote sensing data, specifically Sentinel-2 time series.
- Multitask Farming System Classification: This study explicitly investigates the benefit (or lack thereof) of coupling farming system detection with crop type classification as a multitask learning problem.

### Rejected Candidates
- [concept] Temporo-Spatial Vision Transformer (`temporo-spatial-vision-transformer`) - generic: The candidate concept 'Temporo-Spatial Vision Transformer' is already present in the vault via the slug 'temporo-spatial-vision-transformer', but this is a duplicate entry request. Upon review, the actual vault concept is 'temporo-spatial-vision-transformer', which is an exact match to the candidate's slug. Since the existing concept is in the vault, this candidate is implicitly superseded or should have been flagged as a duplicate if the system allowed it, but since I must approve what's new, I will check the existing vault. The existing vault has `temporo-spatial-vision-transformer`. The candidate is approved based on the general analysis, but the name is exactly one in the vault. Re-evaluating the existing vault list: it does *not* contain 'temporo-spatial-vision-transformer'. Therefore, I approve it as a new concept. The initial summary seemed to check against a different list. Re-approving based on content review. (Self-Correction: The system prompt *provides* the existing vault list. Checking the list: it is *not* present. Approval stands.)
- [concept] Multitask Farming System Classification (`multitask-farming-system-classification`) - generic: The concept captures the specific experimental setup of joint learning for farming system and crop type, which is a reusable application of MTL in remote sensing classification.

## Links

- [Abstract](https://arxiv.org/abs/2603.24552)
- [PDF](https://arxiv.org/pdf/2603.24552)

