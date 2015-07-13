FROM rhcentos7/base-image:latest
MAINTAINER The rongheTV lamp base image <www.ronghe.com> - seanchann


#use offical mysql imange
RUN rpm -Uvh http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm \
  && yum install --setopt=tsflags=nodocs -y mysql httpd php \
  && yum install --setopt=tsflags=nodocs -y php-mysql \
  && yum install --setopt=tsflags=nodocs -y memcached \
  && yum install --setopt=tsflags=nodocs -y php-pecl-memcache \
  && yum clean all

ADD /run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh

EXPOSE 80


CMD ["/run-httpd.sh"]



