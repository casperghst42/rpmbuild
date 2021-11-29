Summary: A version control system.
Name: cvs
Version: 1.11.17
Release: 5
License: GPL
Group: Development/Tools
Source0: https://ccvs.cvshome.org/files/documents/19/192/cvs-%{version}.tar.bz2
Source1: https://ccvs.cvshome.org/files/documents/19/192/cvs-%{version}.tar.bz2.sig
URL: http://www.cvshome.org/
Patch0: cvs-1.11.17-cvspass.patch
Patch1: cvs-1.11.5-extzlib.patch
Patch2: cvs-1.11.2-netbsd-tag.patch
Patch3: cvs-1.11.2-abortabort.patch
Patch4: cvs-1.11.1p1-bs.patch
Patch5: cvs-1.11.17-extzlib2.patch
Patch6: cvs-1.11.17-sccs2rcs.patch
Prereq: /sbin/install-info
Prefix: %{_prefix}
Buildroot: %{_tmppath}/%{name}-root
BuildPreReq: autoconf, automake, libtool, zlib-devel
%{!?nokerberos:BuildPrereq: krb5-devel}

%description
CVS (Concurrent Version System) is a version control system that can
record the history of your files (usually, but not always, source
code). CVS only stores the differences between versions, instead of
every version of every file you have ever created. CVS also keeps a log
of who, when, and why changes occurred.

CVS is very helpful for managing releases and controlling the
concurrent editing of source files among multiple authors. Instead of
providing version control for a collection of files in a single
directory, CVS provides version control for a hierarchical collection
of directories consisting of revision controlled files. These
directories and files can then be combined together to form a software
release.

%prep
%setup -q
%patch0 -p1 -b .cvspass
%patch1 -p1 -b .extzlib
%patch2 -p0 -b .netbsd-tag
%patch3 -p1 -b .abortabort
%patch4 -p1 -b .bs
# Apply a patch to the generated files, OR
# run autoreconf and require autoconf >= 2.58, automake >= 1.7.9
%patch5 -p1 -b .extzlib2
%patch6 -p1 -b .perl

%build
%{!?nokerberos:k5prefix=`krb5-config --prefix`}
%{!?nokerberos:CPPFLAGS=-I${k5prefix}/include/kerberosIV; export CPPFLAGS}
%{!?nokerberos:CFLAGS=-I${k5prefix}/include/kerberosIV; export CFLAGS}
%{!?nokerberos:LIBS="-lkrb4 -ldes425 -lk5crypto"; export LIBS}
%configure --enable-pam \
%{!?nokerberos: --with-gssapi --with-krb4 --enable-encryption}

make
if [ `id -u` -ne 0 ] ; then
	make check
fi

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%{makeinstall}
# forcefully compress the info pages so that install-info will work properly
# in the %%post
gzip $RPM_BUILD_ROOT/%{_infodir}/cvs* || true
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /%{_infodir}/cvs.info.gz /%{_infodir}/dir
/sbin/install-info /%{_infodir}/cvsclient.info.gz /%{_infodir}/dir 

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete /%{_infodir}/cvs.info.gz /%{_infodir}/dir
    /sbin/install-info --delete /%{_infodir}/cvsclient.info.gz /%{_infodir}/dir
