dockerfiles-centos-MySQL
========================

This repo contains a recipe for making Docker container for SSH and MySQL on CentOS 6. 

Check your Docker version

    # docker version

Perform the build

    # docker build --rm -t rhcentos6/mysql:latest .

Check the image out.

    # docker images

Run it:

    # docker run -d -p 3306:3306 rhcentos6/mysql:centos6

Create a data volume container: (it doesn't matter what image you use here, we'll never run this container again; it's just here to reference the data volume)

# docker run --name=mysql-data -v /var/lib/mysql rhcentos6/mysql true

Initialise it using a temporary one-time mariadb container:

# docker run --rm --volumes-from=mysql-data rhcentos6/mysql /config_mysql.sh
And now create the new persistent mariadb container:

# docker run --name=mysql -d -p 3306:3306 --volumes-from=mysql-data rhcentos6/mysql

Get container ID:

    # docker ps

Keep in mind the password set for MySQL is: mysqlPassword

Get the IP address for the container:

    # docker inspect <container_id> | grep -i ipaddr

For MySQL:
    # mysql -h 172.17.0.x -utestdb -pmysqlPassword


Create a table:

```
\> CREATE TABLE test (name VARCHAR(10), owner VARCHAR(10),
    -> species VARCHAR(10), birth DATE, death DATE);
```
