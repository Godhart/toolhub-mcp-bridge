# ADR-0002: Preserve ToolHub hierarchical navigation

Status: Accepted — 2026-09-25

## Context
ToolHub intentionally avoids publishing every tool schema at once. Its native contract is hierarchical `listTools(path)` followed by `callTool(path, payload)`.

## Decision
Expose two stable MCP tools: `toolhub_list(path)` and `toolhub_call(path, arguments)`. Do not flatten ToolHub's complete catalog into MCP `tools/list`, and do not invent a separate full-text search API in v0.1.0.

## Consequences
Context remains bounded as ToolHub grows. MCP clients need one discovery step before an unknown call. A future search capability may be added only if ToolHub itself exposes a stable search contract.
