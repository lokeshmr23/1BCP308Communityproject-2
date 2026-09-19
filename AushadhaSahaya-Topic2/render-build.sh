#!/bin/sh
set -e
echo "== AushadhaSahaya Render Build Pipeline =="
python3 -V
python3 src/make_field_data.py
python3 collect.py
echo "== Build Verified Successfully =="
