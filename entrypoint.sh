#!/bin/sh

if [ "$RUN_MODE" = "test" ]; then
  echo "🔍 Lancement des tests..."
  pytest test_app.py --tb=short > resultats_tests.txt || true
  cat resultats_tests.txt
else
  echo "🚀 Lancement de l’application Flask..."
  python app.py
fi
