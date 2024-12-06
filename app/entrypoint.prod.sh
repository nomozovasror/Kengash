#!/bin/bash

echo "Checking script permissions..."
ls -l /entrypoint.prod.sh

echo "PostgreSQL ishga tushishini kuting..."
while ! nc -z kengash_db 5432; do
  sleep 0.1
done
echo "PostgreSQL tayyor."

#echo "Migratsiyalarni bajarish..."
#python manage.py flush --no-input
#python manage.py migrate

echo "Statik fayllarni yig'ish..."
python manage.py collectstatic --noinput

echo "Django serverini ishga tushirish..."
exec "$@"
