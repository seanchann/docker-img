dockerfiles-centos-nginx
========================

CentOS 7 dockerfile for nginx

To build:

Copy the sources down -

    # docker build --rm -t rhcentos7/nginx:latest .

To run:

    # docker run -d -p 80:80 --name=nginx  rhcentos7/nginx

To test:

    # curl http://localhost

