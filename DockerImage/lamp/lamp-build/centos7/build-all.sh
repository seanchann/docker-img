#!/bin/bash

set -e

# only build mysql for our voip.
# if someone need httpd and php.
# you can comment out that.

__rpm_build(){
    out_package_dir=/home/smit/rpmbuild/RPMS/x86_64/
    out_package_noarch_dir=/home/smit/rpmbuild/RPMS/noarch/

    chown -R smit.smit /home/smit/rpmbuild/RPMS 
    chown -R smit.smit /home/smit/rpmbuild/SRPMS

    #build dependence.
    su - smit -c 'sh ${LAMPHOMEDIR}/build-package.sh mysql'
    yum --setopt=tsflags=nodocs -y install net-tools perl-Data-Dumper perl-DBI
    yum install --disablerepo=\* -y ${out_package_dir}/mysql-*.rpm
    
    #su - smit -c 'sh ${LAMPHOMEDIR}/build-package.sh apr'
    #yum install --disablerepo=\* -y ${out_package_dir}/apr-*.rpm
    
    #su - smit -c 'sh ${LAMPHOMEDIR}/build-package.sh apr-util'
    #yum install --disablerepo=\* -y ${out_package_dir}/apr-util-*.rpm

    #su - smit -c 'sh ${LAMPHOMEDIR}/build-package.sh distcache'
    #yum install --disablerepo=\* -y ${out_package_dir}/distcache-*.rpm
    
    #su - smit -c 'sh ${LAMPHOMEDIR}/build-package.sh libmcrypt'
    #yum install --disablerepo=\* -y ${out_package_dir}/libmcrypt-*.rpm
      
   
    #su - smit -c 'sh ${LAMPHOMEDIR}/build-package.sh apache'
    #yum --setopt=tsflags=nodocs -y install openssl mailcap
    #yum install --disablerepo=\* -y ${out_package_dir}/httpd-*.rpm ${out_package_dir}/mod_*.rpm
    
    #su - smit -c 'sh ${LAMPHOMEDIR}/build-package.sh php'
    # thisi package dependence net-snmp.x86_64 1:5.7.2-18.el7,
    # but thsi needed maridb(conflicts with our mysql).
    
    #cd  ${out_package_dir}
    #mv php-mysqlnd*.rpm  bak.php-mysqlnd*.rpm
    #yum install -y net-snmp
    #yum install --disablerepo=\* -y ${out_package_dir}/php-*.rpm
    #cd -
    
    #su - smit -c 'sh ${LAMPHOMEDIR}/build-package.sh php-pear'
    #yum install --disablerepo=\* -y ${out_package_noarch_dir}/php-pear-*.rpm
    
}

__rpm_build




