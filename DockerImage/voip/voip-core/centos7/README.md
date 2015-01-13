Our base image base on CentOS7 that inherited from Docker hub CentOS official branch

Perform the build
#docker build --rm -t rhcentos7/voip-core:latest .


Launching image

init database first: call opensipsdbctl create and custom-init-voip-db.sh
#docker run -it --rm --link voip-mysql:voipDB   rhcentos7/voip-core opensipsdbctl create
#docker run -it --rm --link voip-mysql:voipDB   rhcentos7/voip-core /usr/share/opensips/rh_extra/custom-init-voip-db.sh  voipDB mysqlPassword


build a voip core data container for  debug 
#docker run  -v /opt/dockershare/voip-core/var/log/opensips:/var/log/opensips -v /opt/dockershare/voip-core/var/log/httpd/:/var/log/httpd -v /opt/dockershare/voip-core/var/www/html:/var/www/html -d --name=voip-core-data   rhcentos7/voip-core /config_voip.sh

run voip core container with data volume
#docker run -e VOIP_SERVER_EXTERNAL_IP=192.168.60.25 -e VOIP_SERVER_EXTERNAL_PORT=5060  --hostname="ivoip.ronghe.tv"  --volumes-from=voip-core-data  --link voip-mysql:voipDB -p 8086:80 -p 5060:5060/udp -p 5065:5065/udp -p 5066:5066 -p 5067:5067 -p 8083:8083/udp -p 8085:8085 -d --name=voip-core   rhcentos7/voip-core

run voip core only
#docker run -e VOIP_SERVER_EXTERNAL_IP=192.168.60.25 -e VOIP_SERVER_EXTERNAL_PORT=5060  --hostname="ivoip.ronghe.tv" --link voip-mysql:voipDB -p 8086:80 -p 5060:5060/udp -p 5065:5065/udp -p 5066:5066 -p 5067:5067 -p 8083:8083/udp -p 8085:8085 -d --name=voip-core   rhcentos7/voip-core



Add eth1 and fix eth0 ip with static ip when container run
#sudo pipework docker0 voip-build  172.17.100.100/16@172.17.42.1
#sudo pipework docker0 voip-core  172.17.100.101/16@172.17.42.1