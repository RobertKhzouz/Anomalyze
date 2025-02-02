#!/bin/bash
set -e

# Load environment variables
export $(grep -v '^#' .env | xargs)

echo "Starting TimescaleDB Setup..."

docker run -d --name timescaledb \
    -p 5432:5432 \
    -e POSTGRES_USER=$POSTGRES_USER \
    -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
    -e POSTGRES_DB=$POSTGRES_DB \
    timescale/timescaledb:latest-pg15