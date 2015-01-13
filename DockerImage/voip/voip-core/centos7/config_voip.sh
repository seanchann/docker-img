#!/bin/bash
#make sure our voip server can run with docker volumes

set -e

__opensips_cp_config(){
    yum -y erase opensips-cp opensips-cp-* 
    rm -rf /var/www/html/opensips-cp
    yum --disablerepo=\* --enablerepo=VoIP-base -y install opensips-cp
}

__opensips_cp_config
