# Centos7 toolchain image

基于centos7创建的toolchain镜像，此镜像中主要包括了gcc g++以及rpm包编译的相关环境。

针对rpm包的签名我们使用的自己生成的签名私钥。具体内容可以参考GPG目录中的说明。

## Perform the build
```bash
docker build --rm -t rhcentos7/toolchain:latest .
```

## Launching image

```bash
docker run --rm -it  rhcentos7/toolchain /bin/bash
```