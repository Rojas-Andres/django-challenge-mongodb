#!/usr/bin/env bash

/usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
exec "$@"
