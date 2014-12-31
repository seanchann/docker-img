Perform the build
#docker build --rm -t rhcentos6/rhnclient:latest .


Launching image
#docker run --rm -it --volumes-from data-volume rhcentos6/rhnclient /bin/bash


Register system on spacewalk
#rhnreg_ks --serverUrl=https://YourSpacewalk.example.org/XMLRPC --sslCACert=/usr/share/rhn/RHN-ORG-TRUSTED-SSL-CERT --activationkey=<key-with-rhel-custom-channel> 
#rhnreg_ks --serverUrl=https://192.168.61.191/XMLRPC --sslCACert=/usr/share/rhn/RHN-ORG-TRUSTED-SSL-CERT --activationkey=<key-with-rhel-custom-channel> 
#rhnreg_ks --serverUrl=https://192.168.61.191/XMLRPC --username=admin  --password=52983720 --sslCACert=/usr/share/rhn/RHN-ORG-TRUSTED-SSL-CERT

