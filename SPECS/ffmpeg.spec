Summary: Utilities and libraries to record, convert and stream audio and video
Name: ffmpeg
Version: 1.2.4
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://ffmpeg.org/

####ffmpeg-1.2.4.tar.bz2

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.ffmpeg.org/releases/ffmpeg-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel
BuildRequires: freetype-devel
BuildRequires: imlib2-devel
BuildRequires: zlib-devel

%description
FFmpeg is a very fast video and audio converter. It can also grab from a
live audio/video source.
The command line interface is designed to be intuitive, in the sense that
ffmpeg tries to figure out all the parameters, when possible. You have
usually to give only the target bitrate you want. FFmpeg can also convert
from any sample rate to any other, and resize video on the fly with a high
quality polyphase filter.

Available rpmbuild rebuild options :
--without : lame vorbis theora faad faac gsm xvid x264 a52dec altivec

%package devel
Summary: Header files and static library for the ffmpeg codec library
Group: Development/Libraries

Requires: imlib2-devel, SDL-devel, freetype-devel, zlib-devel, pkgconfig

%description devel
FFmpeg is a very fast video and audio converter. It can also grab from a
live audio/video source.
The command line interface is designed to be intuitive, in the sense that
ffmpeg tries to figure out all the parameters, when possible. You have
usually to give only the target bitrate you want. FFmpeg can also convert
from any sample rate to any other, and resize video on the fly with a high
quality polyphase filter.

Install this package if you want to compile apps with ffmpeg support.

%package libpostproc
Summary: Video postprocessing library from ffmpeg
Group: System Environment/Libraries
Provides: ffmpeg-libpostproc-devel = %{version}-%{release}
Provides: libpostproc = 1.0-1
Provides: libpostproc-devel = 1.0-1
Obsoletes: libpostproc < 1.0-1
Obsoletes: libpostproc-devel < 1.0-1
Requires: pkgconfig

%description libpostproc
FFmpeg is a very fast video and audio converter. It can also grab from a
live audio/video source.

This package contains only ffmpeg's libpostproc post-processing library which
other projects such as transcode may use. Install this package if you intend
to use MPlayer, transcode or other similar programs.

%prep
%setup

%build
export CFLAGS="%{optflags}"
# We should be using --disable-opts since configure is adding some default opts
# to ours (-O3), but as of 20061215 the build fails on asm stuff when it's set
./configure \
    --prefix="%{_prefix}" \
    --libdir="%{_libdir}" \
    --shlibdir="%{_libdir}" \
    --mandir="%{_mandir}" \
    --incdir="%{_includedir}" \
    --enable-shared \
%ifarch %ix86
    --extra-cflags="%{optflags}" \
%endif
%ifarch x86_64
    --extra-cflags="%{optflags} -fPIC" \
%endif

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot} _docs
%{__make} install DESTDIR="%{buildroot}"

# Remove unwanted files from the included docs
%{__cp} -a doc _docs
%{__rm} -rf _docs/{Makefile,*.texi,*.pl}

