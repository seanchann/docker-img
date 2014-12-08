Our base image base on CentOS7 that inherited from Docker hub CentOS official branch
Note php base on httpd build image or install your httpd rpm packages.


Perform the build
#docker build --rm -t ronghe/centos7:ronghe-php-build .


Launching image
#docker run --rm -it -v /opt/dockershare:/opt/dockershare ronghe/centos7:ronghe-php-build  /bin/bash