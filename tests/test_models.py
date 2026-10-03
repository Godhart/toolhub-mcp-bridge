import pytest
from pydantic import ValidationError
from toolhub_mcp_bridge.models import CallInput

def test_models_forbid_unknown_fields():
    with pytest.raises(ValidationError):
        CallInput(path="/x", arguments={}, typo=True)
