# Using Puppet, create a file in /tmp.
file { 'Holberton file':
  ensure  =>  'present',
  path  =>  '/tmp/school',
  mode  =>  '0744',
  owner =>  'www-data',
  group =>  'www-data',
  content =>  'I love Puppet'
}
