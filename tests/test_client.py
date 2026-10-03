import json
import pytest
import httpx
from toolhub_mcp_bridge.client import ToolHubClient

class Handler:
    def __init__(self): self.requests=[]
    async def __call__(self, request):
        self.requests.append(request)
        if request.method == "GET": return httpx.Response(200, json={"tools": []})
        return httpx.Response(200, json={"success": True})

def make_client(handler, password=None):
    obj = ToolHubClient("http://hub:3000", password)
    transport = httpx.MockTransport(handler)
    obj._client_factory = lambda: httpx.AsyncClient(transport=transport, timeout=obj.timeout)
    return obj

@pytest.mark.asyncio
async def test_list_is_get_to_native_path(monkeypatch):
    h=Handler(); c=make_client(h, "secret")
    result=await c.list_tools("/system")
    assert h.requests[0].method == "GET"
    assert str(h.requests[0].url) == "http://hub:3000/system"
    assert h.requests[0].headers["x-agent-password"] == "secret"
    assert result == {"tools": []}

@pytest.mark.asyncio
async def test_call_is_post_to_native_path():
    h=Handler(); c=make_client(h)
    result=await c.call_tool("/system/ping", {"x":1})
    assert h.requests[0].method == "POST"
    assert json.loads(h.requests[0].content) == {"x":1}
    assert result["success"] is True

@pytest.mark.asyncio
async def test_relative_paths_are_rejected():
    with pytest.raises(ValueError):
        await ToolHubClient("http://hub:3000").list_tools("system")
