#!/usr/bin/python3
'''Module 3-deploy_web_static
Streamlines website deployment. Creates archive of the website,
puts the archive on the web servers and makes the site available to
view'''
from fabric.api import *
from os.path import exists
from datetime import datetime
env.hosts = ['54.237.51.137', '54.85.131.160']


def do_pack():
    '''Generates a .tgz archive from the contents of the web_static folder
    '''
    try:
        local('mkdir -p versions')
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        local('tar -cvzf versions/web_static_{}.tgz web_static'.format(time))
        return 'versions/web_static_{}.tgz'.format(time)
    except Exception:
        return None


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


def deploy():
    '''Creates and distributes an archive to your web servers
    '''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
