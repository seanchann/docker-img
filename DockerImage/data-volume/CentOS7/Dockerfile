## 

FROM rhcentos7/base-image
MAINTAINER data volume  project <xqzhou@ronghe.tv>

ENV DATA_HOME  /opt/dockershare/
ENV MYSQL_DATA ${DATA_HOME}/mysql
ENV PGSQL_DATA  ${DATA_HOME}/pgsql
ENV HTTPD_DATA  ${DATA_HOME}/httpd
ENV VOIP_DATA   ${DATA_HOME}/voip
ENV SPACEWALK_DATA  ${DATA_HOME}/spacewalk

VOLUME ["${MYSQL_DATA}"]
VOLUME ["${PGSQL_DATA}"]
VOLUME ["${HTTPD_DATA}"]
VOLUME ["${VOIP_DATA}"]
VOLUME ["${SPACEWALK_DATA}"]


CMD /bin/sh