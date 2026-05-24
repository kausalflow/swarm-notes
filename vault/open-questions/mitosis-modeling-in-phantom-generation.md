---
created_at: '2026-05-24T07:47:39Z'
source_papers:
- '[[openalex-2605.22563-cell-phantom-video-generation-in-elliptical-fourier-descript]]'
title: Explicit Mitotic Event Modeling
---

**Background:** Cell phantom videos, which are binary masks representing cell morphology over time, require coherent evolution consistent with biological processes to facilitate accurate training of cell tracking models.

**Question / Future Work:** The generation of synthetic cell phantom videos that explicitly model mitotic events remains an unresolved challenge. Existing frameworks frequently struggle to accurately represent the division of a single cell into two daughter cells, necessitating future research to explicitly integrate cellular division dynamics into the generative process.

**Why It Matters:** Mitosis is a fundamental biological process in cell tracking; current models often simplify or discard daughter cells after division, which limits the biological realism and utility of synthetic datasets for tracking long-term cellular lineages.

**Evidence:** Future work aims at extending our framework to explicitly handle mitotic events (generating both daughter cells during cell divisions)