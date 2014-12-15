Our dev tools base image base on CentOS7 that inherited from Docker hub CentOS official branch

Perform the build
#docker build --rm -t rhcentos7/toolchain:latest .


Launching image
#docker run --rm -it -v /opt/dockershare:/opt/dockershare rhcentos7/toolchain /bin/bash