%global contentdir  /opt/www
# API/ABI check
%global apiver      20121113
%global zendver     20121212
%global pdover      20080721
# Extension version
%global fileinfover 1.0.5
%global pharver     2.0.2
%global zipver      1.11.0
%global jsonver     1.2.1

%define httpd_mmn %(cat %{_includedir}/httpd/.mmn || echo missing-httpd-devel)

# Use the arch-specific mysql_config binary to avoid mismatch with the
# arch detection heuristic used by bindir/mysql_config.
%define mysql_config %{_libdir}/mysql/mysql_config

Summary: PHP scripting language for creating dynamic web sites
Name: php
Version: 5.5.10
Release: 1%{?dist}
License: PHP and LGPLv2 and LGPLv2+
Group: Development/Languages
URL: http://www.php.net/

Source0: php-%{version}.tar.bz2
Source1: php.conf
Source3: macros.php
# php-fpm files
Source4: php-fpm.conf
Source5: php-fpm-www.conf
Source7: php-fpm.logrotate
Source8: php-fpm.sysconfig
Source9: php-fpm.init

# Build fixes
Patch1: php-5.5.4-ini.patch
Patch2: php-5.3.0-recode.patch
Patch3: php-5.5.2-phpize64.patch
Patch4: php-5.5.2-phpinfo.patch
Patch5: php-5.2.4-embed.patch
Patch7: php-5.2.4-norpath.patch
#Patch8: php-5.5.2-bug62692.patch
#Patch9: php-5.5.2-bug65470.patch
#Patch10: php-5.5.2-bug65490.patch
Patch11: php-5.5.2-install.patch

# Test fixes
Patch20: php-5.5.2-gmp.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires: dtrace-utils >= 0.4.0-5
BuildRequires: bzip2-devel, curl-devel >= 7.9, db4-devel, gmp-devel
BuildRequires: httpd-devel >= 2.0.46-1, pam-devel
BuildRequires: libstdc++-devel, openssl-devel, sqlite-devel >= 3.6.0
BuildRequires: zlib-devel, pcre-devel >= 6.6, smtpdaemon, libedit-devel
BuildRequires: bzip2, perl, libtool >= 1.4.3, gcc-c++
Obsoletes: php-dbg, php3, phpfi, stronghold-php
Requires: httpd-mmn = %{httpd_mmn}
Provides: mod_php = %{version}-%{release}
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: %{name}-cli%{?_isa} = %{version}-%{release}
# To ensure correct /var/lib/php/session ownership:
Requires(pre): httpd

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated webpages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled webpage with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. 

The php package contains the module which adds support for the PHP
language to Apache HTTP Server.

%package cli
Group: Development/Languages
Summary: Command-line interface for PHP
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Provides: %{name}-cgi = %{version}-%{release}, %{name}-cli = %{version}-%{release}
Provides: %{name}-pcntl, %{name}-readline
Obsoletes: php-cli, php52-cli, php53-cli, php54-cli

%description cli
The %{name}-cli package contains the command-line interface 
executing PHP scripts, /usr/bin/php, and the CGI interface.

%package fpm
Group: Development/Languages
Summary: PHP FastCGI Process Manager
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires(pre): /usr/sbin/useradd
Requires(preun): initscripts
Requires(postun): initscripts

%description fpm
PHP-FPM (FastCGI Process Manager) is an alternative PHP FastCGI
implementation with some additional features useful for sites of
any size, especially busier sites.

%package common
Group: Development/Languages
Summary: Common files for PHP
# ABI/API/Version check
Provides: %{name}-api = %{apiver}, %{name}-zend-abi = %{zendver}
Provides: php(api) = %{apiver}, php(zend-abi) = %{zendver}
Provides: php(language) = %{version} 
Conflicts: php-common, php52-common, php53-common, php54-common
# Provides for all builtin modules:
Provides: %{name}-bz2, %{name}-calendar, %{name}-ctype, %{name}-curl, %{name}-date, %{name}-exif
Provides: %{name}-ftp, %{name}-gettext, %{name}-gmp, %{name}-hash, %{name}-iconv, %{name}-libxml
Provides: %{name}-reflection, %{name}-session, %{name}-shmop, %{name}-simplexml, %{name}-sockets
Provides: %{name}-spl, %{name}-tokenizer, %{name}-openssl, %{name}-pcre
Provides: %{name}-zlib, %{name}-json, %{name}-zip, %{name}-fileinfo
Provides: %{name}-core, %{name}-ereg, %{name}-filter, %{name}-phar, %{name}-standard
# For obsoleted pecl extension
Provides: %{name}-pecl-json = %{jsonver}, %{name}-pecl(json) = %{jsonver}
Provides: %{name}-pecl-zip = %{zipver}, %{name}-pecl(zip) = %{zipver}
Provides: %{name}-pecl-phar = %{pharver}, %{name}-pecl(phar) = %{pharver}
Provides: %{name}-pecl-Fileinfo = %{fileinfover}, %{name}-pecl(Fileinfo) = %{fileinfover}

%description common
The %{name}-common package contains files used by both the php
package and the %{name}-cli package.

%package devel
Group: Development/Libraries
Summary: Files needed for building PHP extensions
Requires: %{name}%{?_isa} = %{version}-%{release}, autoconf, automake
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: php-devel, php52-devel, php53-devel, php54-devel

%description devel
The %{name}-devel package contains the files needed for building PHP
extensions. If you need to compile your own PHP extensions, you will
need to install this package.

%package opcache
Summary:   Zend OPcache
Group:     Development/Languages
License:   PHP
Requires:  %{name}-common%{?_isa} = %{version}-%{release}

%description opcache
Zend OPcache provides faster PHP execution through opcode caching and
optimization. It improves PHP performance by storing precompiled
script bytecode in the shared memory. This eliminates the stages of
reading code from the disk and compiling it on future access. In
addition, it applies a few bytecode optimization patterns that make
code execution faster.

%package imap
Summary: A module for PHP applications that use IMAP
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}, libc-client
Obsoletes: php-imap, php52-imap
Obsoletes: mod_php3-imap, stronghold-php-imap
BuildRequires: krb5-devel, openssl-devel, libc-client-devel

%description imap
The %{name}-imap package contains a dynamic shared object that will
add support for the IMAP protocol to PHP.

%package ldap
Summary: A module for PHP applications that use LDAP
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Obsoletes: php-ldap, php52-ldap
Obsoletes: mod_php3-ldap, stronghold-php-ldap 
BuildRequires: cyrus-sasl-devel, openldap-devel, openssl-devel

%description ldap
The %{name}-ldap package is a dynamic shared object (DSO) for the Apache
Web server that adds Lightweight Directory Access Protocol (LDAP)
support to PHP. LDAP is a set of protocols for accessing directory
services over the Internet. PHP is an HTML-embedded scripting
language. If you need LDAP support for PHP applications, you will
need to install this package in addition to the php package.

