---
# CSL-compatible fields
title: "Perceiving and Predicting Dynamic Sports: Spatiotemporal Intelligence in Vision Models for Egocentric Tennis Video"
author:
  - literal: "Tudor Braicu"
  - literal: "Joseph DelPreto"
  - literal: "Jared Boyer"
  - literal: "Mónika Farsang"
  - literal: "Maximilian Stölzle"
  - literal: "Tim Seyde"
  - literal: "Daniela Rus"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.37619"

# Custom fields
paper_id: "2610.37619"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "vision-language-model"
  - "diffusion-model"
  - "autonomous-agent"
  - "robotics"
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
processed_at: "2026-10-30T11:05:55Z"
created_at: "2026-10-30T11:05:55Z"
---

# Perceiving and Predicting Dynamic Sports: Spatiotemporal Intelligence in Vision Models for Egocentric Tennis Video

**Authors**: Tudor Braicu, Joseph DelPreto, Jared Boyer, Mónika Farsang, Maximilian Stölzle, Tim Seyde, Daniela Rus
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.37619](https://arxiv.org/abs/2610.37619)

## Summary

This paper investigates the spatiotemporal intelligence of foundation vision models using an annotated egocentric and allocentric tennis dataset. The authors evaluate various image encoders, video encoders, and vision-language models across seven prediction tasks, including player/ball localization, trajectory forecasting, stroke anticipation, and contact time estimation. They find that auxiliary depth improves 3D localization while longer histories do not necessarily aid ball forecasting, and they propose a conditional diffusion model for real-time whole-body kinematic motion generation from egocentric video.

## Key Contributions

- Evaluated seven spatiotemporal prediction tasks from egocentric video using image encoders, video encoders, and vision-language models on a newly collected tennis dataset.
- Demonstrated that the best performing models achieve mean current-frame localization errors of 0.14 m for the ego player and 0.54 m for the ball, and future forecasting errors of 0.34 m for the ego player and 0.91 m for the ball over 1.1 s.
- Showed that auxiliary depth information substantially improves 3D ball localization, while longer image histories do not improve ball forecasting.
- Proposed a conditional diffusion model to generate whole-body kinematic tennis motion from vision encoder predictions on egocentric video at real-time rates.

## Archivist Review

The paper evaluates vision models on egocentric tennis video tasks and motion generation, but does not introduce sufficiently reusable foundational concepts or open questions for the time-series and forecasting knowledge vault.

### Rejected Candidates
- [open_question] Metric Depth and Racket Alignment (`metric-depth-and-racket-alignment-in-egocentric-vision`) - low_impact: The open question deals with application-specific egocentric perception bottlenecks (racket alignment) rather than a fundamental theoretical or methodological limitation in time-series or forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2610.37619)
- [PDF](https://arxiv.org/pdf/2610.37619)

