FROM rhcentos7/toolchain
MAINTAINER The rongheTV voip package build image <www.ronghe.com> - chow


### build env
RUN yum install --setopt=tsflags=nodocs -y epel-release; yum clean all

# for mogo-c-driver 
RUN yum install --setopt=tsflags=nodocs -y python-sphinx doxygen

# for OSPToolkit
RUN yum install --setopt=tsflags=nodocs -y openssl-devel

# for mediaproxy
RUN yum install --setopt=tsflags=nodocs -y iptables-devel libnetfilter_conntrack-devel python-devel

# for monit
RUN yum install --setopt=tsflags=nodocs -y pam-devel

# for thrift
# if thrift with java ,then install package :
#ant jakarta-commons-lang slf4j  java-1.6.0-openjdk-javadoc java-1.6.0-openjdk-devel
# if thrift with php, then install package :
# php-devel
RUN yum install --setopt=tsflags=nodocs -y ruby byacc dos2unix libevent-devel libtool\
    mono-devel boost-devel

# for libcouchbase
#RUN yum install --setopt=tsflags=nodocs -y java
   
# for opensips
RUN yum install --setopt=tsflags=nodocs -y  postgresql-devel unixODBC-devel expat-devel lm_sensors-devel\
    net-snmp-devel openldap-devel GeoIP-devel json-c-devel\
    xmlrpc-c-devel libmicrohttpd-devel perl-ExtUtils-Embed\
    radiusclient-ng-devel libconfuse-devel librabbitmq-devel\
    hiredis-devel  db4-devel libmemcached-devel lua-devel\
    lynx libxslt ncurses-devel
                  
# for thridpart rpm install dependence
RUN yum install --setopt=tsflags=nodocs -y openssl perl-Bit-Vector perl-Business-ISBN \
    perl-Business-ISBN-Data  perl-Carp-Clan perl-Class-Accessor perl-Compress-Raw-Bzip2 \
    perl-Compress-Raw-Zlib  perl-Digest  perl-Digest-MD5  perl-Encode-Locale \
    perl-File-Listing perl-HTML-Parser perl-HTML-Tagset perl-HTTP-Cookies \
    perl-HTTP-Daemon  perl-HTTP-Date perl-HTTP-Message perl-HTTP-Negotiate \
    perl-IO-Compress perl-IO-HTML perl-IO-Socket-IP perl-IO-Socket-SSL \
    perl-IO-String  perl-LWP-MediaTypes  perl-Net-HTTP  perl-Net-LibIDN \
    perl-Net-SSLeay perl-TimeDate perl-URI perl-WWW-RobotRules perl-libwww-perl \
    libev

### install from our repository
ADD  http://192.168.60.25/repolamp/LAMP-Base.repo  /etc/yum.repos.d/LAMP-Base.repo
RUN yum install --setopt=tsflags=nodocs -y  mysql mysql-devel

### install httpd for repo
RUN yum install --setopt=tsflags=nodocs -y httpd; yum clean all



ADD ./voip-server.tar.gz  /home/smit/
RUN chown -R  smit.smit /home/smit/voip-server/
RUN yum install --disablerepo=\* --setopt=tsflags=nodocs -y \
    /home/smit/voip-server/thirdPartTools/dependence-rpm/libcouchbase-2.4.3_centos7_x86_64/*.rpm; yum clean all  
     
RUN echo "export OPENSIPHOMEDIR=/home/smit/voip-server/"  >> /etc/profile
RUN echo "export RPMDIR=/home/smit/rpmbuild/"  >> /etc/profile

ADD ./VoIP-Base.repo  /VoIP-Base.repo
ADD ./make-repo.sh /make-repo.sh
ADD ./build-all.sh /build-all.sh

RUN chmod  777  /build-all.sh
RUN chmod 777  /make-repo.sh

#RUN sh build-all.sh

EXPOSE 80
VOLUME ["/home/smit/rpmbuild/RPMS", "/home/smit/rpmbuild/SRPMS", "/var/www/html/repovoip"]


CMD ["/bin/bash", "/make-repo.sh"]
