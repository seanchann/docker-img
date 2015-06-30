# Centos6 image

Our base image base on CentOS6 that inherited from Docker hub CentOS official branch

## Perform the build

```bash
docker build --rm -t rhcentos6/base-image:latest .
```


## Launching image

```bash
docker run --rm -it rhcentos6/base-image /bin/bash
```