---
# CSL-compatible fields
title: "Testing for integer integration in functional time series"
author:
  - literal: "Won‐Ki Seo"
  - literal: "Han Lin Shang"
issued:
  date-parts:
    - [2026, 4, 10]
url: "https://arxiv.org/abs/2503.23960"

# Custom fields
paper_id: "2503.23960"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-13T07:07:59Z"
created_at: "2026-04-13T07:07:59Z"
---

# Testing for integer integration in functional time series

**Authors**: Won‐Ki Seo, Han Lin Shang
**Date**: 2026-04-10
**Paper ID**: [openalex:2503.23960](https://arxiv.org/abs/2503.23960)

## Summary

This paper proposes a statistical testing procedure to identify whether functional time series are integrated of a specific integer order d. The methodology effectively differentiates between integer integration and fractional integration, addressing a critical gap in functional time series analysis. Simulations demonstrate the reliability of the test, and empirical applications to yield curves and mortality data reveal common patterns of first-order integration.

## Key Contributions

- Introduces a statistical testing framework to determine the order of integer integration (d) in functional (curve-valued) time series.
- Provides a mechanism to distinguish between integer-integrated and fractionally-integrated functional time series.
- Validates the methodology through Monte Carlo simulations and applies it to real-world Canadian yield curve data and French mortality data.

## Open Questions & Future Work

- [[robust-testing-fractional-integration-functional-time-series]]
- [[joint-asymptotic-theory-local-alternatives]]

## Archivist Review

The paper addresses a specialized statistical problem in functional time series (testing integer vs fractional integration). No new concepts met the high bar for permanent standalone vault inclusion as they relate to specific hypothesis testing procedures rather than reusable modeling mechanisms. The open questions regarding robust testing and joint asymptotic theory were approved as they identify fundamental theoretical gaps in functional data analysis.

### Approved Open Questions
- Robust fractional integration testing: The sensitivity of testing procedures to the underlying memory parameters is a fundamental bottleneck in functional data analysis, limiting the applicability of these tests in real-world scenarios where the memory order is the primary unknown.
- Joint asymptotic theory development: Joint asymptotics are crucial for establishing the size and power properties of tests when the process is near an integer integration order, which is common in empirical applications like yield curves and mortality rates.

## Links

- [Abstract](https://arxiv.org/abs/2503.23960)
- [PDF](https://arxiv.org/pdf/2503.23960)

