This support docker registry  storage manager web ui.
Thsi project base on docker-registry

First pull your registry from docker hub:
# docker pull atcol/docker-registry-ui


build your data volume£º
# docker run -v /opt/dockershare/registry/web-data:/var/lib/h2 --name=registry_web_data  atcol/docker-registry-ui true

run your registry web ui:
# docker run  --name=registry-ui -d  -p 8091:8080 --volumes-from=registry_web_data  atcol/docker-registry-ui

Note:when restart this container if you not rm /opt/dockershare/registry/web-data/*.lock.db, then
this ui will not work for you.
