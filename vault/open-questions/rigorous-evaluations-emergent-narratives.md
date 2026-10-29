---
created_at: '2026-10-29T11:10:51Z'
source_papers:
- '[[openalex-2610.35628-investigating-forecasting-capabilities-of-narrative-networks]]'
title: Rigorous Evaluation for Emergent Narratives
---

**Background:** Narrative networks constructed from news articles can forecast emergent interactions between entities, but existing evaluations often rely on random negative sampling or mix recurring links.

**Question / Future Work:** Develop rigorous evaluation protocols and learned temporal models for the emergent narrative prediction regime that move beyond uniformly random negatives to historical or degree-matched negatives, thereby isolating genuine structural effects from mere node salience and degree biases.

**Why It Matters:** Crucial for establishing whether narrative network forecasting captures true underlying relational dynamics rather than artifactual degree correlations driven by entity salience and random negative sampling.

**Evidence:** Finally, our emergent-protocol results use uniformly random negatives, which favor degree-based scorers (Poursafaei et al., 2022); endpoint degree and news salience may account for much of Preferential Attachment’s advantage, and isolating a genuinely structural effect would require historical or degree-matched negatives and learned temporal models on the emergent subset. These are directions for future work.