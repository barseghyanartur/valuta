#!/usr/bin/env bash
echo 'Making messages for valuta...'
cd examples/django_example/
./manage.py makemigrations valuta

echo 'Making messages for example projects...'
./manage.py makemigrations

echo 'Applying migrations...'
./manage.py migrate
