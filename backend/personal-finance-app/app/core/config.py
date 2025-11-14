"""Minimal settings for the application.

This module intentionally keeps configuration simple: the application only
requires DATABASE_URL, API_HOST and API_PORT from the environment. Other
settings remain available as safe defaults so other modules (auth, security,
etc.) continue to work without additional environment variables.

When running with the Uvicorn CLI you can use:

    uvicorn app.main:app --reload --env-file .env.dev

which will populate the environment before the app is imported.
"""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class Settings:
    # Required / commonly overridden in dev
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./personal_finance.db")
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))

    # Optional settings with sensible defaults (kept for compatibility)
    APP_NAME: str = "personal-finance-app"
    DEBUG: bool = False
    SECRET_KEY: str = "change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24


settings = Settings()

