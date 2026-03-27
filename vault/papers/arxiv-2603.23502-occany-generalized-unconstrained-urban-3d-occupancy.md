---
# CSL-compatible fields
title: "OccAny: Generalized Unconstrained Urban 3D Occupancy"
author:
  - literal: "Anh-Quan Cao"
  - literal: "Tuan-Hung Vu"
issued:
  date-parts:
    - [2026, 3, 24]
url: "https://arxiv.org/abs/2603.23502"

# Custom fields
paper_id: "2603.23502"
paper_source: "arxiv"
domain: "computer-vision"
tags:
  - "object-detection"
  - "image-segmentation"
  - "multimodal"
  - "vision-language-model"
  - "robustness"
  - "evaluation"
  - "dataset"
architectures:
  []
datasets:
  - "urban occupancy prediction datasets"
skill: "TimeSeriesSkill"
processed_at: "2026-03-25T21:17:54Z"
created_at: "2026-03-25T21:17:54Z"
---

# OccAny: Generalized Unconstrained Urban 3D Occupancy

**Authors**: Anh-Quan Cao, Tuan-Hung Vu
**Date**: 2026-03-24
**Paper ID**: [arxiv:2603.23502](https://arxiv.org/abs/2603.23502)

## Summary

OccAny addresses the limitations of existing 3D occupancy prediction methods, which heavily rely on in-domain annotations and precise sensor priors, by proposing the first generalized framework for unconstrained urban 3D occupancy prediction. The model operates on out-of-domain, uncalibrated scenes using sequential, monocular, or surround-view images to predict metric occupancy alongside segmentation features. Key innovations include Segmentation Forcing to improve occupancy quality and enable mask prediction, and a Novel View Rendering pipeline for geometry completion via test-time augmentation. Extensive experiments validate that OccAny achieves state-of-the-art performance among visual geometry methods while remaining competitive with in-domain self-supervised approaches on standard urban occupancy benchmarks.

## Key Contributions

- Introduction of OccAny, the first generalized 3D occupancy framework capable of operating on out-of-domain, uncalibrated scenes to predict metric occupancy coupled with segmentation features.
- Proposal of Segmentation Forcing to improve the quality of occupancy prediction and enable mask-level output from the model.
- Development of a Novel View Rendering pipeline to infer novel-view geometry, which is utilized for test-time view augmentation to enhance geometry completion.
- Demonstration that OccAny outperforms visual geometry baselines and remains competitive with in-domain self-supervised methods across diverse input settings (sequential, monocular, surround-view).

## Limitations

The abstract focuses on outperforming visual geometry baselines and competing with in-domain self-supervised methods, but does not explicitly detail the remaining gap compared to fully supervised, in-domain methods or the robustness to extreme out-of-domain shifts.

## Key Concepts

- [Segmentation Forcing](../concepts/segmentation-forcing.md): A technique used within the OccAny framework to enhance 3D occupancy quality by enforcing the prediction of segmentation masks alongside the occupancy grid.
- [Novel View Rendering pipeline](../concepts/novel-view-rendering-pipeline.md): A component in OccAny designed to infer novel-view geometry from existing views, facilitating test-time augmentation for improved geometry completion in 3D occupancy prediction.

## Datasets

- [urban occupancy prediction datasets](../datasets/urban-occupancy-prediction-datasets.md)

## Limitations

The abstract focuses on outperforming visual geometry baselines and competing with in-domain self-supervised methods, but does not explicitly detail the remaining gap compared to fully supervised, in-domain methods or the robustness to extreme out-of-domain shifts.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.23502)
- [PDF](https://arxiv.org/pdf/2603.23502)

