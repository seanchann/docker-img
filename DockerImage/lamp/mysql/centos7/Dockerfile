FROM rhcentos7/base-image
MAINTAINER The ronghe lamp run base env image <www.ronghe.com> - chow



RUN yum install --setopt=tsflags=nodocs -y epel-release
RUN yum -y install supervisor

#mysql dependenece , install from base repo
RUN yum install --setopt=tsflags=nodocs -y perl  perl-Data-Dumper psmisc


ADD  http://192.168.60.25/repolamp/LAMP-Base.repo  /etc/yum.repos.d/LAMP-Base.repo
#RUN yum --disablerepo=\* --enablerepo=LAMP-base -y install  mysql
# first install mysql client. then yum will math our repo when install mysql server
RUN yum  -y install mysql-server mysql; yum  clean all


ADD ./start.sh /start.sh
ADD ./config_mysql.sh /config_mysql.sh
ADD ./supervisord.conf /etc/supervisord.conf
ADD ./my.cnf  /my.cnf

RUN chmod 755 /start.sh
RUN chmod 755 /config_mysql.sh
RUN /config_mysql.sh

EXPOSE 3306

# export httpd and mysql volume
VOLUME ["/var/lib/mysql"]


CMD ["/bin/bash", "/start.sh"]