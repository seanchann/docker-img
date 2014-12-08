FROM ronghe/centos7:ronghe-httpd-build
MAINTAINER The ronghe php build rpm image <www.ronghe.com> - chow

# rpmbuild php.


ENV  HOST_SRC_DIR   ./src/
ENV  BASE_BUILD_DIR  /opt/soft/lamp/
ENV  RPMBUILD_DIR  /home/smit/rpmbuild/
ENV  RPM_OUT_DIR  ${RPMBUILD_DIR}/RPMS/x86_64/
ENV  NOARCH_RPM_OUT_DIR  ${RPMBUILD_DIR}/RPMS/noarch/


# build php rpm
ENV  ROOT_DIR  php
ENV  PHP_SRC_PATH  ${BASE_BUILD_DIR}/${ROOT_DIR}/php55
ENV  PHP_SRC   *
ENV  PHP_SPEC  php55.spec
ENV  LIBMCRYPT_SRC_PATH  ${BASE_BUILD_DIR}/${ROOT_DIR}/libmcrypt  
ENV  LIBMCRYPT_SRC  libmcrypt-2.5.8*
ENV  LIBMCRYPT_SPEC libmcrypt.spec
ENV  PHP_PEAR_SRC_PATH   ${BASE_BUILD_DIR}/${ROOT_DIR}/php-pear
ENV  PHP_PEAR_SRC  *
ENV  PHP_PEAR_SPEC  php-pear.spec

# install limcrypt build dependent packages
RUN  yum -y install libtool-ltdl-devel; yum clean all

# install php build dependent packages
RUN yum -y install libxml2-devel bzip2 bzip2-devel libcurl-devel libjpeg-devel\
            libpng-devel libXpm-devel freetype-devel gmp-devel\
            pam-devel ssmtp libedit-devel libc-client-devel\
            net-snmp-devel libxslt-devel libtidy-devel aspell-devel\
            recode-devel libicu-devel enchant-devel; yum clean all;


ADD  ${HOST_SRC_DIR}/php.tar.gz ${BASE_BUILD_DIR}

# build libmcrypt first
USER smit
RUN  cp -rf ${LIBMCRYPT_SRC_PATH}/${LIBMCRYPT_SRC}  ${RPMBUILD_DIR}/SOURCES/
RUN  cp -rf ${LIBMCRYPT_SRC_PATH}/${LIBMCRYPT_SPEC}  ${RPMBUILD_DIR}/SPECS/
RUN  rpmbuild -ba ${RPMBUILD_DIR}/SPECS/${LIBMCRYPT_SPEC}
USER root
RUN  yum -y install ${RPM_OUT_DIR}/libmcrypt-2.5.8-16.el7.centos.x86_64.rpm\
        ${RPM_OUT_DIR}/libmcrypt-devel-2.5.8-16.el7.centos.x86_64.rpm; yum clean all


# build php 
USER smit
RUN  cp -rf ${PHP_SRC_PATH}/${PHP_SRC}  ${RPMBUILD_DIR}/SOURCES/
RUN  cp -rf ${PHP_SRC_PATH}/${PHP_SPEC}  ${RPMBUILD_DIR}/SPECS/
RUN  rpmbuild -ba ${RPMBUILD_DIR}/SPECS/${PHP_SPEC}
USER root
RUN  yum -y install ${RPM_OUT_DIR}/php-5.5.10-1.el7.centos.x86_64.rpm\
        ${RPM_OUT_DIR}/php-process-5.5.10-1.el7.centos.x86_64.rpm\
        ${RPM_OUT_DIR}/php-gd-5.5.10-1.el7.centos.x86_64.rpm\
        ${RPM_OUT_DIR}/php-xml-5.5.10-1.el7.centos.x86_64.rpm\
        ${RPM_OUT_DIR}/php-cli-5.5.10-1.el7.centos.x86_64.rpm\
        ${RPM_OUT_DIR}/php-pdo-5.5.10-1.el7.centos.x86_64.rpm\
        ${RPM_OUT_DIR}/php-common-5.5.10-1.el7.centos.x86_64.rpm; yum clean all

# build php pear
USER smit
RUN  cp -rf ${PHP_PEAR_SRC_PATH}/${PHP_PEAR_SRC}  ${RPMBUILD_DIR}/SOURCES/
RUN  cp -rf ${PHP_PEAR_SRC_PATH}/${PHP_PEAR_SPEC}  ${RPMBUILD_DIR}/SPECS/
RUN  rpmbuild -ba ${RPMBUILD_DIR}/SPECS/${PHP_PEAR_SPEC}
USER root
RUN  yum -y install ${NOARCH_RPM_OUT_DIR}/php-pear-1.9.4-21.el7.centos.noarch.rpm; yum clean all
