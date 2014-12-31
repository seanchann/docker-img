#!/bin/bash

# Make sure we're not confused by old, incompletely-shutdown httpd
# context after restarting the container.  httpd won't start correctly
# if it thinks it is already running.
rm -rf /run/httpd/*


if [ ! -f /opt/dockershare/httpd/var ]; then
    mkdir -p /opt/dockershare/httpd/var/www/
    chmod -R 755 /opt/dockershare/httpd/var/www/
fi


exec /usr/sbin/apachectl -D FOREGROUND
