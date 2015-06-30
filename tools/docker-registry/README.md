# docker registry

构建私有的docker registry。基于的dockerhub上的registry。
注意提供的私有仓库由于devicemapper的大小的限制，最后把registry的数据导出到host上去。

下面就讲述下如何构建自己的registry

首先，拉取registry镜像从docker hub上：

```bash
docker pull registry:latest
```

创建一个registry data volume：

```bash
docker create --name=registry-dv -v /opt/dockerdata/registry/conf:/registry-conf  -v /opt/dockerdata/registry/data/:/data registry
```

注意下，这里我们也指定了自己的配置文件。

启动我们的私有registry

```bash
docker run --name=registry --volumes-from=registry-dv  -e SETTINGS_FLAVOR=prod  -e DOCKER_REGISTRY_CONFIG=/registry-conf/config.yml  -d -p 5000:5000 registry
```
