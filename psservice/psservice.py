#!/usr/bin/python3
# coding: utf-8
import psutil
import os
import requests

check = False
pid_file = "/var/run/nginx.pid"
# Website availability check
try:
    r = requests.get('http://localhost:80')
    if r.status_code == 200:
        pass
except requests.exceptions.ConnectionError:
    print("Error! Service nginx status is not 200")

# Check nginx.pid exists
if not os.path.exists(pid_file):
    print("Error! File nginx.pid does not exist")

# Get info process and port and name
try:
    for proc in psutil.process_iter():
        for connect in proc.connections(kind='inet'):
            if connect.laddr.port == 80 and proc.name() == 'nginx':
                check = True
    if check:
        print("OK! Service nginx is running")
    else:
        print("Warning! Service nginx is not running")
except psutil.AccessDenied:
    print("Permission denied. Use sudo to run the script")
