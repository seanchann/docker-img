FROM rhcentos6/base-image

MAINTAINER The ronghe yum repository manager image <www.ronghe.tv> - chow


ADD ./jpackage.repo /etc/yum.repos.d/jpackage.repo

RUN yum install --setopt=tsflags=nodocs -y http://yum.spacewalkproject.org/2.2/RHEL/6/x86_64/spacewalk-repo-2.2-1.el6.noarch.rpm
RUN yum install --setopt=tsflags=nodocs -y http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm



RUN yum install --setopt=tsflags=nodocs -y spacewalk-postgresql supervisor; yum clean all

# if install pgsql and spaacewalk in same station. run this
RUN yum install --setopt=tsflags=nodocs -y spacewalk-setup-postgresql; yum clean all


ADD ./answers.properties /etc/spacewalk/answers.properties
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD ./run-spacewalk.sh /usr/local/bin/run-spacewalk.sh
ADD ./init-spacewalk.sh  /usr/local/bin/init-spacewalk.sh

RUN chmod -v +x  /usr/local/bin/run-spacewalk.sh
RUN chmod -v +x  /usr/local/bin/init-spacewalk.sh

EXPOSE 80
EXPOSE 443

CMD ["/bin/bash", "/usr/local/bin/run-spacewalk.sh"]