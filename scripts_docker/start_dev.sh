#!/usr/bin/env bash

echo "Executing start_dev.sh"
python manage.py migrate --noinput
python manage.py runserver 0:8000
