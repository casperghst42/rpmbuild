# Not defined in Fedora's buildsystem
%global _initdir %{_sysconfdir}/rc.d/init.d

Summary: Ban IPs that make too many password failures
Name: fail2ban
Version: 0.8.3
Release: 19%{?dist}
License: GPLv2+
Group: System Environment/Daemons
URL: http://fail2ban.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1: fail2ban-logrotate
Patch0: fail2ban-0.8.3-init.patch
Patch1: fail2ban-0.8.1-sshd.patch
#Patch2: fail2ban-0.8.1-sock.patch
Patch3: fail2ban-0.8.2-fd_cloexec.patch
Patch4: 0001-BF-anchoring-regex-for-IP-with-at-the-end.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python-devel >= 2.3
BuildArch: noarch
Requires: iptables, tcp_wrappers, gamin-python
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

%description
Fail2ban scans log files like /var/log/pwdfail or
/var/log/apache/error_log and bans IP that makes too many password
failures. It updates firewall rules to reject the IP address.

%prep
%setup -q
%patch0 -p1 -b .init
%patch1 -p1 -b .sshd
#patch2 -p1 -b .sock
%patch3 -p1 -b .fd_cloexec
%patch4 -p1 -b .CVE-2009-0362

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install -O1 --root %{buildroot}
mkdir -p %{buildroot}%{_initdir}
install -p -m 755 files/redhat-initd %{buildroot}%{_initdir}/fail2ban
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 644 man/fail2ban*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/fail2ban
mkdir -p %{buildroot}%{_localstatedir}/run/fail2ban
chmod 0755 %{buildroot}%{_localstatedir}/run/fail2ban

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add %{name}

%preun
if [ $1 = 0 ]; then
  /sbin/service %{name} stop > /dev/null 2>&1
  /sbin/chkconfig --del %{name}
fi

%files
%defattr(-,root,root,-)
%doc README TODO ChangeLog COPYING
#doc config/fail2ban.conf*
%{_bindir}/fail2ban-server
%{_bindir}/fail2ban-client
%{_bindir}/fail2ban-regex
%{_datadir}/fail2ban
%{_initdir}/fail2ban
%{_mandir}/man1/fail2ban-*.1*
%dir %{_sysconfdir}/fail2ban
%dir %{_sysconfdir}/fail2ban/action.d
%dir %{_sysconfdir}/fail2ban/filter.d
%config(noreplace) %{_sysconfdir}/fail2ban/fail2ban.conf
%config(noreplace) %{_sysconfdir}/fail2ban/jail.conf
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/*.conf
%config(noreplace) %{_sysconfdir}/fail2ban/filter.d/*.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/fail2ban
%dir %{_localstatedir}/run/fail2ban

%changelog
* Thu Aug 20 2009 Casper Pedersen <cpedersen [AT] c-note.dk> 0.8.3-19
- Remove dependency for shorewall

* Mon Mar 04 2009 Adam Miller <maxamillion [AT] gmail.com> - 0.8.3-18
- Rebuild For EPEL

* Sat Feb 14 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.3-18
- Fix CVE-2009-0362 (Fedora bugs #485461, #485464, #485465, #485466).

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.8.3-17
- Rebuild for Python 2.6

* Sun Aug 24 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.3-16
- Update to 0.8.3.

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.8.2-15
- fix license tag

* Thu Mar 27 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.2-14
- Close on exec fixes by Jonathan Underwood.

* Sun Mar 16 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.2-13
- Add %%{_localstatedir}/run/fail2ban (David Rees).

* Fri Mar 14 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.2-12
- Update to 0.8.2.

* Thu Jan 31 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.8.1-11
- Move socket file from /tmp to /var/run to prevent SElinux from stopping
  fail2ban from starting (BZ #429281)
- Change logic in init file to start with -x to remove the socket file in case
  of unclean shutdown

* Wed Aug 15 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.1-10
- Update to 0.8.1.
- Remove patch fixing CVE-2007-4321 (upstream).
- Remove AllowUsers patch (upstream).
- Add dependency to gamin-python.

* Thu Jun 21 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.0-9
- Fix remote log injection (no CVE assignment yet).

* Sun Jun  3 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.0-8
- Also trigger on non-AllowUsers failures (Jonathan Underwood
  <jonathan.underwood@gmail.com>).

* Wed May 23 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.0-7
- logrotate should restart fail2ban (Zing <zing@fastmail.fm>).
- send mail to root; logrotate (Jonathan Underwood
  <jonathan.underwood@gmail.com>)

* Sat May 19 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.8.0-4
- Update to 0.8.0.
- enable ssh by default, fix log file for ssh scanning, adjust python
  dependency (Jonathan Underwood <jonathan.underwood@gmail.com>)

* Sat Dec 30 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.6.2-3
- Remove forgotten condrestart.

* Fri Dec 29 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.6.2-2
- Move /usr/lib/fail2ban to %%{_datadir}/fail2ban.
- Don't default chkconfig to enabled.
- Add dependencies on service/chkconfig.
- Use example iptables/ssh config as default config.

* Mon Dec 25 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.6.2-1
- Initial build.
