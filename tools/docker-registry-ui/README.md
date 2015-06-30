# docker-registry-ui配置

docker registry ui 主要是提供了对docker registry的通过web进行可视化管理的工具。

下面就讲述下配置流程

首先，从dockerhub上拉取docker-registry-ui镜像

```bash
docker pull atcol/docker-registry-ui
```

创建docker registry ui的volume

```bash
docker create -v /opt/dockerdata/registry/web-data:/var/lib/h2 --name=registry-ui-dv  atcol/docker-registry-ui
```

运行registy ui

```bash
docker run  --name=registry-ui -d  -p 8091:8080 --volumes-from=registry-ui-dv  atcol/docker-registry-ui
```


**
注意：
1.当重新启动registry ui的时候可能会失败。我们必须去删除映射到host上的/opt/dockershare/registry/web-data/目录下的所有*.lock.db文件，然后重新启动，就可以正常工作
2.在registry的时候，注意下防火墙的相关配置，防火墙可能会阻碍我们的私有仓库的注册。（验证registry是否可达： wget http://192.168.60.37:5000/v1/search）
**



