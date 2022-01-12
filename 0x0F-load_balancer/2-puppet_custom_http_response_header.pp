#automate the task of creating a custom HTTP header response, but with Puppet.
package { 'nginx':
  ensure => 'installed'
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World'
}

exec { 'modify-default':
  command  => 'sudo sed -i "/server_name _;/a \\\n\\tadd_header X-Served-By $HOSTNAME;"\
    /etc/nginx/sites-available/default;
	       sudo sed -i "/add_header*/a \\\n\\trewrite ^/redirect_me http://www.github.com/jbocane6 permanent;"\
    /etc/nginx/sites-available/default;
	       sudo sed -i "/rewrite*/a \\\n\\terror_page 404 /404.html;\\n\\n\\tlocation = /404.html {\\n\\t\\tinternal;\\n\\t}"\
    /etc/nginx/sites-available/default;',
  provider => shell,
  require  => Package['nginx']
}

service { 'nginx':
  ensure  => 'running',
  require => Exec['modify-default']
}
