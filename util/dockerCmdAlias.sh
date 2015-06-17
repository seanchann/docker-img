#!/bin/bash

alias dr-rmi-none='docker rmi $(docker images | grep "^<none>" | awk "{print $3}")'
alias dr-rm-signle='docker rm $(docker stop $1)'
