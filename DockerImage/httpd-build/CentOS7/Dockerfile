FROM rhcentos7/mysql-build
MAINTAINER The ronghe httpd build rpm image <www.ronghe.com> - chow

# rpmbuild httpd.


ENV  HOST_SRC_DIR   ./src/
ENV  BASE_BUILD_DIR  /opt/soft/lamp/
ENV  RPMBUILD_DIR  /home/smit/rpmbuild/
ENV  RPM_OUT_DIR  /home/smit/rpmbuild/RPMS/x86_64/


ENV  HTTPD_SRC_PATH  ${BASE_BUILD_DIR}/httpd
ENV  HTTPD_SRC   httpd-2.4.10.tar.bz2
ENV  APR_SRC  apr-1.5.1.tar.bz2
ENV  APR_UTIL_SRC  apr-util-1.5.4.tar.bz2

# install apr build dependent packages
RUN  yum -y install autoconf doxygen  libtool; yum clean all


# install apr-util build dependent packages
RUN  yum -y install expat-devel libuuid-devel postgresql-devel\
        sqlite-devel unixODBC-devel openldap-devel openssl-devel nss-devel; yum clean all
# apr-util. use epel repository install other packages        
RUN  yum -y install epel-release; yum clean all
RUN  yum -y install libdb4-devel freetds-devel; yum clean all


# install httpd build dependent packages
RUN  yum -y install lua-devel libxml2-devel; yum clean all


ADD  ${HOST_SRC_DIR}/httpd.tar.gz ${BASE_BUILD_DIR}

# build apr first
USER smit
RUN  cp -rf ${HTTPD_SRC_PATH}/${APR_SRC}  ${RPMBUILD_DIR}/SOURCES/
RUN  rpmbuild -tb ${RPMBUILD_DIR}/SOURCES/${APR_SRC}
USER root
RUN  yum -y install ${RPM_OUT_DIR}/apr-1.5.1-1.x86_64.rpm\
        ${RPM_OUT_DIR}/apr-devel-1.5.1-1.x86_64.rpm; yum clean all




#build apr-util 
USER smit
RUN  cp -rf ${HTTPD_SRC_PATH}/${APR_UTIL_SRC}  ${RPMBUILD_DIR}/SOURCES/
RUN  rpmbuild -tb ${RPMBUILD_DIR}/SOURCES/${APR_UTIL_SRC}
USER root
RUN  yum -y install ${RPM_OUT_DIR}/apr-util-1.5.4-1.x86_64.rpm \
        ${RPM_OUT_DIR}/apr-util-devel-1.5.4-1.x86_64.rpm; yum clean all



# rebuild distcache
USER smit
RUN  cp -rf ${HTTPD_SRC_PATH}/distcache-1.4.5-23.src.rpm  ${RPMBUILD_DIR}/SOURCES/
RUN  rpmbuild --rebuild ${RPMBUILD_DIR}/SOURCES/distcache-1.4.5-23.src.rpm
USER root
RUN yum -y install ${RPM_OUT_DIR}/distcache-1.4.5-23.x86_64.rpm\
        ${RPM_OUT_DIR}/distcache-devel-1.4.5-23.x86_64.rpm; yum clean all
        



# build apache httpd
USER smit
RUN  cp -rf ${HTTPD_SRC_PATH}/${HTTPD_SRC}  ${RPMBUILD_DIR}/SOURCES/
RUN  rpmbuild -tb ${RPMBUILD_DIR}/SOURCES/${HTTPD_SRC}
USER root
RUN  yum -y install ${RPM_OUT_DIR}/httpd-2.4.10-1.x86_64.rpm\
        ${RPM_OUT_DIR}/httpd-tools-2.4.10-1.x86_64.rpm\
        ${RPM_OUT_DIR}/httpd-devel-2.4.10-1.x86_64.rpm; yum clean all
