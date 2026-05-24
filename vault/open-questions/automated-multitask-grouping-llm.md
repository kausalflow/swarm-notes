---
created_at: '2026-05-24T07:47:55Z'
source_papers:
- '[[openalex-2605.22613-evolutionary-multi-task-optimization-for-llm-guided-program]]'
title: Automated Multitask Program Discovery
---

**Background:** Evolutionary search methods for program discovery frequently optimize tasks independently, often neglecting potential synergies between related tasks within a family.

**Question / Future Work:** There is a lack of understanding regarding how to systematically group arbitrary sets of tasks to facilitate effective shared program discovery, as well as how language models can autonomously infer and leverage reusable program structure across diverse task families.

**Why It Matters:** Addressing this is critical for moving beyond manually curated task families and enabling scalable, general-purpose evolutionary program discovery that can autonomously identify and exploit structural commonalities in arbitrary problem spaces.

**Evidence:** A limitation of EMO-STA is that the framework benefits from tasks being related so that a reusable program can address them simply by varying task parameters.