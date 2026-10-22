---
# CSL-compatible fields
title: "Searching for lensed gravitational waves with unlensed templates"
author:
  - literal: "Digvijay Shivaji Wadekar"
  - literal: "Barak Zackay"
  - literal: "Mark Ho-Yeuk Cheung"
  - literal: "Tousif Islam"
  - literal: "Javier Roulet"
  - literal: "Ajit Kumar Mehta"
  - literal: "Tejaswi Venumadhav"
  - literal: "Jonathan Mushkin"
  - literal: "Miguel Zumalacárregui"
  - literal: "Matías Zaldarriaga"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26080"

# Custom fields
paper_id: "2610.26080"
paper_source: "openalex"
domain: "physics"
tags:
  - "robustness"
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
processed_at: "2026-10-22T09:45:25Z"
created_at: "2026-10-22T09:45:25Z"
---

# Searching for lensed gravitational waves with unlensed templates

**Authors**: Digvijay Shivaji Wadekar, Barak Zackay, Mark Ho-Yeuk Cheung, Tousif Islam, Javier Roulet, Ajit Kumar Mehta, Tejaswi Venumadhav, Jonathan Mushkin, Miguel Zumalacárregui, Matías Zaldarriaga
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26080](https://arxiv.org/abs/2610.26080)

## Summary

The authors present a method for searching for lensed gravitational waves using existing unlensed templates, avoiding the computational cost of explicit lensed template banks. By constructing two-image matched-filter outputs directly from standard SNR time series, the approach is over 150 times faster, recovers $\gtrsim97\%$ of optimal SNR for overlapping images, restores signal consistency tests, and significantly expands sensitive volumes for both overlapping and separated lensed images.

## Key Contributions

- Proposes a method to construct the matched-filter output of two-image lensed gravitational wave templates directly from unlensed template SNR time series without additional matched filtering.
- Achieves a detection statistic computation more than 150 times faster than an explicit lensed template bank while recovering $\gtrsim97\%$ of optimal SNR for overlapping images.
- Increases sensitive volume by 2-4x for overlapping lensed signals by restoring signal-consistency tests, and by 1.8-2.6x near fold caustics for separated images.

## Open Questions & Future Work

- [[multi-detector-lensed-gw-search]]

## Archivist Review

Applied strict selection criteria. No reusable forecasting or time series concepts were presented that generalize beyond gravitational wave physics. One open question was reviewed but omitted to maintain vault scarcity and avoid domain-specific extensions outside core time series methodology.

### Approved Open Questions
- Multi-Detector Lensed GW Searches: Demonstrates the practical viability and real-world performance of proposed search statistics on actual detector networks and observing runs.

### Rejected Candidates
- [open_question] Multi-Detector Lensed GW Searches (`multi-detector-lensed-gw-search`) - duplicate_existing: Already exists or not meeting strict novelty threshold in this form.

## Links

- [Abstract](https://arxiv.org/abs/2610.26080)
- [PDF](https://arxiv.org/pdf/2610.26080)

