#!/bin/bash

set -e

#export LAMPHOMEDIR=/opt/lamp/
#export RPMDIR=/home/smit/rpmbuild/

mysqlPath=${LAMPHOMEDIR}/mysql
httpdPath=${LAMPHOMEDIR}/httpd
phpPath=${LAMPHOMEDIR}/php


function build_mysql(){
    name=mysql-5.6.17
    specFile=mysql.spec
    specFileFull=${mysqlPath}/${specFile}
      
    
    \rm -rf ${RPMDIR}/SOURCES/${name}.tar.gz

    cd  ${mysqlPath}
    \tar -czf ${RPMDIR}/SOURCES/${name}.tar.gz  ${name}   
    #cp other source to dir
    \cp -rf  mysql-*.patch  ${RPMDIR}/SOURCES/
    \cp -rf  my_config.h  ${RPMDIR}/SOURCES/
    \cp -rf  mysql.conf  ${RPMDIR}/SOURCES/
    \cp -rf  filter-*.sh  ${RPMDIR}/SOURCES/
    \cp -rf  mysql_config.sh  ${RPMDIR}/SOURCES/
    \cp -rf  mysqld.service  ${RPMDIR}/SOURCES/
    \cp -rf  mysql-systemd-start  ${RPMDIR}/SOURCES/

    \cp -rf ${specFileFull}  ${RPMDIR}/SPECS

    rpmbuild -ba ${RPMDIR}/SPECS/${specFile}
}



function build_apr(){
    name=apr-1.5.1
    
    \rm -rf ${RPMDIR}/SOURCES/${name}.tar.bz2

    cd  ${httpdPath}
    tar -cjf ${RPMDIR}/SOURCES/${name}.tar.bz2 ${name}

    rpmbuild -tb ${RPMDIR}/SOURCES/${name}.tar.bz2
}

function build_apr_util(){
    name=apr-util-1.5.4
    
    \rm -rf ${RPMDIR}/SOURCES/${name}.tar.bz2
    
    cd  ${httpdPath}
    tar -cjf ${RPMDIR}/SOURCES/${name}.tar.bz2 ${name}

    rpmbuild -tb ${RPMDIR}/SOURCES/${name}.tar.bz2
}

function build_distcache(){
    name=distcache-1.4.5-23.src.rpm
    
    \rm -rf ${RPMDIR}/SOURCES/${name}
    
 
    \cp -rf ${httpdPath}/${name} ${RPMDIR}/SOURCES/

    rpmbuild --rebuild ${RPMDIR}/SOURCES/distcache-1.4.5-23.src.rpm
}



function build_httpd(){
    name=httpd-2.4.10
    
    \rm -rf ${RPMDIR}/SOURCES/${name}.tar.bz2

    cd  ${httpdPath}
    tar -cjf ${RPMDIR}/SOURCES/${name}.tar.bz2 ${name}


    rpmbuild -tb ${RPMDIR}/SOURCES/${name}.tar.bz2
}


function build_libmcrypt(){
    name=libmcrypt-2.5.8
    specFile=libmcrypt.spec
    specFileFull=${phpPath}/libmcrypt/${specFile}
      
    
    \rm -rf ${RPMDIR}/SOURCES/${name}.tar.gz
    \rm -rf ${RPMDIR}/SOURCES/${name}*.patch

    cd  ${phpPath}/libmcrypt
    \tar -czf ${RPMDIR}/SOURCES/${name}.tar.gz  ${name}
    cp -rf *.patch ${RPMDIR}/SOURCES/
    
    \cp -rf ${specFileFull}  ${RPMDIR}/SPECS

    rpmbuild -ba ${RPMDIR}/SPECS/${specFile}

}

function build_php_54(){
    name=php-5.4.16
    specFile=php.spec
    specFileFull=${phpPath}/php-5.4.16/${specFile}

    cd  ${phpPath}/${name}
    cp -rf  *   ${RPMDIR}/SOURCES/
    \cp -rf ${specFileFull}  ${RPMDIR}/SPECS

    rpmbuild -ba ${RPMDIR}/SPECS/${specFile}  
}

