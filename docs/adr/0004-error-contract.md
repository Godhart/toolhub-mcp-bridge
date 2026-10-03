# ADR-0004: Stable structured bridge error envelope

Status: Accepted — 2026-09-25

## Decision
Every bridge operation returns either `{ok:true,data:...}` or `{ok:false,source,kind,message,...}`. `source` distinguishes bridge validation/internal failures, ToolHub HTTP failures, and transport failures. Raw successful ToolHub payloads remain under `data` without lossy transformation.

## Consequences
Agents and tests can distinguish where a failure originated. Future ToolSpec structured errors pass through intact in `details`/`data` rather than being flattened into prose.
