Name:	netatalk	
Version: 3.1.8
Release: 1%{?dist}
Summary: Netatalk is a freely-available Open Source AFP fileserver. 
Group: System Environment/Daemons
License: GPL2	
URL: http://netatalk.sourceforge.net/
Source0: http://download.sourceforge.net/netatalk/netatalk-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: cracklib-devel openssl-devel pam quota-devel libtool automake
BuildRequires: autoconf db4-devel pam-devel tcp_wrappers-devel libgcrypt-devel
BuildRequires: avahi-devel libacl-devel openldap-devel
Requires:	pam

%description
Netatalk is a freely-available Open Source AFP fileserver. A *NIX/*BSD system running Netatalk is capable of serving many Macintosh clients simultaneously as an AppleShare file server (AFP).

%package devel
Summary: Headers for Appletalk development
Group: Development/Libraries

%description devel
Headers for Netatalk


%prep
%setup -q

%build
#env LDFLAGS="-Wl,-R%{_libdir}/netatalk"  \
  ./configure --with-init-style=redhat-sysv \
  --bindir=%{_bindir} \
  --libdir=%{_libdir}/netatalk \
  --with-uams-path=%{_libdir}/netatalk \
  --sbindir=%{_sbindir} \
  --sysconfdir=%{_sysconfdir} \
  --mandir=%{_mandir} \
  --localstatedir=%{_var} \
  --includedir=%{_includedir} \
  --datarootdir=%{_datarootdir} \
  --with-init-style=redhat-systemd \
  --with-spotlight \
  --with-cnid-dbd-backend

#
# Add Library search path for libevent.
#
perl -i -pe 's!^LDFLAGS = !LDFLAGS = -rpath %{_libdir}/netatalk!' etc/netatalk/Makefile

make

%install
rm -rf %{BuildRoot}
make install DESTDIR=%{buildroot}
## mkdir -p %{BuildRoot}/lib/systemd/system


# Clean up .a and .la files
find $RPM_BUILD_ROOT -name \*.a -exec rm {} \;
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;

%clean
# rm -rf %{BuildRoot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/extmap.conf
%config(noreplace) %{_sysconfdir}/afp.conf
%config(noreplace) %{_sysconfdir}/pam.d/netatalk
%config(noreplace) %{_sysconfdir}/dbus-session.conf
%config(noreplace) %{_unitdir}/netatalk.service
%{_sbindir}/*
%{_bindir}/*
%exclude %{_bindir}/netatalk-config
%{_mandir}/man*/*
%exclude %{_mandir}/man*/netatalk-config*
%{_libdir}/netatalk/*
%{_var}/netatalk/*
##%{_sysconfdir}/rc.d/init.d/netatalk
#
# TODO: How to deal this script.
#
# %exclude %{_bindir}/event_rpcgen.py

%files devel
%defattr(-,root,root)
%dir %{_includedir}/atalk
%attr(0644,root,root) %{_includedir}/atalk/*
%{_datadir}/aclocal/netatalk.m4
%{_bindir}/netatalk-config
%{_mandir}/man*/netatalk-config.1*
#
# TODO: How to deal these files.
#
#%exclude %{_includedir}/event2
#%exclude %{_libdir}/netatalk/pkgconfig
#%exclude %{_includedir}/usr/include/ev*

%doc

%changelog
* Wed May 11 2016 Casper Pedersen <cpedersen at c-note.dk>
- CentOS 7

* Sun Feb 21 2016 Casper Pedersen <cpedersen at c-note.dk>
- updated to Netatalk 3.1.8

* Tue Sep 15 2015 Casper Pedersen <cpedersen at c-note.dk>
- updated to Netatalk 3.1.7

* Sat Sep 13 2014 Casper Pedersen <cpedersen at c-note.dk>
- updated to Netatalk 3.1.6

* Fri Apr 5 2013 Casper Pedersen <cpedersen at c-note.dk>
- updated to Netatalk 3.0.3

* Fri Jan 25 2013 Hiroyuki Sato <hiroysato at gmail.com> 
- patch removed. libevent search automatically. Thanks HAT.
- Update for 3.0.2. Thanks Svavar Orn.

* Fri Jan 11 2013 Initial Hiroyuki Sato <hiroysato at gmail.com> 
- Initial version.
