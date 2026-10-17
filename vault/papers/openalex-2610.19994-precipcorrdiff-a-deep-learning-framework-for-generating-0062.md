---
# CSL-compatible fields
title: "PrecipCorrDiff: A Deep Learning Framework for Generating 0.0625$^\\circ$ High-Resolution IMD Gridded Precipitation Data"
author:
  - literal: "Bipin Kumar"
  - literal: "Rajib Chattopadhyay"
  - literal: "Harsh P. Bachhav"
  - literal: "Jannu"
  - literal: "Bhupendra Bahadur Singh"
  - literal: "Ramesh Ragala"
  - literal: "ANANDA KUMAR DAS"
  - literal: "Manish Modani"
  - literal: "Thara Prabhakaran"
  - literal: "M. Mohapatra"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.19994"

# Custom fields
paper_id: "2610.19994"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "spatial-resolution"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:56:17Z"
created_at: "2026-10-17T08:56:17Z"
---

# PrecipCorrDiff: A Deep Learning Framework for Generating 0.0625$^\circ$ High-Resolution IMD Gridded Precipitation Data

**Authors**: Bipin Kumar, Rajib Chattopadhyay, Harsh P. Bachhav, Jannu, Bhupendra Bahadur Singh, Ramesh Ragala, ANANDA KUMAR DAS, Manish Modani, Thara Prabhakaran, M. Mohapatra
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.19994](https://arxiv.org/abs/2610.19994)

## Summary

The paper introduces PrecipCorrDiff, a diffusion-based deep learning downscaling framework designed to generate 0.0625-degree high-resolution India Meteorological Department (IMD) precipitation fields from 0.25-degree data. By incorporating a customized loss function and a multi-scale residual generation strategy, PrecipCorrDiff improves spatial variability and accurately captures extreme rainfall events. Validated across four climatologically distinct Indian monsoon regions, the proposed model successfully eliminates systematic negative biases found in prior SRGAN-based approaches and reproduces observed precipitation statistics with near-zero spatial bias.

## Key Contributions

- Developed PrecipCorrDiff, a diffusion-based framework for generating 0.0625-degree high-resolution IMD gridded precipitation data from 0.25-degree inputs.
- Incorporated a customized loss function and a multi-scale residual generation strategy to significantly improve the representation of extreme rainfall events.
- Demonstrated superior performance over SRGAN-based models and original CorrDiff by eliminating systematic negative bias and accurately reproducing spatial patterns across Indian monsoon regions.

## Archivist Review

The proposed concept (PrecipCorrDiff) and open question are both tied too closely to a specific architecture application (IMD precipitation downscaling via modified CorrDiff) rather than broader reusable mechanisms or foundational open challenges. Following strict scarcity and generalizability rules, both candidates are rejected.

### Rejected Candidates
- [concept] PrecipCorrDiff (`precipcorrdiff`) - paper_local: PrecipCorrDiff is a paper-specific application of CorrDiff tailored for IMD precipitation data rather than a broadly reusable standalone forecasting or modeling paradigm.
- [open_question] Joint Fine-Tuning of Two-Stage Diffusion Downscaling Networks (`joint-finetuning-two-stage-diffusion-downscaling-networks`) - low_impact: The question focuses narrowly on joint training of a two-stage downscaling pipeline rather than a fundamental theoretical bottleneck in time series or spatial forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2610.19994)
- [PDF](https://arxiv.org/pdf/2610.19994)

