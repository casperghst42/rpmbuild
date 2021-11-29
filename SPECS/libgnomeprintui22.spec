%define	name		libgnomeprintui22
%define	version		2.8.2
%define	rel		1
%define	release		%{rel}.%{disttag}.%{repotag}
%define	gettext		libgnomeprintui-2.2

%define gtk2_version 2.4.1
%define libgnomeprint_version 2.8.2
%define libgnomecanvas_version 2.8.0

Summary:	GUI support for libgnomeprint
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System Environment/Libraries
URL:		http://ftp.gnome.org/pub/GNOME/sources/libgnomeprintui
Source:		libgnomeprintui-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}
Requires:	gtk2 >= %{gtk2_version}
Requires:	libgnomeprint22 >= %{libgnomeprint_version}
Requires:	libgnomecanvas >= %{libgnomecanvas_version}
BuildRequires:	gtk2-devel >= %{gtk2_version}
BuildRequires:	libgnomeprint22-devel >= %{libgnomeprint_version}
BuildRequires:	libgnomecanvas-devel >= %{libgnomecanvas_version}
BuildPrereq:	automake16 >= 1.6.3
BuildPrereq:	autoconf
BuildPrereq:	libtool
Patch1:		libgnomeprintui-nognomecommon.patch

%description
The libgnomeprintui package contains GTK+ widgets related to printing.

%package devel
Summary:	Libraries and include files for %{name}.
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk2-devel >= %{gtk2_version}
Requires:	libgnomeprint22-devel >= %{libgnomeprint_version}
Requires:	libgnomecanvas-devel >= %{libgnomecanvas_version}

%description devel
Development files for %{name}

%prep
%setup -q -n libgnomeprintui-%{version}

%patch1 -p1 -b .nognomecommon

%build
aclocal
libtoolize --force
autoconf
automake --add-missing
%configure
make

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{gettext}

%clean

%files -f %{gettext}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/libgnomeprintui-2.2/libgnomeprintui/*.h
%{_libdir}/pkgconfig/libgnomeprintui-2.2.pc
%{_datadir}/gtk-doc/html/libgnomeprintui/
%{_libdir}/*.a
%{_libdir}/*.la

%changelog
* Tue Dec 07 2004 Matthew Hall <matt@nrpms.net> 2.8.2-1
- 2.8.2 Release

* Mon Sep 13 2004 Matthew Hall <matt@ecsc.co.uk> 2.8.0-1
- 2.8.0 Release

* Mon Aug 02 2004 Matthew Hall <matt@ecsc.co.uk> 2.7.1-1
- 2.7.1 Release

* Wed Jun 30 2004 Matthew Hall <matt@ecsc.co.uk> 2.7.0-1
- 2.7.0 Release

* Wed Jun 23 2004 Matthew Hall <matt@ecsc.co.uk> 2.6.2-1
- 2.6.2 Release

* Sun May 23 2004 Matthew Hall <matt@ecsc.co.uk> 2.6.1-2
- Rebuild for Fedora Core 2

* Wed Apr 21 2004 Matthew Hall <matt@ecsc.co.uk> 2.6.1-1
- 2.6.1 Release

* Mon Mar 22 2004 Matthew Hall <matt@ecsc.co.uk> 2.6.0-1
- 2.6.0 Release

* Wed Mar 17 2004 Matthew Hall <matt@ecsc.co.uk> 2.5.4-1
- 2.5.4 Release

* Thu Feb 26 2004 Matthew Hall <matt@ecsc.co.uk> 2.5.3-1
- 2.5.3 Release

* Mon Feb 16 2004 Matthew Hall <matt@ecsc.co.uk> 2.5.2-1
- 2.5.2 Release

* Mon Feb 02 2004 Matthew Hall <matt@ecsc.co.uk> 2.5.1-1
- 2.5.1 Release

* Tue Dec 16 2003 Matthew Hall <matt@ecsc.co.uk> 2.5.0.1-1
- 2.5.0.1 Release

* Mon Dec 01 2003 Matthew Hall <matt@ecsc.co.uk> 2.5.0-1
- 2.5.0 Release

* Sat Nov 15 2003 Matthew Hall <matt@ecsc.co.uk> 2.4.0-2
- Rebuild for Fedora Core 1

* Tue Oct 14 2003 Matthew Hall <matt@ecsc.co.uk> 2.4.0-1
- 2.4.0 Release

* Wed Aug 27 2003 Matthew Hall <matt@ecsc.co.uk> 2.3.1-1
- 2.3.1 Release

* Wed Jun 18 2003 Matthew Hall <matt@ecsc.co.uk> 2.2.1.3-1
- 2.2.1.3 Release

* Thu Mar 13 2003 Matthew Hall <matt@ecsc.co.uk> 2.2.1.2-1
- 2.2.1.2 Release

* Fri Jan 31 2003 Matthew Hall <matt@ecsc.co.uk>
- New Spec File