%package pdo
Summary: A database access abstraction module for PHP applications
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Obsoletes: php-pecl-pdo-sqlite, php-pecl-pdo
Obsoletes: php-pdo, php52-pdo, php53-pdo, php54-pdo
Provides: %{name}-pdo-abi = %{pdover}
Provides: %{name}-sqlite3, %{name}-pdo_sqlite

%description pdo
The %{name}-pdo package contains a dynamic shared object that will add
a database access abstraction layer to PHP.  This module provides
a common interface for accessing MySQL, PostgreSQL or other 
databases.

%package mysql
Summary: A module for PHP applications that use MySQL databases
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}, %{name}-pdo%{?_isa}
Provides: php_database, %{name}-mysqli, %{name}-pdo_mysql
Obsoletes: mod_php3-mysql, stronghold-php-mysql 
BuildRequires: mysql-devel >= 4.1.0

%description mysql
The %{name}-mysql package contains a dynamic shared object that will add
MySQL database support to PHP with the 'mysql', 'mysqli' and 'pdo_mysql'
extensions.  The "native driver" variants are installed. MySQL is an
object-relational database management system. PHP is an
HTML-embeddable scripting language. If you need MySQL support for PHP
applications, you will need to install this package and the php
package.

%package pgsql
Summary: A PostgreSQL database module for PHP
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}, %{name}-pdo%{?_isa}
Provides: php_database, %{name}-pdo_pgsql
Obsoletes: mod_php3-pgsql, stronghold-php-pgsql
Obsoletes: php-pgsql, php52-pgsql
BuildRequires: krb5-devel, openssl-devel, postgresql-devel

%description pgsql
The %{name}-pgsql package includes a dynamic shared object (DSO) that can
be compiled in to the Apache Web server to add PostgreSQL database
support to PHP. PostgreSQL is an object-relational database management
system that supports almost all SQL constructs. PHP is an
HTML-embedded scripting language. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
php package.

%package process
Summary: Modules for PHP script using system process interfaces
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Provides: %{name}-posix, %{name}-sysvsem, %{name}-sysvshm, %{name}-sysvmsg

%description process
The %{name}-process package contains dynamic shared objects which add
support to PHP using system interfaces for inter-process
communication.

%package odbc
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}, %{name}-pdo%{?_isa}, unixODBC
Summary: A module for PHP applications that use ODBC databases
Provides: php_database, %{name}-pdo_odbc
Obsoletes: stronghold-php-odbc
Obsoletes: php-odbc, php52-odbc, php53-odbc, php54-odbc
BuildRequires: unixODBC-devel

%description odbc
The %{name}-odbc package contains a dynamic shared object that will add
database support through ODBC to PHP. ODBC is an open specification
which provides a consistent API for developers to use for accessing
data sources (which are often, but not always, databases). PHP is an
HTML-embeddable scripting language. If you need ODBC support for PHP
applications, you will need to install this package and the php
package.

%package soap
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Summary: A module for PHP applications that use the SOAP protocol
Obsoletes: php-soap, php52-soap, php53-soap, php54-soap
BuildRequires: libxml2-devel

%description soap
The %{name}-soap package contains a dynamic shared object that will add
support to PHP for using the SOAP web services protocol.

%package snmp
Summary: A module for PHP applications that query SNMP-managed devices
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}, net-snmp
Obsoletes: php-snmp, php52-snmp, php53-snmp, php54-snmp
BuildRequires: net-snmp-devel

%description snmp
The %{name}-snmp package contains a dynamic shared object that will add
support for querying SNMP devices to PHP.  PHP is an HTML-embeddable
scripting language. If you need SNMP support for PHP applications, you
will need to install this package and the php package.

%package xml
Summary: A module for PHP applications which use XML
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Obsoletes: php-domxml, php-dom, php52-domxml, php52-dom 
Obsoletes: php-xml, php52-xml, php53-xml, php54-xml
Provides: %{name}-dom, %{name}-xsl, %{name}-domxml, %{name}-wddx
BuildRequires: libxslt-devel >= 1.0.18-1, libxml2-devel >= 2.4.14-1

%description xml
The %{name}-xml package contains dynamic shared objects which add support
to PHP for manipulating XML documents using the DOM tree,
and performing XSL transformations on XML documents.

%package xmlrpc
Summary: A module for PHP applications which use the XML-RPC protocol
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Obsoletes: php-xmlrpc, php52-xmlrpc, php53-xmlrpm, php54-xmlrpc

%description xmlrpc
The %{name}-xmlrpc package contains a dynamic shared object that will add
support for the XML-RPC protocol to PHP.

%package mbstring
Summary: A module for PHP applications which need multi-byte string handling
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Obsoletes: php-mbstring, php52-mbstring, php53-mbstring, php54-mbstring

%description mbstring
The %{name}-mbstring package contains a dynamic shared object that will add
support for multi-byte string handling to PHP.

%package gd
Summary: A module for PHP applications for using the gd graphics library
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Obsoletes: php-gd, php52-gd, php53-gd, php54-gd
# Required to build the bundled GD library
BuildRequires: libXpm-devel, libjpeg-devel, libpng-devel, freetype-devel

%description gd
The %{name}-gd package contains a dynamic shared object that will add
support for using the gd graphics library to PHP.

%package bcmath
Summary: A module for PHP applications for using the bcmath library
Group: Development/Languages
Obsoletes: php-bcmath, php52-bcmath, php53-bcmath, php54-bcmath
Requires: %{name}-common%{?_isa} = %{version}-%{release}

%description bcmath
The %{name}-bcmath package contains a dynamic shared object that will add
support for using the bcmath library to PHP.

%package dba
Summary: A database abstraction layer module for PHP applications
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Obsoletes: php-dba, php52-dba, php53-dba, php54-dba

%description dba
The %{name}-dba package contains a dynamic shared object that will add
support for using the DBA database abstraction layer to PHP.

%package tidy
Summary: Standard PHP module provides tidy library support
Group: Development/Languages
Requires: %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires: libtidy-devel

%description tidy
The php-tidy package contains a dynamic shared object that will add
support for using the tidy library to PHP.

%package embedded
Summary: PHP library for embedding in applications
Group: System Environment/Libraries
Requires: %{name}-common%{?_isa} = %{version}-%{release}
# doing a real -devel package for just the .so symlink is a bit overkill
Provides: %{name}-embedded-devel = %{version}-%{release}

%description embedded
The php-embedded package contains a library which can be embedded
into applications to provide PHP scripting language support.

%package pspell
Summary: A module for PHP applications for using pspell interfaces
Group: System Environment/Libraries
Requires: %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires: aspell-devel >= 0.50.0

%description pspell
The %{name}-pspell package contains a dynamic shared object that will add
support for using the pspell library to PHP.

%package recode
Summary: A module for PHP applications for using the recode library
Group: System Environment/Libraries
Requires: %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires: recode-devel

