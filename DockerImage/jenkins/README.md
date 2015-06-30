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