---
# CSL-compatible fields
title: "Leveraging Synthetic and Genetic Data to Improve Epidemic Forecasting"
author:
  - literal: "Dave Osthus"
  - literal: "Alexander C. Murph"
  - literal: "Emma E. Goldberg"
  - literal: "Lauren J. Beesley"
  - literal: "William M. Fischer"
  - literal: "Nidhi K. Parikh"
  - literal: "Lauren A. Castro"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24474"

# Custom fields
paper_id: "2603.24474"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "deep-learning"
  - "synthetic-data-augmentation"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "genetic-information-integration-in-forecasting"
  - "synthetic-data-augmentation-for-epidemic-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:29:00Z"
created_at: "2026-03-28T05:29:00Z"
---

# Leveraging Synthetic and Genetic Data to Improve Epidemic Forecasting

**Authors**: Dave Osthus, Alexander C. Murph, Emma E. Goldberg, Lauren J. Beesley, William M. Fischer, Nidhi K. Parikh, Lauren A. Castro
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24474](https://arxiv.org/abs/2603.24474)

## Summary

This paper investigates methodologies to enhance forecasting for emerging infectious diseases, focusing on utilizing synthetic data and genetic information which are often available early in an outbreak. The authors trained deep learning models on various combinations of real and synthetic COVID-19 case data, with and without associated genetic variant information, to forecast US state-level cases. The key findings show that models benefiting from synthetic data exhibit better accuracy than those relying solely on real data, and the inclusion of genetic data further boosts performance. Crucially, these models significantly outperformed a persistence baseline and several established ensemble methods, offering a strategy blueprint for operational pandemic forecasting.

## Key Contributions

- Demonstrated that deep learning models trained with synthetic epidemic data achieve superior forecast accuracy compared to models trained only on real historical data.
- Validated that incorporating genetic variant information significantly enhances the accuracy of emerging infectious disease forecasts.
- The proposed models consistently outperformed a baseline persistence model and several established real-time forecasting models (e.g., outperforming 15/22 models in the comparison set).
- Provided a blueprint for leveraging underutilized data sources (synthetic and genetic) to improve preparedness for future pandemics.

## Limitations

The study is based on a retrospective analysis of COVID-19 data and the operational impact in a truly 'emerging' (zero-day) scenario is implied but not directly tested with live data streams.

## Key Concepts

- [[genetic-information-integration-in-forecasting]]: The integration of genetic sequence information from variants to improve the accuracy and robustness of infectious disease forecasting models.
- [[synthetic-data-augmentation-for-epidemic-forecasting]]: Using computer-generated time-series data reflective of an epidemic's dynamics to augment or replace limited real-world case data during the initial stages of an outbreak.

## Archivist Review

Two concepts were approved as they capture reusable methodological contributions in the domain of time-series forecasting under extreme data scarcity. The integration of genetic information and the augmentation via synthetic data are both generalizable strategies for improving ML model performance when real historical data is limited, directly addressing a key bottleneck in pandemic preparedness. Other candidates were rejected as they described paper-local experimental setups.

### Approved Concepts
- Genetic Information Integration in Forecasting: The paper explicitly investigates and validates the positive impact of integrating genetic variant data into epidemic forecasting models, suggesting a reusable data modality for future outbreak modeling.
- Synthetic Data Augmentation for Epidemic Forecasting: Demonstrates that synthetically generated epidemic time-series data can outperform real historical data alone for training deep learning models, providing a method to overcome initial data scarcity.

### Rejected Candidates
- [concept] COVID-19 Forecasting Experiment (`covid-19-forecasting-experiment`) - paper_local: This is a specific instance of an experimental setup using a past disease, not a novel, reusable technical concept or architecture.

## Links

- [Abstract](https://arxiv.org/abs/2603.24474)
- [PDF](https://arxiv.org/pdf/2603.24474)

