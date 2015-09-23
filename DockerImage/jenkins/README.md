# 持续化集成工具jenkins与docker

jenkins持续化集成工具在docker中的运行，主要涉及jenkins image的编译、部署jenkins image、jenkins的相关插件的说明、jenkins相关配置说明

## jenkins image的编译

```bash
docker build --rm -t rh/jenkins-plugins:latest -f Dockerfile.plugins .
docker build --rm -t rh/jenkins:latest .
```

注意：安装插件可能会失败，添加http proxy。如：

```text
export http_proxy=proxy-addr:proxy-port;docker build --rm -t rh/jenkins:latest .
```

## 启动 jenkins 容器

### 创建一个jenkins的data volume 容器

```bash
mkdir -p /your/home/tmp
chmod 777 /your/home/tmp
docker create -v /your/home:/var/jenkins_home --name=jenkins-dv  rh/jenkins
```

### 启动一个jenkins容器

```bash
docker run -d -p 8090:8080 --volumes-from jenkins-dv --name myjenkins rh/jenkins
```

**注意：/var/jenkins_home/tmp目前需要手动的在容器内创建下，推荐使用的方式是data volume，提前创建好这些目录，以及给出这些目录的可读写权限**

## jenkins的插件说明

在docker中运行jenkins，由于容器的无状态特性，我们必须重新编译自己的image，安装需要的插件。
如果是采用非docker的安装方式，那么直接在web ui的插件管理中自行安装。

下面我们针对，在docker中运行jenkins，我们安装的插件进行一个说明。

**注意我们安装的插件，都在plugins.txt中罗列**

### git 插件

git插件提供对git命令的支持

### git client插件

提供git client的支持，可以从git仓库拉取代码。

### gitlab hook插件

针对gitlab 提供hook功能，主要是对任务如何触发的定义。比如，如果代码提交到了gitlab，就触发一次编译任务。

### TAP插件

主要是根据build完成后的结果，绘制编译结果统计图。


## jenkins with DIND ##

DIND在很多场合可以简化我们的工作场景，避免对宿主机的进一步的污染，比如Jenkins来编译docker镜像的请求，就可以完全启动一个docker，在docker内部进行docker镜像的编译动作，更大程度上的保证了整个发布流程不会被其他环境因素所干扰。

## DIND的镜像编译 ##

编译DIND镜像的命令：

`docker build --rm -t rh/jenkins-dind:latest -f Dockerfile.dind .`　

## 启动dind容器 ##

由于我们是在docker内部启动docker daemon，因此在run的时候，特别注意权限相关的问题 （privileged）

### 创建一个jenkins的data volume 容器

```bash
mkdir -p /your/home/tmp
chmod 777 /your/home/tmp
docker create -v /your/home:/var/jenkins_home --name=jenkins-dv  rh/jenkins-dind
```

### 启动dind版本的jenkins容器


`docker run --privileged --dns 8.8.8.8 -d --name jenkins --volumes-from jenkins-dv -p 8090:8080 -u root rh/jenkins-dind` 

注意docker in docker的方式需要传递docker的启动参数进来，因此完整的启动命令如下：

`docker run --privileged --dns 8.8.8.8 -d --name jenkins --volumes-from jenkins-dv -p 8090:8080 -e "DOCKER_DAEMON_ARGS=--insecure-registry dockerhub.ironghe.tv:5000" -u root rh/jenkins-dind`


### 启动dind版本容器的注意事项

由于docker in docker它的storage还是必须依赖于宿主机的系统，因此它会在宿主机上创建/var/lib/docker来工作。但是这个有的时候，重新启动和删除的时候，会有devicemapper busy的错误，造成没有删除掉/var/lib/docker，当你在此启动时候，docker daemon就会无法启动。这个时候，我们只需要重新手动删除这个目录即可。