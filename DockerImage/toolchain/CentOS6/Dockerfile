FROM rhcentos6/base-image
MAINTAINER The ronghe development tools chain base image <www.ronghe.com> - chow

#install build tools
RUN  yum -y install  cmake make gcc gcc-c++ tar rpm-build  rpm-sign flex bison; yum clean all

#configure user smit rpmbuild env
USER smit
RUN mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
RUN echo '%_topdir %(echo $HOME)/rpmbuild'  > ~/.rpmmacros

# sign rpm with our private gpg
ADD  ./RPM-GPG-KEY-RH.private  /opt/
RUN  gpg --import /opt/RPM-GPG-KEY-RH.private


RUN  echo '%_signature gpg' >> ~/.rpmmacros
RUN  echo '%_gpg_name  xqzhou (RPM development) <xqzhou@ronghe.tv>' >> ~/.rpmmacros

USER root

VOLUME  ["/home/smit/rpmbuild/RPMS"]


