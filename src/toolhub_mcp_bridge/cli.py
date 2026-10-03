from __future__ import annotations
import argparse, os
from .server import create_server

def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="toolhub-mcp")
    p.add_argument("--url", default=os.getenv("TOOLHUB_URL", "http://127.0.0.1:3000"))
    p.add_argument("--password", default=os.getenv("TOOLHUB_AGENT_PASSWORD"))
    p.add_argument("--timeout", type=float, default=float(os.getenv("TOOLHUB_TIMEOUT", "60")))
    p.add_argument("--transport", choices=("stdio", "streamable-http"), default=os.getenv("TOOLHUB_MCP_TRANSPORT", "stdio"))
    p.add_argument("--host", default=os.getenv("TOOLHUB_MCP_HOST", "127.0.0.1"))
    p.add_argument("--port", type=int, default=int(os.getenv("TOOLHUB_MCP_PORT", "8000")))
    return p

def main() -> None:
    args = parser().parse_args()
    mcp = create_server(args.url, args.password, args.timeout)
    if args.transport == "stdio":
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="streamable-http", host=args.host, port=args.port)

if __name__ == "__main__":
    main()
