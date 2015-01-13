Our lamp image base on ronghe-base that inherited from Docker hub CentOS official branch

Perform the build
#docker build --rm -t rhcentos7/lamp-build:latest .


Launching image

build rpm package data
#docker run   --name=lamp-build-data  -i   rhcentos7/lamp-build  /build-all.sh
clean up data volume
#docker rm -v lamp-build-data

run repo container with rpm package data volumes
#docker run --name=lamp-build  --volumes-from=lamp-build-data -d  --hostname="irepo.ronghe.tv" -p 8088:80  rhcentos7/lamp-build