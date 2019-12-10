# installs ver 2.1.1 of puppet linter

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
