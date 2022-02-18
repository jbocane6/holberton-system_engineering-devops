# Using strace, find out why Apache is returning 500 error. Fix & automate it
exec { 'fix phpp':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => ['/usr/bin', '/bin']
}
