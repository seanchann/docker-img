FROM rhcentos7/base-image
MAINTAINER The ronghe development tools chain base image <www.ronghe.com> - chow

#install build tools
RUN  yum -y install  cmake make gcc gcc-c++ tar rpm-build flex bison; yum clean all

#configure user smit rpmbuild env
USER smit
RUN mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
RUN echo '%_topdir %(echo $HOME)/rpmbuild'  > ~/.rpmmacros

USER root

# built rpm with sign
ADD  RPM-GPG-KEY-RH-7.public  /opt/
RUN  rpm --import /opt/RPM-GPG-KEY-RH-7.public
RUN  echo '%_signature gpg' >> ~/.rpmmacros
RUN  echo '%_gpg_name  xqzhou (RPM Devel) <xqzhou@ronghe.tv>' >> ~/.rpmmacros