fi

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING* DEVEL-CVS FAQ HACKING MINOR-BUGS NEWS
%doc PROJECTS TODO README
%doc doc/*.ps
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/*.info*
%{_datadir}/%{name}

%changelog
* Mon Nov 01 2004 Adrian Havill <havill@redhat.com> 1.11.17-5
- remove csh dep, sccs2rcs to perl (#57974), n-v-r

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun 10 2004 Nalin Dahyabhai <nalin@redhat.com> 1.11.17-2
- rebuild

* Thu Jun 10 2004 Nalin Dahyabhai <nalin@redhat.com> 1.11.17-1
- update to 1.11.17, which includes those last few fixes

* Fri May 28 2004 Nalin Dahyabhai <nalin@redhat.com>
- add security fix for CAN-2004-0416,CAN-2004-0417,CAN-2004-0418 (Stefan Esser)

* Fri May 28 2004 Robert Scheck 1.11.16-0
- update to 1.11.16 (#124239)

* Tue May 18 2004 Nalin Dahyabhai <nalin@redhat.com> 1.11.15-6
- rebuild

* Thu May 13 2004 Nalin Dahyabhai <nalin@redhat.com> 1.11.15-5
- use revised version of Stefan Esser's patch provided by Derek Robert Price

* Mon May  3 2004 Nalin Dahyabhai <nalin@redhat.com> 1.11.15-4
- rebuild

* Mon May  3 2004 Nalin Dahyabhai <nalin@redhat.com> 1.11.15-3
- add patch from Stefan Esser to close CAN-2004-0396

* Wed Apr 21 2004 Nalin Dahyabhai <nalin@redhat.com> 1.11.15-2
- rebuild

* Wed Apr 21 2004 Nalin Dahyabhai <nalin@redhat.com> 1.11.15-1
- update to 1.11.15, fixing CAN-2004-0180 (#120969)

* Tue Mar 23 2004 Nalin Dahyabhai <nalin@redhat.com> 1.11.14-1
- update to 1.11.14

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan  7 2004 Nalin Dahyabhai <nalin@redhat.com> 1.11.11-1
- turn kserver, which people shouldn't use any more, back on

* Tue Dec 30 2003 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.11.11

* Thu Dec 18 2003 Nalin Dahyabhai <nalin@redhat.com> 1.11.10-1
- update to 1.11.10

* Mon Jul 21 2003 Nalin Dahyabhai <nalin@redhat.com> 1.11.5-3
- rebuild

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Apr 30 2003 Nalin Dahyabhai <nalin@redhat.com> 1.11.5-1
- update to 1.11.5
- disable kerberos 4 support

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 21 2003 Nalin Dahyabhai <nalin@redhat.com> 1.11.2-9
- rebuild

* Thu Jan 16 2003 Nalin Dahyabhai <nalin@redhat.com> 1.11.2-8
- incorporate fix for double-free in server (CAN-2003-0015)

* Tue Nov 26 2002 Nalin Dahyabhai <nalin@redhat.com> 1.11.2-7
- don't error out in %%install if the info dir file we remove from the build
  root isn't there (depends on the version of texinfo installed, reported by
  Arnd Bergmann)

* Fri Oct  4 2002 Nalin Dahyabhai <nalin@redhat.com> 1.11.2-6
- fixup LDFLAGS to find multilib Kerberos for linking

* Thu Sep 24 2002 Nalin Dahyabhai <nalin@redhat.com>
- incorporate patch to add 't' as a loginfo format specifier, from NetBSD

* Thu Jul 18 2002 Tim Waugh <twaugh@redhat.com 1.11.2-5
- Fix mktemp patch (bug #66669)
- Incorporate patch to fix verifymsg behaviour on empty logs (bug #66022)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 1.11.2-4
- automated rebuild

* Tue Jun  4 2002 Nalin Dahyabhai <nalin@redhat.com> 1.11.2-3
- incorporate patch to fix incorrect socket descriptor usage (#65225)
- incorporate patches to not choke on empty commit messages and to always
  send them (#66017)
- incorporate patch to not infinitely recurse on assertion failures (#66019)

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May  9 2002 Nalin Dahyabhai <nalin@redhat.com> 1.11.2-1
- update to 1.11.2

* Mon Feb 18 2002 Nalin Dahyabhai <nalin@redhat.com> 1.11.1p1-7
- build with an external zlib
- don't run automake in the %%build phase

* Tue Jan 15 2002 Nalin Dahyabhai <nalin@redhat.com> 1.11.1p1-6
- merge patch to handle timestamping of symlinks in the repository properly,
  from dwmw2 (#23333)

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 1.11.1p1-5
- automated rebuild

* Tue Nov 13 2001 Nalin Dahyabhai <nalin@redhat.com> 1.11.1p1-4
- remove explicit dependency on krb5-libs

* Tue Jul 31 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.11.1p1-3
- Fix up initial cvs login (#47457)
- Bring back the leading newline at the beginning of commit messages
  "a" is one key less than "O". ;)
- Fix build in the current build system

* Mon Jun 25 2001 Bill Nottingham <notting@redhat.com>
- don't own /usr/share/info/dir

* Fri Jun 22 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix the files list

* Mon Jun 18 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.11.1p1
- drop no-longer-necessary patches
- use bundled zlib, because it's apparently not the same as the system zlib
- run the test suite in the build phase
- drop explicit Requires: on perl (RPM will catch the interpreter req)

* Mon Jan 29 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix cvs-1.11-security.patch, which had CR-LF line terminators (#25090)
- check for and ignore ENOENT errors when attempting to remove symlinks (#25173)

* Mon Jan 08 2001 Preston Brown <pbrown@redhat.com>
- patch from Olaf Kirch <okir@lst.de> to do tmp files safely.

* Tue Oct 10 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.11

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Nalin Dahyabhai <nalin@redhat.com>
- always zero errno before calling readdir (#10374)

* Tue Jun 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new build environment (release 6)

* Mon Jun  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new build environment (release 5)
- FHS tweaks
- actually gzip the info pages

* Wed May 10 2000 Nalin Dahyabhai <nalin@redhat.com>
- reverse sense of conditional kerberos dependency
- add kerberos IV patch from Ken Raeburn
- switch to using the system's zlib instead of built-in
- default to unstripped binaries

* Tue Apr  4 2000 Bill Nottingham <notting@redhat.com>
- eliminate explicit krb5-configs dependency

* Mon Mar 20 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.10.8

* Wed Mar  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- make kerberos support conditional at build-time

* Wed Mar  1 2000 Bill Nottingham <notting@redhat.com>
- integrate kerberos support into main tree

* Mon Feb 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- build with gssapi auth (--with-gssapi, --with-encryption)
- apply patch to update libs to krb5 1.1.1

* Fri Feb 04 2000 Cristian Gafton <gafton@redhat.com>
- fix the damn info pages too while we're at it.
- fix description
- man pages are compressed
- make sure %post and %preun work okay

* Sun Jan 9 2000  Jim Kingdon <http://bugzilla.redhat.com/bugzilla>
- update to 1.10.7.

* Wed Jul 14 1999 Jim Kingdon <http://developer.redhat.com>
- add the patch to make 1.10.6 usable
  (http://www.cyclic.com/cvs/dev-known.html).

* Tue Jun  1 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.10.6.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Mon Feb 22 1999 Jeff Johnson <jbj@redhat.com>
- updated text in spec file.

* Mon Feb 22 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.10.5.

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.10.4.

* Tue Oct 20 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.10.3.

* Mon Sep 28 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.10.2.

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- remove trailing characters from rcs2log mktemp args

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.10.1

* Mon Aug 31 1998 Jeff Johnson <jbj@redhat.com>
- fix race conditions in cvsbug/rcs2log

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.10.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.9.30.

* Mon Jun 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Mon Jun  8 1998 Jeff Johnson <jbj@redhat.com>
- build root
- update to 1.9.28

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added install-info stuff
- added changelog section
