FROM rhcentos7/base-image
MAINTAINER The rongheTV supervisord image <www.ronghe.com> - chow



RUN yum install -y epel-release \
  && yum clean all \
  && yum  install -y --setopt=tsflags=nodocs supervisor \
  && yum clean all

ADD run-supervisor.sh /run-supervisor.sh
ADD supervisord.conf /etc/supervisord.conf
RUN chmod 600 /etc/supervisord.conf \
  && chmod +x /run-supervisor.sh

CMD ["/bin/bash", "/run-supervisor.sh"]