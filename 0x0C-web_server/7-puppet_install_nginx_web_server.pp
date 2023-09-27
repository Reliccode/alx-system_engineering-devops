# Class to install and configure Nginx
class nginx_web_server {
  package { 'nginx':
    ensure => 'installed',
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
  }

  file { '/var/www/html/index.html':
    ensure  => 'file',
    content => 'Hello World!',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    source  => 'puppet:///modules/nginx_web_server/default',
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/redirect':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
    notify  => Service['nginx'],
  }
}

# Apply the class to node
node 'default' {
  include nginx_web_server
}
