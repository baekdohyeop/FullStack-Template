#! /usr/bin/env bash

# Let the DB start
python /app/app/prestart.py

# Run migrations
alembic upgrade head
