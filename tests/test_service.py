import pytest
from toolhub_mcp_bridge.client import ToolHubError
from toolhub_mcp_bridge.service import BridgeService

class Fake:
    async def list_tools(self, path): return {"path": path}
    async def call_tool(self, path, args): return {"path": path, "args": args}

class Failing:
    async def list_tools(self, path): raise ToolHubError("denied", status_code=401, details={"error": "bad password"})

@pytest.mark.asyncio
async def test_success_envelope():
    result = await BridgeService(Fake()).list_tools("/")
    assert result == {"ok": True, "data": {"path": "/"}}

@pytest.mark.asyncio
async def test_toolhub_error_is_machine_readable():
    result = await BridgeService(Failing()).list_tools("/")
    assert result["ok"] is False
    assert result["source"] == "toolhub"
    assert result["status_code"] == 401
