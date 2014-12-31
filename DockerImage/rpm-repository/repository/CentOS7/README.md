Perform the build
#docker build --rm -t rhcentos7/repository:latest .


Launching image
#docker run -d -p 80:80 --volumes-from data-volume rhcentos7/repository /bin/bash

