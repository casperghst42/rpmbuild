Name:		MakeMKV
Version:	1.9.10
Release:	2
Summary:	Convert video into other formats

Group:		Applications/Multimedia
License:	Complicated
URL:		http://www.makemkv.com/
Source0:	http://www.makemkv.com/download/makemkv-bin-%{version}.tar.gz
Source1:	http://www.makemkv.com/download/makemkv-oss-%{version}.tar.gz
# If you need to build in an automated system like mock - comment out
# the nosource below to build a src.rpm
nosource:	0
nosource:	1

#The Makefile strips the libraries - debug package useless
%define debug_package %{nil}

# These are for building in RHEL/CentOS 7
#  ffmpeg from http://awel.domblogger.net/7/media/
BuildRequires:	openssl-devel
BuildRequires:	ffmpeg-devel >= 2.0.0
BuildRequires:	mesa-libGL-devel
BuildRequires:	qt-devel >= 4
#Requires:	

%description
MakeMKV is your one-click solution to convert video that you own into free and
patents-unencumbered format that can be played everywhere. MakeMKV is a format
converter, otherwise called "transcoder". It converts the video clips from
proprietary (and usually encrypted) disc into a set of MKV files, preserving
most information but not changing it in any way. The MKV format can store
multiple video/audio tracks with all meta-information and preserve chapters.
There are many players that can play MKV files nearly on all platforms, and
there are tools to convert MKV files to many formats, including DVD and Blu-ray
discs.

%package oss
Summary:	The OSS components of MakeMKV
Group:		Applications/Multimedia
License:	LGPLv2 
Requires:	%{name}-bin = %{version}-%{release}

%description oss
This is the Open Source component of MakeMKV. You also need to install the
closed source binary component for it to work.

MakeMKV is your one-click solution to convert video that you own into free and
patents-unencumbered format that can be played everywhere. MakeMKV is a format
converter, otherwise called "transcoder". It converts the video clips from
proprietary (and usually encrypted) disc into a set of MKV files, preserving
most information but not changing it in any way. The MKV format can store
multiple video/audio tracks with all meta-information and preserve chapters.
There are many players that can play MKV files nearly on all platforms, and
there are tools to convert MKV files to many formats, including DVD and Blu-ray
discs.

%package bin
Summary:	Binary source component of MakeMKV
Group:		Applications/Multimedia
License:	Commercial
Requires:	%{name}-oss = %{version}-%{release}
%ifarch i686
Requires:	%{name}-bin-mmdtsdec = %{version}-%{release}
%endif

%description bin
This is the Closed Source binary component of MakeMKV. You also need to install
the closed source binary component for it to work.

MakeMKV is your one-click solution to convert video that you own into free and
patents-unencumbered format that can be played everywhere. MakeMKV is a format
converter, otherwise called "transcoder". It converts the video clips from
proprietary (and usually encrypted) disc into a set of MKV files, preserving
most information but not changing it in any way. The MKV format can store
multiple video/audio tracks with all meta-information and preserve chapters.
There are many players that can play MKV files nearly on all platforms, and
there are tools to convert MKV files to many formats, including DVD and Blu-ray
discs.

%package bin-mmdtsdec
Summary:	Binary source DTS Decoder component of MakeMKV
Group:		Applications/Multimedia
License:	Commercial
Requires:	%{name}-bin = %{version}-%{release}


%description bin-mmdtsdec
This package includes the DTS decoder binary, which will pull in 32-bit library
dependencies on x86_64 systems.


%prep
%setup -q -c -T
tar -zxf %{SOURCE0}
tar -zxf %{SOURCE1}


%build
cd makemkv-oss-%{version}
#fix library install location
sed -i -e s?"LIBDIR=.*"?"LIBDIR=\$(PREFIX)/%{_lib}"? Makefile.in
CFLAGS="-D __STDC_FORMAT_MACROS" %configure
make %{?_smp_mflags}
cd ..


%install
cd makemkv-oss-%{version}
make install DESTDIR=%{buildroot}
chmod +x %{buildroot}%{_libdir}/lib*
cd ../makemkv-bin-%{version}
# If you need to build in an automated build system such as mock, uncomment
#  below AFTER you read and agree to the license.
#sed -i -e s?"^install: tmp/eula_accepted"?"install:"? Makefile

make install DESTDIR=%{buildroot}
cd ..

%post oss -p /sbin/ldconfig

%postun oss -p /sbin/ldconfig


%files oss
%defattr(-,root,root,-)
%doc makemkv-oss-%{version}/License.txt
%{_bindir}/makemkv
%{_libdir}/lib*.so.*
%{_datadir}/applications/makemkv.desktop
%{_datadir}/icons/hicolor/*/apps/makemkv.png

%files bin
%defattr(-,root,root,-)
%doc makemkv-bin-%{version}/src/eula_en_linux.txt
%{_bindir}/makemkvcon
%{_datadir}/MakeMKV

%files bin-mmdtsdec
%defattr(-,root,root,-)
%doc makemkv-bin-%{version}/src/eula_en_linux.txt
%{_bindir}/mmdtsdec

%changelog
* Thu Oct 02 2014 Alice Wonder <alicewonder@shastaherps.org> - 1.8.13-2
- Split mmdtsdec into separate package, +x the shared libraries

* Thu Oct 02 2014 Alice Wonder <alicewonder@shastaherps.org> - 1.8.13-1
- Initial spec file for RHEL/CentOS 7
