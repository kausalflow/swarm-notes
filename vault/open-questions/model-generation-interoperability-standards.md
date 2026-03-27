---
created_at: '2026-03-27T15:44:35Z'
source_papers:
- '[[openalex-2603.23015-janusbm-a-dual-fidelity-multi-zone-white-box-building-modeli]]'
title: Integrate GIS/BIM standards
---

**Background:** The modeling framework currently generates thermal models based on custom inputs, but interoperability with common building data standards is limited for large-scale scenario exploration.

**Question / Future Work:** Integrate common building geometry and attribute standards, such as CityGML, IFC, and gbXML, as upstream providers for generating the RoomFlex6D topology and parameter tables to maintain interoperability while preserving the efficiency required for large-scale scenario exploration.

**Why It Matters:** Integrating standardized formats is essential for broader adoption and seamless integration with existing building data workflows (e.g., BIM).

**Evidence:** Finally in future work on model generation, the CityGML, IFC and gbXML source can be used as upstream providers of building geometry and attributes (Benner, 2026), which would then be compiled into the RoomFlex6D topology and parameter tables to maintain both interoperability and the efficiency required for large-scale scenario exploration.