FROM rhcentos7/base-image
MAINTAINER The rongheTV base image <www.ronghe.com> - chow


RUN yum install --setopt=tsflags=nodocs -y epel-release; yum clean all

# install opensips rpm dependence
RUN yum install --setopt=tsflags=nodocs -y m4  libconfuse radiusclient-ng\
    hiredis librabbitmq cronie  rsyslog perl psmisc supervisor \
    GeoIP gnutls  libevent libmemcached libmicrohttpd libtool-ltdl lm_sensors-libs \
    net-snmp-agent-libs net-snmp-libs  net-snmp-utils nettle perl-Authen-SASL \
    perl-Convert-ASN1 perl-DBI  perl-Digest-HMAC perl-Digest-SHA  perl-Frontier-RPC-Client\
    perl-Frontier-RPC-doc  perl-GSSAPI  perl-JSON  perl-LDAP  perl-Net-Daemon \
    perl-PlRPC  perl-Text-Soundex  perl-Text-Unidecode  perl-XML-Filter-BufferText \
    perl-XML-NamespaceSupport perl-XML-Parser perl-XML-SAX-Base perl-XML-SAX-Writer \
    postgresql-libs tcp_wrappers-libs  unixODBC  xmlrpc-c \
    #thirdpart tools dependence
    openssl perl-Bit-Vector perl-Business-ISBN \
    perl-Business-ISBN-Data  perl-Carp-Clan perl-Class-Accessor perl-Compress-Raw-Bzip2 \
    perl-Compress-Raw-Zlib  perl-Digest  perl-Digest-MD5  perl-Encode-Locale \
    perl-File-Listing perl-HTML-Parser perl-HTML-Tagset perl-HTTP-Cookies \
    perl-HTTP-Daemon  perl-HTTP-Date perl-HTTP-Message perl-HTTP-Negotiate \
    perl-IO-Compress perl-IO-HTML perl-IO-Socket-IP perl-IO-Socket-SSL \
    perl-IO-String  perl-LWP-MediaTypes  perl-Net-HTTP  perl-Net-LibIDN \
    perl-Net-SSLeay perl-TimeDate perl-URI perl-WWW-RobotRules perl-libwww-perl

# support our service command. may be docker will fix systemd.
# then we remove this support
RUN yum install --setopt=tsflags=nodocs -y initscripts

### install from our repository
ADD  http://192.168.60.25/repolamp/LAMP-Base.repo  /etc/yum.repos.d/LAMP-Base.repo

RUN yum  install -y  mysql httpd php php-common php-cli php-mysql php-pdo\
    php-process php-xml php-pear
#ADD ./httpd.conf  /etc/httpd/conf/httpd.conf


ADD http://192.168.60.25/repovoip/VoIP-Base.repo /etc/yum.repos.d/
# thrift not match our repo. so disablerepo=epel
RUN echo "cache-bust" && yum install --setopt=tsflags=nodocs -y --disablerepo=epel thrift thrift-cpp
RUN echo "cache-bust" && yum install --setopt=tsflags=nodocs -y  OSPToolkit libmemcache\
        mongo-c-driver monit libcouchbase2-core
RUN echo "cache-bust" && yum install -y opensips*; yum clean all



## mkdir subsys
RUN mkdir -p /var/lock/subsys


#fix rsyslog bug.
#because this system cant not use systemd for rsyslog
ADD ./rsyslog.conf  /etc/rsyslog.conf

ADD ./init.d/crond   /etc/rc.d/init.d/crond
ADD ./init.d/httpd   /etc/rc.d/init.d/httpd
ADD ./init.d/rsyslog   /etc/rc.d/init.d/rsyslog

ADD ./monit.d/cron   /etc/monit.d/cron
ADD ./monit.d/httpd   /etc/monit.d/httpd
ADD ./monit.d/rsyslog  /etc/monit.d/rsyslog


ADD ./pipework  /usr/sbin/


ADD ./run-voip.sh  /run-voip.sh
ADD ./config_voip.sh  /config_voip.sh
RUN chmod 755 /config_voip.sh
RUN chmod 755 /run-voip.sh


#config default env
ENV VOIP_SERVER_INTERFACE eth0
ENV VOIP_SERVER_MAIN_IP 172.17.100.100
ENV VOIP_SERVER_ALTERNATE_IP 172.17.100.101
ENV VOIP_STUN_MAIN_PORT 5060
ENV VOIP_STUN_ALTERNATE_PORT 5065
ENV VOIP_SIP_DOMAIN ivoip.ronghe.tv
ENV VOIP_SERVER_BEHIND_NAT yes
ENV VOIP_SERVER_EXTERNAL_IP 192.168.60.25
ENV VOIP_SERVER_EXTERNAL_PORT 5060


#generate default config file
RUN  cd /etc/opensips/ \
        && ./op_create_cfg_by_m4.sh opensipsctlrc opensipsctlrc \
        && ./op_create_cfg_by_m4.sh opensipscfg opensips.cfg
#init our custom config
RUN  cd /usr/share/opensips/rh_extra/ \
        && ./custom-init-voip-server.sh


EXPOSE 80 5060 5065 5066 5067 8083 8085
VOLUME ["/var/www/html", "/var/log/httpd", "/var/log/opensips"]


CMD ["/bin/bash", "run-voip.sh"]
