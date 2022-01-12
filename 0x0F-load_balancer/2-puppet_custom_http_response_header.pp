#automate the task of creating a custom HTTP header response, but with Puppet.
package { 'nginx':
  ensure => 'installed'
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World'
}

file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => '\trewrite ^/redirect_me github.com/jbocane6 permanent\n\terror_page 404 /error404.html;\nlocation =  /error404.html {\n\troot /var/www/html/;\n\tinternal;\n};\n\tadd_header X-Served-By "$HOSTNAME";'
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx']
}
