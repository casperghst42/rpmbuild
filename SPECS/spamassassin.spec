%define real_name Mail-SpamAssassin
%define krb5backcompat %([ -a /usr/kerberos/include/krb5.h ] && echo 1 || echo 0)

%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Summary: Spam filter for email which can be invoked from mail delivery agents.
Name: spamassassin
Version: 3.0.6
Release: 1.el4
License: Apache License
Group: Applications/Internet
URL: http://spamassassin.apache.org/
Source0: http://www.apache.org/dist/%{name}/%{real_name}-%{version}.tar.bz2
Source2: redhat_local.cf
Source3: spamassassin-default.rc
Source4: spamassassin-spamc.rc
Source5: spamassassin.sysconfig
Source10: spamassassin-helper.sh
# Patches 0-99 are RH specific
# none yet
# Patches 100+ are SVN backports (DO NOT REUSE!)
Patch122: spamassassin-3.0.5-nls-spamd-init.patch
Patch123: spamassassin-3.0.5-RSL-removal.patch

# end of patches
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Buildroot: %{_tmppath}/%{name}-root
Requires: /sbin/chkconfig /sbin/service

BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(Net::DNS)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(HTML::Parser)
BuildRequires: openssl-devel

Requires: perl(Net::DNS)
Requires: perl(Time::HiRes)
Requires: perl(DB_File)
Requires: procmail

Obsoletes: perl-Mail-SpamAssassin

%description
SpamAssassin provides you with a way to reduce if not completely eliminate
Unsolicited Commercial Email (SPAM) from your incoming email.  It can
be invoked by a MDA such as sendmail or postfix, or can be called from
a procmail script, .forward file, etc.  It uses a genetic-algorithm
evolved scoring system to identify messages which look spammy, then
adds headers to the message so they can be filtered by the user's mail
reading software.  This distribution includes the spamd/spamc components
which create a server that considerably speeds processing of mail.

To enable spamassassin, if you are receiving mail locally, simply add
this line to your ~/.procmailrc:
INCLUDERC=/etc/mail/spamassassin/spamassassin-default.rc

To filter spam for all users, add that line to /etc/procmailrc
(creating if necessary).

%prep
%setup -q -n Mail-SpamAssassin-%{version}
# Patches 0-99 are RH specific
# none yet
# Patches 100+ are SVN backports (DO NOT REUSE!)
%patch122 -p1
%patch123 -p1
# end of patches

%build
export CFLAGS="$RPM_OPT_FLAGS"
%{__perl} Makefile.PL DESTDIR=$RPM_BUILD_ROOT/ SYSCONFDIR=%{_sysconfdir} INSTALLDIRS=vendor ENABLE_SSL=yes < /dev/null

%{__make} %{?krb5backcompat:SSLCFLAGS=-DSPAMC_SSL\ -I/usr/kerberos/include} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall PREFIX=%buildroot/%{prefix} \
	INSTALLMAN1DIR=%buildroot/%{_mandir}/man1 \
	INSTALLMAN3DIR=%buildroot/%{_mandir}/man3 \
	LOCAL_RULES_DIR=%{buildroot}/etc/mail/spamassassin
