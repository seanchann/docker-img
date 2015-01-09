#!/bin/bash

set -e

. /usr/sbin/rpm-repo-func.sh

repodir=/var/www/html/repolamp/centos/7/os/x86_64/Packages


#install our lamp package we use them for repo web server
#\cd /var/www/html/repolamp/centos/7/os/x86_64/Packages/ 
#yum install --disablerepo=\* -y mysql-community-client*.rpm mysql-community-libs*.rpm mysql-community-common*.rpm
#yum install httpd-*.rpm


__rpm_make_repo $repodir
mv /LAMP-Base.repo   /var/www/html/repolamp/LAMP-Base.repo
__rpm_run_httpd

