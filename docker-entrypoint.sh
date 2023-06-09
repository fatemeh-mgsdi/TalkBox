#!/bin/sh

until python3 manage.py migrate
do
    echo "Waiting for postgres ready..."
    sleep 5
done

uvicorn TalkBox.asgi:application --host 0.0.0.0 --port 8000


