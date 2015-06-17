#!/bin/bash


__config_lvs(){
  echo "1" >/proc/sys/net/ipv4/ip_forward

}



__config_lvs
sh /run-supervisor.sh

