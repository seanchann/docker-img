FROM ronghe/centos7:ronghe-base
MAINTAINER The ronghe development tools chain base image <www.ronghe.com> - chow

#install build tools
RUN  yum -y install  cmake make gcc gcc-c++ tar rpm-build flex bison; yum clean all

#configure user smit rpmbuild env
USER smit
RUN mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
RUN echo '%_topdir %(echo $HOME)/rpmbuild'  > ~/.rpmmacros

USER root

