#!/bin/bash
python manage.py makemigrations --noinput
python manage.py migrate --noinput
celery -A config  worker -l info
python manage.py collectstatic
gunicorn config.wsgi:application --bind 0.0.0.0:8000
