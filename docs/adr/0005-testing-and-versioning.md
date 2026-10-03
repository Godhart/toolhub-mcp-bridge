# ADR-0005: Accumulating regression suite and version invariant

Status: Accepted — 2026-09-25

## Decision
Tests are cumulative across releases. Every bug fix or new behavior adds regression coverage. CI/release tests must verify that the package `__version__` equals `project.version` in `pyproject.toml`.
