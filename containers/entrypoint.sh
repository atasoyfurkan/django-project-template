#!/bin/ash

set -e

./containers/wait-for-it.sh --host=$DB_HOST --port=$DB_PORT
# python3 manage.py db_entrypoint
python3 manage.py migrate
python3 manage.py collectstatic --noinput > /dev/null &

exec $@