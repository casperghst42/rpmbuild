Name:         gnump3d
License:      GPL
Group:        Productivity/Networking/Web/Servers
Version:      2.9.5
Release:      5
Packager:     Casper Pedersen <cpedersen[at]c-note.dk>
URL:	      http://www.gnu.org/software/gnump3d/
Summary:      GNU MP3 Streaming Server
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Source:       http://savannah.gnu.org/download/gnump3d/gnump3d-%{version}.tar.gz
Source1:      gnump3d.logrotate
Patch0:       gnump3d-makefile.diff
Patch1:	      gnump3d.conf.diff
BuildArch:    noarch
Requires:     perl >= 5.8.4
Requires:     /bin/sh
Provides:     perl(gnump3d::readtags)

%description
gnump3d is a simple server allows you to stream MP3's and OGG Vorbis
files across a network.

%prep
%setup -q
%patch0
%patch1

%build

%install
rm -Rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/var/log/gnump3d
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
mkdir -p $RPM_BUILD_ROOT/etc/init.d

install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/logrotate.d/gnump3d
install -m 644 rcfiles/redhat $RPM_BUILD_ROOT/etc/init.d/gnump3d

%clean
if [ -n "$RPM_BUILD_ROOT" ] ; then
   rm -rf $RPM_BUILD_ROOT
fi


%pre
/usr/sbin/useradd -r -o -g nobody -u 63 -s /bin/false -c "GNUMP3 daemon" -d /var/lib/nobody gnump3d 2> /dev/null || :

%post
test -f /var/log/gnump3d/access.log || {
  touch /var/log/gnump3d/access.log;
  chmod 640 /var/log/gnump3d/access.log;
  chown gnump3d /var/log/gnump3d/access.log
}

%preun
%postun

%files
%defattr(-,root,root)
%doc COPYING AUTHORS README TODO
%doc %{_mandir}/man1/*
%dir /etc/gnump3d/*
/usr/share/gnump3d/*
/usr/lib/perl5/*/gnump3d
%{_bindir}/gnump3d*
%attr(755,root,root) /etc/init.d/gnump3d
%config(noreplace) /etc/logrotate.d/gnump3d
%attr(755,gnump3d,root) %dir /var/log/gnump3d
%attr(755,gnump3d,root) %dir /var/cache/gnump3d
%attr(755,gnump3d,root) %dir /var/cache/gnump3d/serving

%changelog -n gnump3d
* Tue Oct 11 2005 - cpedersen[at]c-note.dk	2.9.5-5
- Cleaned up the spec file
- Made it work on Redhat/Fedora
* Fri Sep 23 2005 - cpedersen@novell.com	2.9.5-4
- Update to version 2.9.5
* Wed May 19 2004 - kukuk@suse.de
- Update to version 2.8
* Tue Feb 24 2004 - hmacht@suse.de
- building as non-root
* Wed Jan 28 2004 - tsieden@suse.de
- Removed the "german umlauts" fix because it will break the
  UTF-8 compatibility
* Mon Jan 26 2004 - tsieden@suse.de
-  Update to 2.6
-  Fix handling of german umlauts in generated playlists
* Sat Dec 20 2003 - tsieden@suse.de
- added 'next unless $data;' to gnump3d2 (bug #33066)
  (originated by mls@suse.de)
* Fri Aug 29 2003 - kukuk@suse.de
- Call useradd with -r for system account [Bug #29611]
* Wed Jul 30 2003 - kukuk@suse.de
- Try to restart the server on update
* Fri Jul 25 2003 - kukuk@suse.de
- Update to 2.5b
* Mon Feb 17 2003 - kukuk@suse.de
- Update to 2.2 (reimplemented in perl)
* Fri Jan 10 2003 - kukuk@suse.de
- Update to final 1.0 release
* Fri Aug 30 2002 - kukuk@suse.de
- Add own "gnump3d" user, so that logfiles are not owned by nobody.
- Fix handling of logfiles after rotation (gnump3d creates the
  first log file as root and tries to modify it later as gnump3d).
- Add config file for logroration
* Sat Aug 24 2002 - kukuk@suse.de
- Update to final tar archive for 1.0-pre1 (includes libtool fixes)
* Mon Aug 12 2002 - kukuk@suse.de
- Update to current CVS version
* Wed Jul 24 2002 - kukuk@suse.de
- Initial version
