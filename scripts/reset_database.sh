#!/usr/bin/env bash

set -e

echo "Stopping database container..."
docker-compose down -v --remove-orphans

echo "Deleting data folder..."
rm -rf data/

echo "Creating database container..."
docker-compose up -d

echo "Waiting for database to be ready..."
sleep 15

echo "Applying migrations..."
docker run --rm --network host \
    -v `pwd`/flyway/sql:/flyway/sql \
    flyway/flyway \
    -url="jdbc:mysql://localhost:3306/template?allowPublicKeyRetrieval=true" \
    -user=root \
    -password= \
    -locations="filesystem:/flyway/sql" \
    migrate
