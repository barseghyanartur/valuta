#!/usr/bin/env bash
pycallgraph \
  --stdlib \
  --include "valuta.*" \
  --include "*.*" \
  --max-depth=20 \
  graphviz \
  -- benchmarks/profile.py
