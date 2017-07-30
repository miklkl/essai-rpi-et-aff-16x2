#!/usr/bin/env python
# -*- coding: utf-8 -*-

##### Modules #####
import socket
import os
##### Variables #####
gw = os.popen("ip -4 route show default").read().split()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw[2], 0))
ipaddr = s.getsockname()[0]
host = socket.gethostname()

##### Programme #####

print ("IP:", ipaddr," Host:", host)