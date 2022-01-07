package { 'nginx':
  ensure => 'installed'
}

file { '/var/www/html/index.html':
  content => 'Hello World'
}

file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me https:www.github.com/jbocane6/ permanent;'
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx']
}
