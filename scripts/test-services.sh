#!/usr/bin/env bash

# Exit on error
set -e

echo "Running tests for all services..."

# Auth Service
echo "--------------------------------------------------"
echo "Testing Auth Service..."
cd services/auth-service
uv sync
uv run bash scripts/tests-start.sh "Local Test - Auth Service"
cd ../..

echo "--------------------------------------------------"
echo "All tests passed!"
