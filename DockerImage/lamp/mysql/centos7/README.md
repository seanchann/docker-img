# mysql with docker

## Perform the build

```bash
docker build --rm -t rhcentos7/mysql:latest .
```

## 运行mysql的服务

创建一个mysql的data volume

```bash
docker create -v yourdir:/var/lib/mysql  --name=mysql-dv  rhcentos7/mysql
```

可以通过-v来映射已有的mysql数据目录或者使用下面的命令重新初始化一个数据volume

```bash
docker run -v yourdir:/var/lib/mysql --name=mysql-dv  rhcentos7/mysql /config_mysql.sh
```


启动一个mysql的容器

```bash
docker run -d -p 3306:3306  --name=your-sql-name  --volumes-from=mysql-dv rhcentos7/mysql
```
