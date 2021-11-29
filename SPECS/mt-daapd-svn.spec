Summary: A multi-threaded implementation of Apple's DAAP server
Name: mt-daapd-svn
Version: 1696
Release: 14
Epoch: 0
License: GPL
Packager: Casper Pedersen <cpedersen[at]c-note.dk>
Group: Development/Networking
URL: http://nightlies.mt-daapd.org/dl.php?FILE=%{name}-%{version}.tar.gz
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: libid3tag 
Requires: sqlite >= 3
BuildRequires: libid3tag-devel 
BuildRequires: sqlite-devel >= 3
# Obsoletes: mt-daapd-svn < %{version}

%description
A multi-threaded implementation of Apple's DAAP server, mt-daapd
allows a Linux machine to advertise MP3 files to to used by 
Windows or Mac iTunes clients.  This version uses Apple's ASPL Rendezvous
daemon.

%prep
%setup -q

%build
./configure --prefix=/usr --libdir=$RPM_BUILD_ROOT/%{_libdir} --enable-sqlite3 --enable-mdns

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr 
mkdir -p $RPM_BUILD_ROOT/%{_initrddir}
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/cache/mt-daapd
# cat contrib/init.d/mt-daapd-fedora.templ |  sed '/daemon/{s/\@prefix\@/\/usr/g}' | sed 's/\@prefix@//g' > $RPM_BUILD_ROOT/%{_initrddir}/mt-daapd
cat contrib/mt-daapd.conf | sed 's/\@prefix\@/\/usr/g' | sed '/^playlist/{s/\/usr//g}' | sed 's/\db_type = sqlite/db_type = sqlite3/g' | sed 's/\@dbdir\@/\/var\/cache\/mt-daapd/g' >  $RPM_BUILD_ROOT/%{_sysconfdir}/mt-daapd.conf
cat contrib/init.d/mt-daapd-fedora | sed 's/\/usr\/etc/\/etc/g' | sed 's/daapd.conf/mt-daapd.conf/g' > $RPM_BUILD_ROOT/%{_initrddir}/mt-daapd
if [ -f contrib/mt-daapd.playlist ] ; then
  cp contrib/mt-daapd.playlist $RPM_BUILD_ROOT/%{_sysconfdir}
fi

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(755,nobody,-) %config(noreplace) /%{_sysconfdir}/mt-daapd.conf
%attr(755,nobody,-) %{_localstatedir}/cache/mt-daapd
%attr(755,-,-) %{_initrddir}/mt-daapd
%{_sbindir}/mt-daapd
%{_datadir}/mt-daapd/*
%{_bindir}/mt-daapd-ssc.sh
%{_bindir}/wavstreamer
%{_libdir}/mt-daapd/plugins
%doc README NEWS TODO COPYING CREDITS INSTALL 


%changelog
* Thu Jan 15 2008 Casper Pedersen <c-note.dk> 1696-14
- x86-64

* Wed Nov 21 2007 Casper Pedersen <cpedersen[at]c-note.dk> 1696-13
- %config(noreplace) for /etc/mt-daapd.conf - will create a rpmnew instead of rpmsave

* Wed Oct 31 2007 Casper Pedersen <cpedersen[at]c-note.dk> 1696-12
- Update to SVN Build 1696
- Fix for /usr/lib/mt-daapd in mt-daapd.conf

* Fri Oct 19 2007 Casper Pedersen <cpedersen[at]c-note.dk> 1676-11
- Update to SVN Build 1676

* Tue Jun 5 2007 Casper Pedersen <cpedersen[at]c-note.dk> 1586-10
- Update to SVN Build 1586

* Thu Apr 19 2007 Casper Pedersen <cpedersen[at]c-note.dk> 1545-9
- Update to SVN Build 1545

* Mon Apr 2 2007 Casper Pedersen <cpedersen[at]c-note.dk> 1518-8
- Update to SVN Build 1518

* Thu Mar 29 2007 Casper Pedersen <cpedersen[at]c-note.dk> 1515-7
- Update to SVN Build 1515

* Thu Mar 1 2007 Casper Pedersen <cpedersen[at]c-note.dk> 1498-6
- Update to SVN Build 1498

* Sat Dec 23 2006 Casper Pedersen <cpedersen[at]c-note.dk> 1463-5
- Update to SVN Build 1463

* Mon Dec 11 2006 Casper Pedersen <cpedersen[at]c-note.dk> 1450-4
- Update to SVN Build 1450

* Fri Oct 20 2006 Casper Pedersen <cpedersen[at]c-note.dk> 1400-3
- SVN Build 1400

* Sun Oct 15 2006 Casper Pedersen <cpedersen[at]c-note.dk> 1393-2
- SVN Build 1393
- made mt-daapd.conf and /var/cache/mt-daapd writeable for nobody

* Sat Sep 16 2006 Casper Pedersen <cpedersen[at]c-note.dk> 1376-1
- SVN Build 1376

* Tue Jan 18 2005 ron <ron@pedde.com>
- Update to 0.2.1, add oggvorbis

* Tue Jun 01 2004 ron <ron@pedde.com>
- Update to 0.2.0

* Mon Apr 06 2004 ron <ron@pedde.com>
- Update to 0.2.0-pre1
- Add /var/cache/mt-daapd

* Thu Jan 29 2004 ron <ron@pedde.com>
- Update to 0.1.1

* Fri Nov 14 2003 root <root@hafnium.corbey.com> 
- Initial build.


