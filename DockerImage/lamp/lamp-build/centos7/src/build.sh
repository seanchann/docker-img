#/bin/bash

## build common service by source code


function help()
{
    echo "help:buid.sh [target:={apache | mysql | php | memcached | all}]  [workdir]\
    [needDecompress:={0:don't need decompress | 1: need decompress}]"
}

if [ "x$2" = "x" ]; then
    help
    exit;
fi


if [ "x$3" = "x" ]; then
    help
    exit;
fi

WORKDIR=$2
DECOMPRESSFLAG=$3



function build_pcre()
{
    #decompress packet
    \cd ${WORKDIR}
    if [ "$DECOMPRESSFLAG" = "1" ]; then
        # clean first
        \rm -rf ${WORKDIR}/pcre-8.36
        \tar -zxvf pcre-8.36.tar.gz
    fi
    
    #build pcre
    \cd  ${WORKDIR}/pcre-8.36
    make clean
    ./configure 
    make && make install
    
}


#depend on pcre .
function build_apache()
{   
    # do depend first
    build_pcre
    \yum -y install zlib-devel openssl-devel; yum clean all
    

    #decompress our packet
    \cd ${WORKDIR}
    if [ "$DECOMPRESSFLAG" = "1" ]; then
        #clean build env first
        \rm -rf ${WORKDIR}/httpd-2.4.10/
        \rm -rf ${WORKDIR}/apr-1.4.6/
        \rm -rf ${WORKDIR}/apr-util-1.5.2/
        
        \tar -zxvf httpd-2.4.10.tar.gz 
        \tar -zxvf apr-1.4.6.tar.gz 
        \tar -zxvf apr-util-1.5.2.tar.gz
    fi
    
    \mv ./apr-1.4.6 ./httpd-2.4.10/srclib/apr
    \mv ./apr-util-1.5.2  ./httpd-2.4.10/srclib/apr-util
    
    
    \mkdir /opt/www
    \mkdir -p /opt/apache_log/access_log

    #add apache user
    \mkdir -p /opt/apache/home/
    \groupadd apache
    \useradd -m -d /opt/apache/home/apache -g apache -s /sbin/nologin apache
    
    #build apache
    \cd ${WORKDIR}/httpd-2.4.10    
    make clean 
    ./configure --prefix=/opt/apache --enable-so  --enable-mods-shared=all   --enable-deflate=shared --enable-ssl=shared --enable-expires=shared --enable-headers=shared --enable-rewrite=shared --enable-static-support --with-included-apr --with-mpm=prefork --enable-cache --enable-file-cache --with-pcre=/opt/pcre --enable-ssl=static --enable-ssl
    make && make install
    
}


function build_mysql()
{       
    # do depend first
    \yum -y install ncurses-devel perl-Data-Dumper; yum clean all

    #decompress our packet
    \cd ${WORKDIR}
    if [ "$DECOMPRESSFLAG" = "1" ]; then
        #clean env first
        \rm -rf  ${WORKDIR}/mysql-5.6.17
        
        \tar -zxvf mysql-5.6.17.tar.gz
    fi
    
    
    #add mysql user 
    \groupadd mysql
    \useradd -g mysql -s /sbin/nologin -M mysql
    
    \cd ${WORKDIR}/mysql-5.6.17    
    \rm -rf 
    make clean 
    cmake -DCMAKE_INSTALL_PREFIX=/opt/mysql -DMYSQL_UNIX_ADDR=/opt/mysql/mysql.sock -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_ARCHIVE_STORAGE_ENGINE=1 -DWITH_BLACKHOLE_STORAGE_ENGINE=1 -DWITH_MEMORY_STORAGE_ENGINE=1 -DWITH_READLINE=1 -DENABLED_LOCAL_INFILE=1 -DMYSQL_DATADIR=/opt/mysql/data -DMYSQL_USER=mysql -DMYSQL_TCP_PORT=3306 -DEXTRA_CHARSETS=all   -DSYSCONFDIR=/opt/mysql        
    make && make install
    
    #init mysql
    cd /opt/mysql
    chown -R mysql.mysql /opt/mysql
    /opt/mysql/scripts/mysql_install_db --defaults-file=/opt/mysql/my.cnf --user=mysql --basedir=/opt/mysql  --datadir=/opt/mysql/data        
}



