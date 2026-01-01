Summary: sudo no password for mock
Name: sudomock
Version: 1.0
Release: 2%{?dist}
Group: Development/Languages
License: GPL-2.0-or-later
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: sudo, coreutils
Requires: sudo, coreutils
Source1: https://raw.githubusercontent.com/rpmsoftwarecollection/sudomock/refs/heads/master/php56build.repo


%description
sudo no password for mock

%install
mkdir -p %{buildroot}/tmp/
touch %{buildroot}/tmp/sudomockdeleteme
mkdir -p %{buildroot}/etc/yum.repos.d/
cp %{SOURCE1} %{buildroot}/etc/yum.repos.d/

%post
rm -f /tmp/sudomockdeleteme
echo "mockbuild ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
echo "ALL            ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers

%files
/tmp/sudomockdeleteme
/etc/yum.repos.d/php56build.repo