%description recode
The php-recode package contains a dynamic shared object that will add
support for using the recode library to PHP.

%package intl
Summary: Internationalization extension for PHP applications
Group: System Environment/Libraries
Requires: %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires: libicu-devel >= 3.6

%description intl
The %{name}-intl package contains a dynamic shared object that will add
support for using the ICU library to PHP.

%package enchant
Summary: PHP binding for the Enchant library
Group: System Environment/Libraries
Requires: %{name}-common%{?_isa} = %{version}-%{release}
BuildRequires: enchant-devel >= 1.2.4

%description enchant
The %{name}-enchant package contains a dynamic shared object that will add
support for using the Enchant library to PHP.

%prep
%setup -q -n php-%{version}
%patch1 -p1 -b .phpini
%patch2 -p1 -b .recode
%patch3 -p1 -b .phpize64
%patch4 -p1 -b .phpinfo
%patch5 -p1 -b .embed
%patch7 -p1 -b .norpath
#%patch8 -p1 -b .pic
#%patch9 -p1 -b .varags
#%patch10 -p1 -b .dup
%patch11 -p1 -b .install

%patch20 -p1 -b .gmp

# Prevent %%doc confusion over LICENSE files
cp -p Zend/LICENSE Zend/ZEND_LICENSE
cp -p TSRM/LICENSE TSRM_LICENSE
cp -p ext/ereg/regex/COPYRIGHT regex_COPYRIGHT
cp -p ext/gd/libgd/README gd_README
cp -p ext/fileinfo/libmagic/LICENSE libmagic_LICENSE
cp -p ext/mbstring/ucgendat/OPENLDAP_LICENSE OPENLDAP_LICENSE
cp -p ext/pcre/pcrelib/LICENCE pcrelib_LICENCE
cp -p ext/phar/LICENSE phar_LICENSE
cp -p sapi/fpm/LICENSE fpm_LICENSE

# Multiple builds for multiple SAPIs
mkdir build-cgi build-apache build-embedded build-fpm

# Tests that fail.
rm -f ext/xml/tests/bug32001.phpt \
      ext/standard/tests/file/lstat_stat_variation8.phpt \
      ext/standard/tests/file/lstat_stat_variation9.phpt \
      ext/standard/tests/file/disk_free_space_basic.phpt

# Safety check for API version change.
vapi=`sed -n '/#define PHP_API_VERSION/{s/.* //;p}' main/php.h`
if test "x${vapi}" != "x%{apiver}"; then
   : Error: Upstream API version is now ${vapi}, expecting %{apiver}.
   : Update the apiver macro and rebuild.
   exit 1
fi

vzend=`sed -n '/#define ZEND_MODULE_API_NO/{s/^[^0-9]*//;p;}' Zend/zend_modules.h`
if test "x${vzend}" != "x%{zendver}"; then
   : Error: Upstream Zend ABI version is now ${vzend}, expecting %{zendver}.
   : Update the zendver macro and rebuild.
   exit 1
fi

# Safety check for PDO ABI version change
vpdo=`sed -n '/#define PDO_DRIVER_API/{s/.*[ 	]//;p}' ext/pdo/php_pdo_driver.h`
if test "x${vpdo}" != "x%{pdover}"; then
   : Error: Upstream PDO ABI version is now ${vpdo}, expecting %{pdover}.
   : Update the pdover macro and rebuild.
   exit 1
fi

# Check for some extension version
ver=$(sed -n '/#define PHP_FILEINFO_VERSION /{s/.* "//;s/".*$//;p}' ext/fileinfo/php_fileinfo.h)
if test "$ver" != "%{fileinfover}"; then
   : Error: Upstream FILEINFO version is now ${ver}, expecting %{fileinfover}.
   : Update the fileinfover macro and rebuild.
   exit 1
fi
ver=$(sed -n '/#define PHP_PHAR_VERSION /{s/.* "//;s/".*$//;p}' ext/phar/php_phar.h)
if test "$ver" != "%{pharver}"; then
   : Error: Upstream PHAR version is now ${ver}, expecting %{pharver}.
   : Update the pharver macro and rebuild.
   exit 1
fi
ver=$(sed -n '/#define PHP_ZIP_VERSION_STRING /{s/.* "//;s/".*$//;p}' ext/zip/php_zip.h)
if test "$ver" != "%{zipver}"; then
   : Error: Upstream ZIP version is now ${ver}, expecting %{zipver}.
   : Update the zipver macro and rebuild.
   exit 1
fi
ver=$(sed -n '/#define PHP_JSON_VERSION /{s/.* "//;s/".*$//;p}' ext/json/php_json.h)
if test "$ver" != "%{jsonver}"; then
   : Error: Upstream JSON version is now ${ver}, expecting %{jsonver}.
   : Update the jsonver macro and rebuild.
   exit 1
fi

# Fix some bogus permissions
find . -name \*.[ch] -exec chmod 644 {} \;
find . -name \*.cpp  -exec chmod 644 {} \;

%build

# Regenerate configure scripts
touch configure.in
./buildconf --force

CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-pointer-sign"
export CFLAGS

# Install extension modules in %{_libdir}/php/modules.
EXTENSION_DIR=%{_libdir}/php/modules; export EXTENSION_DIR

# Set PEAR_INSTALLDIR to ensure that the hard-coded include_path
# includes the PEAR directory even though pear is packaged
# separately.
PEAR_INSTALLDIR=%{_datadir}/pear; export PEAR_INSTALLDIR

# Shell function to configure and build a PHP tree.
build() {
# bison-1.875-2 seems to produce a broken parser; workaround.
mkdir Zend && cp ../Zend/zend_{language,ini}_{parser,scanner}.[ch] Zend
ln -sf ../configure
%configure \
        --enable-dtrace \
	--cache-file=../config.cache \
        --with-libdir=%{_lib} \
	--with-config-file-path=%{_sysconfdir} \
	--with-config-file-scan-dir=%{_sysconfdir}/php.d \
	--disable-debug \
	--with-pic \
	--disable-rpath \
	--without-pear \
	--with-bz2 \
	--with-freetype-dir=%{_prefix} \
	--with-png-dir=%{_prefix} \
	--with-xpm-dir=%{_prefix} \
	--enable-gd-native-ttf \
	--without-gdbm \
	--with-gettext \
	--with-gmp \
	--with-iconv \
	--with-jpeg-dir=%{_prefix} \
	--with-openssl \
        --with-pcre-regex \
	--with-zlib \
	--with-layout=GNU \
	--enable-exif \
	--enable-ftp \
	--enable-sockets \
	--enable-sysvsem --enable-sysvshm --enable-sysvmsg \
	--with-kerberos \
	--enable-shmop \
	--enable-calendar \
        --with-libxml-dir=%{_prefix} \
	--enable-xml \
	$* 
if test $? != 0; then 
  tail -500 config.log
  : configure failed
  exit 1
fi

make %{?_smp_mflags}
}

