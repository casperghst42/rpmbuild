Name:           minidlna
Version:        1.1.1
Release:        1%{?dist}.lux.1
Summary:        Lightweight DLNA/UPnP-AV server targeted at embedded systems

Group:          System Environment/Daemons
License:        GPLv2 
URL:            http://sourceforge.net/projects/minidlna/
Source0:        http://downloads.sourceforge.net/%{name}/%{version}/%{name}-%{version}.tar.gz
# Systemd unit file
Source1:        %{name}.service
# tmpfiles configuration for the /run directory
Source2:        %{name}-tmpfiles.conf 
# From Nux Dextop package
Source100:	minidlnad.init
Source101:	Note-for-MiniDLNA-transcode.txt
Patch1:		%{name}-%{version}_transcode.patch
Patch2:		%{name}-1.1.1.lux_user.patch
# A correction taken from minidlna-1.1.0_transcode.patch, which was lost somehow in 1.1.1
Patch100:	%{name}-1.1.1.lux_transcode.patch

BuildRequires:  libuuid-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  sqlite-devel
BuildRequires:  libvorbis-devel
BuildRequires:  flac-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libexif-devel
BuildRequires:  gettext
Requires(pre):  shadow-utils
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig, /sbin/service

%description
MiniDLNA (aka ReadyDLNA) is server software with the aim of being fully 
compliant with DLNA/UPnP-AV clients.

The minidlna daemon serves media files (music, pictures, and video) to 
clients on your network.  Example clients include applications such as 
Totem and XBMC, and devices such as portable media players, smartphones, 
and televisions.


%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch100 -p1

# Edit the default config file 
perl -pi -e 's/#?user=.*/user=minidlna/' minidlna.conf
sed -i 's/#log_dir=\/var\/log/#log_dir=\/var\/log\/minidlna/' \
  %{name}.conf

cp %{SOURCE101} .


%build
%configure \
  --disable-silent-rules \
  --with-db-path=%{_localstatedir}/cache/%{name} \
  --with-log-path=%{_localstatedir}/log/%{name} \
  --enable-tivo

make %{?_smp_mflags} 


%install
make install DESTDIR=%{buildroot}

# Install config file
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 minidlna.conf %{buildroot}%{_sysconfdir}

mkdir -p %{buildroot}%{_initrddir}
install -m 644 %{SOURCE100} %{buildroot}%{_initrddir}/minidlnad

# Install man pages
mkdir -p %{buildroot}%{_mandir}/man5
install -m 644 minidlna.conf.5 %{buildroot}%{_mandir}/man5/
mkdir -p %{buildroot}%{_mandir}/man8
install -m 644 minidlnad.8 %{buildroot}%{_mandir}/man8/

mkdir -p %{buildroot}/run/
install -d -m 0755 %{buildroot}/run/%{name}/

# Create cache and log directories
mkdir -p %{buildroot}%{_localstatedir}/cache
install -d -m 0755 %{buildroot}%{_localstatedir}/cache/%{name}/
mkdir -p %{buildroot}%{_localstatedir}/log
install -d -m 0755 %{buildroot}%{_localstatedir}/log/%{name}/

%find_lang %{name}


%pre
getent group minidlna >/dev/null || groupadd -r minidlna
getent passwd minidlna >/dev/null || \
useradd -r -g minidlna -d /dev/null -s /sbin/nologin \
  -c "minidlna service account" minidlna
exit 0


%post
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /sbin/chkconfig --add minidlnad >/dev/null 2>&1 || :
fi


%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service minidlnad stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del minidlnad >/dev/null 2>&1 || :
fi


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/minidlna.conf
%attr(0755,root,root) %{_sbindir}/minidlnad
%attr(0755,root,root) %{_initrddir}/minidlnad
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/minidlnad.8*
%dir %attr(-,minidlna,minidlna) /run/%{name}
%dir %attr(-,minidlna,minidlna) %{_localstatedir}/cache/%{name}/
%dir %attr(-,minidlna,minidlna) %{_localstatedir}/log/%{name}/
%doc AUTHORS COPYING LICENCE.miniupnpd NEWS README TODO
%doc Note-for-MiniDLNA-transcode.txt


%changelog
* Sun Sep 15 2013 Andrea Musuruane <musuruan@gmail.com> - 1.1.0-1
- Updated to upstream 1.1.0
- Better systemd integration

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.26-3
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.26-2
- Rebuilt for x264/FFmpeg

* Wed May 08 2013 Andrea Musuruane <musuruan@gmail.com> - 1.0.26-1
- Updated to upstream 1.0.26

* Wed Jan 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.25-4
- Rebuilt for ffmpeg

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.25-3
- Rebuilt for FFmpeg 1.0

* Sat Nov 03 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.25-2
- Fixed FTBFS caused by ffmpeg 1.0
- Updated minidlna.service I forgot to commit (BZ #2294)

* Sat Jul 14 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.25-1
- Updated to upstream 1.0.25

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.24-3
- Rebuilt for FFmpeg

* Wed Apr 25 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.24-2
- Run the daemon with the minidlna user (BZ #2294)
- Updated Debian man pages

* Sun Feb 19 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.24-1
- Updated to upstream 1.0.24

* Sat Jan 28 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.23-1
- Updated to upstream 1.0.23

* Sun Jan 22 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.22-2
- Fixed systemd unit file

* Sun Jan 15 2012 Andrea Musuruane <musuruan@gmail.com> 1.0.22-1
- Updated to upstream 1.0.22
- Removed default Fedora RPM features (defattr, BuildRoot, clean section)
- Better consistent macro usage

* Sat Jul 23 2011 Andrea Musuruane <musuruan@gmail.com> 1.0.21-1
- Updated to upstream 1.0.21

* Sat Jun 18 2011 Andrea Musuruane <musuruan@gmail.com> 1.0.20-1
- First release
- Used Debian man pages

