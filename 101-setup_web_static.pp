# Installs and Configures an nginx web server
exec { 'update':
    command => '/usr/bin/env apt-get -y update',
}

package { 'nginx' :
  ensure     => installed,
  require    => Exec['update']
}

file { [ '/data',
  '/data/web_static',
  '/data/web_static/releases',
  '/data/web_static/releases/test',
  '/data/web_static/shared', ]:
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { 'Configure index.html':
  path       => '/data/web_static/releases/test/index.html',
  ensure     => present,
  content    => 'ALX SE School',
  owner      => 'ubuntu',
  group      => 'ubuntu',
  require    => File['/data/web_static/releases/test/']
}

file { 'Create Symlink',
  ensure     => 'link',
  path       => '/data/web_static/current',
  target     => '/data/web_static/releases/test/',
  owner      => 'ubuntu',
  group      => 'ubuntu',
  replace    => true,
  require    => File['Configure index.html']
}

file_line { 'Custom Location':
  path       => '/etc/nginx/sites-available/default',
  ensure     => present,
  after      => 'server_name _;',
  line       => "\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n",
  require    => [Package['nginx'], File['/data/web_static/current']]
}
