#!/bin/sh
while ! nc -z $DB_HOST $DB_PORT; do sleep 1; done;
poetry run alembic upgrade head

export PGPASSWORD=$DB_PASS

psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f /app/insert_into_tables.sql

poetry run uvicorn main:app --host 0.0.0.0 --port 8000