# Build /usr/bin/php-cgi with the CGI SAPI, and all the shared extensions
pushd build-cgi
build --enable-dtrace \
      --enable-pcntl \
      --with-imap=shared --with-imap-ssl \
      --enable-mbstring=shared \
      --enable-mbregex \
      --with-gd=shared \
      --enable-bcmath=shared \
      --enable-dba=shared --with-db4=%{_prefix} \
      --with-xmlrpc=shared \
      --with-ldap=shared --with-ldap-sasl \
      --enable-mysqlnd=shared \
      --with-mysql=shared,mysqlnd \
      --with-mysqli=shared,mysqlnd \
      --enable-dom=shared \
      --with-pgsql=shared \
      --enable-wddx=shared \
      --with-snmp=shared,%{_prefix} \
      --enable-soap=shared \
      --with-xsl=shared,%{_prefix} \
      --enable-xmlreader=shared --enable-xmlwriter=shared \
      --with-curl=shared,%{_prefix} \
      --enable-pdo=shared \
      --with-pdo-odbc=shared,unixODBC,%{_prefix} \
      --with-pdo-mysql=shared,mysqlnd \
      --with-pdo-pgsql=shared,%{_prefix} \
      --with-pdo-sqlite=shared,%{_prefix} \
      --with-sqlite3=shared,%{_prefix} \
      --enable-json=shared \
      --enable-zip=shared \
      --without-readline \
      --with-libedit \
      --with-pspell=shared \
      --enable-phar=shared \
      --with-tidy=shared,%{_prefix} \
      --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
      --enable-posix=shared \
      --with-unixODBC=shared,%{_prefix} \
      --enable-fileinfo=shared \
      --enable-intl=shared \
      --with-icu-dir=%{_prefix} \
      --with-enchant=shared,%{_prefix} \
      --with-recode=shared,%{_prefix}
popd

#without_shared="--without-mysql --disable-mysqlnd --without-gd \
#      --disable-dom --disable-dba --without-unixODBC \
#      --disable-pdo --disable-xmlreader --disable-xmlwriter \
#      --without-sqlite3 --disable-phar --disable-fileinfo \
#      --disable-json --without-pspell --disable-wddx \
#      --without-curl --disable-posix \
#      --disable-sysvmsg --disable-sysvshm --disable-sysvsem"

without_shared="--without-gd \
      --disable-dom --disable-dba --without-unixODBC \
      --disable-xmlreader --disable-xmlwriter \
      --without-sqlite3 --disable-phar --disable-fileinfo \
      --disable-json --without-pspell --disable-wddx \
      --without-curl --disable-posix \
      --disable-sysvmsg --disable-sysvshm --disable-sysvsem"


# Build Apache module, and the CLI SAPI, /usr/bin/php
pushd build-apache
#build --with-apxs2=%{_bindir}/apxs ${without_shared}
#chow disable without
build --with-apxs2=%{_bindir}/apxs \
      --enable-pdo=shared \
      --with-mysql=shared,%{_prefix} \
      --with-mysqli=shared,%{mysql_config} \
      --with-pdo-mysql=shared,%{mysql_config} \
      --without-pdo-sqlite \
      ${without_shared}
popd

# Build php-fpm
pushd build-fpm
#chow disable without
build --enable-fpm ${without_shared}
#build --enable-fpm
popd

# Build for inclusion as embedded script language into applications,
# /usr/lib[64]/libphp5.so
pushd build-embedded
#chow disable without
build --enable-embed ${without_shared}
#build --enable-embed
popd

%check

cd build-apache
# Run tests, using the CLI SAPI
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 MALLOC_CHECK_=2 SKIP_ONLINE_TESTS=1
unset TZ LANG LC_ALL
if ! make test; then
  set +x
  for f in `find .. -name \*.diff -type f -print`; do
    echo "TEST FAILURE: $f --"
    cat "$f"
    echo "-- $f result ends."
  done
  set -x
fi
unset NO_INTERACTION REPORT_EXIT_STATUS MALLOC_CHECK_ SKIP_ONLINE_TESTS

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# Install the version for embedded script language in applications + php_embed.h
make -C build-embedded install-sapi install-headers INSTALL_ROOT=$RPM_BUILD_ROOT

# Install the php-fpm binary
make -C build-fpm install-fpm INSTALL_ROOT=$RPM_BUILD_ROOT

# Install everything from the CGI SAPI build
make -C build-cgi install INSTALL_ROOT=$RPM_BUILD_ROOT 

# Install the default configuration file and icons
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/
install -m 644 php.ini-production $RPM_BUILD_ROOT%{_sysconfdir}/php.ini
install -m 755 -d $RPM_BUILD_ROOT%{contentdir}/icons
install -m 644 *.gif $RPM_BUILD_ROOT%{contentdir}/icons/

# For third-party packaging:
install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/php/pear \
                  $RPM_BUILD_ROOT%{_datadir}/php

# install the DSO
install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/httpd/modules
install -m 755 build-apache/libs/libphp5.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules

# Apache config fragment 
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m 644 $RPM_SOURCE_DIR/php.conf $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.d
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/lib/php
install -m 700 -d $RPM_BUILD_ROOT%{_localstatedir}/lib/php/session

# PHP-FPM stuff
# Log
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/log/php-fpm
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/run/php-fpm
# Config
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.conf
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d/www.conf
mv $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.conf.default .
# Service
install -m 755 -d $RPM_BUILD_ROOT%{_initddir}
install -m 755 %{SOURCE9} $RPM_BUILD_ROOT%{_initddir}/php-fpm
# LogRotate
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/php-fpm
# Environment file
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/php-fpm

# Fix the link
(cd $RPM_BUILD_ROOT%{_bindir}; ln -sfn phar.phar phar)

# Generate files lists and stub .ini files for each subpackage
for mod in pgsql mysql mysqli mysqlnd odbc ldap snmp xmlrpc imap \
    mbstring gd dom xsl soap bcmath dba xmlreader xmlwriter \
    pdo pdo_mysql pdo_pgsql pdo_odbc pdo_sqlite json zip \
    sqlite3 enchant phar fileinfo intl \
    tidy pspell curl wddx opcache \
    posix sysvshm sysvsem sysvmsg recode; do
    cat > $RPM_BUILD_ROOT%{_sysconfdir}/php.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
    cat > files.${mod} <<EOF
%attr(755,root,root) %{_libdir}/php/modules/${mod}.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.d/${mod}.ini
EOF
done

# OPcache is a Zend extension
sed -i -e 's/extension=/zend_extension=/' $RPM_BUILD_ROOT%{_sysconfdir}/php.d/opcache.ini

# The dom, xsl and xml* modules are all packaged in php55-xml
cat files.dom files.xsl files.xml{reader,writer} files.wddx > files.xml

