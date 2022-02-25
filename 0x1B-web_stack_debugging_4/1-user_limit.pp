# Change the OS configuration so that it is possible to login
# with the holberton user and open a file without any error message.

exec { 'fix ulimit':
  command  => 'sed -i "56,57d" /etc/security/limits.conf',
  provider => 'shell'
}
