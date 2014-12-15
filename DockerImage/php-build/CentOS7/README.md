Our base image base on CentOS7 that inherited from Docker hub CentOS official branch
Note php base on httpd build image or install your httpd rpm packages.


Perform the build
#docker build --rm -t rhcentos7/php-build:latest .


Launching image
#docker run --rm -it -v /opt/dockershare:/opt/dockershare rhcentos7/php-build  /bin/bash