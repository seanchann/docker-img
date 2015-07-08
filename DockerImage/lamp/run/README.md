# lamp with docker

构建用于lamp运行的基础docker镜像，lamp的版本均采用发行包安装的方式而不是源码安装的方式，如有特殊需求请自行源码编译安装。

## 编译lamp镜像


```bash
docker build --rm -t rhcentos7/lamp:latest .
```

## 启动lamp容器

```bash
docker run -p 80:80 -d rhcentos7/lamp
```

## 使用规则

其他的镜像在使用lamp作为基础镜像的时候，完成下面的步骤：

* 在Dockerfile中：FROM rhcentos7/lamp:latest
* 根据需要覆盖httpd以及php等的配置文件。
* 调用sh /run-httpd.sh 启动http