# lvs使用须知

lvs作为负载均衡的利器，在很大程度上给我们的软件提供了横向扩展的灵活性。
因此我们制作了lvs的docker 镜像，此镜像主要用于测试，调试我们的后端业务，在生产环境中，建议还是使用独立的裸机安装或者负载均衡器来代替。

## 镜像编译

### lvs依赖组件的镜像编译

```bash
docker build --rm -t rhcentos7/lvsdep:latest -f ./Dockerfile.lvsdep .
```

### lvs运行镜像编译

```bash
docker build --rm -t rhcentos7/lvs:latest -f ./Dockerfile.lvs .
```

## 运行container

```bash
docker run --rm -it -v /opt/dockershare:/opt/dockershare rhcentos7/base-image /bin/bash
```

## 配置须知

