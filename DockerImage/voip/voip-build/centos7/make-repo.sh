#!/bin/bash

set -e

. /usr/sbin/rpm-repo-func.sh

repodir=/var/www/html/repovoip/centos/7/os/x86_64/Packages

__rpm_make_repo $repodir
cp -rf /VoIP-Base.repo   /var/www/html/repovoip/VoIP-Base.repo
__rpm_run_httpd

