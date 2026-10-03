from __future__ import annotations
from typing import Any
from .client import ToolHubClient, ToolHubError
from .models import BridgeError, BridgeResult

class BridgeService:
    def __init__(self, client: ToolHubClient):
        self.client = client

    async def list_tools(self, path: str = "/") -> dict[str, Any]:
        return await self._run(self.client.list_tools, path)

    async def call_tool(self, path: str, arguments: dict[str, Any] | None = None) -> dict[str, Any]:
        return await self._run(self.client.call_tool, path, arguments or {})

    async def _run(self, fn, *args) -> dict[str, Any]:
        try:
            return BridgeResult(data=await fn(*args)).model_dump(mode="json")
        except ValueError as exc:
            return BridgeError(source="bridge", kind="invalid_request", message=str(exc)).model_dump(mode="json")
        except ToolHubError as exc:
            source = "toolhub" if exc.status_code is not None else "transport"
            kind = "http_error" if exc.status_code is not None else "connection_error"
            return BridgeError(source=source, kind=kind, message=str(exc), status_code=exc.status_code, details=exc.details).model_dump(mode="json")
        except Exception as exc:
            return BridgeError(source="bridge", kind="internal_error", message=str(exc)).model_dump(mode="json")
