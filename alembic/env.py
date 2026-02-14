import asyncio
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# This is the Alembic Config object, which provides
# access to the values within the .ini file in use.
# 
# This is used for *the* Alembic configuration object,
# that is, the object that uses the .ini file.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from yourapp import mymodel
# target_metadata = mymodel.Base.metadata

from myapp.models import Base  # Adjust this import based on your project structure

target_metadata = Base.metadata

# this function is used to run migrations in a special asynchronous context
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_bind_param=process_bind_param,
            include_schemas=True,
            future=True,
        )

        # Start the migration runner
        with context.begin_transaction():
            context.run_migrations()

# Entry point for running migrations
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()