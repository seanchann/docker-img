## 

FROM rhcentos7/base-image
MAINTAINER data volume  project <xqzhou@ronghe.tv>

ENV DATA_HOME  /opt/dockershare/
ENV MYSQL_DATA ${DATA_HOME}/mysql
ENV PGSQL_DATA  ${DATA_HOME}/pgsql
ENV HTTPD_DATA  ${DATA_HOME}/httpd
ENV VOIP_DATA   ${DATA_HOME}/voip
ENV SPACEWALK_DATA  ${DATA_HOME}/spacewalk
ENV RPMPACKAGE_DATA  ${DATA_HOME}/rpmpackage

VOLUME ["${MYSQL_DATA}", "${PGSQL_DATA}","${HTTPD_DATA}", "${VOIP_DATA}","${SPACEWALK_DATA}", "${RPMPACKAGE_DATA}"]

CMD ["/bin/bash"]
