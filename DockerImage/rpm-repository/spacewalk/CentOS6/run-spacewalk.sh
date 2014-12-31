#!/bin/bash


/bin/sh /usr/local/bin/init-spacewalk.sh

sed -i 's/shared_buffers = 384MB/shared_buffers = 100MB/g' /var/lib/pgsql/data/postgresql.conf
sysctl -w kernel.shmmax=134217728 > /dev/null

__run_supervisor() {
supervisord -n
}

rm -Rf /var/lib/jabberd/db/*
/usr/sbin/spacewalk-service restart
__run_supervisor

