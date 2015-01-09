#!/bin/bash

__mysql_config() {
# Hack to get MySQL up and running... I need to look into it more.
echo "Running the mysql_config function."
yum -y erase mysql mysql-server
rm -rf  /var/lib/mysql/ /etc/my.cnf

# user our private repo install mysql
#yum -y install mysql mysql-server
yum --disablerepo=\* --enablerepo=LAMP-base -y install  mysql mysql-server

mysql_install_db

#allways use our custom config
cp -rf /my.cnf /etc/my.cnf
#disable this config generate by mysql_install_db
sed -i 's*^sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES*#sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES*'  /usr/my.cnf 

chown -R mysql:mysql /var/lib/mysql
/usr/bin/mysqld_safe & 
sleep 10
}

__start_mysql() {
echo "Running the start_mysql function."
mysqladmin -u root password mysqlPassword
mysql -uroot -pmysqlPassword -e "CREATE DATABASE testdb"
mysql -uroot -pmysqlPassword -e "GRANT ALL PRIVILEGES ON testdb.* TO 'testdb'@'localhost' IDENTIFIED BY 'mysqlPassword'; FLUSH PRIVILEGES;"
mysql -uroot -pmysqlPassword -e "GRANT ALL PRIVILEGES ON *.* TO 'testdb'@'%' IDENTIFIED BY 'mysqlPassword' WITH GRANT OPTION; FLUSH PRIVILEGES;"
mysql -uroot -pmysqlPassword -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'mysqlPassword' WITH GRANT OPTION; FLUSH PRIVILEGES;"
mysql -uroot -pmysqlPassword -e "select user, host FROM mysql.user;"
killall mysqld
sleep 10
}

# Call all functions
__mysql_config
__start_mysql
