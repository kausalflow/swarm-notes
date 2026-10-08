---
# CSL-compatible fields
title: "Comparing two approaches for modelling the loss given default of credit cards: Run-off triangles vs regression"
author:
  - literal: "Arno Botha"
  - literal: "Henko Crewe"
  - literal: "Marcel Müller"
  - literal: "Janette Larney"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.05926"

# Custom fields
paper_id: "2610.05926"
paper_source: "openalex"
domain: "finance"
tags:
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:42:00Z"
created_at: "2026-10-08T11:42:00Z"
---

# Comparing two approaches for modelling the loss given default of credit cards: Run-off triangles vs regression

**Authors**: Arno Botha, Henko Crewe, Marcel Müller, Janette Larney
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.05926](https://arxiv.org/abs/2610.05926)

## Summary

This paper compares traditional run-off triangles (ROTs) with a two-stage regression-based approach for estimating loss given default (LGD) in credit card portfolios. Using data-driven diagnostics, the authors show that regression-based models successfully recover the U-shaped empirical LGD distribution and track mean empirical loss rates much closer over time than ROTs. These findings suggest that regression-based LGD models offer superior prediction accuracy, making them preferable for regulatory frameworks like IFRS 9.

## Key Contributions

- Benchmarks the industry-standard run-off triangles (ROTs) approach against a two-stage regression-based LGD model using credit card data.
- Demonstrates that the regression-based approach successfully recovers the characteristic U-shaped empirical LGD distribution, whereas the ROT-based approach cannot.
- Shows that regression-based aggregate LGD estimates track the mean empirical loss rate over time much closer than ROT-based estimates, which diverge substantially.
- Highlights the superior prediction accuracy of regression-based LGD modeling for IFRS 9 accounting framework compliance.

## Limitations

Future work could explore extending the regression-based approach to other retail and non-retail credit portfolios beyond credit cards.

## Archivist Review

Followed strict selection policies by rejecting paper-local benchmark discussions and broad future work suggestions that lack specific technical bottlenecks. No concepts or datasets qualified for permanent standalone notes.

### Rejected Candidates
- [open_question] Future Directions in LGD Modeling (`lgd-modeling-methodologies-future-work`) - weak_evidence: The future work suggestion is overly broad and represents standard incremental extensions rather than a distinct, rigorous unresolved bottleneck in time series or financial machine learning theory.

## Links

- [Abstract](https://arxiv.org/abs/2610.05926)
- [PDF](https://arxiv.org/pdf/2610.05926)

