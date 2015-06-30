FROM centos:centos7
MAINTAINER The rongheTV base image <www.ronghe.com> - chow

# add the worker user named smit
RUN  yum -y install passwd sudo; yum clean all \
  && groupadd -r -g 6000 smit \
  && useradd -u 6000 -r -m -g smit smit \
  && passwd -d smit \
  && echo "%smit           ALL=(ALL)       NOPASSWD:ALL" >> /etc/sudoers \
  && cp -rf /usr/share/zoneinfo/Asia/Chongqing /etc/localtime