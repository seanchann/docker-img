FROM rhcentos7/toolchain
MAINTAINER The ronghe lamp(only support mysql) build env image <www.ronghe.com> - chow

RUN yum --setopt=tsflags=nodocs -y install epel-release

#mysql build dependence
RUN  yum --setopt=tsflags=nodocs -y install perl-Time-HiRes perl-Env\
        time libaio-devel ncurses-devel openssl-devel zlib-devel

#httpd build dependence
#RUN  yum --setopt=tsflags=nodocs -y install autoconf  libtool doxygen \
#        expat-devel libuuid-devel postgresql-devel  sqlite-devel \
#        unixODBC-devel openldap-devel nss-devel libdb4-devel freetds-devel \
#        lua-devel libxml2-devel
#libmcrpyt build depnedence
#RUN  yum --setopt=tsflags=nodocs -y install libtool-ltdl-devel
#php build dependence
#RUN  yum --setopt=tsflags=nodocs -y install bzip2-devel libcurl-devel gmp-devel\
#        pam-devel ssmtp libedit-devel  libzip-devel  systemd-devel\ 
#        net-snmp-devel libxslt-devel libjpeg-devel  libpng-devel freetype-devel \
#        libXpm-devel t1lib-devel tokyocabinet-devel   aspell-devel  recode-devel\
#        libicu-devel enchant-devel

# for our repo use
RUN yum --setopt=tsflags=nodocs -y install httpd
        
RUN  mkdir -p /home/smit/lamp/
ADD  ./src/mysql.tar.gz  /home/smit/lamp/
#ADD  ./src/httpd.tar.gz  /home/smit/lamp/
#ADD  ./src/php.tar.gz  /home/smit/lamp/

ADD  ./src/build-package.sh  /home/smit/lamp/build-package.sh
RUN  chmod 777  /home/smit/lamp/build-package.sh

RUN  chown -R smit.smit /home/smit/lamp/

RUN echo "export LAMPHOMEDIR=/home/smit/lamp/"  >> /etc/profile
RUN echo "export RPMDIR=/home/smit/rpmbuild/"  >> /etc/profile

ADD  ./build-all.sh   /build-all.sh
RUN  chmod 777  /build-all.sh
#RUN  /build-all.sh

ADD ./LAMP-Base.repo  /LAMP-Base.repo
ADD ./make-repo.sh /make-repo.sh
RUN  chmod 777  /make-repo.sh


EXPOSE 80
VOLUME ["/home/smit/rpmbuild/RPMS", "/home/smit/rpmbuild/SRPMS", "/var/www/html/repolamp"]


CMD ["/bin/bash", "/make-repo.sh"]