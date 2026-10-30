---
# CSL-compatible fields
title: "FORESEE-MS: Toward Prospective Spatial Forecasting of Future Multiple Sclerosis Lesions from Baseline FLAIR MRI"
author:
  - literal: "Maryam Akhavan Aghdam"
  - literal: "Sudip Mittal"
  - literal: "Noorbakhsh Amiri Golilarz"
  - literal: "Shahram Rahimi"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.36428"

# Custom fields
paper_id: "2610.36428"
paper_source: "openalex"
domain: "medicine"
tags:
  - "vision-transformer"
  - "vit"
  - "evaluation"
  - "dataset"
architectures:
  - "encoder-decoder"
datasets:
  - "msseg-2"
concept_slugs:
  []
dataset_slugs:
  - "msseg-2"
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:05:22Z"
created_at: "2026-10-30T11:05:22Z"
---

# FORESEE-MS: Toward Prospective Spatial Forecasting of Future Multiple Sclerosis Lesions from Baseline FLAIR MRI

**Authors**: Maryam Akhavan Aghdam, Sudip Mittal, Noorbakhsh Amiri Golilarz, Shahram Rahimi
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.36428](https://arxiv.org/abs/2610.36428)

## Summary

This study investigates prospective spatial forecasting of future multiple sclerosis (MS) lesions from baseline FLAIR MRI using the newly introduced FORESEE-MS evaluation protocol and MSSEG-2 dataset. The authors evaluate five deep learning architectures against a fold-specific population-prior atlas. Results show that while the population-prior baseline achieves the highest pooled voxel-level AUROC and AUPRC, select deep learning models such as 3D U-Net exhibit higher mean within-patient Recall@Top-K%, though differences lack statistical significance in this small cohort.

## Key Contributions

- Introduces FORESEE-MS, an evaluation protocol utilizing a fold-specific population-prior atlas for prospective spatial forecasting of multiple sclerosis lesions from baseline FLAIR MRI.
- Evaluates five deep learning models (3D U-Net, Attn+ResBlock+VAE, ViT, and two SwinUNETR variants) using 5-fold cross-validation on 39 subjects from the MSSEG-2 dataset.
- Demonstrates that while a population-prior atlas achieves superior pooled voxel-level AUROC and AUPRC, 3D U-Net and Attn+ResBlock+VAE attain higher mean voxel-level within-patient Recall@Top-K% across evaluated thresholds.

## Limitations

Evaluated on a small cohort of 39 subjects, leaving uncertainty regarding whether deep learning models outperform population-prior atlases for robust patient-specific MS lesion forecasting.

## Open Questions & Future Work

- [[large-multisite-cohort-lesion-forecasting]]

## Archivist Review

Approved the MSSEG-2 dataset as it is central to the evaluation of multiple sclerosis lesion forecasting. The open question was evaluated and rejected as standard sample size expansion future work.

### Approved Open Questions
- Multi-Site Cohort Lesion Forecasting: Crucial for establishing whether deep learning models can genuinely extract patient-specific predictive signals for multiple sclerosis lesion formation beyond population priors.

### Rejected Candidates
- [open_question] Multi-Site Cohort Lesion Forecasting (`large-multisite-cohort-lesion-forecasting`) - not_novel: Already covered or standard future work on sample size scaling.

## Datasets

- [[msseg-2]]

## Links

- [Abstract](https://arxiv.org/abs/2610.36428)
- [PDF](https://arxiv.org/pdf/2610.36428)