function build_mcrypt()
{
    #decompress our packet
    cd ${WORKDIR}
    if [ "$DECOMPRESSFLAG" = "1" ]; then
        #clean env first
        \rm -rf ${WORKDIR}/libmcrypt-2.5.8
        
        tar -zxvf libmcrypt-2.5.8.tar.gz
    fi
    
    #build mcrypt
    cd ${WORKDIR}/libmcrypt-2.5.8  
    ./configure
    make && make install
}

#depend mcrypt
function build_php()
{
    # do depend first
    build_mcrypt
    \yum -y install perl libxml2-devel bzip2 bzip2-devel libcurl-devel libjpeg-devel libpng-devel libXpm-devel freetype-devel; yum clean all

    #decompress our packet
    cd ${WORKDIR}
    if [ "$DECOMPRESSFLAG" = "1" ]; then
        #clean env first
        \rm -rf ${WORKDIR}/php-5.5.10
        
        tar -xvf php-5.5.10.tar
    fi
    
    
    #build php
    cd ${WORKDIR}/php-5.5.10
    ./configure --with-apxs2=/usr/bin/apxs  --with-mysql --with-mysqli --with-libxml-dir --with-config-file-path=/opt/apache/conf --with-gd --enable-gd-native-ttf --with-zlib --with-mcrypt --with-pdo-mysql= --enable-shmop --enable-soap --enable-sockets --enable-wddx --enable-zip --with-xmlrpc --enable-fpm --enable-mbstring --with-zlib-dir --with-bz2 --with-curl --enable-exif --enable-ftp --with-jpeg-dir  --with-png-dir --with-freetype-dir 
    make && make install
    
}



# build php memcache client 
function build_php_memcache()
{
    #decompress our packet
    cd ${WORKDIR}
    if [ "$DECOMPRESSFLAG" = "1" ]; then
        #clean env first
        \rm -rf ${WORKDIR}/memcache-2.2.7
        
        \tar -zxvf memcache-2.2.7.tgz
    fi
    
    cd ${WORKDIR}/memcache-2.2.7
    /opt/php/bin/phpize
    ./configure --enable-memcache --with-php-config=/opt/php/bin/php-config --with-zlib-dir
    make && make install
}


function build_libevent()
{
    #decompress our packet
    cd ${WORKDIR}
    if [ "$DECOMPRESSFLAG" = "1" ]; then
        #clean env first
        \rm -rf ${WORKDIR}/libevent-1.4.13-stable
        
        \tar -zxvf libevent-1.4.13-stable.tar.gz
    fi

    cd ${WORKDIR}/libevent-1.4.13-stable
    ./configure --prefix=/usr/lib64/
    make && make install
    ln -s /usr/lib64/lib/libevent-1.4.so.2  /usr/lib64/libevent-1.4.so.2
}


function buld_memcached()
{
    #do depend first
    build_php_memcache
    build_libevent

    #decompress our packet
    cd ${WORKDIR}
    if [ "$DECOMPRESSFLAG" = "1" ]; then
        #clean env first
        \rm -rf ${WORKDIR}/memcached-1.4.5
        
        \tar -zxvf memcached-1.4.5.tar.gz
    fi
    
    cd ${WORKDIR}/memcached-1.4.5
    ./configure  --prefix=/opt/memcached/ --with-libevent=/usr/lib64/
    make && make install
}




echo "build $1" 
if [ "$1" = "apache" ]; then
    build_apache
elif [ "$1" = "mysql" ]; then
    build_mysql
elif [ "$1" = "php" ]; then
    build_php
elif [ "$1" = "memcached" ]; then
    buld_memcached
elif [ "$1" = "all" ]; then
    build_apache
    build_mysql
    build_php
    buld_memcached 
else
    help
fi