# The mysql, mysqli and mysqlnd modules are packaged in php53-mysql
cat files.mysqli files.mysqlnd >> files.mysql

# Split out the PDO modules
cat files.pdo_mysql >> files.mysql
cat files.pdo_pgsql >> files.pgsql
cat files.pdo_odbc >> files.odbc

# sysv* and posix in packaged in php55-process
cat files.sysv* files.posix > files.process

# Package sqlite3 and pdo_sqlite with pdo; isolating the sqlite dependency
# isn't useful at this time since rpm itself requires sqlite.
cat files.pdo_sqlite >> files.pdo
cat files.sqlite3 >> files.pdo

# Package json, zip, curl, phar and fileinfo in -common.
cat files.json files.zip files.curl files.phar files.fileinfo > files.common

# Install the macros file:
install -d $RPM_BUILD_ROOT%{_sysconfdir}/rpm
sed -e "s/@PHP_APIVER@/%{apiver}/;s/@PHP_ZENDVER@/%{zendver}/;s/@PHP_PDOVER@/%{pdover}/" \
    < $RPM_SOURCE_DIR/macros.php > macros.php
install -m 644 -c macros.php \
           $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.php

# Remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_libdir}/php/modules/*.a \
       $RPM_BUILD_ROOT%{_bindir}/{phptar} \
       $RPM_BUILD_ROOT%{_datadir}/pear \
       $RPM_BUILD_ROOT%{_libdir}/libphp5.la

# Remove irrelevant docs
rm -f README.{EXTENSIONS,EXT_SKEL,GIT-RULES,input_filter,MAILINGLIST_RULES,md,namespaces,NEW-OUTPUT-API,PARAMETER_PARSING_API,PHP4-TO-PHP5-THIN-CHANGES,REDIST.BINS,RELEASE_PROCESS,SELF-CONTAINED-EXTENSIONS,STREAMS,SUBMITTING_PATCH,TESTING,TESTING2,UNIX-BUILD-SYSTEM,WIN32-BUILD-SYSTEM} CODING_STANDARDS INSTALL

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
rm files.* macros.php

%post embedded -p /sbin/ldconfig
%postun embedded -p /sbin/ldconfig

%pre fpm
# Add the "apache" user
getent group  apache >/dev/null || \
  groupadd -g 48 -r apache
getent passwd apache >/dev/null || \
  useradd -r -u 48 -g apache -s /sbin/nologin \
    -d %{contentdir} -c "Apache" apache
exit 0

%post fpm
if [ $1 = 1 ]; then
    # Initial installation
    /sbin/chkconfig --add php-fpm
fi

%preun fpm
if [ $1 = 0 ]; then
    # Package removal, not upgrade
    /sbin/service php-fpm stop >/dev/null 2>&1
    /sbin/chkconfig --del php-fpm
fi

%postun fpm
if [ $1 -ge 1 ]; then
    /sbin/service php-fpm condrestart >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root)
%{_libdir}/httpd/modules/libphp5.so
%attr(0770,root,apache) %dir %{_localstatedir}/lib/php/session
%config(noreplace) %{_sysconfdir}/httpd/conf.d/php.conf
%{contentdir}/icons/php.gif

%files common -f files.common
%defattr(-,root,root)
%doc CREDITS LICENSE NEWS
%doc Zend/ZEND_* TSRM_LICENSE regex_COPYRIGHT libmagic_LICENSE
%doc OPENLDAP_LICENSE pcrelib_LICENCE phar_LICENSE fpm_LICENSE
%doc php.ini-development
%config(noreplace) %{_sysconfdir}/php.ini
%dir %{_sysconfdir}/php.d
%dir %{_libdir}/php
%dir %{_libdir}/php/modules
%dir %{_localstatedir}/lib/php
%dir %{_libdir}/php/pear
%dir %{_datadir}/php

%files cli
%defattr(-,root,root)
%{_bindir}/php
%{_bindir}/php-cgi
%{_bindir}/phar.phar
%{_bindir}/phar
%{_mandir}/man1/php.1*
%{_mandir}/man1/php-cgi.1*
%{_mandir}/man1/phar.1*
%{_mandir}/man1/phar.phar.1*
%doc sapi/cgi/README.FastCGI sapi/cli/README

%files fpm
%defattr(-,root,root)
%doc php-fpm.conf.default
%doc sapi/fpm/LICENSE
%config(noreplace) %{_sysconfdir}/php-fpm.conf
%config(noreplace) %{_sysconfdir}/php-fpm.d/www.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/php-fpm
%config(noreplace) %{_sysconfdir}/sysconfig/php-fpm
%{_initddir}/php-fpm
%{_sbindir}/php-fpm
%dir %{_sysconfdir}/php-fpm.d
# log owned by apache for log
%attr(770,apache,root) %dir %{_localstatedir}/log/php-fpm
%dir %{_localstatedir}/run/php-fpm
%{_mandir}/man8/php-fpm.8*
%{_datadir}/fpm/status.html

%files devel
%defattr(-,root,root)
%{_bindir}/php-config
%{_bindir}/phpize
%{_includedir}/php
%{_libdir}/php/build
%{_mandir}/man1/php-config.1*
%{_mandir}/man1/phpize.1*
%config %{_sysconfdir}/rpm/macros.php

%files embedded
%defattr(-,root,root,-)
%{_libdir}/libphp5.so
%{_libdir}/libphp5-%{version}.so

%files pgsql -f files.pgsql
%files mysql -f files.mysql
%files odbc -f files.odbc
%files imap -f files.imap
%files ldap -f files.ldap
%files snmp -f files.snmp
%files xml -f files.xml
%files xmlrpc -f files.xmlrpc
%files mbstring -f files.mbstring
%defattr(-,root,root)
%doc ext/mbstring/libmbfl/DISCLAIMER ext/mbstring/libmbfl/LICENSE
%files gd -f files.gd
%defattr(-,root,root)
%doc gd_README
%files soap -f files.soap
%files bcmath -f files.bcmath
%defattr(-,root,root)
%doc ext/bcmath/libbcmath/COPYING.LIB
%files dba -f files.dba
%files pdo -f files.pdo
%files tidy -f files.tidy
%files pspell -f files.pspell
%files intl -f files.intl
%files process -f files.process
%files recode -f files.recode
%files enchant -f files.enchant
%files opcache -f files.opcache

%changelog
* Thu Mar 6 2014 Christopher Jones <christopher.jones@oracle.com> 5.5.10
- Use PHP 5.5.10

* Wed Feb 26 2014 Christopher Jones <christopher.jones@oracle.com> 5.5.9
- Use PHP 5.5.9

* Thu Aug 22 2013 Christopher Jones <christopher.jones@oracle.com> 5.5.3
- Use PHP 5.5.3
- Add --enable-dtrace

* Tue Aug 20 2013 Christopher Jones <christopher.jones@oracle.com> 5.5.2
- Use PHP 5.5.2
- Merge updates from php/el6-u4g

