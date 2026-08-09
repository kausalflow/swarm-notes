---
# CSL-compatible fields
title: "QuanTiMedAI: Quantum-Enhanced Time-Series Model guided by Agentic AI for Cardiac Arrest Mortality Prediction"
author:
  - literal: "Mutasim Fuad Sarker"
  - literal: "Adiba Rahman Namira"
  - literal: "Wafa Binte Alam"
  - literal: "Md Adnan Arefeen"
  - literal: "Mahzabeen Emu"
  - literal: "Sumaiya Tabassum Nimi"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.06294"

# Custom fields
paper_id: "2608.06294"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "llm"
  - "agent-ic"
  - "quantum-computing"
  - "healthcare"
  - "prediction"
  - "recurrent-neural-network"
architectures:
  - "recurrent-neural-network"
datasets:
  - "mimic-iv"
concept_slugs:
  []
dataset_slugs:
  - "mimic-iv"
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:40:11Z"
created_at: "2026-08-09T05:40:11Z"
---

# QuanTiMedAI: Quantum-Enhanced Time-Series Model guided by Agentic AI for Cardiac Arrest Mortality Prediction

**Authors**: Mutasim Fuad Sarker, Adiba Rahman Namira, Wafa Binte Alam, Md Adnan Arefeen, Mahzabeen Emu, Sumaiya Tabassum Nimi
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.06294](https://arxiv.org/abs/2608.06294)

## Summary

QuanTiMedAI is a novel quantum-agentic framework designed to predict cardiac arrest mortality in intensive care units by replacing static admission summaries with continuous temporal physiological tracking. The system integrates an agentic LLM for clinically informed feature discovery with a compact quantum recurrent network that achieves superior predictive performance while requiring an exceptionally low parameter count. Evaluated on a MIMIC-IV cardiac arrest cohort, the model attains an AUROC of 0.852 with only 605 parameters, outperforming current state-of-the-art classical baselines.

## Key Contributions

- Introduces QuanTiMedAI, a quantum-agentic framework combining agentic LLM-guided feature discovery with a compact quantum recurrent network.
- Demonstrates that agentic LLM-guided feature selection outperforms conventional feature selection approaches in capturing physiological progression.
- Achieves an AUROC of 0.852 on a MIMIC-IV cardiac arrest cohort using only 605 parameters, outperforming classical baselines by 2.9 percent.

## Limitations

Evaluated solely on a single MIMIC-IV cardiac arrest cohort; broader clinical generalizability across diverse ICU settings remains to be tested.

## Open Questions & Future Work

- [[noisy-quantum-hardware-validation]]

## Archivist Review

Applied rigorous filtering to preserve only reusable open questions and standard datasets while rejecting paper-local framework names.

### Approved Open Questions
- Validation on Noisy Quantum Hardware: Critical for transitioning quantum machine learning models from theoretical or simulated feasibility to robust, deployable clinical tools on near-term NISQ hardware.

### Rejected Candidates
- [concept] QuanTiMedAI (`quantimedai`) - paper_local: Paper-local architecture name that bundles multiple specific methods rather than a standalone, broadly reusable modeling primitive.

## Datasets

- [[mimic-iv]]

## Links

- [Abstract](https://arxiv.org/abs/2608.06294)
- [PDF](https://arxiv.org/pdf/2608.06294)

