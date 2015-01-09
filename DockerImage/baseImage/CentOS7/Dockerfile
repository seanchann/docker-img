FROM centos:latest
MAINTAINER The rongheTV base image <www.ronghe.com> - chow

# add the worker user named smit
RUN  yum -y install passwd sudo; yum clean all
RUN  groupadd -r -g 6000 smit
RUN  useradd -u 6000 -r -m -g smit smit
RUN  passwd -d smit

# add smit into sudo and run any command with nopasswd.
RUN  echo "%smit           ALL=(ALL)       NOPASSWD:ALL" >> /etc/sudoers

# use default Chongqing tomezone
RUN cp -rf /usr/share/zoneinfo/Asia/Chongqing /etc/localtime