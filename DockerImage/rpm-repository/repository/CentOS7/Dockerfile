FROM rhcentos7/base-image
MAINTAINER The rongheTV rhn client env image <www.ronghe.com> - chow


RUN yum install --setopt=tsflags=nodocs -y httpd createrepo; yum clean all


EXPOST 80

ENV HTTPDDOCROOT  /opt/dockershare/httpd/

#change doc root for httpd
RUN sed -i 's#^DocumentRoot "/var/www/html"#DocumentRoot "/opt/dockershare/httpd/var/www/html"#' /etc/httpd/conf/httpd.conf
RUN sed -i 's#^<Directory "/var/www">#<Directory "/opt/dockershare/httpd/var/www/">#'  /etc/httpd/conf/httpd.conf
RUN sed -i 's#^<Directory "/var/www/html">#<Directory "/opt/dockershare/httpd/var/www/html">#'  /etc/httpd/conf/httpd.conf


ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh




CMD ["/run-httpd.sh"]


