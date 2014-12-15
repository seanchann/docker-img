#!/bin/bash

DB_NAME=${DB_NAME:-}
DB_USER=${DB_USER:-}
DB_PASS=${DB_PASS:-}
PG_CONFDIR="/opt/dokcershare/pgsql/data"

__create_user() {
  #Grant rights
  usermod -G wheel postgres

  # Check to see if we have pre-defined credentials to use
if [ -n "${DB_USER}" ]; then
  if [ -z "${DB_PASS}" ]; then
    echo ""
    echo "WARNING: "
    echo "No password specified for \"${DB_USER}\". Generating one"
    echo ""
    DB_PASS=$(pwgen -c -n -1 12)
    echo "Password for \"${DB_USER}\" created as: \"${DB_PASS}\""
  fi
    echo "Creating user \"${DB_USER}\"..."
    echo "CREATE ROLE ${DB_USER} with CREATEROLE login superuser PASSWORD '${DB_PASS}';" |
      sudo -u postgres -H postgres --single \
       -c config_file=${PG_CONFDIR}/postgresql.conf -D ${PG_CONFDIR}
  
fi

if [ -n "${DB_NAME}" ]; then
  echo "Creating database \"${DB_NAME}\"..."
  echo "CREATE DATABASE ${DB_NAME};" | \
    sudo -u postgres -H postgres --single \
     -c config_file=${PG_CONFDIR}/postgresql.conf -D ${PG_CONFDIR}

  if [ -n "${DB_USER}" ]; then
    echo "Granting access to database \"${DB_NAME}\" for user \"${DB_USER}\"..."
    echo "GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} to ${DB_USER};" |
      sudo -u postgres -H postgres --single \
      -c config_file=${PG_CONFDIR}/postgresql.conf -D ${PG_CONFDIR}
  fi
fi
}


__run_supervisor() {
supervisord -n
}

NEED_INIT_DATA="false"
#init spacewalk db
__spacewalk_init_db() {

    if [ "$NEED_INIT_DATA" = "true" ]; then
        sudo -u postgres pg_ctl start -D /opt/dockershare/pgsql/data
        su - postgres -c 'PGPASSWORD=spacepw; createdb -E UTF8 spaceschema ; createlang plpgsql spaceschema ; createlang pltclu spaceschema ; yes $PGPASSWORD | createuser -P -sDR spaceuser'
        sudo -u postgres pg_ctl stop -D /opt/dockershare/pgsql/data
    
        mv /pg_hba.conf  ${PGSQL_HOME}/data/pg_hba.conf
        chown -v postgres.postgres ${PGSQL_HOME}/data/pg_hba.conf
    fi
}


__init_data() {
    if [ ! -f "$PGSQL_HOME/data/postgresql.conf" ]; then
    
        mkdir -p ${PGSQL_HOME}/data
        chown -R -v postgres.postgres ${PGSQL_HOME}
        
        /usr/bin/postgresql-setup initdb
        

        mv  /postgresql.conf   ${PGSQL_HOME}/data/postgresql.conf
        chown -v postgres.postgres ${PGSQL_HOME}/data/postgresql.conf
        
        NEED_INIT_DATA="true"
    fi

}


# Call all functions
__init_data
__create_user
__spacewalk_init_db
__run_supervisor