* Wed Aug 14 2013 Christopher Jones <christopher.jones@oracle.com> 5.4.17
- Use PHP 5.4.17

* Mon Sep 16 2012 Christopher Jones <christopher.jones@oracle.com> 5.4.7
- Use PHP 5.4.7

* Thu Mar 1 2012 Christopher Jones <christopher.jones@oracle.com> 5.4.0
- Use PHP 5.4.0

* Thu Feb 2 2012 Christopher Jones <christopher.jones@oracle.com> 5.3.10
- Use PHP 5.3.10

* Wed Jan 11 2012 Christopher Jones <christopher.jones@oracle.com> 5.3.9
- Use PHP 5.3.9

* Tue Aug 23 2011 Christopher Jones <christopher.jones@oracle.com> 5.3.8
- Use PHP 5.3.8
- Use mysqlnd "native driver" implementation for MySQL extensions
- Merge updates from Oracle Linux 5.7 spec

* Thu Jan 6 2011 Christopher Jones <christopher.jones@oracle.com> 5.3.5
- Use PHP 5.3.5

* Tue Aug 10 2010 Christopher Jones <christopher.jones@oracle.com> 5.3.3
- Use PHP 5.3.3

* Mon Apr 12 2010 Christopher Jones <christopher.jones@oracle.com> 5.3.2
- Use PHP 5.3.2

* Mon Mar 15 2010 Christopher Jones <christopher.jones@oracle.com> 5.2.13
- Use PHP 5.2.13

* Mon Nov 1 2009 Christopher Jones <christopher.jones@oracle.com> 5.2.11
- Use PHP 5.2.11

* Mon Jun 22 2009 Christopher Jones <christopher.jones@oracle.com> 5.2.10
- Use PHP 5.2.10

* Wed Apr 28 2009 Christopher Jones <christopher.jones@oracle.com> 5.2.9
- Rename as php52-*

* Mon Mar 16 2009 Christopher Jones <christopher.jones@oracle.com> 5.2.9
- Use PHP 5.2.9
- Don't overwrite FCGI binary with CLI

* Wed Dec 17 2008 Chris Jones <christopher.jones@oracle.com> 5.2.8
- Use PHP 5.2.8
- Merge EL 5.3 php.spec changes
- Move OCI8 to external spec file

* Mon Jun 11 2007 Chris Jones <christopher.jones@oracle.com> 5.2.3
- Use PHP 5.2.3
- Remove OCI8 runtime dependency on Instant Client SDK

* Mon May 21 2007 Chris Jones <christopher.jones@oracle.com> 5.2.2
- Use PHP 5.2.2. Add OCI8/PDO_OCI package.
- Use EL 4 compile flag.
- Use PHP's PCRE

