Name:           vpnc-nortel
Version:        0.5.2
Release:        2
Summary:        IPSec VPN client - for Nortel
Group:          Applications/Internet
License:        GPL
URL:            http://svn.unix-ag.uni-kl.de/vpnc/branches/vpnc-nortel/
Source0:        vpnc-nortel-%{version}.tar.gz
Source1:        default.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libgcrypt-devel
Requires:       libgcrypt

%description
A VPN client compatible with Nortel Contivity equipment.

Supports IPSec (ESP) with Mode Configuration and Xauth.  Supports only
shared-secret IPSec authentication, 3DES, MD5, and IP tunneling.

%prep
%setup -q -n %{name}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/vpnc
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8

install -m 755 vpnc $RPM_BUILD_ROOT%{_sbindir}
install -m 755 pcf2vpnc $RPM_BUILD_ROOT%{_sbindir}

install -m 600 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/vpnc
install -m 755 vpnc-disconnect $RPM_BUILD_ROOT%{_sysconfdir}/vpnc
install -m 755 vpnc-script $RPM_BUILD_ROOT%{_sysconfdir}/vpnc

install -m 644 vpnc.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 pcf2vpnc.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 cisco-decrypt.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog VERSION split_tunnel.txt
%doc %{_mandir}/man1/*
%doc %{_mandir}/man8/*
%dev(c, 10, 200) /dev/tun
%config(noreplace) /etc/vpnc/default.conf
%config /etc/vpnc/*
%{_sbindir}/*

%changelog
* Sun Aug 30 2009 Casper Pedersen <cpedersen@novell.com> 0.5.2-2
- added split_tunnel.txt

* Tue Aug 25 2009 Casper Pedersen <cpedersen@novell.com> 0.5.2-1
- build vpnc-nortel

* Wed Jan 05 2005 Warren Togami <wtogami@redhat.com> 0.3.2-3
- Fix 64bit

* Thu Dec 23 2004 Warren Togami <wtogami@redhat.com> 0.3.2-2
- make PIE (davej)

* Mon Dec 20 2004 Warren Togami <wtogami@redhat.com> 0.3.2-1
- 0.3.2

