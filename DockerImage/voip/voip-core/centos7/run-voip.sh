#!/bin/bash


set -e

__run_supervisord(){
    /usr/bin/supervisord -n
}

__run_monit(){
    monit -d 10 -Ic /etc/monitrc     
}


#fix our ip addr. because of cant not use fixed ip .
__fix_opensipscfg_ipaddr(){

    eth0IP=$(ip addr | grep 'eth0:' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/')
    export VOIP_SERVER_MAIN_IP=$eth0IP
    
    pipework --wait -i eth1
    
    cd /etc/opensips
    sh /etc/opensips/op_create_cfg_by_m4.sh opensipscfg opensips.cfg
    sh /etc/opensips/op_create_cfg_by_m4.sh opensipsctlrc opensipsctlrc
}



__fix_opensipscfg_ipaddr
__run_monit