# toolhub-mcp-bridge 0.1.0

A small MCP facade over ToolHub's native hierarchical Agent API.

## MCP surface
- `toolhub_list(path="/")` — browse a branch and obtain ToolHub metadata/schema.
- `toolhub_call(path, arguments={})` — execute a known tool.

The bridge deliberately does **not** flatten all ToolHub tools into MCP `tools/list`.

## Install
```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .
# development/tests
pip install -e '.[dev]'
```

## Configure and run
```bash
export TOOLHUB_URL=http://127.0.0.1:3000
export TOOLHUB_AGENT_PASSWORD=123

toolhub-mcp                         # stdio (default)
toolhub-mcp --transport streamable-http --host 127.0.0.1 --port 8000
```

Equivalent CLI flags: `--url`, `--password`, `--timeout`, `--transport`, `--host`, `--port`.

## MCP client configuration (stdio example)
```json
{
  "mcpServers": {
    "toolhub": {
      "command": "/absolute/path/to/.venv/bin/toolhub-mcp",
      "env": {
        "TOOLHUB_URL": "http://127.0.0.1:3000",
        "TOOLHUB_AGENT_PASSWORD": "123"
      }
    }
  }
}
```

## Security
The bridge uses only ToolHub agent credentials (`x-agent-password`). Do not give it the admin password. Bind Streamable HTTP to localhost unless you intentionally add an appropriate network/auth boundary in front of it.

## Tests
```bash
pytest
```

Architectural decisions are append-only records in `docs/adr/`. Tests are cumulative; new releases must add regression tests for new behavior and bugs.
