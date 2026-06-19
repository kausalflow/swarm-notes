---
# CSL-compatible fields
title: "HLS-GPT: A Generative Pretrained Transformer (GPT) for Continental-Scale NASA Harmonized Landsat and Sentinel-2 (HLS) Reflectance Reconstruction Across All Bands on Arbitrary Dates"
author:
  - literal: "Junjie Li"
  - literal: "Hankui K. Zhang"
  - literal: "David P. Roy"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.18115"

# Custom fields
paper_id: "2606.18115"
paper_source: "openalex"
domain: "computer-vision, remote-sensing"
tags:
  - "transformer"
  - "llm"
  - "vision-language-model"
  - "time-series"
  - "remote-sensing"
  - "generative-pre-training"
  - "masked-autoencoder-foundation-models"
architectures:
  - "decoder-only"
datasets:
  - "Harmonized Landsat Sentinel-2"
concept_slugs:
  - "hls-gpt"
dataset_slugs:
  - "harmonized-landsat-sentinel-2"
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:25:03Z"
created_at: "2026-06-19T09:25:03Z"
---

# HLS-GPT: A Generative Pretrained Transformer (GPT) for Continental-Scale NASA Harmonized Landsat and Sentinel-2 (HLS) Reflectance Reconstruction Across All Bands on Arbitrary Dates

**Authors**: Junjie Li, Hankui K. Zhang, David P. Roy
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.18115](https://arxiv.org/abs/2606.18115)

## Summary

HLS-GPT is a generative Transformer designed for continental-scale surface reflectance reconstruction of NASA Harmonized Landsat and Sentinel-2 data. By utilizing a hierarchical architecture, it unifies the spectral band configurations of different sensors and reconstructs missing observations for any given pixel and date. The model exhibits high robustness to irregular sampling and varying spectral requirements, outperforming existing benchmarks including the NASA-IBM Prithvi model.

## Key Contributions

- Introduced HLS-GPT, a hierarchical Transformer model for single-pixel surface reflectance reconstruction from 12-month time series.
- Achieved reconstruction RMSE below 0.026 across all HLS spectral bands, outperforming the NASA-IBM Prithvi model on large-scale geographic tiles.
- Demonstrated robust performance under high masking ratios (10-50%), maintaining all-band RMSE below 0.028 even under sparse, irregular observation conditions.

## Key Concepts

- [[hls-gpt]]: A hierarchical Transformer model for reconstructing Harmonized Landsat Sentinel-2 surface reflectance across all spectral bands on arbitrary dates.

## Archivist Review

The HLS-GPT architecture is approved as a reusable paradigm for multi-source, multi-spectral remote sensing reconstruction. The Harmonized Landsat Sentinel-2 dataset is approved as a critical, high-impact data source for satellite time-series analysis. No new open questions were identified that met the criteria for permanence.

### Approved Concepts
- HLS-GPT: Provides a novel, scalable approach for full-spectral reflectance reconstruction of multi-sensor satellite imagery across irregular time series.

## Datasets

- [[harmonized-landsat-sentinel-2]]

## Links

- [Abstract](https://arxiv.org/abs/2606.18115)
- [PDF](https://arxiv.org/pdf/2606.18115)

