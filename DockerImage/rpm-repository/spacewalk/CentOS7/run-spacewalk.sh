#!/bin/bash

#sed -i 's/shared_buffers = 384MB/shared_buffers = 100MB/g' /var/lib/pgsql/data/postgresql.conf
sysctl -w kernel.shmmax=134217728 > /dev/null

# when use external postgresql . update answers.properties
#spacewalk-setup --disconnected --external-postgresql --answer-file=/etc/spacewalk/answers.properties

exec supervisord -c /etc/supervisor/conf.d/supervisord.conf

