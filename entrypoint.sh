#!/bin/sh

echo "Waiting for database..."
until nc -z -v -w30 db 5432; do
  echo "Waiting for database..."
  sleep 1
done
echo "Database is ready!"

# Check if the project is already created
if [ ! -f "manage.py" ]; then
  echo "Creating new Django project..."
  django-admin startproject config .
fi

echo "Running migrations..."
python manage.py migrate
echo "Migrations completed."

# Running Django server
exec "$@"