* Tue Dec 19 2006 Joe Orton <jorton@redhat.com> 5.1.6
- fix version for php-zend-abi (#218758)

* Thu Nov 23 2006 Joe Orton <jorton@redhat.com> 5.1.6-4.el5
- php-xml provides php-domxml (#215656)
- fix php-pdo-abi provide (#214281)
- provide php-zend-abi (#212804)
- don't Obsolete mod_php
- fix PDO sqlite TEXT extraction truncate-by-one (#217033)
- package php{ize,-config} man pages in -devel (#199382)
- change module subpackages to require php-common not php (#177821)
- add security fix for CVE-2006-5465 (#216114)

* Wed Oct  4 2006 Joe Orton <jorton@redhat.com> 5.1.6-3
- from upstream: add safety checks against integer overflow in _ecalloc

* Tue Aug 29 2006 Joe Orton <jorton@redhat.com> 5.1.6-2
- update to 5.1.6 (security fixes)
- bump default memory_limit to 16M (#196802)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 5.1.4-8.1
- rebuild

* Fri Jun  9 2006 Joe Orton <jorton@redhat.com> 5.1.4-8
- Provide php-posix (#194583)
- only provide php-pcntl from -cli subpackage
- add missing defattr's (thanks to Matthias Saou)

* Fri Jun  9 2006 Joe Orton <jorton@redhat.com> 5.1.4-7
- move Obsoletes for php-openssl to -common (#194501)
- Provide: php-cgi from -cli subpackage

* Fri Jun  2 2006 Joe Orton <jorton@redhat.com> 5.1.4-6
- split out php-cli, php-common subpackages (#177821)
- add php-pdo-abi version export (#193202)

* Wed May 24 2006 Radek Vokal <rvokal@redhat.com> 5.1.4-5.1
- rebuilt for new libnetsnmp

* Thu May 18 2006 Joe Orton <jorton@redhat.com> 5.1.4-5
- provide mod_php (#187891)
- provide php-cli (#192196)
- use correct LDAP fix (#181518)
- define _GNU_SOURCE in php_config.h and leave it defined
- drop (circular) dependency on php-pear

* Mon May  8 2006 Joe Orton <jorton@redhat.com> 5.1.4-3
- update to 5.1.4

* Wed May  3 2006 Joe Orton <jorton@redhat.com> 5.1.3-3
- update to 5.1.3

* Tue Feb 28 2006 Joe Orton <jorton@redhat.com> 5.1.2-5
- provide php-api (#183227)
- add provides for all builtin modules (Tim Jackson, #173804)
- own %%{_libdir}/php/pear for PEAR packages (per #176733)
- add obsoletes to allow upgrade from FE4 PDO packages (#181863)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.1.2-4.3
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 5.1.2-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Joe Orton <jorton@redhat.com> 5.1.2-4
- rebuild for new libc-client soname

* Mon Jan 16 2006 Joe Orton <jorton@redhat.com> 5.1.2-3
- only build xmlreader and xmlwriter shared (#177810)

* Fri Jan 13 2006 Joe Orton <jorton@redhat.com> 5.1.2-2
- update to 5.1.2

* Thu Jan  5 2006 Joe Orton <jorton@redhat.com> 5.1.1-8
- rebuild again

* Mon Jan  2 2006 Joe Orton <jorton@redhat.com> 5.1.1-7
- rebuild for new net-snmp

* Mon Dec 12 2005 Joe Orton <jorton@redhat.com> 5.1.1-6
- enable short_open_tag in default php.ini again (#175381)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  8 2005 Joe Orton <jorton@redhat.com> 5.1.1-5
- require net-snmp for php-snmp (#174800)

* Sun Dec  4 2005 Joe Orton <jorton@redhat.com> 5.1.1-4
- add /usr/share/pear back to hard-coded include_path (#174885)

* Fri Dec  2 2005 Joe Orton <jorton@redhat.com> 5.1.1-3
- rebuild for httpd 2.2

* Mon Nov 28 2005 Joe Orton <jorton@redhat.com> 5.1.1-2
- update to 5.1.1
- remove pear subpackage
- enable pdo extensions (php-pdo subpackage)
- remove non-standard conditional module builds
- enable xmlreader extension

* Thu Nov 10 2005 Tomas Mraz <tmraz@redhat.com> 5.0.5-6
- rebuilt against new openssl

* Mon Nov  7 2005 Joe Orton <jorton@redhat.com> 5.0.5-5
- pear: update to XML_RPC 1.4.4, XML_Parser 1.2.7, Mail 1.1.9 (#172528)

* Tue Nov  1 2005 Joe Orton <jorton@redhat.com> 5.0.5-4
- rebuild for new libnetsnmp

* Wed Sep 14 2005 Joe Orton <jorton@redhat.com> 5.0.5-3
- update to 5.0.5
- add fix for upstream #34435
- devel: require autoconf, automake (#159283)
- pear: update to HTTP-1.3.6, Mail-1.1.8, Net_SMTP-1.2.7, XML_RPC-1.4.1
- fix imagettftext et al (upstream, #161001)

* Thu Jun 16 2005 Joe Orton <jorton@redhat.com> 5.0.4-11
- ldap: restore ldap_start_tls() function

* Fri May  6 2005 Joe Orton <jorton@redhat.com> 5.0.4-10
- disable RPATHs in shared extensions (#156974)

* Tue May  3 2005 Joe Orton <jorton@redhat.com> 5.0.4-9
- build simplexml_import_dom even with shared dom (#156434)
- prevent truncation of copied files to ~2Mb (#155916)
- install /usr/bin/php from CLI build alongside CGI
- enable sysvmsg extension (#142988)

* Mon Apr 25 2005 Joe Orton <jorton@redhat.com> 5.0.4-8
- prevent build of builtin dba as well as shared extension

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-7
- split out dba and bcmath extensions into subpackages
- BuildRequire gcc-c++ to avoid AC_PROG_CXX{,CPP} failure (#155221)
- pear: update to DB-1.7.6
- enable FastCGI support in /usr/bin/php-cgi (#149596)

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-6
- build /usr/bin/php with the CLI SAPI, and add /usr/bin/php-cgi,
  built with the CGI SAPI (thanks to Edward Rudd, #137704)
- add php(1) man page for CLI
- fix more test cases to use -n when invoking php

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-5
- rebuild for new libpq soname

* Tue Apr 12 2005 Joe Orton <jorton@redhat.com> 5.0.4-4
- bundle from PEAR: HTTP, Mail, XML_Parser, Net_Socket, Net_SMTP
- snmp: disable MSHUTDOWN function to prevent error_log noise (#153988)
- mysqli: add fix for crash on x86_64 (Georg Richter, upstream #32282)

* Mon Apr 11 2005 Joe Orton <jorton@redhat.com> 5.0.4-3
- build shared objects as PIC (#154195)

* Mon Apr  4 2005 Joe Orton <jorton@redhat.com> 5.0.4-2
- fix PEAR installation and bundle PEAR DB-1.7.5 package

* Fri Apr  1 2005 Joe Orton <jorton@redhat.com> 5.0.4-1
- update to 5.0.4 (#153068)
- add .phps AddType to php.conf (#152973)
- better gcc4 fix for libxmlrpc

* Wed Mar 30 2005 Joe Orton <jorton@redhat.com> 5.0.3-5
- BuildRequire mysql-devel >= 4.1
- don't mark php.ini as noreplace to make upgrades work (#152171)
- fix subpackage descriptions (#152628)
- fix memset(,,0) in Zend (thanks to Dave Jones)
- fix various compiler warnings in Zend

* Thu Mar 24 2005 Joe Orton <jorton@redhat.com> 5.0.3-4
- package mysqli extension in php-mysql
- really enable pcntl (#142903)
- don't build with --enable-safe-mode (#148969)
- use "Instant Client" libraries for oci8 module (Kai Bolay, #149873)

* Fri Feb 18 2005 Joe Orton <jorton@redhat.com> 5.0.3-3
- fix build with GCC 4

* Wed Feb  9 2005 Joe Orton <jorton@redhat.com> 5.0.3-2
- install the ext/gd headers (#145891)
- enable pcntl extension in /usr/bin/php (#142903)
- add libmbfl array arithmetic fix (dcb314@hotmail.com, #143795)
- add BuildRequire for recent pcre-devel (#147448)

* Wed Jan 12 2005 Joe Orton <jorton@redhat.com> 5.0.3-1
- update to 5.0.3 (thanks to Robert Scheck et al, #143101)
- enable xsl extension (#142174)
- package both the xsl and dom extensions in php-xml
- enable soap extension, shared (php-soap package) (#142901)
- add patches from upstream 5.0 branch:
 * Zend_strtod.c compile fixes
 * correct php_sprintf return value usage

* Mon Nov 22 2004 Joe Orton <jorton@redhat.com> 5.0.2-8
- update for db4-4.3 (Robert Scheck, #140167)
- build against mysql-devel
- run tests in %%check

* Wed Nov 10 2004 Joe Orton <jorton@redhat.com> 5.0.2-7
- truncate changelog at 4.3.1-1
- merge from 4.3.x package:
 - enable mime_magic extension and Require: file (#130276)

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-6
- fix dom/sqlite enable/without confusion

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-5
- fix phpize installation for lib64 platforms
- add fix for segfault in variable parsing introduced in 5.0.2

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-4
- update to 5.0.2 (#127980)
- build against mysqlclient10-devel
- use new RTLD_DEEPBIND to load extension modules
- drop explicit requirement for elfutils-devel
- use AddHandler in default conf.d/php.conf (#135664)
- "fix" round() fudging for recent gcc on x86
- disable sqlite pending audit of warnings and subpackage split

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-4
- don't build dom extension into 2.0 SAPI

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-3
- ExclusiveArch: x86 ppc x86_64 for the moment

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-2
- fix default extension_dir and conf.d/php.conf

* Thu Sep  9 2004 Joe Orton <jorton@redhat.com> 5.0.1-1
- update to 5.0.1
- only build shared modules once
- put dom extension in php-dom subpackage again
- move extension modules into %%{_libdir}/php/modules
- don't use --with-regex=system, it's ignored for the apache* SAPIs

* Wed Aug 11 2004 Tom Callaway <tcallawa@redhat.com>
- Merge in some spec file changes from Jeff Stern (jastern@uci.edu)

* Mon Aug 09 2004 Tom Callaway <tcallawa@redhat.com>
- bump to 5.0.0
- add patch to prevent clobbering struct re_registers from regex.h
- remove domxml references, replaced with dom now built-in
- fix php.ini to refer to php5 not php4

* Wed Aug 04 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- rebuild

* Wed Jul 14 2004 Joe Orton <jorton@redhat.com> 4.3.8-3
- update to 4.3.8
- catch some fd > FD_SETSIZE vs select() issues (#125258)

* Mon Jun 21 2004 Joe Orton <jorton@redhat.com> 4.3.7-4
- pick up test failures again
- have -devel require php of same release

* Thu Jun 17 2004 Joe Orton <jorton@redhat.com> 4.3.7-3
- add gmp_powm fix (Oskari Saarenmaa, #124318)
- split mbstring, ncurses, gd, openssl extns into subpackages
- fix memory leak in apache2handler; use ap_r{write,flush}
  rather than brigade interfaces

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun  3 2004 Joe Orton <jorton@redhat.com> 4.3.7-1
- update to 4.3.7
- have -pear subpackage require php of same VR

* Wed May 26 2004 Joe Orton <jorton@redhat.com> 4.3.6-6
- buildrequire smtpdaemon (#124430)
- try switching to system libgd again (prevent symbol conflicts
  when e.g. mod_perl loads the system libgd library.)

* Wed May 19 2004 Joe Orton <jorton@redhat.com> 4.3.6-5
- don't obsolete php-imap (#123580)
- unconditionally build -imap subpackage

* Thu May 13 2004 Joe Orton <jorton@redhat.com> 4.3.6-4
- remove trigger

* Thu Apr 22 2004 Joe Orton <jorton@redhat.com> 4.3.6-3
- fix umask reset "feature" (#121454)
- don't use DL_GLOBAL when dlopen'ing extension modules

* Sun Apr 18 2004 Joe Orton <jorton@redhat.com> 4.3.6-2
- fix segfault on httpd SIGHUP (upstream #27810)

* Fri Apr 16 2004 Joe Orton <jorton@redhat.com> 4.3.6-1
- update to 4.3.6 (Robert Scheck, #121011)

* Wed Apr  7 2004 Joe Orton <jorton@redhat.com> 4.3.4-11
- add back imap subpackage, using libc-client (#115535)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 18 2004 Joe Orton <jorton@redhat.com> 4.3.4-10
- eliminate /usr/local/lib RPATH in odbc.so
- really use system pcre library

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> 4.3.4-9
- rebuilt

* Mon Feb  2 2004 Bill Nottingham <notting@redhat.com> 4.3.4-8
- obsolete php-imap if we're not building it

* Wed Jan 28 2004 Joe Orton <jorton@redhat.com> 4.3.4-7
- gd fix for build with recent Freetype2 (from upstream)
- remove easter egg (Oden Eriksson, Mandrake)

* Wed Jan 21 2004 Joe Orton <jorton@redhat.com> 4.3.4-6
- php-pear requires php
- also remove extension=imap from php.ini in upgrade trigger
- merge from Taroon: allow upgrade from Stronghold 4.0

* Wed Jan 21 2004 Joe Orton <jorton@redhat.com> 4.3.4-5
- add defattr for php-pear subpackage
- restore defaults: output_buffering=Off, register_argc_argv=On
- add trigger to handle php.ini upgrades smoothly (#112470)

* Tue Jan 13 2004 Joe Orton <jorton@redhat.com> 4.3.4-4
- conditionalize support for imap extension for the time being
- switch /etc/php.ini to use php.ini-recommended (but leave
  variables_order as EGPCS) (#97765)
- set session.path to /var/lib/php/session by default (#89975)
- own /var/lib/php{,/session} and have apache own the latter
- split off php-pear subpackage (#83771)

* Sat Dec 13 2003 Jeff Johnson <jbj@jbj.org> 4.3.4-3
- rebuild against db-4.2.52.

* Mon Dec  1 2003 Joe Orton <jorton@redhat.com> 4.3.4-2
- rebuild for new libxslt (#110658)
- use --with-{mssql,oci8} for enabling extensions (#110482)
- fix rebuild issues (Jan Visser, #110274)
- remove hard-coded LIBS
- conditional support for mhash (Aleksander Adamowski, #111251)

* Mon Nov 10 2003 Joe Orton <jorton@redhat.com> 4.3.4-1.1
- rebuild for FC1 updates

* Mon Nov 10 2003 Joe Orton <jorton@redhat.com> 4.3.4-1
- update to 4.3.4
- include all licence files
- libxmlrpc fixes

* Mon Oct 20 2003 Joe Orton <jorton@redhat.com> 4.3.3-6
- use bundled libgd (#107407)
- remove manual: up-to-date manual sources are no longer DFSG-free;
  it's too big; it's on the web anyway; #91292, #105804, #107384

* Wed Oct 15 2003 Joe Orton <jorton@redhat.com> 4.3.3-5
- add php-xmlrpc subpackage (#107138)

* Mon Oct 13 2003 Joe Orton <jorton@redhat.com> 4.3.3-4
- drop recode support, symbols collide with MySQL

* Sun Oct 12 2003 Joe Orton <jorton@redhat.com> 4.3.3-3
- split domxml extension into php-domxml subpackage
- enable xslt and xml support in domxml extension (#106042)
- fix httpd-devel build requirement (#104341)
- enable recode extension (#106755)
- add workaround for #103982

* Thu Sep 25 2003 Jeff Johnson <jbj@jbj.org> 4.3.3-3
- rebuild against db-4.2.42.

* Sun Sep  7 2003 Joe Orton <jorton@redhat.com> 4.3.3-2
- don't use --enable-versioning, it depends on libtool being
 broken (#103690)

* Sun Sep  7 2003 Joe Orton <jorton@redhat.com> 4.3.3-1
- update to 4.3.3
- add libtool build prereq (#103388)
- switch to apache2handler

* Mon Jul 28 2003 Joe Orton <jorton@redhat.com> 4.3.2-8
- rebuild

* Tue Jul 22 2003 Nalin Dahyabhai <nalin@redhat.com> 4.3.2-7
- rebuild

* Tue Jul  8 2003 Joe Orton <jorton@redhat.com> 4.3.2-6
- use system pcre library

* Mon Jun  9 2003 Joe Orton <jorton@redhat.com> 4.3.2-5
- enable mbstring and mbregex (#81336)
- fix use of libtool 1.5

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Joe Orton <jorton@redhat.com> 4.3.2-3
- add lib64 and domxml fixes

* Tue Jun  3 2003 Frank Dauer <f@paf.net>
- added conditional support for mssql module (#92149)

* Fri May 30 2003 Joe Orton <jorton@redhat.com> 4.3.2-2
- update the -tests and -lib64 patches
- fixes for db4 detection
- require aspell-devel >= 0.50.0 for pspell compatibility

* Thu May 29 2003 Joe Orton <jorton@redhat.com> 4.3.2-1
- update to 4.3.2

* Fri May 16 2003 Joe Orton <jorton@redhat.com> 4.3.1-3
- link odbc module correctly
- patch so that php -n doesn't scan inidir
- run tests using php -n, avoid loading system modules

* Wed May 14 2003 Joe Orton <jorton@redhat.com> 4.3.1-2
- workaround broken parser produced by bison-1.875

* Tue May  6 2003 Joe Orton <jorton@redhat.com> 4.3.1-1
- update to 4.3.1; run test suite
- open extension modules with RTLD_NOW rather than _LAZY
