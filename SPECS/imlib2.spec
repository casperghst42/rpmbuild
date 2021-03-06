# $Id: imlib2.spec 4365 2006-05-08 18:59:07Z dries $
# Authority: matthias
# Upstream: Carsten Haitzler <raster$rasterman,com>
# Upstream: <enlightenment-devel$lists,sourceforge,net>

#define date 20030417

%{?dist: %{expand: %%define %dist 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: Powerful image loading and rendering library
Name: imlib2
Version: 1.2.2
Release: %{?date:0.%{date}.}1.rf
License: BSD
Group: System Environment/Libraries
URL: http://enlightenment.org/pages/imlib2.html
Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/enlightenment/imlib2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: freetype-devel >= 1.2
BuildRequires: zlib-devel, bzip2-devel
BuildRequires: libpng-devel, libjpeg-devel, libungif-devel, libtiff-devel
# The ltdl.h file is required...
BuildRequires: libtool, gcc-c++
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXext-devel}

%description
Imlib2 is an advanced replacement library for libraries like libXpm that
provides many more features with much greater flexibility and speed than
standard libraries, including font rasterization, rotation, RGBA space
rendering and blending, dynamic binary filters, scripting, and more.


%package devel
Summary: Imlib2 header, static libraries and documentation
Group: Development/Libraries
Requires: %{name} = %{version}
%{?_without_modxorg:Requires: XFree86-devel}
%{!?_without_modxorg:Requires: libX11-devel}
Requires: pkgconfig

%description devel
Header, static libraries and documentation for Imlib2.


%prep
%setup
%{__perl} -pi.orig -e 's|/lib(?=[^/\w])|/%{_lib}|g' configure

%build
%configure \
    --with-pic \
    --x-libraries="%{_prefix}/X11R6/%{_lib}" \
%ifarch %{ix86}
    --enable-mmx
%else
    --disable-mmx
%endif
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/ README
%{_bindir}/imlib2_*
%{_libdir}/libImlib2.so.*
%{_libdir}/imlib2/
%{_datadir}/imlib2/

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/imlib2-config
%{_includedir}/Imlib2.h
%{_libdir}/libImlib2.a
### Required by kdelibs bug (RHbz #142244)
%{_libdir}/libImlib2.la
%{_libdir}/libImlib2.so
%exclude %{_libdir}/imlib2/filters/*.a
%exclude %{_libdir}/imlib2/filters/*.la
%exclude %{_libdir}/imlib2/loaders/*.a
%exclude %{_libdir}/imlib2/loaders/*.la
%{_libdir}/pkgconfig/imlib2.pc


%changelog
* Mon May 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.2-1 - 4365/dries
- Updated to release 1.2.2.

* Mon Jan 17 2005 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Added --x-libraries and improved x86_64 perl oneliner.
- Updated to release 1.2.0.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 1.1.2-2
- Added bzip2 support.
- Add --with-pic configure option, but lib still seems to have non-pic code.

* Sat Sep 25 2004 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1.2. (Antti Markus)

* Sat May 29 2004 Dag Wieers <dag@wieers.com> - 1.1.0-3
- Merged my imlib2 package.
- Disable mmx on non-ix86 architectures.

* Thu Mar 25 2004 Matthias Saou <http://freshrpms.net/> 1.1.0-2
- Removed the explicit XFree86-libs dependency.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Update to 1.1.0.
- Added pkgconfig entry and devel dependency.
- Rebuild for Fedora Core 1.

* Thu Apr 17 2003 Matthias Saou <http://freshrpms.net/>
- Update to today's CVS 1.0.7 snapshot.
- Spec file cleanup, main and devel are what they should be now.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la files.

* Fri Feb 21 2003 Matthias Saou <http://freshrpms.net/>
- Fixed s/XFree86/XFree86-libs/ in dependencies.

* Wed Nov 13 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 8.0.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.6.
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Mon Nov 26 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and update to 1.0.4.

* Mon Jan 8 2001 The Rasterman <raster@rasterman.com>
- Fix Requires & BuildRequires for freetype.

* Sat Sep 30 2000 Lyle Kempler <term@kempler.net>
- Bring back building imlib2 as root via autogen.sh for the lazy (me)
- Some minor changes

* Sat Sep 30 2000 Joakim Bodin <bodin@dreamhosted.com>
- Linux-Mandrake:ise the spec file

* Tue Sep 12 2000 The Rasterman <raster@rasterman.com>
- Redo spec file

* Wed Aug 30 2000 Lyle Kempler <kempler@utdallas.edu>
- Include imlib2-config

* Sat May 20 2000 Lyle Kempler <kempler@utdallas.edu>
- Fixed problems with requiring imlib2_view
- Went back to imlib2_view (not imlib2-view)

* Tue Nov 2 1999 Lyle Kempler <kempler@utdallas.edu>
- Mangled imlib 1.9.8 imlib spec file into imlib2 spec file

