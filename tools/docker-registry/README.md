This support docker registry storage manager.

First pull your registry from docker hub:
#docker pull registry:latest

build your data volume and make sure
copy your custom config file to host dir
# docker run --name=registry-data -v /opt/dockershare/registry/conf:/registry-conf  -v /opt/dockershare/registry/data/:/data registry   true

run your registry with your custom config.xml
# docker run --name=registry --volumes-from=registry-data  -e SETTINGS_FLAVOR=prod  -e DOCKER_REGISTRY_CONFIG=/registry-conf/config.yml  -d -p 5000:5000 registry
