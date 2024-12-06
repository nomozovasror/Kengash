#!/bin/bash
set -e  # Exit on any error

echo "PostgreSQL ishga tushishini kuting..."
while ! nc -z kengash_db 5432; do
  sleep 0.1
done
echo "PostgreSQL tayyor."

echo "Migratsiyalarni bajarish..."
python manage.py migrate --no-input

echo "Statik fayllarni yig'ish..."
python manage.py collectstatic --no-input

# Django serverni boshqa protsessda ishga tushirish
echo "Django serverini ishga tushirish..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000 &

# Botni ishga tushirish
echo "Botni ishga tushirish..."
python bot.py &

wait
