---
# CSL-compatible fields
title: "TabPFN-3.5: Technical Report"
author:
  - literal: "Benjamin Jäger"
  - literal: "Nick Erickson"
  - literal: "Léo Grinsztajn"
  - literal: "Felix Birkel"
  - literal: "Klemens Flöge"
  - literal: "Oscar Key"
  - literal: "Kursat Kaya"
  - literal: "Jonas Kübler"
  - literal: "Adèle Frankel"
  - literal: "Tobias Schröder"
  - literal: "Anurag Garg"
  - literal: "Jan Hendrik Metzen"
  - literal: "David Salinas"
  - literal: "Simon Bing"
  - literal: "Kristina Collins"
  - literal: "Tuana Celik"
  - literal: "Vahid Balazadeh"
  - literal: "Lydia Sidhoum"
  - literal: "Tomás Pereda"
  - literal: "Brendan Roof"
  - literal: "Andrej Tschalzev"
  - literal: "Siyuan Guo"
  - literal: "Philipp Singer"
  - literal: "Lennart Purucker"
  - literal: "Jake Robertson"
  - literal: "Marie Salmon"
  - literal: "Philipp Jund"
  - literal: "Jerry Chen"
  - literal: "Diana Kriuchkova"
  - literal: "Arthur Cahu"
  - literal: "Eliott Kalfon"
  - literal: "Adrian Hayler"
  - literal: "Georg Grab"
  - literal: "Vitor Monteiro"
  - literal: "Lilly Wehrhahn"
  - literal: "Dominik Safaric"
  - literal: "Clara Cornu"
  - literal: "Alan Arazi"
  - literal: "Rylee Grace"
  - literal: "Simone Alessi"
  - literal: "Mihir Manium"
  - literal: "Bernhard Schölkopf"
  - literal: "Yann LeCun"
  - literal: "Madelon Hulsebos"
  - literal: "Sauraj Gambhir"
  - literal: "Noah Hollmann"
  - literal: "Frank Hutter"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.17895"

# Custom fields
paper_id: "2609.17895"
paper_source: "openalex"
domain: "nlp"
tags:
  - "tabular-foundation-model"
  - "multimodal"
  - "benchmark"
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
processed_at: "2026-09-18T09:17:45Z"
created_at: "2026-09-18T09:17:45Z"
---

# TabPFN-3.5: Technical Report

**Authors**: Benjamin Jäger, Nick Erickson, Léo Grinsztajn, Felix Birkel, Klemens Flöge, Oscar Key, Kursat Kaya, Jonas Kübler, Adèle Frankel, Tobias Schröder, Anurag Garg, Jan Hendrik Metzen, David Salinas, Simon Bing, Kristina Collins, Tuana Celik, Vahid Balazadeh, Lydia Sidhoum, Tomás Pereda, Brendan Roof, Andrej Tschalzev, Siyuan Guo, Philipp Singer, Lennart Purucker, Jake Robertson, Marie Salmon, Philipp Jund, Jerry Chen, Diana Kriuchkova, Arthur Cahu, Eliott Kalfon, Adrian Hayler, Georg Grab, Vitor Monteiro, Lilly Wehrhahn, Dominik Safaric, Clara Cornu, Alan Arazi, Rylee Grace, Simone Alessi, Mihir Manium, Bernhard Schölkopf, Yann LeCun, Madelon Hulsebos, Sauraj Gambhir, Noah Hollmann, Frank Hutter
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.17895](https://arxiv.org/abs/2609.17895)

## Summary

TabPFN-3.5 is introduced as a new flagship tabular foundation model that significantly outperforms its predecessors and existing baselines across standard tabular benchmarks. It expands capabilities to handle complex real-world data challenges, including non-i.i.d. splits, heterogeneous data types (strings, text, images), and wide or high-cardinality tables. Additionally, variants like TabPFN-3.5-Fast and TabPFN-3.5-Thinking offer optimized inference speeds and inference-time compute scaling.

## Key Contributions

- Introduces TabPFN-3.5, a flagship tabular foundation model that sets a new state of the art on standard tabular prediction in TabArena.
- Extends capabilities to non-i.i.d. data, temporal or grouped splits, tables with strings, text, images, high-cardinality categoricals, and wide tables.
- Releases TabPFN-3.5-Fast for up to 3x faster inference and TabPFN-3.5-Thinking for inference-time computation scaling.

## Archivist Review

The submitted paper is a technical report on a tabular foundation model (TabPFN-3.5). Following the strict knowledge vault criteria and time-series skill constraints, model versions and specific tabular evaluation frameworks are paper-local or outside the scope of reusable forecasting mechanisms and open research questions. Therefore, both candidates are rejected.

### Rejected Candidates
- [concept] TabPFN-3.5 (`tabpfn-3-5`) - paper_local: TabPFN-3.5 is a specific versioned model family rather than a general methodological concept or reusable forecasting mechanism.
- [open_question] Non-I.I.D. Tabular Generalization (`non-iid-tabular-generalization`) - paper_local: The question focuses on tabular foundation model generalization on tabular and temporal splits rather than core time-series or forecasting methodology.

## Links

- [Abstract](https://arxiv.org/abs/2609.17895)
- [PDF](https://arxiv.org/pdf/2609.17895)

