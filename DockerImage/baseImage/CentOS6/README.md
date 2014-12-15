Our base image base on CentOS7 that inherited from Docker hub CentOS official branch

Perform the build
#docker build --rm -t rhcentos6/base-image:latest .


Launching image
#docker run --rm -it  rhcentos6/base-image /bin/bash