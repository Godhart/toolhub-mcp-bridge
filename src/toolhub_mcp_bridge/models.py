from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field

class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

class ListInput(StrictModel):
    path: str = Field(default="/", min_length=1, description="ToolHub tree path to inspect")

class CallInput(StrictModel):
    path: str = Field(min_length=1, description="Absolute ToolHub path of the tool")
    arguments: dict[str, Any] = Field(default_factory=dict)

class BridgeError(StrictModel):
    ok: Literal[False] = False
    source: Literal["bridge", "toolhub", "transport"]
    kind: str
    message: str
    status_code: int | None = None
    details: Any | None = None

class BridgeResult(StrictModel):
    ok: Literal[True] = True
    data: Any
