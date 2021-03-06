Name:           gpgme
Version:        1.0.1
Release:        5
Epoch:          0
Summary:        GnuPG Made Easy

License:        GPL
Group:          Applications/System
URL:            http://www.gnupg.org/related_software/gpgme/
Source:         ftp://ftp.gnupg.org/gcrypt/alpha/gpgme/gpgme-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gnupg >= 0:1.2.2, %{_bindir}/gpgsm
BuildRequires:  libgpg-error-devel >= 0:0.5
Requires:       gnupg >= 0:1.2.2, %{_bindir}/gpgsm

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package        devel
Summary:        Static libraries and header files from GPGME, GnuPG Made Easy
Group:          Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}, libgpg-error-devel
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info

%description    devel
Static libraries and header files from GPGME, GnuPG Made Easy.


%prep
%setup -q

%build
%configure --enable-static --with-pth=no
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT{%{_infodir}/dir,%{_libdir}/*.la}


%check || :
make check


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :

%postun devel
if [ $1 -eq 0 ] ; then
  /sbin/install-info --delete %{_infodir}/%{name}.info \
    %{_infodir}/dir 2>/dev/null || :
fi


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README* THANKS TODO VERSION
%{_libdir}/libgpgme*.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/gpgme-config
%{_includedir}/gpgme.h
%{_libdir}/libgpgme*.a
%{_libdir}/libgpgme*.so
%{_datadir}/aclocal/gpgme.m4
%{_infodir}/gpgme.info*


%changelog
* Mon Jan 03 2005 Casper Pedersen <cpedersen[at]c-note.dk> - 0:1.0.1-5
- version 1.0.1 
- this is needed to get SeaHorse to work
- Drop BR pth-devel and build --with-pth=no as per. spec file for 0.3.16-5

* Tue Dec 14 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.4.3-4
- Add similar fd select race/lockup fix as for GPGME 0.3.16.

* Sun May  2 2004 Ville Skytt?? <ville.skytta at iki.fi> - 0:0.4.3-0.fdr.3
- Require %%{_bindir}/gpgsm instead of newpg.
- Cosmetic spec file improvements.

* Thu Oct 23 2003 Ville Skytt?? <ville.skytta at iki.fi> - 0:0.4.3-0.fdr.2
- Update description.

* Tue Oct  7 2003 Ville Skytt?? <ville.skytta at iki.fi> - 0:0.4.3-0.fdr.1
- Update to 0.4.3.

* Fri Aug 15 2003 Ville Skytt?? <ville.skytta at iki.fi> - 0:0.4.2-0.fdr.1
- Update to 0.4.2.
- make check in the %%check section.

* Thu Jul 10 2003 Ville Skytt?? <ville.skytta at iki.fi> - 0:0.4.1-0.fdr.1
- Update to 0.4.1.
- Make -devel cooperate with --excludedocs.

* Sat Apr 19 2003 Ville Skytt?? <ville.skytta at iki.fi> - 0:0.4.0-0.fdr.2
- BuildRequire pth-devel, fix missing epoch in -devel Requires (#169).
- Save .spec in UTF-8.

* Sat Mar 22 2003 Ville Skytt?? <ville.skytta at iki.fi> - 0:0.4.0-0.fdr.1
- Update to current Fedora guidelines.
- Exclude %%{_libdir}/*.la.

* Tue Feb 12 2003 Warren Togami <warren@togami.com> 0.4.0-1.fedora.3
- info/dir temporary workaround

* Sat Feb  8 2003 Ville Skytt?? <ville.skytta at iki.fi> - 0.4.0-1.fedora.1
- First Fedora release.

