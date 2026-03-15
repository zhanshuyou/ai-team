#!/usr/bin/env bash
# Lint check script — runs available linters in the project
# Usage: bash scripts/lint-check.sh [path]

set -euo pipefail

TARGET="${1:-.}"

echo "=== Running lint checks on: $TARGET ==="

# Detect and run available linters
if [ -f "package.json" ]; then
  if command -v npx &> /dev/null; then
    if grep -q '"eslint"' package.json 2>/dev/null; then
      echo "--- ESLint ---"
      npx eslint "$TARGET" --max-warnings=0 || true
    fi
    if grep -q '"prettier"' package.json 2>/dev/null; then
      echo "--- Prettier ---"
      npx prettier --check "$TARGET" || true
    fi
    if grep -q '"tsc"' package.json 2>/dev/null || grep -q '"typescript"' package.json 2>/dev/null; then
      echo "--- TypeScript ---"
      npx tsc --noEmit || true
    fi
  fi
fi

if [ -f "pyproject.toml" ] || [ -f "setup.py" ] || [ -f "requirements.txt" ]; then
  if command -v ruff &> /dev/null; then
    echo "--- Ruff ---"
    ruff check "$TARGET" || true
  elif command -v flake8 &> /dev/null; then
    echo "--- Flake8 ---"
    flake8 "$TARGET" || true
  fi
  if command -v mypy &> /dev/null; then
    echo "--- Mypy ---"
    mypy "$TARGET" || true
  fi
fi

echo "=== Lint checks complete ==="
