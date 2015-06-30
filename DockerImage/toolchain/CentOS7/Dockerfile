FROM rhcentos7/base-image
MAINTAINER The ronghe development tools chain base image <www.ronghe.com> - chow

#install build tools
RUN  yum -y install  cmake make gcc gcc-c++ tar rpm-build  rpm-sign flex bison createrepo; yum clean all

#configure user smit rpmbuild env
USER smit
RUN mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS} \
  && echo '%_topdir %(echo $HOME)/rpmbuild'  > ~/.rpmmacros


# sign rpm with our private gpg
ADD  ./RPM-GPG-KEY-RH.private  /opt/
RUN  gpg  --import /opt/RPM-GPG-KEY-RH.private \
  && echo '%_signature gpg' >> ~/.rpmmacros \
  && echo '%_gpg_name  xqzhou (RPM development) <xqzhou@ronghe.tv>' >> ~/.rpmmacros

USER root

ENV RPMROOTDIR /home/smit/rpmbuild/
ADD ./rpm-repo-func.sh  /usr/sbin/rpm-repo-func.sh
RUN  chmod +x /usr/sbin/rpm-repo-func.sh



