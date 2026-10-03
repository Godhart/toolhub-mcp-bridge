# ADR-0003: stdio first, Streamable HTTP second

Status: Accepted — 2026-09-25

## Decision
Support `stdio` as the default local transport and `streamable-http` for deployed/network use. Do not add new SSE-specific code.

## Rationale
This follows the current MCP Python SDK transport guidance and keeps the local setup minimal.
