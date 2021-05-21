#!/usr/bin/env bash
pip-compile examples/requirements/dev.in
pip install -r examples/requirements/dev.txt
pip install -e .
mkdir -p var/logs examples/db examples/media examples/media/static
python examples/simple/manage.py collectstatic --noinput
python examples/simple/manage.py migrate --noinput
