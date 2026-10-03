from __future__ import annotations
from typing import Any
from mcp.server import MCPServer
from .client import ToolHubClient
from .service import BridgeService

INSTRUCTIONS = """ToolHub is hierarchical. Browse the relevant path with toolhub_list before calling a tool whose path/schema is not already known. Do not invent tool paths or arguments."""

def create_server(base_url: str, password: str | None = None, timeout: float = 60.0) -> MCPServer:
    service = BridgeService(ToolHubClient(base_url, password, timeout=timeout))
    mcp = MCPServer("toolhub-mcp-bridge", instructions=INSTRUCTIONS)

    @mcp.tool(title="Browse ToolHub")
    async def toolhub_list(path: str = "/") -> dict[str, Any]:
        """Browse a ToolHub folder. Returns its child categories/tools and ToolHub-provided metadata/schemas."""
        return await service.list_tools(path)

    @mcp.tool(title="Call ToolHub tool")
    async def toolhub_call(path: str, arguments: dict[str, Any] | None = None) -> dict[str, Any]:
        """Execute a known ToolHub tool by absolute path. Browse first when the path or arguments are unknown."""
        return await service.call_tool(path, arguments)

    return mcp
