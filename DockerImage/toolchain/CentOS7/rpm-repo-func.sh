# support rpm make repo function
#

__rpm_make_repo(){
    if [ "$RPMREPODIRx" = "x" ]; then
        echo "please, support rpm repo directory"
        exit 1
    fi
    
    RPMREPODIR=$1
    #create repo first
    
    mkdir -p ${RPMREPODIR}
    
    x86_64_path=${RPMROOTDIR}/RPMS/x86_64
    noarch_path=${RPMROOTDIR}/RPMS/noarch
    
    if [ -d $x86_64_path ]; then
        if [ "$(ls -A $x86_64_path)" ]; then
            \cp -rf $x86_64_path/*.rpm  ${RPMREPODIR}
        fi
    fi
    
    if [ -d $noarch_path ]; then
        if [ "$(ls -A $noarch_path)" ]; then    
            \cp -rf $noarch_path/*.rpm  ${RPMREPODIR}
        fi
    fi
    
    createrepo -p -d -o ${RPMREPODIR}  ${RPMREPODIR}
    
}

# when call this function, ensure you install httpd.
__rpm_run_httpd(){
    rm -rf /run/httpd/*
    exec /usr/sbin/apachectl -D FOREGROUND
}
