#!/bin/bash
set -e

# Ensure we are in the repository root (or relative to this script)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Building Quartz website directly from vault..."
cd "$ROOT_DIR/website"

# The github action environment will already have correct node versions, 
# but if running locally we should make sure npx executes correctly.
npx quartz build -d ../vault

echo "Build complete!"
