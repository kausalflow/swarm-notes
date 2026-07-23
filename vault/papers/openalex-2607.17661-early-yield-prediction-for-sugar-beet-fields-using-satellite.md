---
# CSL-compatible fields
title: "Early Yield Prediction for Sugar Beet Fields using Satellite Data -- Learnings from Specialized Vision Transformers"
author:
  - literal: "Philipp Vaeth"
  - literal: "Bhumika Laxman Sadbhave"
  - literal: "Denise Dejon"
  - literal: "Gunther Schorcht"
  - literal: "Magda Gregorová"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.17661"

# Custom fields
paper_id: "2607.17661"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "vision-transformer"
  - "vit"
  - "multimodal"
  - "forecasting"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:27:31Z"
created_at: "2026-07-23T07:27:31Z"
---

# Early Yield Prediction for Sugar Beet Fields using Satellite Data -- Learnings from Specialized Vision Transformers

**Authors**: Philipp Vaeth, Bhumika Laxman Sadbhave, Denise Dejon, Gunther Schorcht, Magda Gregorová
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.17661](https://arxiv.org/abs/2607.17661)

## Summary

This paper explores early harvest yield prediction for sugar beet fields using optical Sentinel-2 satellite imagery and specialized vision transformers. The authors demonstrate that incorporating uncommon architectural choices—specifically very small patch sizes and all available spectral bands—significantly improves predictive performance. Furthermore, they introduce a ranking-based detection approach to effectively identify underperforming, low-yield fields early in the growth cycle.

## Key Contributions

- Demonstrated early sugar beet harvest yield forecasting using purely optical Sentinel-2 imagery and specialized vision transformers.
- Empirically showed that small patch sizes and utilizing all Sentinel-2 spectral bands improve model performance.
- Developed a modified training setup and ranking-based detection method to identify low-yield fields early in the growth cycle.

## Archivist Review

In accordance with the strict vault selectivity policy, no concepts or open questions were approved. The paper explores agricultural yield forecasting using standard vision transformers on Sentinel-2 satellite imagery, which applies existing architectures rather than introducing fundamentally reusable methodological primitives or high-impact open questions.

### Rejected Candidates
- [open_question] Limitations of Pixel-Level Transformers (`pixel-level-transformer-limitations`) - low_impact: Standard exploration of scaling limits and optimization hurdles for ultra-small vision transformer patch sizes.
- [open_question] Explainability of Learned Spectral Bands (`explainability-of-learned-spectral-bands`) - low_impact: Routine future work proposing feature attribution and interpretability analysis for end-to-end multispectral models.

## Links

- [Abstract](https://arxiv.org/abs/2607.17661)
- [PDF](https://arxiv.org/pdf/2607.17661)