chmod 755 %buildroot/%{_bindir}/* # allow stripping
install -d %buildroot/%{_initrddir}
install -m 0755 spamd/redhat-rc-script.sh %buildroot/%{_initrddir}/spamassassin

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/local.cf
install -m644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/spamassassin

install -m 0644 %{SOURCE3} %buildroot/etc/mail/spamassassin
install -m 0644 %{SOURCE4} %buildroot/etc/mail/spamassassin
install -m 0755 %{SOURCE10} %buildroot/etc/mail/spamassassin

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -v {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'

find $RPM_BUILD_ROOT/usr -type f -print |
        sed "s@^$RPM_BUILD_ROOT@@g" |
        grep -v perllocal.pod |
        grep -v "\.packlist" > %{name}-%{version}-filelist
if [ "$(cat %{name}-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi
find $RPM_BUILD_ROOT%{perl_vendorlib}/* -type d -print |
        sed "s@^$RPM_BUILD_ROOT@%dir @g" >> %{name}-%{version}-filelist

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/spamassassin

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc BUGS LICENSE NOTICE CREDITS Changes README STATUS TRADEMARK UPGRADE
%doc USAGE sample-nonspam.txt sample-spam.txt
%config %{_initrddir}/spamassassin
%config(noreplace) %{_sysconfdir}/mail/spamassassin
%config(noreplace) %{_sysconfdir}/sysconfig/spamassassin
%dir %{_datadir}/spamassassin
%dir %{_localstatedir}/run/spamassassin

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add spamassassin

# -a and --auto-whitelist options were removed from 3.0.0
# prevent service startup failure
TMPFILE=$(/bin/mktemp /etc/sysconfig/spamassassin.XXXXXX) || exit 1
cp /etc/sysconfig/spamassassin $TMPFILE
perl -p -i -e 's/(["\s]-\w+)a/$1/ ; s/(["\s]-)a(\w+)/$1$2/ ; s/(["\s])-a\b/$1/' $TMPFILE
perl -p -i -e 's/ --auto-whitelist//' $TMPFILE
# replace /etc/sysconfig/spamassassin only if it actually changed
cmp /etc/sysconfig/spamassassin $TMPFILE || cp $TMPFILE /etc/sysconfig/spamassassin
rm $TMPFILE

if [ -f /etc/spamassassin.cf ]; then
	%{__mv} /etc/spamassassin.cf /etc/mail/spamassassin/migrated.cf
fi
if [ -f /etc/mail/spamassassin.cf ]; then
	%{__mv} /etc/mail/spamassassin.cf /etc/mail/spamassassin/migrated.cf
fi

%postun
if [ "$1" -ge "1" ]; then
    /sbin/service spamassassin condrestart > /dev/null 2>&1
fi
exit 0

%preun
if [ $1 = 0 ] ; then
    /sbin/service spamassassin stop >/dev/null 2>&1
    /sbin/chkconfig --del spamassassin
fi
exit 0

%changelog
* Fri Jun 02 2006 Warren Togami <wtogami@redhat.com> - 3.0.6-1
- CVE-2006-2447

* Tue May 09 2006 Warren Togami <wtogami@redhat.com> - 3.0.5-4
- Remove RCVD_IN_RSL (#191033)
- Preserve timestamp and context of /etc/sysconfig/spamassassin (#178580)

* Fri Jan 06 2006 Warren Togami <wtogami@redhat.com> - 3.0.5-3
- rebuild

* Thu Dec 01 2005 Warren Togami <wtogami@redhat.com> - 3.0.5-2
- #174579 nls initscript for i18n (Thanks Rudolf Kastl)

* Tue Nov 29 2005 Warren Togami <wtogami@redhat.com> - 3.0.5-1
- 3.0.5

* Tue Nov 08 2005 Warren Togami <wtogami@redhat.com> - 3.0.4-2
- 3.0.5 release candidate

* Sun Jun 05 2005 Warren Togami <wtogami@redhat.com> - 3.0.4-1
- 3.0.4 with more bug fixes and CAN-2005-1266

* Tue May 17 2005 Warren Togami <wtogami@redhat.com> - 3.0.3-4
- allow user-level disabling of subject rewriting pref (#147464)

* Wed Apr 27 2005 Warren Togami <wtogami@redhat.com> - 3.0.3-3
- 3.0.3
- SA#4287 retval fix
- allow replacement of rc service script during upgrades

* Mon Apr 25 2005 Warren Togami <wtogami@redhat.com> - 3.0.3-0.r164513
- 3.0.3-r164513 (almost final)

* Thu Apr 21 2005 Warren Togami <wtogami@redhat.com> - 3.0.2-9
- SA#4191 uri_to_domain() is broken for urls with empty port
  SA#4232 multipart message with 0 parts -> uninitialized in m//
  SA#4121 Score for user defined rules become ignored
  SA#3944 get_envelope_from not handling received header

* Sun Apr 10 2005 Ville Skyttä <ville.skytta at iki.fi> - 3.0.2-8
- Own /usr/share/spamassassin (#152534).
- Drop no longer needed dependency filter script.

* Sun Apr 02 2005 Warren Togami <wtogami@redhat.com> 3.0.2-7
- req DB_File (#143186)

* Sat Apr 02 2005 Warren Togami <wtogami@redhat.com> 3.0.2-6
- test svn 3.0 stable r122144 snapshot
  SA#3826 #4044 #4050 #4048 #4075 #4064 #4075 #4034 #3952

* Thu Mar 24 2005 Florian La Roche <laroche@redhat.com>
- add "exit 0" to postun script

* Thu Mar 24 2005 Joe Orton <jorton@redhat.com> 3.0.2-4
- package the NOTICE file

* Thu Mar 17 2005 Warren Togami <wtogami@redhat.com> - 3.0.2-3
- reinclude ia64, thanks jvdias

* Tue Mar 15 2005 Warren Togami <wtogami@redhat.com> - 3.0.2-2
- exclude ia64 for now due to Bug #151127

* Mon Dec 20 2004 Warren Togami <wtogami@redhat.com> - 3.0.2-1
- 3.0.2

* Sun Oct 31 2004 Warren Togami <wtogami@redhat.com> - 3.0.1-1
- 3.0.1

* Mon Oct 18 2004 Warren Togami <wtogami@redhat.com> - 3.0.0-3
- Fix local.cf rewrite subject option (#133355 Christof Damian)

* Sat Sep 25 2004 Warren Togami <wtogami@redhat.com> - 3.0.0-2
- Update URL, cleanup name (Robert Scheck #133622)

* Thu Sep 23 2004 Warren Togami <wtogami@redhat.com> - 3.0.0-1
- match upstream version
- #133422 Future proof krb5 back compat (Milan Kerslager)

* Wed Sep 22 2004 Warren Togami <wtogami@redhat.com> - 3.0-10 
- 3.0.0 final

* Sun Sep 12 2004 Warren Togami <wtogami@redhat.com> - 3.0-9.rc4
- 3.0 rc4
- update krb5 backcompat patch (John Lundin)

* Sat Sep 04 2004 Warren Togami <wtogami@redhat.com> - 3.0-8.rc3
- 3.0 rc3

* Sun Aug 29 2004 Warren Togami <wtogami@redhat.com> - 3.0-7.rc2
- 3.0 rc2

* Sat Aug 21 2004 Warren Togami <wtogami@redhat.com> - 3.0-6.rc1
- fix perl module syntax in req and buildreqs

* Thu Aug 19 2004 Warren Togami <wtogami@redhat.com> - 3.0-5.rc1
- 3.0 rc1

* Sat Aug 07 2004 Warren Togami <wtogami@redhat.com> - 3.0-3.pre4
- 3.0 pre4

* Wed Jul 28 2004 Warren Togami <wtogami@redhat.com> - 3.0-3.pre2
- 3.0 pre2

* Mon Jun 20 2004 Warren Togami <wtogami@redhat.com> - 3.0-2.pre1
- 3.0.0 pre1
- remove unnecessary patches applied upstream
- update krb5 backcompat patch

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 31 2004 Warren Togami <wtogami@redhat.com> - 3.0-svn20040530
- svn snapshot 20040530
- #124870 prevent service startup failure due to old -a option
- #124871 more docs
- #124872 unowned directories

* Tue May 24 2004 Warren Togami <wtogami@redhat.com> - 3.0-svn20040524
- #123432 do not start service by default
- #122488 remove CRLF's
- #123706 correct license
- svn snapshot 20040524
- svn snapshot 20040518

* Sun May  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 2.63-8
- #122233
- Require perl(:MODULE_COMPAT_*).
- Use %%{_mandir} and %%{_initrddir}.
- Fix License tag and include License in docs.
- Backslashify multiline init script description.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb  11 2004 Warren Togami <wtogami@redhat.com> 2.63-6
- require sitelib instead

* Wed Jan  21 2004 Warren Togami <wtogami@redhat.com> 2.63-3
- krb5-backcompat.patch so older krb5-devel does not fail

* Wed Jan  21 2004 Warren Togami <wtogami@redhat.com> 2.63-2
- upgrade to 2.63

* Mon Jan  19 2004 Warren Togami <wtogami@redhat.com> 2.62-3
- Ville Skyttä's fixes from #113596 including:
- Fix buildroot traces
- enable openssl
- Trailing slash to DESTDIR (bug 90202 comment 14).
- export optflags so they're honored, affects spamc only. 

* Mon Jan  19 2004 Warren Togami <wtogami@redhat.com> 2.62-2
- upgrade to 2.62
- Prereq -> Requires, former is deprecated
- Require current version of perl
- Remove urban myth clean test
- TODO: Get rid of prefix

* Wed Dec  31 2003 Dan Walsh <dwalsh@redhat.com> 2.61-2
- Change sysconfdir to not use full path

* Tue Dec  9 2003 Chip Turner <cturner@redhat.com> 2.61-1
- upgrade to 2.61

* Fri Sep 26 2003 Chip Turner <cturner@redhat.com> 2.60-2
- update to 2.60

* Sat Jul  5 2003 Chip Turner <cturner@redhat.com> 2.55-3
- change perl dependency to more accurate versions with explicit epochs

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat May 31 2003 Chip Turner <cturner@redhat.com> 2.55-1
- move to upstream version 2.55

* Tue May 13 2003 Chip Turner <cturner@redhat.com>
- bump for build
- change init.d script to not default to started

* Sun May 04 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- remove Distribution: tag in spec file

* Wed Apr 16 2003 Chip Turner <cturner@redhat.com> 2.53-5
- remove SIGCHILD patch to properly return it to SIG_IGN now that
  waitpid isn't used on Linux

* Mon Apr 14 2003 Chip Turner <cturner@redhat.com> 2.53-4.8.x
- update to 2.53 from upstream

* Fri Mar 21 2003 Chip Turner <cturner@redhat.com> 2.50-3.8.x
- update patch for servicename; should fix restarting/runlevel issues (#85975)

* Thu Mar 13 2003 Chip Turner <cturner@redhat.com> 2.50-2.8.x
- update to 2.50

* Tue Feb 25 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 21 2003 Chip Turner <cturner@redhat.com>
- revert double fix for 84774

* Mon Feb 17 2003 Bill Nottingham <notting@redhat.com>
- fix startup (#84445)

* Thu Feb 13 2003 Bill Nottingham <notting@redhat.com>
- fix paths in initscript (#84216)

* Thu Feb 13 2003 Chip Turner <cturner@redhat.com>
- removing -P option since it is the default now, bug 84144

* Wed Feb 12 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- fix SIGCHLD handling

* Mon Feb 10 2003 Bill Nottingham <notting@redhat.com>
- move condrestart to %postun

* Sun Feb  2 2003 Chip Turner <cturner@redhat.com>
- update to 2.44
- add condrestart to service script

* Thu Jan 30 2003 Chip Turner <cturner@redhat.com>
- release bump and rebuild

* Wed Jan 29 2003 Chip Turner <cturner@redhat.com>
- add upstream bsmtp off-by-one patch

* Mon Jan 20 2003 Chip Turner <cturner@redhat.com>
- add wrapper for 'spamassassin -e' for native evolution spam filtering

* Sat Jan  4 2003 Jeff Johnson <jbj@redhat.com> 2.43-10
- use internal dep generator.

* Wed Jan  1 2003 Chip Turner <cturner@redhat.com>
- rebuild

* Tue Dec 17 2002 Bill Nottingham <notting@redhat.com> 2.43-7
- don't run by default

* Sat Dec 14 2002 Tim Powers <timp@redhat.com> 2.43-6
- don't use rpms internal dep generator
- buildrequire perl-Time-HiRes instead of perl(Time:HiRes) so we can satisfy build deps in the build system

* Fri Nov 22 2002 Tim Powers <timp@redhat.com>
- rebuilt to solve broken perl deps

* Thu Aug 15 2002 Chip Turner <cturner@redhat.com>
- speedup patch from upstream

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Thu Jul 18 2002 Chip Turner <cturner@redhat.com>
- better control of service level, improvement in %post script.
- (contribs from schirmer@taytron.net)

* Fri Jun 28 2002 Chip Turner <cturner@redhat.com>
- added proper BuildRequire

* Wed Jun 26 2002 Chip Turner <cturner@redhat.com>
- updated to 2.31, added .rc file for procmail to INCLUDERC to enable

* Fri Apr 19 2002 Theo Van Dinter <felicity@kluge.net>
- Updated for 2.20 release
- made /etc/mail/spamassassin a config directory so local.cf doesn't get wiped out
- added a patch to remove findbin stuff

* Wed Feb 27 2002 Craig Hughes <craig@hughes-family.org>
- Updated for 2.1 release

* Sat Feb 02 2002 Theo Van Dinter <felicity@kluge.net>
- Updates for 2.01 release
- Fixed rc file
- RPM now buildable as non-root
- fixed post_service errors
- fixed provides to include perl modules
- use file find instead of manually specifying files

* Tue Jan 15 2002 Craig Hughes <craig@hughes-family.org>
- Updated for 2.0 release

* Wed Dec 05 2001 Craig Hughes <craig@hughes-family.org>
- Updated for final 1.5 distribution.

* Sun Nov 18 2001 Craig Hughes <craig@hughes-family.org>
- first version of rpm.

