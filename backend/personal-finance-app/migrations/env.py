"""Alembic env.py minimal placeholder
This file is a lightweight placeholder so Alembic commands won't fail if run
before migrations are configured. Replace with a real alembic env.py when you
configure Alembic and SQLAlchemy metadata.
"""
from logging.config import fileConfig
import os

from sqlalchemy import engine_from_config
from sqlalchemy import pool

# this is the Alembic Config object, which provides
# access to the values within the .ini file
from alembic import context

config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Placeholder metadata - import your models' metadata here when available
target_metadata = None


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = os.getenv('DATABASE_URL', 'sqlite:///./personal_finance.db')
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
