Summary: Networking utility that manages TCP and UDP connections
Name: netcat
Version: 0.7.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://netcat.sourceforge.net/
Source: http://prdownloads.sourceforge.net/netcat/netcat-%{version}.tar.bz2
Packager: Giovanni Giacobbi <giovanni@giacobbi.net>
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Netcat is a featured networking utility which reads and writes data across
network connections, using the TCP/IP protocol.
It is designed to be a reliable "back-end" tool that can be used directly or
easily driven by other programs and scripts. At the same time, it is a
feature-rich network debugging and exploration tool, since it can create
almost any kind of connection you would need and has several interesting
built-in capabilities.

%prep
%setup -q

%build
%configure
#configure --program-suffix= --program-prefix=

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"
unlink $RPM_BUILD_ROOT/usr/bin/nc
rm -rf $RPM_BUILD_ROOT/usr/share/info/dir

# ugly hack in order to include the structured directory in the rpm
rm -f doc/drafts/Makefile*

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/migration doc/drafts

%{_bindir}/netcat
##%{_bindir}/nc

%{_infodir}/*
%{_mandir}/*/*

%post
## /sbin/install-info %{_infodir}/netcat.info.gz %{_infodir}/dir

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete %{_infodir}/netcat.info.gz %{_infodir}/dir
fi

%changelog
* Sun Jan 11 2004 Giovanni Giacobbi <giovanni@giacobbi.net> 0.7.1-1
- Minor spec file cleanup
- Updated to version 0.7.1.

* Thu Aug 21 2003 Giovanni Giacobbi <giovanni@giacobbi.net> 0.7.0-1
- Updated to version 0.7.0.

* Tue Oct 15 2002 Giovanni Giacobbi <giovanni@giacobbi.net> 0.6.1-1
- Updated author's email address.
- Now adds info entries in the global info directory on install.
- Updated to version 0.6.1.

* Thu Aug 22 2002 Giovanni Giacobbi <giovanni@giacobbi.net> 0.6.0-1
- Final updates for the public release.

* Tue Aug 20 2002 Giovanni Giacobbi <giovanni@giacobbi.net> 0.6.0-0.5
- Some updates, still testing for first public release.

* Sat Jun 15 2002 Giovanni Giacobbi <giovanni@giacobbi.net> 0.5.1-1
- First testing package v0.5.1.
