Summary: Forwards compatibility package for python(abi).
Name: pythonabi
Version: 2.3.4
Release: 14
Epoch: 1
License: GPL
Group: Development/Languages
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python = %{version}
Provides: python(abi) = %(echo %{version} | awk -F. '{print $1 "." $2}')

%description
Forwards compatibility package for python(abi).

%files
%defattr(-,root,root,-)

%changelog
* Mon Dec 26 2005 Casper Pedersen <cpedersen[at]c-note.dk>
- CentOS4
- Updated

* Mon Jan  3 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.


