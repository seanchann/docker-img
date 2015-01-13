#!/bin/bash

cp -rf /home/smit/project/voip/opensips/voip-server-publish .
rm -rf ./voip-server
mv -f ./voip-server-publish ./voip-server
tar -czf voip-server.tar.gz ./voip-server