function build_php_55(){
    name=php-5.5.10
    specFile=php55.spec
    specFileFull=${phpPath}/php55/${specFile}
      
    
    \rm -rf ${RPMDIR}/SOURCES/${name}.tar.gz
    \rm -rf ${RPMDIR}/SOURCES/php*.patch
    \rm -rf ${RPMDIR}/SOURCES/macros.php
    \rm -rf ${RPMDIR}/SOURCES/php.conf
    \rm -rf ${RPMDIR}/SOURCES/php-fpm.conf
    \rm -rf ${RPMDIR}/SOURCES/php-fpm.init
    \rm -rf ${RPMDIR}/SOURCES/php-fpm.logrotate
    \rm -rf ${RPMDIR}/SOURCES/php-fpm.sysconfig
    \rm -rf ${RPMDIR}/SOURCES/php-fpm-www.conf

    cd  ${phpPath}/php55
    \tar -cjf ${RPMDIR}/SOURCES/${name}.tar.bz2  ${name}
    cp -rf php*.patch  ${RPMDIR}/SOURCES/
    cp -rf macros.php  ${RPMDIR}/SOURCES/
    cp -rf php.conf  ${RPMDIR}/SOURCES/
    cp -rf php-fpm.conf  ${RPMDIR}/SOURCES/
    cp -rf php-fpm.init  ${RPMDIR}/SOURCES/
    cp -rf php-fpm.logrotate  ${RPMDIR}/SOURCES/
    cp -rf php-fpm.sysconfig  ${RPMDIR}/SOURCES/
    cp -rf php-fpm-www.conf  ${RPMDIR}/SOURCES/
    
    \cp -rf ${specFileFull}  ${RPMDIR}/SPECS

    rpmbuild -ba ${RPMDIR}/SPECS/${specFile}   
}


function build_php_pear(){
    name=PEAR-1.9.4.tgz
    specFile=php-pear.spec
    specFileFull=${phpPath}/php-pear/${specFile}
    
    
    \rm -rf ${RPMDIR}/SOURCES/${name}
    \rm -rf ${RPMDIR}/SOURCES/php-pear*.patch
    \rm -rf ${RPMDIR}/SOURCES/Archive_Tar-1.3.11.tgz
    \rm -rf ${RPMDIR}/SOURCES/Console_Getopt-1.3.1.tgz
    \rm -rf ${RPMDIR}/SOURCES/install-pear.php
    \rm -rf ${RPMDIR}/SOURCES/macros.pear
    \rm -rf ${RPMDIR}/SOURCES/pear.1
    \rm -rf ${RPMDIR}/SOURCES/pear.conf.5
    \rm -rf ${RPMDIR}/SOURCES/peardev.1
    \rm -rf ${RPMDIR}/SOURCES/peardev.sh
    \rm -rf ${RPMDIR}/SOURCES/pear.sh
    \rm -rf ${RPMDIR}/SOURCES/pecl.1
    \rm -rf ${RPMDIR}/SOURCES/pecl.sh
    \rm -rf ${RPMDIR}/SOURCES/strip.php
    \rm -rf ${RPMDIR}/SOURCES/Structures_Graph-1.0.4.tgz
    \rm -rf ${RPMDIR}/SOURCES/XML_Util-1.2.1.tgz
    

    cd  ${phpPath}/php-pear
    \tar -czf ${RPMDIR}/SOURCES/${name}  ${name}
    cp -rf php-pear*.patch *.tgz install-pear.php macros.pear pear.1\
        pear.conf.5 peardev.1 peardev.sh pear.sh pecl.1 pecl.sh strip.php\
        Structures_Graph-1.0.4.tgz XML_Util-1.2.1.tgz  ${RPMDIR}/SOURCES/
    
    \cp -rf ${specFileFull}  ${RPMDIR}/SPECS

    rpmbuild -ba ${RPMDIR}/SPECS/${specFile}  
}


function help(){
    echo "help:buid.sh [target:={apache | mysql | php | php-pear | apr | apr-util | distcache | libmcrypt}]"
}


if [ "x$1" = "x" ]; then
    help
    exit 1;
fi

if [ "$1" = "apache" ]; then
    echo "build apache"
    build_httpd 
elif [ "$1" = "mysql" ]; then
    echo "build mysql"
    build_mysql
elif [ "$1" = "php" ]; then
    echo "build php"
    #build_php
    build_php_54
elif [ "$1" = "php-pear" ]; then
    echo "build php-pear"
    build_php_pear
elif [ "$1" = "apr" ]; then
    echo "build apr"
    build_apr 
elif [ "$1" = "apr-util" ]; then
    echo "build apr-util"
    build_apr_util 
elif [ "$1" = "distcache" ]; then
    echo "build distcache"
    build_distcache 
elif [ "$1" = "libmcrypt" ]; then
    echo "build libmcrypt"
    build_libmcrypt                 
else
    help
    exit 1
fi