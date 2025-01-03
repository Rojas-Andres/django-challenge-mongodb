#!/usr/bin/env bash
python manage.py collectstatic --noinput

/usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
exec "$@"
