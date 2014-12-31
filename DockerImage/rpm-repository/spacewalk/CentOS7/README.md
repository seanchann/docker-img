#docker-spacewalk

##Overview

An experiment to get [Spacewalk](http://spacewalk.redhat.com/) 2.2 running under Docker, as I wanted a quick means of running up the app to test stuff out. At the moment the application and the Postgres database all run within the same container. It'd be quite simple to split them out across separate containers and connect them together using --link and --volumes-from. 

##Building the image

Clone this repository, change into the source directory and run:
Our base image base on CentOS7 that inherited from Docker hub CentOS official branch

Perform the build
#docker build --rm -t rhcentos7/spacewalk:latest .



Launching image
#docker run --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro --volumes-from data-volume -d --link postgresql:pgdb -P --name rpm-repository rhcentos7/spacewalk



