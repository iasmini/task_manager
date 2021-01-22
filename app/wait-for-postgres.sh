#!/bin/sh

# wait-for-postgres.sh
# https://docs.docker.com/compose/startup-order/
# -e  Exit immediately if a command exits with a non-zero status.

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"