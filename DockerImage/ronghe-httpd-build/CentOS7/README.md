Our base image base on CentOS7 that inherited from Docker hub CentOS official branch
Note httpd base on mysql build image or install your mysql rpm packages.


Perform the build
#docker build --rm -t ronghe/centos7:ronghe-httpd-build .


Launching image
#docker run --rm -it -v /opt/dockershare:/opt/dockershare ronghe/centos7:ronghe-httpd-build /bin/bash