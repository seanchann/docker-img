#!/bin/bash

set -e


__rpm_build(){
    chown -R smit.smit /home/smit/rpmbuild/RPMS
    # build thirdtools first
    su - smit -c 'sh ${OPENSIPHOMEDIR}/build/build-packet.sh thirdPartTools all'

    # install custom package for opensips
    \cd /home/smit/rpmbuild/RPMS/x86_64/
    yum install -y thrift-*.rpm  OSPToolkit-*.rpm  libmemcache-*.rpm\
        mongo-c-driver-*.rpm  monit-*.rpm

    # build opensips 
    su - smit -c  'sh ${OPENSIPHOMEDIR}/build/build-packet.sh opensips'

    # install opensips and opensips-cp
    \cd /home/smit/rpmbuild/RPMS/x86_64/
    yum install -y opensips-*.rpm
}


__rpm_build
#copy our dependence rpm to rpm out dir
\cp -rf /home/smit/voip-server/thirdPartTools/dependence-rpm/libcouchbase-2.4.3_centos7_x86_64/*.rpm  /home/smit/rpmbuild/RPMS/x86_64/

