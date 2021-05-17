#!/usr/bin/env bash
./scripts/uninstall.sh
./scripts/install.sh
rm docs/*.rst
rm -rf builddocs/
sphinx-apidoc src/valuta --full -o docs -H 'valuta' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -f -d 20
cp docs/conf.py.distrib docs/conf.py
