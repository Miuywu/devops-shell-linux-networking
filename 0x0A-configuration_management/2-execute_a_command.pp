# puppet exec then puppet kill

exec { 'killmenow':
  path    => '/usr/bin/',
  command => 'pkill -f killmenow',
}
