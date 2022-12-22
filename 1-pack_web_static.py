#!/usr/bin/python3
'''Module 1-web_pack_static
Packs the static web page folder web_static into a .tgz file
'''
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    '''Packs the static web page folder web_static into a .tgz file
    '''
    now = datetime.now()
    date = now.strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(file_name))
    if os.path.exists(file_name):
        return file_name
    else:
        return None
