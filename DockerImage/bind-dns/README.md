# bind dns service #

BIND is open source software that implements the Domain Name System (DNS) protocols for the Internet. It is a reference implementation of those protocols, but it is also production-grade software, suitable for use in high-volume and high-reliability applications.

# bind dns with docker #

我们将bind做成docker镜像为服务提供相关的dns解析。下面使我们部署bind的步骤：

首先拉取镜像下来

    docker pull sameersbn/bind:latest

启动bind容器

`docker run --name bind -d --restart=always \
  --publish 53:53/udp --publish 10000:10000 \
  --volume /srv/docker/bind:/data \
  sameersbn/bind:latest`

如果需要配置webmin，添加--env ROOT_PASSWORD=secretpassword