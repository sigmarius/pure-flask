#!/usr/bin/env bash

echo "Running migrations!"

flask db upgrade

exec "$@"