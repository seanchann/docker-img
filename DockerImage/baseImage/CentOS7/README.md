# Centos7 image

Our base image base on CentOS7 that inherited from Docker hub CentOS official branch

## Perform the build

```bash
docker build --rm -t rhcentos7/base-image:latest .
```


## Launching image

```bash
docker run --rm -it rhcentos7/base-image /bin/bash
```