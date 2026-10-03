# ADR-0001: Keep MCP support in a separate adapter

Status: Accepted — 2026-09-25

## Context
ToolHub is an execution engine with its own REST/SDK contract. MCP is an integration protocol used by external hosts.

## Decision
`toolhub-mcp-bridge` is a separate package/process. ToolHub core remains MCP-agnostic on its agent-facing side. The bridge translates MCP calls to the public ToolHub agent API only.

## Consequences
MCP SDK churn is isolated from ToolHub; the bridge can be upgraded/replaced independently; no admin credentials are required by the bridge.
