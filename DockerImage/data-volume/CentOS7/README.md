This docker support some specific volume.
cotains: 
mysql  pgsql  httpd  voip  spacewalk


To build the image

# docker build --rm -t rhcentos7/data-volume:latest .


Launching data-volume for pgsql 
#docker run -d -v /home/smit/dockershare/pgsql:/opt/dockershare/pgsql --name=pgsql-data  rhcentos7/data-volume 
#docker run -d -v /home/smit/dockershare/spacewalk:/opt/dockershare/spacewalk -v /home/smit/dockershare/httpd:/opt/dockershare/httpd -v /home/smit/dockershare/mysql:/opt/dockershare/mysql -v /home/smit/dockershare/voip:/opt/dockershare/voip  --name=data-volume  rhcentos7/data-volume


#docker run -d -v /opt/dockershare/spacewalk:/opt/dockershare/spacewalk -v /opt/dockershare/httpd:/opt/dockershare/httpd -v /opt/dockershare/mysql:/opt/dockershare/mysql -v /opt/dockershare/voip:/opt/dockershare/voip  --name=data-volume  rhcentos7/data-volume

