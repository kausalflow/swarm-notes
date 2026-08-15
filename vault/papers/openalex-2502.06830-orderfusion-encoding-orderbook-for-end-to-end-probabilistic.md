---
# CSL-compatible fields
title: "OrderFusion: Encoding orderbook for end-to-end probabilistic intraday electricity price forecasting"
author:
  - literal: "Runyao Yu"
  - literal: "Yuchen Tao"
  - literal: "Fabian Leimgruber"
  - literal: "Tara Esterl"
  - literal: "Jochen Stiasny"
  - literal: "Derek W. Bunn"
  - literal: "Qingsong Wen"
  - literal: "Hongye Guo"
  - literal: "Jochen L. Cremer"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2502.06830"

# Custom fields
paper_id: "2502.06830"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "probabilistic-forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "orderfusion"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-15T05:15:00Z"
created_at: "2026-08-15T05:15:00Z"
---

# OrderFusion: Encoding orderbook for end-to-end probabilistic intraday electricity price forecasting

**Authors**: Runyao Yu, Yuchen Tao, Fabian Leimgruber, Tara Esterl, Jochen Stiasny, Derek W. Bunn, Qingsong Wen, Hongye Guo, Jochen L. Cremer
**Date**: 2026-08-13
**Paper ID**: [openalex:2502.06830](https://arxiv.org/abs/2502.06830)

## Summary

This paper introduces OrderFusion, an end-to-end probabilistic forecasting model designed for intraday electricity prices using raw orderbook data. Existing approaches often rely on hand-crafted feature extraction and separate quantile models, suffering from quantile crossing and breaking end-to-end training. OrderFusion captures buy-sell dynamics via interaction-aware representations, hierarchically estimates multiple quantiles, and achieves superior performance with a highly parameter-efficient architecture of under 5,000 parameters across German and Austrian electricity markets.

## Key Contributions

- Proposes OrderFusion, an end-to-end probabilistic model for intraday electricity price forecasting that operates directly on raw orderbook data.
- Introduces interaction-aware representations of buy-sell dynamics to embed market microstructures without hand-crafted domain features.
- Achieves parameter efficiency with only 4,872 parameters while outperforming competitive baselines across German and Austrian electricity markets on ID1, ID2, and ID3 price indices.

## Open Questions & Future Work

- [[incorporating-exogenous-fundamentals-in-intraday-forecasting]]

## Key Concepts

- [[orderfusion]]: An end-to-end probabilistic model for intraday electricity price forecasting that encodes raw orderbook buy-sell dynamics.

## Archivist Review

Approved the core framework OrderFusion as a reusable concept for limit-order book modeling and the open question regarding exogenous fundamentals in intraday forecasting. Adhered strictly to the scarcity policy and review standards.

### Approved Concepts
- OrderFusion: Core methodological framework of the paper, introducing interaction-aware representations for raw orderbook forecasting.

### Approved Open Questions
- Exogenous Fundamentals in Intraday Forecasting: Incorporating exogenous fundamental data alongside orderbook microstructure can bridge the gap between technical market microstructure models and fundamental power-system economic drivers.

## Links

- [Abstract](https://arxiv.org/abs/2502.06830)
- [PDF](https://arxiv.org/pdf/2502.06830)

