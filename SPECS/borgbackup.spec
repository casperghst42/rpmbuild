%global srcname borgbackup
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

Name:           %{srcname}
Version:        1.1.1
Release:        1%{?dist}
Summary:        A deduplicating backup program with compression and authenticated encryption

License:        BSD
URL:            https://borgbackup.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

Patch0:         0001-utf8-to-unicode-string-literal.patch
Patch1:         0002-disable-sphinx-man-page-build.patch

# build
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  python%{python3_pkgversion}-llfuse

# test
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-msgpack >= 0.4.6

# docs
%if 0%{?rhel}
# python3-sphinx packages are not available in epel
# so we use the old python2
BuildRequires:  python-sphinx
%else
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

# no python deps
BuildRequires:  openssl-devel >= 1.0.0
BuildRequires:  lz4-devel
BuildRequires:  fuse-devel
BuildRequires:  libacl-devel

Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-msgpack >= 0.4.6
Requires:       python%{python3_pkgversion}-llfuse
Requires:       fuse

%description
BorgBackup (short: Borg) is a deduplicating backup program. Optionally, it
supports compression and authenticated encryption.

%prep
%setup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

# epel only has python2-sphinx and python2 has some problems
# with utf8 and it needs a patched docs until
# there is a python3 of sphinx
%patch0 -p1

# we don't need the guzzley_sphinx theme for only man page generation
%patch1 -p1

%build
%py3_build

# MANPAGE GENERATION
# workaround to dump sphinx_rtd_theme dependency - not needed for manpages
export READTHEDOCS=True

# workaround to include borg module for usage generation
export PYTHONPATH=$(pwd)/build/$(ls build/ | grep 'lib.')

%if 0%{?rhel}
make -C docs man
%else
make -C docs SPHINXBUILD=sphinx-build-3 man
%endif

%install
find . -name *.so -type f -exec chmod 0755 {} \;

%py3_install
install -D -m 0644 docs/_build/man/borg*.1* %{buildroot}%{_mandir}/man1/borg.1

%check
export PYTHONPATH=$(pwd)/build/$(ls build/ | grep 'lib.')

# workaround to prevent test issues with ascii/utf-8 under rhel 7
%if 0%{?rhel} || 0%{?fedora} == 25
export LANG=en_US.UTF-8
%endif

# exclude test_fuse: there is no modprobe in mock for fuse
# exclude test_non_ascii_acl: problem with mock
# exclude benchmark: not relevant for package build
# exclude test_dash_open: pytest stub has a bug and is fixed in 3.0.2 (epel7 uses 2.8.5
py.test-3 -vk "not test_non_ascii_acl and not test_fuse and not benchmark and not test_dash_open" $PYTHONPATH/borg/testsuite/*.py

%files 
%license LICENSE
%doc README.rst PKG-INFO AUTHORS
%doc docs/changes.rst
%{_mandir}/man1/*

%{python3_sitearch}/*
%{_bindir}/borg
%{_bindir}/borgfs


%changelog
* Wed Nov 01 2017 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.1.1-1
- upstream version 1.1.1

* Mon Oct 09 2017 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.1.0-1
- upstream version 1.1.0 (BZ#1499512)
- added missing fuse dependency (BZ#1493434)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.11-3
- removed sphinx_rtd_theme dependency

* Sat Jul 29 2017 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.11-1
- upstream version 1.0.11 (BZ#1473897)
- removed setup.py build_api

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.10-1
- upstream version 1.0.10 (BZ#1421660)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.9-1
- upstream version 1.0.9 (BZ#1406277)
- fix manifest spoofing vulnerability - see docs for info

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.8-3
- Rebuild for Python 3.6

* Mon Oct 31 2016 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.8-2
- upstream version 1.0.8 (BZ#1389986)

* Sun Aug 21 2016 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.7-1
- security fix with borg serve and restrict-to-path (BZ#1354371)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.6-1
- upstream version 1.0.6 (BZ#1354371)
- update source url (now pointing to files.pythonhosted.org)
- testsuite on XFS is patched upstream

* Fri Jul 01 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.3-2
- Fix testsuite on XFS (#1331820)

* Sun May 22 2016 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.3-1
- Added requires for setuptools (BZ#1335325)
- upstream version 1.0.3

* Thu Apr 28 2016 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.2-2
- rebuilt

* Thu Apr 28 2016 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.2-2
- Missing dependency python-setuptools

* Sun Apr 17 2016 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.2-1
- added epel7 specific parts
- make manpage generation work with epel7
- upstream version 1.0.2

* Sat Apr 16 2016 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.1-2
- simplified specfile
- removed unneeded dependencies: python3-mock, python3-pytest-cov

* Sun Apr 10 2016 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.1-1
- Upstream version 1.0.1. see changelog

* Thu Apr 07 2016 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.0-2
- Added requires for python3-llfuse (#1324685)
- Added minversion for openssl

* Mon Apr 04 2016 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.0.0-1
- Upstream version 1.0.0
- Rewrote build requirements for EPEL7

* Thu Dec 17 2015 Benjamin Pereto <benjamin@sandchaschte.ch> - 0.29.0-3
- Specified correct project URL
- Added Buildrequires python3-sphinx_rtd_theme for f23

* Thu Dec 17 2015 Benjamin Pereto <benjamin@sandchaschte.ch> - 0.29.0-2
- Cleanup Spec
- Rename package to borgbackup
 
* Mon Dec 14 2015 Benjamin Pereto <benjamin@sandchaschte.ch> - 0.29.0-1
- New Upstream Version
- Added manpage from Upstream
- Testsuite now functional without benchmark

* Sat Dec 05 2015 Benjamin Pereto <benjamin@sandchaschte.ch> - 0.28.2-6
- Added correct testsuite to check
- Removed unnessesary statements

* Fri Dec 04 2015 Benjamin Pereto <benjamin@sandchaschte.ch> - 0.28.2-5
- Renamed Specfile to python3 only and remove pre-built egg-info

* Wed Dec 02 2015 Benjamin Pereto <benjamin@sandchaschte.ch> - 0.28.2-4
- Removed double package statement and sum macro

* Tue Dec 01 2015 Benjamin Pereto <benjamin@sandchaschte.ch> - 0.28.2-3
- Added dependency python3-msgpack to buildrequires

* Tue Dec 01 2015 Benjamin Pereto <benjamin@sandchaschte.ch> - 0.28.2-2
- Added dependency python3-msgpack

* Tue Dec 01 2015 Benjamin Pereto <benjamin@sandchaschte.ch> - 0.28.2-1
- Initial Packaging for the BorgBackup Project

