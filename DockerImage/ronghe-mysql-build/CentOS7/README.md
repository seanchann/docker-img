Our base image base on CentOS7 that inherited from Docker hub CentOS official branch

Perform the build
#docker build --rm -t ronghe/centos7:ronghe-mysql-build .


Launching image
#docker run --rm -it -v /opt/dockershare:/opt/dockershare ronghe/centos7:ronghe-mysql-build /bin/bash