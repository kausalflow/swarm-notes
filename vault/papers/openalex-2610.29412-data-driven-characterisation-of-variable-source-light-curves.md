---
# CSL-compatible fields
title: "Data-driven characterisation of variable source light curves with multimodal representation learning"
author:
  - literal: "M. Madarász"
  - literal: "Gabor Marton"
  - literal: "M. Audard"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.29412"

# Custom fields
paper_id: "2610.29412"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "transformer"
  - "self-supervised-learning"
  - "multimodal"
  - "time-series"
  - "representation-learning"
  - "contrastive-learning"
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
processed_at: "2026-10-25T09:30:37Z"
created_at: "2026-10-25T09:30:37Z"
---

# Data-driven characterisation of variable source light curves with multimodal representation learning

**Authors**: M. Madarász, Gabor Marton, M. Audard
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.29412](https://arxiv.org/abs/2610.29412)

## Summary

The paper introduces a survey-agnostic, self-supervised framework for characterizing variable astronomical sources from photometric time series without requiring labelled data. It combines a Transformer encoder operating on raw time-domain observations with a CNN processing generalized Lomb-Scargle periodograms, trained jointly via split-half augmentation and VICReg regularization. Evaluated on 37,006 ZTF sources, the resulting 64-dimensional embeddings achieve strong classification performance across variable star classes and capture physically interpretable properties.

## Key Contributions

- Introduced a survey-agnostic self-supervised framework combining a Transformer encoder for raw time-domain observations and a CNN for generalized Lomb-Scargle periodograms via VICReg objectives without labelled training data.
- Evaluated on 37,006 ZTF sources across 14 variable star classes, achieving 77.1% balanced accuracy at the individual class level and 90.5% at the broad category level using frozen 64-dimensional embeddings.
- Demonstrated that combining light curve and periodogram branches improves balanced accuracy by up to 14.9 percentage points over single modalities.
- Showed multi-band embedding concatenation improves balanced accuracy to 86.1% by capturing complementary wavelength-dependent information.

## Limitations

Evaluated primarily on ZTF data; performance on heterogeneous space-based surveys with vastly different cadences requires further tuning.

## Archivist Review

Strictly applied review guidelines and domain knowledge: no concepts or open questions met the high bar for permanent standalone vault notes, as the underlying methodologies (Transformers, CNNs, VICReg) and future directions are standard applications within time-series representation learning.

### Rejected Candidates
- [open_question] Joint Multi-band Multimodal Training (`joint-multimodal-multiband-training`) - low_impact: Future work on multi-band concatenation vs joint training is a routine scaling and architecture exploration rather than a fundamental theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.29412)
- [PDF](https://arxiv.org/pdf/2610.29412)

