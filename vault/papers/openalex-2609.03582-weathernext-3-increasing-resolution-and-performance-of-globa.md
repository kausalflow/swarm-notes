---
# CSL-compatible fields
title: "WeatherNext 3: Increasing resolution and performance of global weather models with raw observations"
author:
  - literal: "Stephan Rasp"
  - literal: "Boris Babenko"
  - literal: "Dominic Masters"
  - literal: "Andrew El-Kadi"
  - literal: "Samier Merchant"
  - literal: "Guy Shalev"
  - literal: "Ilan Price"
  - literal: "Fred Zyda"
  - literal: "Remi Lam"
  - literal: "Sasha Shysheya"
  - literal: "Matthew Willson"
  - literal: "Stratis Markou"
  - literal: "Shreya Agrawal"
  - literal: "Suhani Vora"
  - literal: "Mohammed Alewi Hassen"
  - literal: "Sunny Mak"
  - literal: "Tom R. Andersson"
  - literal: "Megan Bela"
  - literal: "Akib Uddin"
  - literal: "Nofar Peled Levi"
  - literal: "Ben Gaiarin"
  - literal: "Ferran Alet"
  - literal: "Aaron Bell"
  - literal: "Peter Battaglia"
  - literal: "Álvaro Sánchez‐González"
issued:
  date-parts:
    - [2026, 9, 3]
url: "https://arxiv.org/abs/2609.03582"

# Custom fields
paper_id: "2609.03582"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-06T09:01:19Z"
created_at: "2026-09-06T09:01:19Z"
---

# WeatherNext 3: Increasing resolution and performance of global weather models with raw observations

**Authors**: Stephan Rasp, Boris Babenko, Dominic Masters, Andrew El-Kadi, Samier Merchant, Guy Shalev, Ilan Price, Fred Zyda, Remi Lam, Sasha Shysheya, Matthew Willson, Stratis Markou, Shreya Agrawal, Suhani Vora, Mohammed Alewi Hassen, Sunny Mak, Tom R. Andersson, Megan Bela, Akib Uddin, Nofar Peled Levi, Ben Gaiarin, Ferran Alet, Aaron Bell, Peter Battaglia, Álvaro Sánchez‐González
**Date**: 2026-09-03
**Paper ID**: [openalex:2609.03582](https://arxiv.org/abs/2609.03582)

## Summary

WeatherNext 3 is an advanced global AI weather forecasting model that addresses the limitations of traditional models by ingesting raw low-latency geostationary satellite data and sparse station observations instead of relying exclusively on analysis data. It achieves hourly forecasts at 0.1-degree spatial resolution, matching the resolution of leading physics-based models while predicting variables like precipitation, tropical cyclones, and local station observations. By eliminating the separation between data assimilation, forecasting, and post-processing, WeatherNext 3 sets a new state-of-the-art in probabilistic medium-range weather prediction.

## Key Contributions

- WeatherNext 3 establishes a new state-of-the-art for probabilistic medium-range forecasting skill by moving beyond analysis data and ingesting raw low-latency geostationary satellite and sparse station observations.
- Achieves hourly forecasts with high spatial resolution (0.1 degree resolution for single-level variables including solar radiation and cloud cover) matching physics-based global models.
- Directly predicts satellite-derived precipitation estimates, tropical cyclones, and station observations (such as 2m temperature and dewpoint at arbitrary locations and times) with substantially lower error than competing global models.
- Unifies data assimilation, forecasting, and post-processing into a single end-to-end framework.

## Open Questions & Future Work

- [[understanding-short-lead-performance-anomalies]]
- [[evaluating-extreme-precipitation-and-weather-extremes]]

## Archivist Review

Approved two specific open questions regarding short lead performance anomalies and the evaluation of extreme precipitation in probabilistic weather models, while rejecting local system concepts that lack broader conceptual independence.

### Approved Open Questions
- Short Lead Performance Anomalies: Understanding and resolving short-lead performance anomalies is critical for deploying seamless operational weather forecasting systems that maintain high fidelity from the initial hours onward.
- Evaluating Extreme Weather Extremes: Accurate forecasting of extreme weather events is vital for disaster mitigation and warning systems, making the extension of probabilistic models to high-intensity extremes an important open direction.

## Links

- [Abstract](https://arxiv.org/abs/2609.03582)
- [PDF](https://arxiv.org/pdf/2609.03582)

