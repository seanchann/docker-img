FROM rhcentos6/base-image
MAINTAINER The rongheTV rhn client env image <www.ronghe.com> - chow



#RUN yum install --setopt=tsflags=nodocs -y http://yum.spacewalkproject.org/2.2-client/RHEL/6/x86_64/spacewalk-client-repo-2.2-1.el6.noarch.rpm
RUN yum install --setopt=tsflags=nodocs -y http://yum.spacewalkproject.org/2.2/RHEL/6/x86_64/spacewalk-repo-2.2-1.el6.noarch.rpm
RUN yum install --setopt=tsflags=nodocs -y http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

RUN yum install --setopt=tsflags=nodocs -y rhnpush
#RUN yum install -y http://192.168.61.191.com/pub/rhn-org-trusted-ssl-cert-1.0-1.noarch.rpm


