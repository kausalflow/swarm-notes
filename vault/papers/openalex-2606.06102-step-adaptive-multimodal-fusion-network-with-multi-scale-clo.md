---
# CSL-compatible fields
title: "Step-adaptive multimodal fusion network with multi-scale cloud feature learning for ultra-short-term solar irradiance forecasting"
author:
  - literal: "Jingxin Zhang"
  - literal: "Xiaoqin Wang"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06102"

# Custom fields
paper_id: "2606.06102"
paper_source: "openalex"
domain: "time-series"
tags:
  - "multimodal"
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "lstm"
architectures:
  []
datasets:
  - "NREL"
concept_slugs:
  - "step-adaptive-low-frequency-compensation-unit"
dataset_slugs:
  - "nrel"
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:19:25Z"
created_at: "2026-06-07T08:19:25Z"
---

# Step-adaptive multimodal fusion network with multi-scale cloud feature learning for ultra-short-term solar irradiance forecasting

**Authors**: Jingxin Zhang, Xiaoqin Wang
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06102](https://arxiv.org/abs/2606.06102)

## Summary

This paper introduces a multimodal fusion network for ultra-short-term solar irradiance forecasting by combining ground-based cloud imagery with meteorological time-series data. To address current limitations in spatial feature extraction and horizon-dependent modeling, the authors employ InceptionNeXt for multi-scale image processing and a novel step-adaptive low-frequency compensation unit. Temporal dependencies are captured via a TempAttnLSTM, enabling robust multi-step prediction. Experimental results on the NREL dataset and field deployments show significant improvements over existing forecasting baselines.

## Key Contributions

- Introduces a multi-source data fusion model integrating ground-based cloud images and meteorological time-series for solar irradiance forecasting.
- Utilizes InceptionNeXt to extract multi-scale spatial cloud features, overcoming limitations of standard convolutions.
- Develops a step-adaptive low-frequency compensation unit to dynamically adjust information modulation according to the forecast horizon.
- Demonstrates superior performance over state-of-the-art models on the NREL benchmark and practical photovoltaic station data.

## Key Concepts

- [[step-adaptive-low-frequency-compensation-unit]]: A mechanism that dynamically modulates low-frequency signal components based on the specific prediction time step.

## Archivist Review

I have approved the step-adaptive low-frequency compensation unit as it introduces a reusable mechanism for horizon-dependent signal modulation. I have also approved the NREL dataset as it is a widely utilized, standard public resource for solar irradiance forecasting. Other concepts were rejected as they represent routine architectural combinations or off-the-shelf components.

### Approved Concepts
- Step-adaptive low-frequency compensation unit: Addresses the failure of fixed frequency compensation strategies in ultra-short-term forecasting by making them horizon-dependent.

### Rejected Candidates
- [concept] InceptionNeXt (`inceptionnext`) - not_novel: This is an off-the-shelf computer vision architecture repurposed for image feature extraction, not a core time-series forecasting innovation.
- [concept] TempAttnLSTM (`tempattnlstm`) - not_novel: This is a routine combination of existing temporal attention and LSTM components, which does not constitute a distinct novel contribution.

## Datasets

- [[nrel]]

## Links

- [Abstract](https://arxiv.org/abs/2606.06102)
- [PDF](https://arxiv.org/pdf/2606.06102)

