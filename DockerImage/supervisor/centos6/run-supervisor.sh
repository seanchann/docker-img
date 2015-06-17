#!/bin/bash


__run_supervisord(){
  /usr/bin/supervisord -n -c /etc/supervisord.conf
}

__run_supervisord