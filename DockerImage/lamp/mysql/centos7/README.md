Our lamp image base on ronghe-base that inherited from Docker hub CentOS official branch

Perform the build
#docker build --rm -t rhcentos7/mysql:latest .


create a mysql data volume container:
# docker run --name=your-volume-name  rhcentos7/mysql true

Initialise it using a temporary one-time mariadb container:
# docker run --rm --volumes-from=your-volume-name rhcentos7/mysql /config_mysql.sh

Then run mysql server container:

# docker run -d -p 3306:3306  --name=your-sql-name  --volumes-from=your-volume-name rhcentos7/mysql
