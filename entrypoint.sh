#!/bin/bash
python manage.py makemigrations --noinput
python manage.py migrate --noinput
celery -A config  worker -l info
gunicorn config.wsgi:application --bind 0.0.0.0:8000
