---
# CSL-compatible fields
title: "A Coherent Harmonic Summing Pulsar Search Code"
author:
  - literal: "Scott M. Ransom"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11749"

# Custom fields
paper_id: "2610.11749"
paper_source: "openalex"
domain: "computer-vision"
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
processed_at: "2026-10-11T11:05:31Z"
created_at: "2026-10-11T11:05:31Z"
---

# A Coherent Harmonic Summing Pulsar Search Code

**Authors**: Scott M. Ransom
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11749](https://arxiv.org/abs/2610.11749)

## Summary

CoherentSearch.jl is an open-source Julia code for pulsar searches that bypasses traditional incoherent harmonic power summation by reconstructing pulse profiles directly from Fourier transform complex amplitudes. By interpolating and inverse-transforming harmonics into a profile tested against boxcar templates with a closed-form noise model, it maintains a stable false-alarm threshold under red noise. In extensive simulated injection studies, the method significantly outperforms standard tools like riptide and PRESTO in recovery rate while offering substantial speedups across multi-core CPUs and modern GPUs.

## Key Contributions

- CoherentSearch.jl reconstructs pulsar pulse profiles directly from Fourier transform complex amplitudes via interpolation and inverse transformation, outperforming traditional incoherent power summation.
- Recovers 76% of simulated pulsars in white noise compared to 64% for riptide's FFA and 42% for PRESTO's accelsearch in an injection study of over 860,000 pulsars.
- Maintains a stable threshold under red noise and achieves 1.4-2.2x speedup on 1 CPU core, scaling up to 27x on 48 cores and 9x faster on modern GPUs relative to workstation baselines.

## Archivist Review

The submitted paper focuses on an astronomy software tool (CoherentSearch.jl) for pulsar searching via Fourier-domain harmonic reconstruction. While highly effective for radio astronomy, it does not introduce general machine learning concepts, forecasting techniques, or datasets suitable for the ML/time-series knowledge vault. Thus, all candidates were rejected under the strict selection criteria.

### Rejected Candidates
- [open_question] Fourier-Domain Coherent Acceleration Search (`fourier-domain-coherent-acceleration-search`) - low_impact: Domain-specific astronomy problem regarding pulsar binary motion rather than a general machine learning or time-series forecasting bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.11749)
- [PDF](https://arxiv.org/pdf/2610.11749)

