ched How To Start
### Memcached Docker Start

```
#/bin/bash
IMG=192.168.60.37:5000/sameersbn/memcached
docker run -p 11211:11211 -d --name=test-memcached $IMG
```
###memcached login
* telnet {ip} {port} 

* example:    
  `telnet 192.168.60.38 11211`
