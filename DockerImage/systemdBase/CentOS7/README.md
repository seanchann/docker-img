Our base image base on CentOS7 that inherited from Docker hub CentOS official branch

Perform the build
#docker build --rm -t rhcentos7/systemd-base:latest .


#Launching image  
#docker run -it ¨Cprivileged  -v /sys/fs/cgroup:/sys/fs/cgroup:ro rhcentos7/systemd-base:latest /bin/bash