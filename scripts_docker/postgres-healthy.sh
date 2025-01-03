#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $MONGO_HOST $MONGO_PORT; do
        sleep 0.1
    done

    echo "PostgresSQL started"
fi

exec "$@"
