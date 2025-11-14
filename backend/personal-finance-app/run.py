"""Small runner that accepts an --env file and starts the app with uvicorn.

Usage examples:
  python run.py --env .env.dev --reload
  python run.py --env ./config/.env.local

This requires `python-dotenv` to be installed. If not available the script
will fall back to a tiny parser for KEY=VALUE lines.
"""
from __future__ import annotations

import argparse
import os
import sys
from typing import Optional


def _load_dotenv(path: str) -> None:
    """Load environment variables from `path`.

    Tries python-dotenv first; falls back to a simple parser if unavailable.
    """
    try:
        from dotenv import load_dotenv

        load_dotenv(dotenv_path=path, override=True)
        return
    except Exception:
        pass

    # Fallback: very small KEY=VALUE parser
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())
    except FileNotFoundError:
        print(f"Env file not found: {path}", file=sys.stderr)
        sys.exit(2)


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Run the FastAPI app with optional env file")
    parser.add_argument("--env", help="Path to an env file to load before starting the app")
    parser.add_argument("--host", help="Host to bind (overrides API_HOST)", default=os.getenv("API_HOST", "127.0.0.1"))
    parser.add_argument("--port", help="Port to bind (overrides API_PORT)", type=int, default=int(os.getenv("API_PORT", "8000")))
    parser.add_argument("--reload", help="Enable uvicorn reload", action="store_true")

    args = parser.parse_args(argv)

    if args.env:
        _load_dotenv(args.env)

    # Import here so that env is loaded before app config reads it
    try:
        import uvicorn

        # uvicorn.run expects the import path to the ASGI app
        uvicorn.run("app.main:app", host=args.host, port=args.port, reload=args.reload)
    except Exception as exc:
        print("Failed to start uvicorn:", exc, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