# The <postproc/postprocess.h> is now at <ffmpeg/postprocess.h>, so provide
# a compatibility symlink
%{__mkdir_p} %{buildroot}%{_includedir}/postproc/
%{__ln_s} ../ffmpeg/postprocess.h %{buildroot}%{_includedir}/postproc/postprocess.h

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig
chcon -t textrel_shlib_t %{_libdir}/libav{codec,device,format,util}.so.*.*.* &>/dev/null || :

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING* CREDITS INSTALL MAINTAINERS README
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/*.so*

%files devel
%defattr(-, root, root, 0755)
%doc _docs/*
%{_includedir}/libavcodec/
%{_includedir}/libavdevice/
%{_includedir}/libavfilter/
%{_includedir}/libavformat/
%{_includedir}/libavutil/
%{_includedir}/libswscale/
%{_includedir}/libswresample/
%{_libdir}/*.a*
%{_libdir}/*.so*
%{_libdir}/pkgconfig/*

#%files libpostproc
#%defattr(-, root, root, 0755)
#%{_includedir}/libpostproc/
#%{_includedir}/postproc/
#%{_libdir}/libpostproc.a
#%{_libdir}/libpostproc.so*
#%{_libdir}/pkgconfig/libpostproc.pc

%changelog
* Sun Jan 29 2012 Dag Wieers <dag@wieers.com> - 0.6.5-1
- Updated to release 0.6.5.

* Sat Dec 04 2010 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Sun Jun 13 2010 Dag Wieers <dag@wieers.com> - 0.5.2-2
- Added more functionality.

* Fri Jun 11 2010 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Updated to release 0.5.2.

* Fri Nov 06 2009 Dag Wieers <dag@wieers.com> - 0.5-3
- Rebuild against newer faad2 2.7.

* Fri Jul 24 2009 Dag Wieers <dag@wieers.com> - 0.5-2
- Change incdir to %%{_includedir}.

* Wed Jul 08 2009 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.
- Disabled speex support, lacking speex 1.2.
- Rebuild against x264-0.4.20090708.

* Mon Jun 04 2007 Dag Wieers <dag@wieers.com> - 0.4.9-0.9.20070530
- Rebuild against x264-0.4.20070529 because I missed it.

* Wed May 30 2007 Matthias Saou <http://freshrpms.net/> 0.4.9-0.8.20070530
- Update to today's SVN codebase.
- Rename various options to match new configure names.
- Remove dca support since it's no longer available with the external lib.
- Enable theora support by default.

* Tue Jan  9 2007 Matthias Saou <http://freshrpms.net/> 0.4.9-0.8.20070109
- Update to today's SVN codebase, fixes the non existing ffmpeg.pc refrence.
- Add faad2 patch.

* Fri Dec 15 2006 Matthias Saou <http://freshrpms.net/> 0.4.9-0.7.20061215
- Update to today's SVN codebase.
- Update gsm patch so that it still applies.
- Remove no longer needed x264 patch.
- Remove --disable-opts option for now, as the build fails without. It seems
  like an option from -O3 might be required for inline asm to work on x86.

* Tue Oct 24 2006 Matthias Saou <http://freshrpms.net/> 0.4.9-0.7.20060918
- Try to update, but stick with 20060918 as linking "as needed" is causing
  too much trouble for now (libdca and libmp3lame with libm functions).
- Include patch to work with latest x264.
- Update URL and remove non-%%date stuff since there are no more releases.
- Change group to Applications/Multimedia since ffmpeg is an application.
- Remove dc1394 support since the lib isn't available anymore anyway.

* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 0.4.9-0.6.20060918
- Update to today's SVN codebase.
- Remove theora support, it seems to be gone...
- Remove a52 patch as ffmpeg doesn't link against it anyway.
- Make installlib works again, so don't manually install anymore.
- Remove all prever stuff that hasn't been useful in ages.
- Change postproc/postprocess.h to be a symlink.

* Fri May 12 2006 Matthias Saou <http://freshrpms.net/> 0.4.9-0.5.20060317
- Change selinux library context in %%post to allow text relocation.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.4.9-0.4.20060317
- Update to CVS snapshot.
- The libraries are versionned at last, so no longer use the autoreqprov hack.
- Override incdir to get install to work properly.
- Provide a postprocess.h compatibility copy.

* Wed Dec  7 2005 Matthias Saou <http://freshrpms.net/> 0.4.9-0.3.20051207
- Update to CVS snapshot.
- Added theora, gsm, x264, dts and dc1394 rebuild options, all on by default.
- Nope, disable dc1394, as it fails to build.
- Add GSM patch <gsm.h> -> <gsm/gsm.h>
- Enable pthreads explicitly, as the build fails otherwise.
- Include new pkgconfig files, add pkgconfig requirements to devel packages.
- Add new libavutil.so* provides.
- Rename libpostproc package to ffmpeg-libpostproc, in order to make things
  easier to obsolete the old mplayer sub-package.
- No longer use %%configure, since --host makes the script stop.
- No longer explicitly disable MMX for non-x86 (works again on x86_64).

* Tue May  3 2005 Matthias Saou <http://freshrpms.net/> 0.4.9-0.20050427.1
- Downgrade to 20050427 since avcodec.h is missing AVCodecContext otherwise.
- Re-enable upgrade path for FC3.

* Tue May  3 2005 Matthias Saou <http://freshrpms.net/> 0.4.9-0.1.20050502
- Update and include patches from Enrico to fix gcc4 build.
- Remove no longer include static libs from the devel package.
- Remove no longer required explicit requirements.
- Clean up obsolete stuff from the build : separate libpostproc compile etc.

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 0.4.9-0.1.20050417
- Update to today's snapshot (no upgrade path, but that shouldn't matter).
- Disable patch3 as it's nowhere to be found :-(
- Added theora... hmm, nope, the build is broken.

* Sat Jan 15 2005 Dag Wieers <dag@wieers.com> - 0.4.9-0.20041110.3
- Exclude libpostproc.so* from ffmpeg package.

* Sun Nov 21 2004 Matthias Saou <http://freshrpms.net/> 0.4.9-0.20041110.2
- Put back explicit requirements since some (all?) don't get properly added
  automatically, like faad2 (thanks to Holden McGroin).

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 0.4.9-0.20041110.1
- Update to latest CVS snaphsot.
- Explicitely disable mmx on non-x86 to fix x86_64 build.
- Add -fPIC to --extra-cflags on non-x86 to fix x86_64 build, as it seems mmx
  and pic are mutually exclusive (build fails with both).

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 0.4.9-0.20041102.1
- Update to 20040926 CVS to fix FC3 compilation problems... not!
- Moved OPTFLAGS to --extra-cflags configure option... no better!
- Add HAVE_LRINTF workaround to fix compile failure... yeah, one less.
- Disable -fPIC, libpostproc breaks with it enabled... argh :-(
- ...I give up, disable a52 for now.

* Mon Sep 27 2004 Matthias Saou <http://freshrpms.net/> 0.4.9-0.pre1.1
- Update to 0.4.9-pre1.
- Enable GPL, pp, shared and shared-pp!
- Add sharedpp and nostrip patches from livna.org rpm.
- Add PIC vs. __PIC__ patch.
- Re-enable MMX.
- Add mandatory -fomit-frame-pointer flag to not bomb on compile.
- Added man pages.
- Added -UUSE_FASTMEMCPY for libpostproc, otherwise we get :
  libpostproc.so.0: undefined reference to `fast_memcpy'

* Mon Aug  2 2004 Matthias Saou <http://freshrpms.net/> 0.4.8-3
- Removed explicit binary dependencies.
- Removed faac support, it doesn't exist.
- Seems like Imlib2 support is broken...
- Added missing -devel requirements for the -devel package.

* Thu Jun 03 2004 Dag Wieers <dag@wieers.com> - 0.4.8-3
- Fixes for building for x86_64 architecture.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 0.4.8-3
- Rebuilt for Fedora Core 2.

* Sat Feb 21 2004 Matthias Saou <http://freshrpms.net/> 0.4.8-2
- Add faac support.
- Enable pp.
- Remove unneeded explicit main a52dec dependency.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.4.8-1
- Update to 0.4.8.
- Steal some changes back from Troy Engel : Disabling mmx to make the build
  succeed and added man pages.
- Re-enabled auto provides but added explicit libavcodec.so and libavformat.so.
- Rebuild for Fedora Core 1.

* Mon Aug 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.7.

* Fri Aug  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to todays's snapshot.

* Tue Jul  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to a CVS snapshot as videolan-client 0.6.0 needs it.
- Enable faad, imlib2 and SDL support.
- Force OPTFLAGS to remove -mcpu, -march and -pipe that all prevent building!

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Hardcode provides in order to get it right :-/

* Tue Feb 25 2002 Matthias Saou <http://freshrpms.net/>
- Moved libavcodec.so to the main package to fix dependency problems.

* Wed Feb 19 2002 Matthias Saou <http://freshrpms.net/>
- Major spec file updates, based on a very nice Mandrake spec.
- Revert to the 0.4.6 release as CVS snapshots don't build.

* Tue Feb  4 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

