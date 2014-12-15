#docker-spacewalk

##Overview

An experiment to get [Spacewalk](http://spacewalk.redhat.com/) 2.2 running under Docker, 
as I wanted a quick means of running up the app to test stuff out. 
At the moment the application and the Postgres database all run within the same container.
 It'd be quite simple to split them out across separate containers and connect 
 them together using --link and --volumes-from. 
Notice:Our base image base on CentOS7 that inherited from Docker hub CentOS official branch

##Building the image
#docker build --rm -t rhcentos6/rpm-repository:latest .

Launching image with data-volume and use external pgsql with --link .
Notice : we configure FQDN: "yum.ronghe.tv"(this for ssl certs)
#docker run --privileged -h yum.ronghe.tv --volumes-from data-volume -d --link postgresql:pgdb -P --name rpm-repository rhcentos6/rpm-repository
build postgresql within spacewalk
#docker run --privileged -h yum.ronghe.tv --volumes-from data-volume -d  -p 80:80 -p 443:443 --name rpm-repository rhcentos6/rpm-repository

run docker with run-spacewalk.sh . beause of CMD default config lost when commit
#docker run --privileged -h yum.ronghe.tv --volumes-from data-volume -d  -p 80:80 -p 443:443 --name rpm-repository rhcentos6/rpm-repository /bin/bash /usr/local/bin/run-spacewalk.sh


First start a container exec bottom command for init spacewalk:
# spacewalk-setup --disconnected --external-postgresql --answer-file=/etc/spacewalk/answers.properties
Use internal sql
# spacewalk-setup --disconnected  --answer-file=/etc/spacewalk/answers.properties

Notice flowing command do not use . it just record here
#sed -i 's/shared_buffers = 384MB/shared_buffers = 100MB/g' /var/lib/pgsql/data/postgresql.conf
#sysctl -w kernel.shmmax=134217728 > /dev/null



