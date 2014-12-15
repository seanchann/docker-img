#FROM rhcentos7/base-image
FROM rhcentos7/systemd-base

MAINTAINER The ronghe yum repository manager image <www.ronghe.com> - chow

ADD ./jpackage.repo /etc/yum.repos.d/jpackage.repo
ADD ./answers.properties /etc/spacewalk/answers.properties

ENV  SPACEWALK_REPO_RPM  http://yum.spacewalkproject.org/2.2/RHEL/7/x86_64/spacewalk-repo-2.2-1.el7.noarch.rpm
ENV  PEAR_MAIL_RPM   http://jensd.be/download/perl-Mail-RFC822-Address-0.3-12.fc18.noarch.rpm
ENV  EPEL_RELEASE_RPM  http://mirror.centos.org/centos/7/extras/x86_64/Packages/epel-release-7-2.noarch.rpm

# install spacewalk repo
RUN yum install --setopt=tsflags=nodocs -y ${SPACEWALK_REPO_RPM}; yum clean all

# using spacewalk-nightly repo. some packet miss in spacewalk repo
# Nigthly repo contains developers snapshot and it is not suitable 
# for production environment.
RUN sed -i 's/enabled=0/enabled=1/' /etc/yum.repos.d/spacewalk-nightly.repo
RUN sed -i 's/enabled=1/enabled=0/' /etc/yum.repos.d/spacewalk.repo



# install epel release repo
RUN yum install --setopt=tsflags=nodocs -y ${EPEL_RELEASE_RPM}; yum clean all

# install some packages  for spacewalk dependent.
# this packages still miss in repo
RUN yum install --setopt=tsflags=nodocs -y ${PEAR_MAIL_RPM}; yum clean all


#RUN yum install --setopt=tsflags=nodocs -y spacewalk-setup-postgresql spacewalk-postgresql supervisor; yum clean all
# use seperate db so not needed spacewalk-setup-postgresql 
RUN yum install --setopt=tsflags=nodocs -y  spacewalk-postgresql supervisor; yum clean all


#ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
#ADD ./run-spacewalk.sh /usr/local/bin/run-spacewalk.sh

RUN sysctl -w kernel.shmmax=134217728 > /dev/null


EXPOSE 80
EXPOSE 443

#CMD ["/usr/local/bin/run-spacewalk.sh"]
CMD ["/sbin/init"]
