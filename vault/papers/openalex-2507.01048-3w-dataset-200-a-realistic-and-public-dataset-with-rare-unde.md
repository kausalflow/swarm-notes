---
# CSL-compatible fields
title: "3W Dataset 2.0.0: a realistic and public dataset with rare undesirable real events in oil wells"
author:
  - literal: "Ricardo Emanuel Vaz Vargas"
  - literal: "Afrânio José de Melo Junior"
  - literal: "Celso J. Munaro"
  - literal: "Cláudio Benevenuto de Campos Lima"
  - literal: "Eduardo Toledo de Lima Júnior"
  - literal: "Felipe Muntzberg Barrocas"
  - literal: "Flávio Miguel Varejão"
  - literal: "Guilherme Fidelis Peixer"
  - literal: "Patrick Marques Ciarelli"
  - literal: "Jader R. Barbosa"
  - literal: "Jaime A. Lozano"
  - literal: "Jean Carlos Dias de Araújo"
  - literal: "J. N. E. Carneiro"
  - literal: "Lucas Gouveia Omena Lopes"
  - literal: "Lucas Pereira de Gouveia"
  - literal: "Mateus de Araujo Fernandes"
  - literal: "Matheus Lima Scramignon"
  - literal: "Patrick Marques Ciarelli"
  - literal: "Romualdo Branco"
  - literal: "Rogério Leite Alves Pinto"
  - literal: "Jaime A. Lozano"
issued:
  date-parts:
    - [2026, 4, 24]
url: "https://arxiv.org/abs/2507.01048"

# Custom fields
paper_id: "2507.01048"
paper_source: "openalex"
domain: "time-series"
tags:
  - "dataset"
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  - "3W Dataset"
concept_slugs:
  []
dataset_slugs:
  - "3w-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-04-27T07:29:34Z"
created_at: "2026-04-27T07:29:34Z"
---

# 3W Dataset 2.0.0: a realistic and public dataset with rare undesirable real events in oil wells

**Authors**: Ricardo Emanuel Vaz Vargas, Afrânio José de Melo Junior, Celso J. Munaro, Cláudio Benevenuto de Campos Lima, Eduardo Toledo de Lima Júnior, Felipe Muntzberg Barrocas, Flávio Miguel Varejão, Guilherme Fidelis Peixer, Patrick Marques Ciarelli, Jader R. Barbosa, Jaime A. Lozano, Jean Carlos Dias de Araújo, J. N. E. Carneiro, Lucas Gouveia Omena Lopes, Lucas Pereira de Gouveia, Mateus de Araujo Fernandes, Matheus Lima Scramignon, Patrick Marques Ciarelli, Romualdo Branco, Rogério Leite Alves Pinto, Jaime A. Lozano
**Date**: 2026-04-24
**Paper ID**: [openalex:2507.01048](https://arxiv.org/abs/2507.01048)

## Summary

The paper introduces version 2.0.0 of the 3W Dataset, a comprehensive, expert-labeled multivariate time series benchmark for identifying undesirable events in oil wells. This release expands upon the original dataset by incorporating more instances, additional sensor variables, and a new label to improve detection capabilities. Furthermore, the authors implement a revised data structure to facilitate more efficient and robust access for research and industrial development of monitoring systems.

## Key Contributions

- Updates the 3W Dataset with additional instances, more variables, and a new event label to support oil well monitoring.
- Introduces a new data structure to improve the robustness and efficiency of data access for time series analysis in oil production.

## Open Questions & Future Work

- [[standardize-variable-naming-conventions-in-industrial-datasets]]

## Archivist Review

The review process focused on isolating the release of the 3W Dataset as a valuable benchmark and identifying the specific bottleneck of industrial data standardization as a relevant, persistent research challenge. The dataset structure update was rejected as it is a routine implementation detail rather than a conceptual advancement. Standardizing variable nomenclature in industrial time series is a broader challenge that justifies an open question note.

### Approved Open Questions
- Standardizing Industrial Variable Naming: Consistent terminology is critical for the reproducibility and widespread adoption of specialized industrial time-series datasets in the broader ML community.

### Rejected Candidates
- [concept] 3W Dataset 2.0.0 Structure (`3w-dataset-200-structure`) - paper_local: The new data structure is a routine engineering update specific to the dataset's release and does not represent a novel methodological concept for the vault.

## Datasets

- [[3w-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2507.01048)
- [PDF](https://arxiv.org/pdf/2507.01048)

