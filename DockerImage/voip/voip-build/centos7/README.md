Our base image base on CentOS7 that inherited from Docker hub CentOS official branch

Perform the build
#docker build --rm -t rhcentos7/voip-build:latest .


Launching image

build rpm package
#docker run   --name=voip-build-data -i rhcentos7/voip-build  /build-all.sh
clean up data volume
#docker rm -v voip-build-data

start a voip repo container with custom rpm
#docker run  -d --name=voip-build --volumes-from=voip-build-data  --hostname="irepo.ronghe.tv" -p 8089:80  rhcentos7/voip-build




