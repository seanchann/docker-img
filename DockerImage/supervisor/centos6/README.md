# supervisor 在docker中的使用

由于在docker的一个容器中，默认不能启动多个进程，因此只能首先启动supervisor，进而通过supervisor启动其他的进程。

## 编译supervisor镜像


```bash
docker build --rm -t rhcentos6/supervisor:latest .
```

## 用户使用规则

其他的镜像在使用supervisor镜像的时候，完成下面的步骤：

* 在Dockerfile中：FROM rhcentos7/supervisor
* 将需要启动的程序配置到/etc/supervisord.conf中，centos6版本下的supervisor的include section是有问题的。
* 调用sh /run-supervisor.sh