Our base image base on CentOS7 that inherited from Docker hub CentOS official branch
Note httpd base on mysql build image or install your mysql rpm packages.


Perform the build
#docker build --rm -t rhcentos7/httpd-build:latest .


Launching image
#docker run --rm -it -v /opt/dockershare:/opt/dockershare rhcentos7/httpd-build /bin/bash