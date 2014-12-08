FROM ronghe/centos7:ronghe-toolschain
MAINTAINER The ronghe mysql build rpm image <www.ronghe.com> - chow



ENV  HOST_SRC_DIR   ./src/
ENV  BASE_BUILD_DIR  /opt/soft/lamp/
ENV  RPMBUILD_DIR  /home/smit/rpmbuild/
ENV  RPM_OUT_DIR  /home/smit/rpmbuild/RPMS/x86_64/


ENV  MYSQL_SRC_PATH  ${BASE_BUILD_DIR}/mysql
ENV  MYSQL_SPEC  mysql.5.6.17.spec
ENV  MYSQL_SRC   mysql-5.6.17.tar.gz



# build mysql rpm
RUN  yum -y install ncurses-devel perl-Data-Dumper gperf time zlib-devel libaio-devel; yum clean all


ADD  ${HOST_SRC_DIR}/mysql.tar.gz  ${BASE_BUILD_DIR}


#when use mysql new version. 
#need to generate mysql.*.spec file by cmake
#RUN  mkdir -p  ${MYSQL_SRC_PATH}/mysql-rpm-spec\
#        && cd  ${MYSQL_SRC_PATH}/mysql-rpm-spec\
#        && cmake ${MYSQL_SRC_PATH}/mysql-5.6.17
#RUN  cp -rf ${MYSQL_SRC_PATH}/mysql-rpm-spec/support-files/mysql.5.6.17.spec  ${RPMBUILD_DIR}/SPECS/

USER smit
RUN  cp -rf ${MYSQL_SRC_PATH}/${MYSQL_SRC}  ${RPMBUILD_DIR}/SOURCES/
RUN  cp -rf ${MYSQL_SRC_PATH}/${MYSQL_SPEC}  ${RPMBUILD_DIR}/SPECS/
RUN  rpmbuild -ba  ${RPMBUILD_DIR}/SPECS/${MYSQL_SPEC}

USER root
RUN  yum -y install ${RPM_OUT_DIR}/MySQL-server-5.6.17-1.linux_glibc.x86_64.rpm\
    ${RPM_OUT_DIR}/MySQL-client-5.6.17-1.linux_glibc.x86_64.rpm \
    ${RPM_OUT_DIR}/MySQL-devel-5.6.17-1.linux_glibc.x86_64.rpm \
    ${RPM_OUT_DIR}/MySQL-shared-5.6.17-1.linux_glibc.x86_64.rpm; yum clean all

