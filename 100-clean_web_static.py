#!/usr/bin/python3
'''Module 100-clean_web_static.py
Deletes out-of-date archives, using the function do_clean'''
from fabric.api import *


def do_clean(number=0):
    '''Deletes out-of-date archives
    '''
    number = int(number)
    if number == 0 or number == 1:
        number = 2
    else:
        number += 1
    local('ls -t versions | tail -n +{} | xargs rm -rf'.format(number))
    run('ls -t /data/web_static/releases | tail -n +{} | xargs rm -rf'
        .format(number))
