## 

FROM rhcentos7/base-image
MAINTAINER postgresql project <xqzhou@ronghe.tv>

ENV PGSQL_HOME  /opt/dockershare/pgsql


#RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install postgresql-server postgresql postgresql-contrib postgresql-pltcl supervisor; yum clean all

ADD ./postgresql-setup /usr/bin/postgresql-setup
ADD ./supervisord.conf /etc/supervisord.conf
ADD ./start_postgres.sh  /start_postgres.sh
ADD ./postgresql.conf  /postgresql.conf
ADD ./pg_hba.conf  /pg_hba.conf

#Sudo requires a tty. fix that.
RUN sed -i 's/.*requiretty$/#Defaults requiretty/' /etc/sudoers
RUN chmod +x /usr/bin/postgresql-setup
RUN chmod +x /start_postgres.sh



EXPOSE 5432

CMD ["/bin/bash", "/start_postgres.sh"]
