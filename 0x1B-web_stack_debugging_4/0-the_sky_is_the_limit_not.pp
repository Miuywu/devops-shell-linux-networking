# user request limit to 3000
exec { 'limit':command => "sed -i -e 's/15/3000/g' /etc/default/nginx; service nginx restart",path    => ['/bin', '/usr/bin', '/usr/sbin']}