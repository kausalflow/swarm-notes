---
# CSL-compatible fields
title: "VLTI/PIONIER imaging of post-AGB binaries. An INSPIRING hunt for inner rim substructures in circumbinary discs"
author:
  - literal: "Toon De Prins"
  - literal: "Akke Corporaal"
  - literal: "J. Kluska"
  - literal: "D. Kamath"
  - literal: "Hans Van Winckel"
  - literal: "Kateryna Andrych"
  - literal: "Javier Alcolea"
  - literal: "Narsireddy Anugu"
  - literal: "Jean-Philippe Berger"
  - literal: "V. Bujarrabal"
  - literal: "I. Gallardo Cava"
  - literal: "Stefan Kraus"
  - literal: "Hans Olofsson"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13445"

# Custom fields
paper_id: "2605.13445"
paper_source: "openalex"
domain: "biology"
tags:
  - "multimodal"
  - "dataset"
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
processed_at: "2026-05-16T07:11:00Z"
created_at: "2026-05-16T07:11:00Z"
---

# VLTI/PIONIER imaging of post-AGB binaries. An INSPIRING hunt for inner rim substructures in circumbinary discs

**Authors**: Toon De Prins, Akke Corporaal, J. Kluska, D. Kamath, Hans Van Winckel, Kateryna Andrych, Javier Alcolea, Narsireddy Anugu, Jean-Philippe Berger, V. Bujarrabal, I. Gallardo Cava, Stefan Kraus, Hans Olofsson
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13445](https://arxiv.org/abs/2605.13445)

## Summary

This paper presents a systematic NIR interferometric imaging survey of eight post-AGB circumbinary discs using the VLTI/PIONIER instrument. By employing a specialized image reconstruction pipeline based on the SPARCO approach and the ORGANIC algorithm, the authors achieved milliarcsecond-scale resolution to study inner rim morphologies. The results reveal diverse, non-axisymmetric dust structures, including robust azimuthal brightness enhancements and complex arcs that suggest dynamic interactions with central binaries. This work establishes a foundation for future multi-wavelength and time-series observations to distinguish between radiative responses and hydrodynamical instabilities in these systems.

## Key Contributions

- Conducted the first homogeneous interferometric imaging survey of inner post-AGB circumbinary disc regions at 1-2 mas resolution.
- Implemented a robust image reconstruction workflow integrating the SPARCO modeling approach with the ORGANIC algorithm for NIR interferometry.
- Identified azimuthal brightness enhancements and complex morphological substructures in a significant subset of post-AGB binaries, indicating complex dynamical or radiative disc responses.

## Open Questions & Future Work

- [[origin-of-post-agb-disc-substructures]]

## Archivist Review

The paper describes an astrophysical imaging survey and reconstruction workflow. I have approved the open question concerning the physical origin of inner rim substructures, as it defines a significant, unresolved astrophysical problem. The proposed image reconstruction workflow is rejected as it is a domain-specific observational technique rather than a reusable machine learning methodology.

### Approved Open Questions
- Physical origin of inner rim substructures: Establishing the physical origin of these substructures is critical to understanding the dynamical interaction between central binaries and their discs, as well as testing hypotheses related to refractory depletion and second-generation planet formation.

### Rejected Candidates
- [concept] SPARCO-ORGANIC reconstruction workflow (`sparco-organic-reconstruction-workflow`) - paper_local: The image reconstruction pipeline is an application-specific workflow for interferometry rather than a general ML mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2605.13445)
- [PDF](https://arxiv.org/pdf/2605.13445)

