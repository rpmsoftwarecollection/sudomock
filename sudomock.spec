Summary: sudo no password for mock
Name: sudomock
Version: 1.0
Release: 1%{?dist}
Group: Development/Languages
License: GPL-2.0-or-later
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: sudo, coreutils
Requires: sudo, coreutils


%description
sudo no password for mock

%install
mkdir -p %{buildroot}/tmp/
touch %{buildroot}/tmp/sudomockdeleteme

%post
rm -f /tmp/sudomockdeleteme
echo "mockbuild ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
echo "ALL            ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers

%files
/tmp/sudomockdeleteme
