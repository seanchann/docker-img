Perform the build
#docker build --rm -t rhcentos6/rhnpush:latest .


Launching image
#docker run --rm -it --volumes-from data-volume rhcentos6/rhnpush /bin/bash

push your package
# rhnpush -v --channel=centos7-voip-x86_64 --server=http://localhost --dir=/root/package/


