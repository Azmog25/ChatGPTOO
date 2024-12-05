#!/bin/bash

set -e  # Arrêter le script en cas d'erreur

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000