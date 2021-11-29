Name:           dcraw 
Version:        1.315
Release:        3.fdr
Summary:        This is a portable ANSI C program to convert raw image files from any digital camera into PPM format

Group:          Applications/Multimedia
License:        free
URL:            http://www.cybercom.net/~dcoffin/dcraw
Source0:        http://www.cybercom.net/~dcoffin/dcraw/dcraw.c
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libjpeg-devel
BuildRequires:  glibc-devel
BuildRequires:	lcms-devel
Requires:       libjpeg
Requires:	glibc

%description    
Dave Coffin's raw photo decoder. Copyright 1997-2004 by Dave Coffin, dcoffin a cybercom o net. This is a portable ANSI C program to convert raw image files from any digital camera into PPM format.  TIFF and CIFF parsing a based upon public specifications, but no such documentation is available for the raw sensor data, so writing this program has been an immense effort. This code is freely licensed for all uses, commercial and otherwise.  Comments, questions, and encouragement are welcome.

#Summary:        
#Group:          Development/Libraries
#Requires:       %{name} = %{epoch}:%{version}-%{release}

#%description    devel
#<Long description of sub-package here>
#<Multiple lines are fine>


%prep
mkdir -p %{buildroot}%{_bindir}

%setup -q -T -c -n dcraw


%build
wget http://www.cybercom.net/~dcoffin/dcraw/dcraw.c
cp -ar dcraw.c %{_topdir}/SOURCES/
## cp -ar %{SOURCE0} .
#gcc -o dcraw -O3 dcraw.c -lm -ljpeg
gcc -o dcraw -O4 dcraw.c -lm -ljpeg -llcms

%install
cp dcraw %{buildroot}%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%post

%preun

%postun


%files 
%attr(755,root,root) %{_bindir}/dcraw

%changelog
* Sun Feb 26 2006 Casper Pedersen <cpedersen[at]c-note.dk> - 1.315-3
Updated to 1.315

* Mon Nov 22 2004 Casper Pedersen <cpedersen[AT]c-note.dk> - 1.215-2
- 1.215 
- added auto download of dcraw.c

* Fri Sep 13 2004 Casper Pedersen <cpedersen[AT]c-note.dk> - 1.203-1
- Initial RPM release.
