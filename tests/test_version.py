import tomllib
from pathlib import Path
from toolhub_mcp_bridge import __version__

def test_package_version_matches_pyproject():
    data = tomllib.loads((Path(__file__).parents[1] / "pyproject.toml").read_text())
    assert data["project"]["version"] == __version__
