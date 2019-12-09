exec { 'killmenow':
  path    => '/usr/bin/',
  command => 'pkill -f ./killmenow',
}
