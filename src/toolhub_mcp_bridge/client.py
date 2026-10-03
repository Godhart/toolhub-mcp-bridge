from __future__ import annotations
import httpx
from typing import Any

class ToolHubError(RuntimeError):
    def __init__(self, message: str, *, status_code: int | None = None, details: Any = None):
        super().__init__(message)
        self.status_code = status_code
        self.details = details

class ToolHubClient:
    def __init__(self, base_url: str, password: str | None = None, *, timeout: float = 60.0):
        self.base_url = base_url.rstrip("/")
        self.password = password
        self.timeout = timeout
        self._client_factory = lambda: httpx.AsyncClient(timeout=self.timeout)

    def _headers(self) -> dict[str, str]:
        headers = {"accept": "application/json"}
        if self.password:
            headers["x-agent-password"] = self.password
        return headers

    @staticmethod
    def normalize_path(path: str) -> str:
        if not path.startswith("/"):
            raise ValueError("ToolHub path must be absolute and start with '/'")
        if "?" in path or "#" in path:
            raise ValueError("ToolHub path must not contain query or fragment")
        return path

    async def _request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> Any:
        path = self.normalize_path(path)
        try:
            async with self._client_factory() as client:
                response = await client.request(method, f"{self.base_url}{path}", headers=self._headers(), json=payload)
        except httpx.HTTPError as exc:
            raise ToolHubError(str(exc)) from exc
        text = response.text
        try:
            body = response.json() if text else {}
        except ValueError:
            body = {"raw": text}
        if not response.is_success:
            raise ToolHubError(f"ToolHub returned HTTP {response.status_code}", status_code=response.status_code, details=body)
        return body

    async def list_tools(self, path: str = "/") -> Any:
        return await self._request("GET", path)

    async def call_tool(self, path: str, arguments: dict[str, Any] | None = None) -> Any:
        return await self._request("POST", path, arguments or {})
