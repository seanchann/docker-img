#!/bin/bash


/bin/sh /usr/local/bin/init-spacewalk.sh

__run_supervisor() {
supervisord -n
}


__run_supervisor

