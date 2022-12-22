#!/usr/bin/python3
'''Module 2-do_deploy_web_static
Distributes an archive to your web servers, using do_deploy()
'''
from fabric.api import *
from os.path import exists
env.hosts = ['54.237.51.137', '54.85.131.160']


def do_deploy(archive_path):
    '''Distributes an archive to your web servers
    '''
    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        filename = archive_path.split('/')[-1]
        folder = filename.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}'.format(folder))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
            filename, folder))
        run('rm /tmp/{}'.format(filename))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}'.format(folder, folder))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(folder))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} \
            /data/web_static/current'.format(
            folder))
        return True
    except Exception:
        return False
