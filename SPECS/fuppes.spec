Summary:		FUPPES Free UPNP entertainment server
Name:			fuppes
Version:		0.660
Release:		0
Epoch:			1
License:		GPL
Packager:		Casper Pedersen  <http://www.c-note.dk>
Group:			Applications/Multimedia
URL:			http://fuppes.ulrich-voelkel.de/
##Source0:		http://fuppes.ulrich-voelkel.de/download/%{name}.tar.bz2
Source0:		http://downloads.sourceforge.net/project/fuppes/fuppes/SVN-660/%{name}-%{version}.tar.gz
Source1:		fuppes.init
Source2:		fuppes.cfg
Source3:		vfolder.cfg
Source4:		fuppes.cron
BuildRequires:		pcre-devel libxml2-devel ffmpeg-devel sqlite-devel taglib-devel libtheora-devel libmp4v2-devel libmad-devel exiv2-devel libmpcdec-devel
BuildRoot: 		%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		pcre libxml2 ffmpeg sqlite taglib libtheora libmp4v2 libmad exiv2 libmpcdec wget
Requires(post):		/sbin/chkconfig
Requires(post):		/sbin/service
Requires(pre):		/usr/sbin/useradd
Requires(preun): 	/sbin/chkconfig
Requires(preun): 	/usr/sbin/userdel
Requires(preun): 	/sbin/service
Requires(postun): 	/sbin/service

%description
A free, multiplatform UPnP A/V Media Server
FUPPES supports a wide range of UPnP MediaRenderers
as well as on-the-fly transcoding of various audio, video
and image formats. FUPPES also includes basic DLNA support.

%prep
%setup -q
#%patch0 -p1
%build
####./configure --prefix=/usr --enable-video-transcoding --sysconfdir=/etc --datadir=/var/cache/fuppes
./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-transcoder-ffmpeg --enable-taglib --enable-mp4v2  --enable-lame --enable-mad --enable-faad  --enable-mp4v2
%{__make}


%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install
%{__install} -d -m0740 %{buildroot}%{_sysconfdir}/fuppes
%{__install} -d -m0740 %{buildroot}%{_localstatedir}/log/fuppes
%{__install} -D -m0755 %SOURCE1 %{buildroot}%{_sysconfdir}/init.d/fuppes
%{__install} -D -m0740 %SOURCE2 %{buildroot}%{_sysconfdir}/fuppes/fuppes.cfg
%{__install} -D -m0755 %SOURCE3 %{buildroot}%{_sysconfdir}/fuppes/vfolder.cfg
%{__install} -D -m0755 %SOURCE4 %{buildroot}%{_sysconfdir}/cron.hourly/fuppes
mkdir -p %{buildroot}/var/cache/fuppes


%pre
/usr/sbin/useradd -r -s /sbin/nologin -d /var/cache/fuppes \
        -c "fuppes user" fuppes &>/dev/null || :

%post
## it's bad form to start daemons per default
##/sbin/chkconfig --add fuppes || :

%preun
if [ $1 -eq 0 ]; then
/sbin/service fuppes stop &>/dev/null || :
/sbin/chkconfig --del fuppes || :
/usr/sbin/userdel fuppes || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%doc README
%dir %attr (-,fuppes,fuppes) %{_localstatedir}/log/fuppes
%dir %attr (-,fuppes,fuppes) %{_sysconfdir}/fuppes
%dir %attr (-,fuppes,fuppes) %{_var}/cache/%{name}
%attr (-,fuppes,fuppes) %{_sysconfdir}/%{name}/fuppes.cfg
%attr (-,fuppes,fuppes) %{_sysconfdir}/%{name}/vfolder.cfg
%{_sysconfdir}/init.d/%{name}
%{_sysconfdir}/cron.hourly/%{name}
%{_bindir}/*
%{_libdir}/*
%{_var}/cache/%{name}
%{_includedir}/*
%{_datadir}/%{name}/*

%changelog
* Thu Nov 18 2010 Casper Pedersen <cpedersen@c-note.dk> 0.660-1
- updated with the latest stable version of Fuppes
- fixing up the spec file

* Wed Oct 29 2008 Andrew Colin Kissa <andrew@topdog-software.com>
- Initial Package.

