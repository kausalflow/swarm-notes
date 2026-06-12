---
created_at: '2026-06-12T08:53:17Z'
source_papers:
- '[[openalex-2606.10663-reconstructing-opc-ua-address-spaces-from-time-series-databa]]'
title: Preserving custom type hierarchies
---

**Background:** OPC UA systems utilize complex type hierarchies where custom ObjectTypes and VariableTypes define the semantic structure of nodes.

**Question / Future Work:** Develop mechanisms to preserve the complete custom type hierarchy during the persistence and reconstruction process, ensuring that specialized type definitions and their relationships are accurately reflected in the reconstructed endpoint.

**Why It Matters:** Preserving type hierarchies is essential for maintaining the semantic fidelity and interoperability of industrial digital twins.

**Evidence:** Limitations remain: the reconstruction is snapshot-based, and custom ObjectType / VariableType definitions reattach to built-in base types in the current implementation.