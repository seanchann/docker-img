#!/bin/bash

SPACEWALK_HOME=/opt/dockershare/spacewalk/
PG_HOME=${SPACEWALK_HOME}/pgsql/
NEED_INIT="false"
PGNAME=spaceschema

exists_db() {
    EXISTS=$(runuser - postgres -c 'psql -t -c "select datname from pg_database where datname='"'$PGNAME'"';"')
    if [ "x$EXISTS" == "x $PGNAME" ] ; then
        return 0
    else
        return 1
    fi
}


if exists_db ; then
    echo "Database \"$PGNAME\" already exists"
    NEED_INIT="false"
else
    echo "Database \"$PGNAME\" does not exist"
    NEED_INIT="true"
fi




function init_pgsql()
{
    mkdir -p ${PG_HOME}/data

    rm -rf /var/lib/pgsql

    ln -s ${PG_HOME} /var/lib/pgsql

    chown -R -v postgres.postgres ${PG_HOME}
}


if [ "$NEED_INIT" = "true" ]; then
    echo "init spacewalk begin..."
    init_pgsql
    
    
    
    #init spacewalk when container start
    #spacewalk-setup --disconnected --external-postgresql --answer-file=/etc/spacewalk/answers.properties
    spacewalk-setup --disconnected  --answer-file=/etc/spacewalk/answers.properties
    
    sed -i 's#^mount_point = /var/satellite#mount_point = /opt/dockershare/spacewalk/var/satellite#' /etc/rhn/rhn.conf
    sed -i 's#^kickstart_mount_point = /var/satellite#kickstart_mount_point = /opt/dockershare/spacewalk/var/satellite#' /etc/rhn/rhn.conf
    sed -i 's#^repomd_cache_mount_point = /var/cache#repomd_cache_mount_point = /opt/dockershare/spacewalk/var/cache#' /etc/rhn/rhn.conf
    
    mkdir -p /opt/dockershare/spacewalk/var/cache
    
    mkdir -p /opt/dockershare/spacewalk/var/satellite
    chown -R -v apache.root /opt/dockershare/spacewalk/var/satellite

fi

 