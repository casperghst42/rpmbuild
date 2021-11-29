%define contentdir /var/www
%define suexec_caller apache
%define mmn 20020903
%define aprver 0

Summary: Apache HTTP Server
Name: httpd
Version: 2.0.46
Release: 40.ent
URL: http://httpd.apache.org/
Source0: http://www.apache.org/dist/httpd/httpd-%{version}.tar.gz
Source1: index.html
Source3: httpd.logrotate
Source4: httpd.init
Source6: powered_by.gif
Source7: powered_by_rh.png
Source10: httpd.conf
Source11: ssl.conf
Source12: welcome.conf
Source14: mod_ssl-Makefile.crt
Source15: mod_ssl-Makefile.crl
Source16: certwatch.c
Source17: certwatch.cron
# Documentation
Source30: migration.xml
Source31: migration.css
Source32: html.xsl
Source33: README.confd
Source34: certwatch.xml
# build/scripts patches
Patch1: httpd-2.0.40-apctl.patch
Patch2: httpd-2.0.36-apxs.patch
Patch3: httpd-2.0.36-sslink.patch
Patch4: httpd-2.0.45-parallel.patch
Patch5: httpd-2.0.45-deplibs.patch
Patch7: httpd-2.0.46-siglist.patch
Patch8: httpd-2.0.46-aprconfig.patch
Patch9: httpd-2.0.46-suexec.patch
Patch10: httpd-2.0.45-syspcre.patch
Patch11: httpd-2.0.46-aputest.patch
# Bug fixes
Patch20: httpd-2.0.45-encode.patch
Patch21: httpd-2.0.45-davfs.patch
Patch22: httpd-2.0.45-davetag.patch
Patch23: httpd-2.0.46-sslincl.patch
Patch24: httpd-2.0.46-shmcb.patch
Patch25: httpd-2.0.46-logtimez.patch
Patch26: httpd-2.0.46-md5dig.patch
Patch27: httpd-2.0.46-rolog.patch
Patch28: httpd-2.0.46-include.patch
Patch29: httpd-2.0.46-sslcleanup.patch
Patch30: httpd-2.0.46-nested.patch
Patch31: httpd-2.0.46-deflate.patch
Patch32: httpd-2.0.46-sslmutex.patch
Patch33: httpd-2.0.46-miscfix.patch
Patch34: httpd-2.0.46-sslio.patch
Patch35: httpd-2.0.46-cache.patch
Patch36: httpd-2.0.46-graceful.patch
Patch37: httpd-2.0.46-confcont.patch
Patch38: httpd-2.0.46-srvheader.patch
Patch39: httpd-2.0.46-sslerr.patch
Patch100: httpd-2.0.46-execfail.patch
Patch101: httpd-2.0.46-worker.patch
Patch102: httpd-2.0.46-sslfakeauth.patch
Patch103: httpd-2.0.46-metharray.patch
Patch104: httpd-2.0.46-expires.patch
Patch105: httpd-2.0.46-worker2.patch
Patch106: httpd-2.0.46-proxy11.patch
Patch107: httpd-2.0.46-sslvars.patch
Patch108: httpd-2.0.46-davbadfrag.patch
Patch109: httpd-2.0.46-dav401dest.patch
Patch110: httpd-2.0.46-apusdbm.patch
Patch111: httpd-2.0.46-shapass.patch
Patch112: httpd-2.0.46-autoindex.patch
Patch113: httpd-2.0.46-sslscache.patch
Patch114: httpd-2.0.46-manpages.patch
Patch115: httpd-2.0.48-davmisc.patch
Patch116: httpd-2.0.46-digestmeth.patch
Patch117: httpd-2.0.46-deflate2.patch
Patch118: httpd-2.0.46-vhostaddr.patch
Patch119: httpd-2.0.46-cgirange.patch
Patch120: httpd-2.0.46-rgetline.patch
Patch121: httpd-2.0.46-davfslock.patch
# features/functional changes
Patch40: httpd-2.0.45-cnfdir.patch
Patch41: httpd-2.0.36-redhat.patch
Patch42: httpd-2.0.40-xfsz.patch
Patch43: httpd-2.0.40-pod.patch
Patch44: httpd-2.0.40-noshmht.patch
Patch45: httpd-2.0.45-proxy.patch
Patch46: httpd-2.0.46-distcache.patch
Patch47: httpd-2.0.46-largefile.patch
Patch48: httpd-2.0.46-testhook.patch
Patch49: httpd-2.0.46-dumpcerts.patch
Patch50: httpd-2.0.46-v4listen.patch
Patch51: httpd-2.0.46-addrconfig.patch
Patch52: httpd-2.0.46-guardarea.patch
Patch53: httpd-2.0.46-sslremain.patch
Patch54: httpd-2.0.46-davstream.patch
Patch55: httpd-2.0.46-aprmtime.patch
Patch56: httpd-2.0.46-apudbver.patch
Patch57: httpd-2.0.46-fdsetsize.patch
Patch58: httpd-2.0.46-cgibucket.patch
Patch59: httpd-2.0.46-aprlargecopy.patch
Patch150: httpd-2.0.46-sslhooks.patch
# Security fixes
Patch60: httpd-2.0.46-CAN-2003-0192.patch
Patch61: httpd-2.0.46-CAN-2003-0253.patch
Patch62: httpd-2.0.46-CAN-2003-0254.patch
Patch63: httpd-2.0.40-CAN-2003-0020.patch
Patch64: httpd-2.0.46-VU379828.patch
Patch65: httpd-2.0.46-CAN-2003-0542.patch
Patch66: httpd-2.0.46-CAN-2004-0113.patch
Patch67: httpd-2.0.46-CAN-2004-0488.patch
Patch68: httpd-2.0.46-CAN-2004-0493.patch
Patch69: httpd-2.0.46-CAN-2004-0747.patch
Patch70: httpd-2.0.46-CAN-2004-0748.patch
Patch71: httpd-2.0.46-CAN-2004-0751.patch
Patch72: httpd-2.0.46-CAN-2004-0786.patch
Patch73: httpd-2.0.46-CAN-2004-0809.patch
License: Apache Software License
Group: System Environment/Daemons
BuildRoot: %{_tmppath}/%{name}-root
BuildPrereq: db4-devel, expat-devel, findutils, perl, pkgconfig, xmlto >= 0.0.11
BuildPrereq: libtool >= 1.4.3-6, pcre-devel
Requires: /etc/mime.types, gawk, /usr/share/magic.mime, /usr/bin/find
Prereq: /sbin/chkconfig, /bin/mktemp, /bin/rm, /bin/mv
Prereq: sh-utils, textutils, /usr/sbin/useradd
Provides: webserver
Provides: httpd-mmn = %{mmn}
Provides: apr = 0.9.3-2, apr-util = 0.9.3-2
Obsoletes: apache, secureweb, mod_dav, mod_gzip, stronghold-apache, stronghold-htdocs
Obsoletes: mod_put, mod_roaming

%description
Apache is a powerful, full-featured, efficient, and freely-available
Web server. Apache is also the most popular Web server on the
Internet.

%package devel
Group: Development/Libraries
Summary: Development tools for the Apache HTTP server.
Obsoletes: secureweb-devel, apache-devel, stronghold-apache-devel
Requires: httpd = %{version}-%{release}
Provides: apr-devel = 0.9.3-2, apr-util-devel = 0.9.3-2

%description devel
The httpd-devel package contains the APXS binary and other files
that you need to build Dynamic Shared Objects (DSOs) for Apache.

If you are installing the Apache HTTP server and you want to be
able to compile or develop additional modules for Apache, you need
to install this package.

%package -n mod_ssl
Group: System Environment/Daemons
Summary: SSL/TLS module for the Apache HTTP server
Serial: 1
BuildPrereq: openssl-devel, distcache-devel
Prereq: openssl, dev, /bin/cat
Requires: httpd = %{version}-%{release}, make, httpd-mmn = %{mmn}
Obsoletes: stronghold-mod_ssl

%description -n mod_ssl
The mod_ssl module provides strong cryptography for the Apache Web
server via the Secure Sockets Layer (SSL) and Transport Layer
Security (TLS) protocols.

%prep
%setup -q
%patch1 -p0 -b .apctl
%patch2 -p1 -b .apxs
%patch3 -p1 -b .sslink
%patch4 -p0 -b .parallel
%patch5 -p1 -b .deplibs
%patch7 -p1 -b .siglist
%patch8 -p1 -b .aprconfig
%patch9 -p1 -b .suexec
%patch10 -p1 -b .syspcre
%patch11 -p1 -b .aputest

# no -b to prevent droplets in install root
%patch20 -p1
%patch21 -p1 -b .davfs
%patch22 -p1 -b .davetag
%patch23 -p1 -b .sslincl
%patch24 -p1 -b .shmcb
%patch25 -p1 -b .logtimez
%patch26 -p1 -b .md5dig
%patch27 -p1 -b .rolog
%patch28 -p1 -b .include
%patch29 -p1 -b .sslcleanup
%patch30 -p1 -b .nested
%patch31 -p1 -b .deflate
%patch32 -p1 -b .sslmutex
%patch33 -p1 -b .miscfix
%patch34 -p1 -b .sslio
%patch35 -p1 -b .cache
%patch36 -p1 -b .graceful
%patch37 -p1 -b .confcont
%patch38 -p1 -b .srvheader
%patch39 -p1 -b .sslerr
%patch100 -p1 -b .execfail
%patch101 -p1 -b .worker
%patch102 -p1 -b .sslfakeauth
%patch103 -p1 -b .metharray
%patch104 -p1 -b .expires
%patch105 -p1 -b .worker2
%patch106 -p1 -b .proxy11
%patch107 -p1 -b .sslvars
%patch108 -p1 -b .davbadfrag
%patch109 -p1 -b .dav401dest
%patch110 -p1 -b .apusdbm
%patch111 -p1 -b .shapass
%patch112 -p1 -b .autoindex
%patch113 -p1 -b .sslscache
%patch114 -p1 -b .manpages
%patch115 -p1 -b .davmisc
%patch116 -p1 -b .digestmeth
%patch117 -p1 -b .deflate2
%patch118 -p1 -b .vhostaddr
%patch119 -p1 -b .cgirange
%patch120 -p1 -b .rgetline
%patch121 -p1 -b .davfslock

%patch40 -p1 -b .cnfdir
%patch41 -p0 -b .redhat
%patch42 -p0 -b .xfsz
%patch43 -p0 -b .pod
%patch44 -p1 -b .noshmht
%patch45 -p1 -b .proxy
%patch46 -p1 -b .distcache
%patch47 -p1 -b .largefile
%patch48 -p1 -b .testhook
%patch49 -p1 -b .dumpcerts
%patch50 -p1 -b .v4listen
%patch51 -p1 -b .addrconfig
%patch52 -p1 -b .guardarea
%patch53 -p1 -b .sslremain
%patch54 -p1 -b .davstream
%patch55 -p1 -b .aprmtime
%patch56 -p1 -b .apudbver
%patch57 -p1 -b .fdsetsize
%patch58 -p1 -b .cgibucket
%patch59 -p1 -b .aprlargecopy
%patch150 -p1 -b .sslhooks

%patch60 -p1 -b .can0192
%patch61 -p1 -b .can0254
%patch62 -p1 -b .can0253
%patch63 -p1 -b .can0020
%patch64 -p1 -b .vu379828
%patch65 -p1 -b .can0542
%patch66 -p1 -b .can0113
%patch67 -p1 -b .can0488
%patch68 -p1 -b .can0493
%patch69 -p1 -b .can0747
%patch70 -p1 -b .can0748
%patch71 -p1 -b .can0751
%patch72 -p1 -b .can0786
%patch73 -p1 -b .can0809

# Safety check: prevent build if defined MMN does not equal upstream MMN.
vmmn=`echo MODULE_MAGIC_NUMBER_MAJOR | cpp -include \`pwd\`/include/ap_mmn.h | sed -n '/^2/p'`
if test "x${vmmn}" != "x%{mmn}"; then
   : Error: Upstream MMN is now ${vmmn}, packaged MMN is %{mmn}.
   : Update the mmn macro and rebuild.
   exit 1
fi

# update location of migration guide in apachectl
%{__perl} -pi -e "s:\@docdir\@:%{_docdir}/%{name}-%{version}:g" \
	support/apachectl.in

: Using `gcc --version | sed q`

%build
# regenerate configure scripts
./buildconf

# Fix for http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=103316
perl -pi.libtool -e 's/^  x86_64\*\|s390x\*\)$/  x86_64\*\|s390x\*\|powerpc64\*\)/g' \
        srclib/apr/configure
RETVAL=3; diff srclib/apr/configure.libtool srclib/apr/configure || RETVAL=$?
if [ $RETVAL -ne 1 ]; then
  : failed to fix libtool bug?
  exit 1
fi

# Remove .RE and .RS from man pages, they look bad
perl -pi -e 's/^.R[ES]$//g' docs/man/*.[1-8]

# Build certwatch & man page
cc $RPM_OPT_FLAGS -o certwatch -Wall -Werror $RPM_SOURCE_DIR/certwatch.c -lcrypto
xmlto man $RPM_SOURCE_DIR/certwatch.xml

# Before configure; fix location of build dir in generated apxs
%{__perl} -pi -e "s:\@exp_installbuilddir\@:%{_libdir}/httpd/build:g" \
	support/apxs.in

# build the migration guide
xmlto --skip-validation -x $RPM_SOURCE_DIR/html.xsl html-nochunks $RPM_SOURCE_DIR/migration.xml
cp $RPM_SOURCE_DIR/migration.css . # make %%doc happy

CFLAGS="$RPM_OPT_FLAGS -DSSL_EXPERIMENTAL_ENGINE"
if pkg-config openssl ; then
	# configure -C barfs with trailing spaces in CFLAGS
	CFLAGS="$CFLAGS `pkg-config --cflags openssl | sed 's/ *$//'`"
	AP_LIBS="$AP_LIBS `pkg-config --libs openssl`"
else
	AP_LIBS="-lssl -lcrypto"
fi
export CFLAGS
export AP_LIBS

function mpmbuild()
{
mpm=$1; shift
mkdir $mpm; pushd $mpm
cat > config.cache <<EOF
ac_cv_func_pthread_mutexattr_setpshared=no
ac_cv_func_sem_open=no
ac_cv_have_decl_sys_siglist=yes
EOF
../configure -C \
 	--prefix=%{_sysconfdir}/httpd \
 	--exec-prefix=%{_prefix} \
 	--bindir=%{_bindir} \
 	--sbindir=%{_sbindir} \
 	--mandir=%{_mandir} \
	--libdir=%{_libdir} \
	--sysconfdir=%{_sysconfdir}/httpd/conf \
	--includedir=%{_includedir}/httpd \
	--libexecdir=%{_libdir}/httpd/modules \
	--datadir=%{contentdir} \
        --with-installbuilddir=%{_libdir}/httpd/build \
	--with-mpm=$mpm \
	--enable-suexec --with-suexec \
	--with-suexec-caller=%{suexec_caller} \
	--with-suexec-docroot=%{contentdir} \
	--with-suexec-logfile=%{_localstatedir}/log/httpd/suexec.log \
	--with-suexec-bin=%{_sbindir}/suexec \
	--with-suexec-uidmin=500 --with-suexec-gidmin=100 \
        --disable-v4-mapped \
        --with-devrandom=/dev/urandom \
        --without-gdbm \
	$*

make %{?_smp_mflags}
popd
}

# Only bother enabling optional modules for main build.
mpmbuild prefork --enable-mods-shared=all \
	--enable-ssl --with-ssl \
        --enable-distcache \
	--enable-deflate \
        --enable-logio \
	--enable-proxy --enable-proxy-connect \
	--enable-proxy-http --enable-proxy-ftp \
        --enable-cache --enable-mem-cache \
        --enable-file-cache --enable-disk-cache

# To prevent most modules being built statically into httpd.worker, 
# easiest way seems to be enable them shared.  Point worker build
# at the pre-built apr/apr-util for prefork.
pfroot=`pwd`/prefork/srclib
mpmbuild worker --enable-mods-shared=all \
        --with-apr=${pfroot}/apr --with-apr-util=${pfroot}/apr-util \
        --disable-rewrite --disable-headers --disable-proxy --disable-cache

# Sanity check that the built binaries have the same set of 
# builtin modules.
./prefork/httpd -l | grep -v prefork > prefork.mods
./worker/httpd -l | grep -v worker > worker.mods
if ! diff -u prefork.mods worker.mods; then
  : Different modules built into httpd binaries, will not proceed
  exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT

# Classify ab and logresolve as section 1 commands, as they are in /usr/bin
mv docs/man/ab.8 docs/man/ab.1
sed -e "1s/logresolve 8/logresolve 1/" \
  < docs/man/logresolve.8 > docs/man/logresolve.1
rm docs/man/logresolve.8

# Munge apr-config and apu-config to not reference the build root
perl -pi -e "s|/usr/src[^\"]*|/usr/lib/httpd/build|g" \
        prefork/srclib/apr{,-util}/ap[ru]-config

pushd prefork
make DESTDIR=$RPM_BUILD_ROOT install
popd
# install worker binary
install -m 755 worker/.libs/httpd $RPM_BUILD_ROOT%{_sbindir}/httpd.worker

# install conf file/directory
mkdir $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m 644 $RPM_SOURCE_DIR/README.confd \
   $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/README
install -m 644 $RPM_SOURCE_DIR/ssl.conf \
   $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/ssl.conf
install -m 644 $RPM_SOURCE_DIR/welcome.conf \
   $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/welcome.conf

rm $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/*.conf
install -m 644 $RPM_SOURCE_DIR/httpd.conf \
   $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/httpd.conf

# mod_ssl bits
for suffix in crl crt csr key prm; do
   mkdir $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/ssl.${suffix}
done

# Makefiles for certificate management
for ext in crt crl; do 
  install -m 644 $RPM_SOURCE_DIR/mod_ssl-Makefile.${ext} \
	$RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf/ssl.${ext}/Makefile.${ext}
done
ln -s ../../../usr/share/ssl/certs/Makefile $RPM_BUILD_ROOT/etc/httpd/conf

# for holding mod_dav lock database
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/dav

# create a prototype session cache
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/mod_ssl
touch $RPM_BUILD_ROOT%{_localstatedir}/cache/mod_ssl/scache.{dir,pag,sem}

# create cache root
mkdir $RPM_BUILD_ROOT%{_localstatedir}/cache/mod_proxy

# move utilities to /usr/bin
mv $RPM_BUILD_ROOT%{_sbindir}/{ab,htdbm,logresolve,htpasswd,htdigest} \
   $RPM_BUILD_ROOT%{_bindir}

# move builddir to the right place
mv $RPM_BUILD_ROOT%{contentdir}/build $RPM_BUILD_ROOT%{_libdir}/httpd/build
rm $RPM_BUILD_ROOT%{_libdir}/httpd/build/libtool
ln -s ../../../..%{_bindir}/libtool $RPM_BUILD_ROOT%{_libdir}/httpd/build/libtool

# Install and sanitize config_vars file: relocate the build directory into 
# libdir; reference correct libtool; remove references to RPM build root.
sed -e "s|%{contentdir}/build|%{_libdir}/httpd/build|g" \
    -e "/AP_LIBS/d" -e "/abs_srcdir/d" \
    -e "/^LIBTOOL/s|/[^ ]*/libtool|%{_bindir}/libtool|" \
    -e "s|/usr/src/.*/srclib/apr.*/include|/usr/include/httpd|" \
    -e "s|^EXTRA_INCLUDES.*$|EXTRA_INCLUDES = -I\$(includedir)|g" \
  < prefork/build/config_vars.mk \
  > $RPM_BUILD_ROOT%{_libdir}/httpd/build/config_vars.mk

# Make the MMN accessible to module packages
echo %{mmn} > $RPM_BUILD_ROOT%{_includedir}/httpd/.mmn

# docroot
mkdir $RPM_BUILD_ROOT%{contentdir}/html
install -m 644 $RPM_SOURCE_DIR/index.html \
	$RPM_BUILD_ROOT%{contentdir}/error/noindex.html

install -m 644 $RPM_SOURCE_DIR/powered_by.gif \
	$RPM_BUILD_ROOT%{contentdir}/icons
install -m 644 $RPM_SOURCE_DIR/powered_by_rh.png \
	$RPM_BUILD_ROOT%{contentdir}/icons

# logs
rmdir $RPM_BUILD_ROOT%{_sysconfdir}/httpd/logs
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/httpd

# symlinks for /etc/httpd
ln -s ../..%{_localstatedir}/log/httpd $RPM_BUILD_ROOT/etc/httpd/logs
ln -s ../..%{_localstatedir}/run $RPM_BUILD_ROOT/etc/httpd/run
ln -s ../..%{_libdir}/httpd/modules $RPM_BUILD_ROOT/etc/httpd/modules
ln -s ../..%{_libdir}/httpd/build $RPM_BUILD_ROOT/etc/httpd/build

# install SYSV init stuff
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m755 $RPM_SOURCE_DIR/httpd.init \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/httpd
%{__perl} -pi -e "s:\@docdir\@:%{_docdir}/%{name}-%{version}:g" \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/httpd	

# install log rotation stuff
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
install -m644 $RPM_SOURCE_DIR/httpd.logrotate \
	$RPM_BUILD_ROOT/etc/logrotate.d/httpd

# fix man page paths
sed -e "s|/usr/local/apache2/conf/httpd.conf|/etc/httpd/conf/httpd.conf|" \
    -e "s|/usr/local/apache2/conf/mime.types|/etc/mime.types|" \
    -e "s|/usr/local/apache2/conf/magic|/etc/httpd/conf/magic|" \
    -e "s|/usr/local/apache2/logs/error_log|/var/log/httpd/error_log|" \
    -e "s|/usr/local/apache2/logs/access_log|/var/log/httpd/access_log|" \
    -e "s|/usr/local/apache2/logs/httpd.pid|/var/run/httpd.pid|" \
    -e "s|/usr/local/apache2|/etc/httpd|" < docs/man/httpd.8 \
  > $RPM_BUILD_ROOT%{_mandir}/man8/httpd.8

# install certwatch
install -m 755 certwatch \
   $RPM_BUILD_ROOT%{_sbindir}/certwatch
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
install -m 755 $RPM_SOURCE_DIR/certwatch.cron \
   $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/certwatch
install -m 644 certwatch.8 \
   $RPM_BUILD_ROOT%{_mandir}/man8/certwatch.8

# Remove headers which are not part of the API
rm -f $RPM_BUILD_ROOT%{_includedir}/httpd/{ssl_expr_parse.h,ssl_util_table.h}

# Remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.exp \
      $RPM_BUILD_ROOT/etc/httpd/conf/mime.types \
      $RPM_BUILD_ROOT%{_libdir}/httpd/modules/*.exp \
      $RPM_BUILD_ROOT%{_sbindir}/{checkgid,dbmmanage,envvars*} \
      $RPM_BUILD_ROOT%{contentdir}/htdocs/* \
      $RPM_BUILD_ROOT%{contentdir}/cgi-bin/* \
      $RPM_BUILD_ROOT%{_mandir}/man1/dbmmanage.*
rm -rf $RPM_BUILD_ROOT%{contentdir}/manual

# Make suexec a+rw so it can be stripped.  %%files lists real permissions
chmod 755 $RPM_BUILD_ROOT%{_sbindir}/suexec

%pre
# Add the "apache" user
/usr/sbin/useradd -c "Apache" -u 48 \
	-s /sbin/nologin -r -d %{contentdir} apache 2> /dev/null || :

# Prevent removal of index.html on upgrades from 1.3
%triggerun -- apache < 2.0, stronghold-apache < 2.0
if [ -r %{contentdir}/index.html -a ! -r %{contentdir}/index.html.rpmold ]; then
  mv %{contentdir}/index.html %{contentdir}/index.html.rpmold
fi

%triggerpostun -- apache < 2.0
/sbin/chkconfig --add httpd

%triggerpostun -- stronghold-apache < 2.0
/sbin/chkconfig --add httpd

%post
# Register the httpd service
/sbin/chkconfig --add httpd

%preun
if [ $1 = 0 ]; then
	/sbin/service httpd stop > /dev/null 2>&1
	/sbin/chkconfig --del httpd
fi

%post -n mod_ssl
/sbin/ldconfig ### is this needed?
umask 077

if [ ! -f %{_sysconfdir}/httpd/conf/ssl.key/server.key ] ; then
%{_bindir}/openssl genrsa -rand /proc/apm:/proc/cpuinfo:/proc/dma:/proc/filesystems:/proc/interrupts:/proc/ioports:/proc/pci:/proc/rtc:/proc/uptime 1024 > %{_sysconfdir}/httpd/conf/ssl.key/server.key 2> /dev/null
fi

FQDN=`hostname`
if [ "x${FQDN}" = "x" ]; then
   FQDN=localhost.localdomain
fi

if [ ! -f %{_sysconfdir}/httpd/conf/ssl.crt/server.crt ] ; then
cat << EOF | %{_bindir}/openssl req -new -key %{_sysconfdir}/httpd/conf/ssl.key/server.key -x509 -days 365 -out %{_sysconfdir}/httpd/conf/ssl.crt/server.crt 2>/dev/null
--
SomeState
SomeCity
SomeOrganization
SomeOrganizationalUnit
${FQDN}
root@${FQDN}
EOF
fi

%check
# Check the built modules are all PIC
if readelf -d $RPM_BUILD_ROOT%{_libdir}/httpd/modules/*.so | grep TEXTREL; then
   : modules contain non-relocatable code
   exit 1  
fi

pushd prefork/srclib/apr-util/test
%define aputests testmd5 testrmm teststrmatch testuri
make %{?_smp_mflags} %{aputests} testdbm
for t in %{aputests}; do ./${t} || exit 1; done
./testdbm auto tsdbm
./testdbm -tDB auto tbdb.db
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%doc ABOUT_APACHE README CHANGES LICENSE
%doc migration.html migration.css

%dir %{_sysconfdir}/httpd
%{_sysconfdir}/httpd/modules
%{_sysconfdir}/httpd/logs
%{_sysconfdir}/httpd/run
%dir %{_sysconfdir}/httpd/conf
%config(noreplace) %{_sysconfdir}/httpd/conf/*.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/welcome.conf
%config(noreplace) %{_sysconfdir}/httpd/conf/magic

%config(noreplace) %{_sysconfdir}/logrotate.d/httpd
%config %{_sysconfdir}/rc.d/init.d/httpd

%dir %{_sysconfdir}/httpd/conf.d
%{_sysconfdir}/httpd/conf.d/README

%{_bindir}/ab
%{_bindir}/ht*
%{_bindir}/logresolve
%{_sbindir}/httpd
%{_sbindir}/httpd.worker
%{_sbindir}/apachectl
%{_sbindir}/rotatelogs
%attr(4510,root,%{suexec_caller}) %{_sbindir}/suexec

%{_libdir}/libapr-%{aprver}.so.*
%{_libdir}/libaprutil-%{aprver}.so.*

%dir %{_libdir}/httpd
%dir %{_libdir}/httpd/modules
# everything but mod_ssl.so:
%{_libdir}/httpd/modules/mod_[a-r]*.so
%{_libdir}/httpd/modules/mod_s[petu]*.so
%{_libdir}/httpd/modules/mod_[t-z]*.so

%dir %{contentdir}
%dir %{contentdir}/cgi-bin
%dir %{contentdir}/html
%dir %{contentdir}/icons
%dir %{contentdir}/error
%dir %{contentdir}/error/include
%{contentdir}/icons/*
%{contentdir}/error/README
%{contentdir}/error/noindex.html
%config %{contentdir}/error/*.var
%config %{contentdir}/error/include/*.html

%attr(0700,root,root) %dir %{_localstatedir}/log/httpd
%attr(0700,apache,apache) %dir %{_localstatedir}/lib/dav
%attr(0700,apache,apache) %dir %{_localstatedir}/cache/mod_proxy

%{_mandir}/man1/*

%{_mandir}/man8/apachectl*
%{_mandir}/man8/httpd*
%{_mandir}/man8/rotatelogs*
%{_mandir}/man8/suexec*

%files -n mod_ssl
%defattr(-,root,root)
%{_sbindir}/certwatch
%{_sysconfdir}/cron.daily/certwatch
%{_libdir}/httpd/modules/mod_ssl.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/ssl.conf
%attr(0700,root,root) %dir %{_sysconfdir}/httpd/conf/ssl.*
%config %{_sysconfdir}/httpd/conf/Makefile
%config %{_sysconfdir}/httpd/conf/ssl.*/*
%attr(0700,apache,root) %dir %{_localstatedir}/cache/mod_ssl
%attr(0600,apache,root) %ghost %{_localstatedir}/cache/mod_ssl/scache.dir
%attr(0600,apache,root) %ghost %{_localstatedir}/cache/mod_ssl/scache.pag
%attr(0600,apache,root) %ghost %{_localstatedir}/cache/mod_ssl/scache.sem
%{_mandir}/man8/certwatch.8*

%files devel
%defattr(-,root,root)
%{_bindir}/ap?-config
%{_libdir}/libapr*-%{aprver}.so
%{_libdir}/libapr*-%{aprver}.la
%{_libdir}/libapr*-%{aprver}.a
%{_includedir}/httpd
%{_sysconfdir}/httpd/build
%{_sbindir}/apxs
%{_mandir}/man8/apxs.8*
%dir %{_libdir}/httpd/build
%{_libdir}/httpd/build/*.mk
%{_libdir}/httpd/build/instdso.sh
%{_libdir}/httpd/build/libtool

%changelog
* Mon Sep 13 2004 Joe Orton <jorton@redhat.com> 2.0.46-40.ent
- mod_dav_fs: security fix for indirect lock refresh (CAN-2004-0809)
- mod_dav_fs: fix indirect lock handling on 64-bit platforms

* Mon Sep  6 2004 Joe Orton <jorton@redhat.com> 2.0.46-39.ent
- add security fixes for CAN-2004-0747, CAN-2004-0786
- mod_ssl: add security fix for CAN-2004-0751
- split security fix for CAN-2004-0748 out from -sslio patch
- merge ap_rgetline_core NUL-termination fixes from 2.0.5[01]
- have -devel require httpd of same V-R

* Mon Jul 12 2004 Joe Orton <jorton@redhat.com> 2.0.46-38.ent
- drop suexec minimum acceptable gid to 100 (#127667)
- mod_ssl: fix for upstream #29964

* Tue Jun 29 2004 Joe Orton <jorton@redhat.com> 2.0.46-37.ent
- add security fix for CAN-2004-0493 (Jeff Trawick) 

* Tue Jun 22 2004 Joe Orton <jorton@redhat.com> 2.0.46-36.ent
- mod_ssl: add ssl_is_https optional hook
- mod_rewrite: add %%{SSL:...} SSL variable lookup hook
- mod_rewrite: fix %%{HTTPS} variable (#120096)
- mod_headers: add %%{...}s SSL variable lookup hook

* Tue Jun  1 2004 Joe Orton <jorton@redhat.com> 2.0.46-35.ent
- mod_deflate: fix memory consumption for large responses
- fix handling of CGI scripts which produce a Content-Range header 
- merge from upstream:
 * fix vhost address handling (Jeff Trawick)

* Mon May 24 2004 Joe Orton <jorton@redhat.com> 2.0.46-34.ent
- mod_cgi: updated CGI bucket patch (more #112216)
- mod_ssl: security fix for overflow in FakeBasicAuth (CVE CAN-2004-0488)
- docs: man page presentation fixes
- mod_dav: fix to propagate executable property across COPY/MOVE
- mod_dav: fix some minor 2518 compliance issues and one 2617 issue  
- apr: support >2Gb files in apr_file_copy()
- merge from upstream:
 * mod_auth_digest: fix for subrequest method handling (Josh Dady)

* Tue Apr  6 2004 Joe Orton <jorton@redhat.com> 2.0.46-33.ent
- fix SHA1 password support (#119651)
- mod_autoindex: don't truncate output on stat() failure (#117959)
- mod_ssl: fix shmcb corruption with small caches (Geoff Thorpe)
- mod_ssl: fix memory leak in session cache (Madhu Mathihalli)
- include the mod_ext_filter module (#120072)
- mod_cgi: handle concurrent output on stderr/stdout (#112216)

* Mon Mar  1 2004 Joe Orton <jorton@redhat.com> 2.0.46-32.ent
- improved fix for CAN-2004-0113

* Thu Feb 26 2004 Joe Orton <jorton@redhat.com> 2.0.46-31.ent
- mod_ssl: fix memory leak, CVE CAN-2004-0113
- remove check that accept() returns fd < FD_SETSIZE (#116576)

* Thu Feb 19 2004 Joe Orton <jorton@redhat.com> 2.0.46-30.ent
- add mod_include rewrite from 2.0.49 (André Malo)

* Mon Feb 16 2004 Joe Orton <jorton@redhat.com> 2.0.46-29.ent
- rebuild for gcc optimisation fix on IA64 (#115328)
- add fix for apr_dbm_exists() for sdbm on ppc64/s390x

* Tue Feb 10 2004 Joe Orton <jorton@redhat.com> 2.0.46-28.ent
- add libtool symlink in /etc/httpd/build (#113720)
- mod_ssl: ssl_var_lookup fixes
- use system pcre to prevent conflicts with PHP (#98056)
- merge from upstream:
 * mod_dav: streaming PROPFIND responses (Ben Sussman)
 * apr: add apr_file_mtime_set
 * apr-util: add apu-config --db-version and apu_want.h support

* Tue Jan 27 2004 Joe Orton <jorton@redhat.com> 2.0.46-27.ent
- tighten parsing of CPP output in MMN check (#113934)
- fix AP[RU]_INCLUDEDIR in config_vars.mk (#112771)
- ensure that suexec is stripped and has minimal dependencies
- mod_ssl: fix streaming nph- CGI scripts over SSL
- mod_proxy: fix some HTTP compliance issues
- drop gdbm support from apr-util due to licence incompatibility
- add mod_logio
- merge from upstream:
 * fix worker crasher, memory corruption fix (Jeff Trawick)

* Wed Jan  7 2004 Joe Orton <jorton@redhat.com> 2.0.46-26.ent.1
- merge from upstream:
 * mod_proxy: fix a memory leak (Larry Hoppi, upstream #24991)
 * worker: fix a misleading warning message (Jeff Trawick)
 * mod_ssl: fix FakeBasicAuth for subrequests (Sander Striker)
 * mod_expires: several bug fixes (including #113929)

* Mon Nov 10 2003 Joe Orton <jorton@redhat.com> 2.0.46-26.ent
- include security fix for CVE CAN-2003-0542
- speed up graceful restart in prefork (#105725)
- move away /var/www/html/index.html before upgrade from 1.3 (#70705)
- fix for config parser to support containers without args
- include mpm*.h to fix mod_fastcgi build (#108080)
- mod_ssl: avoid error stack dumps during pphrase prompts
- mod_ssl: restore readable error descriptions in error log
- mod_proxy: fix Server header for proxied requests
- mod_cgi: fix logging of script exec failure messages
- mod_log_config: fix logging of timezone (upstream #23642)
- mod_include: fix for r->filename handling (upstream #23836)

* Thu Sep 25 2003 Joe Orton <jorton@redhat.com> 2.0.46-25.ent
- final migration guide updates

* Wed Sep 24 2003 Joe Orton <jorton@redhat.com> 2.0.46-24.ent
- update migration guide

* Fri Sep 19 2003 Joe Orton <jorton@redhat.com> 2.0.46-23.ent
- mention how to disable cronned warnings in certwatch(8)
- add fix for segfaults in proxy_fixup

* Tue Sep 16 2003 Joe Orton <jorton@redhat.com> 2.0.46-22.ent
- don't mention CompatEnvVars in ssl.conf
- add LoadModule for suexec to default httpd.conf
- avoid pathological read() behaviour in mod_disk_cache

* Fri Sep 12 2003 Joe Orton <jorton@redhat.com> 2.0.46-21.ent
- fix cleanup of -config scripts

* Fri Sep 12 2003 Joe Orton <jorton@redhat.com> 2.0.46-20.ent
- improve default ssl.conf (Florian La Roche, #103271)
- include ap[ru]-config, provide apr{,-util}-devel (Florian, #98445)

* Thu Sep 11 2003 Joe Orton <jorton@redhat.com> 2.0.46-19.ent
- obsolete mod_put, mod_roaming
- add SSL_CLIENT_V_REMAIN to mod_ssl
- tweak list syntax in man pages
- bump the module magic minor for VU#379828 (Peter Bowen, #104223)
- avoid split for FLUSH at end of brigade (via Peter Bowen, #104224)
- fix example location of ca-bundle.crt (#99243)

* Fri Sep  5 2003 Joe Orton <jorton@redhat.com> 2.0.46-18.ent
- fix including mod_ssl.h

* Fri Aug 29 2003 Joe Orton <jorton@redhat.com> 2.0.46-17.ent
- add new welcome page and logo (Garrett LeSage)
- mod_ssl: grammar fixes for private key prompting,
 fix for mod_ssl plain-HTTP-not-SSL error check (Steve Henson),
 CLIENT_CERT_CHAIN_ lookup fix (Jeff Trawick)
- mod_log_config: fix logging 0 bytes sent in CLF (Astrid Keßler)

* Thu Aug 28 2003 Joe Orton <jorton@redhat.com> 2.0.46-16.ent
- add ThreadGuardArea directive
- trim list of installed headers
- link libapr and libaprutil against libpthread
- from upstream (mostly): mod_ssl I/O filter fixes
- don't add -L/usr/lib64 to LDFLAGS

* Wed Aug 27 2003 Joe Orton <jorton@redhat.com> 2.0.46-15.ent
- include certwatch(8) in mod_ssl package
- remove ssl_mutex at startup if left from previous invocation
- add trigger for upgrade from Stronghold

* Tue Aug 26 2003 Joe Orton <jorton@redhat.com> 2.0.46-14.ent
- allow upgrade from Stronghold 4.0

* Fri Aug 22 2003 Joe Orton <jorton@redhat.com> 2.0.46-13.ent
- enable crypto accelerator support

* Thu Aug 21 2003 Joe Orton <jorton@redhat.com> 2.0.46-12.ent
- security fixes for CVE CAN-2003-0020, CERT VU#379828
- complete removal of Welcome page bypass (#99206)
- use AI_ADDRCONFIG in getaddrinfo() calls where appropriate 
- from upstream: mod_deflate fixes

* Mon Aug  4 2003 Joe Orton <jorton@redhat.com> 2.0.46-11.ent
- support httpd -t -DDUMP_CERTS to dump SSL certificates
- use /dev/urandom to fix slow mod_auth_digest startup
- add apr fix for race in nested mutexes
- disable multilingual error docs by default (#99472)
- move configuration for Welcome page to conf.d (#99206)
- default Listen to use IPv4 not IPv6 if no address is specified

* Wed Jul 30 2003 Joe Orton <jorton@redhat.com> 2.0.46-10.ent
- add fix for mod_ssl leaving libcrypto in bad state during startup
- allow large (>2gb) log files on 32-bit platforms (#80603)
- fix handling of -Wc, options when linking in apxs

* Wed Jul 30 2003 Joe Orton <jorton@redhat.com> 2.0.46-9.ent
- rebuild to fix #101145

* Tue Jul 29 2003 Joe Orton <jorton@redhat.com> 2.0.46-8.ent
- security fixes for CAN-2003-0192, CAN-2003-0253, CAN-2003-0254
- use anonymous shmem in shmcb, avoiding #80520
- use sys_siglist[] array for signal number->name mappings
- disable use of IPv4-mapped IPv6 addresses
- only listen on 0.0.0.0 in default config (#98916)
- don't add eNULL cipher in default ssl.conf (#98401)
- load mod_deflate in default config
- from upstream: mod_include fixes; open log files read-only;
  AddLanguage fixes to httpd.conf

* Thu Jul  3 2003 Joe Orton <jorton@redhat.com> 2.0.46-7.ent
- fix to link mod_ssl against distcache correctly

* Tue Jun 17 2003 Joe Orton <jorton@redhat.com> 2.0.46-6.ent
- add distcache support (feature #87074)
- update server version string
- remove mod_cgid
- use shmcb as default session cache in ssl.conf
- fix mod_ssl.h for use in installed tree

* Tue Jun 10 2003 Joe Orton <jorton@redhat.com> 2.0.46-5.ent
- fix apxs -q LIBTOOL, apxs -g

* Tue Jun 10 2003 Joe Orton <jorton@redhat.com> 2.0.46-4.ent
- fix httpd.worker
- remove -manual subpackage

* Thu May 29 2003 Joe Orton <jorton@redhat.com> 2.0.46-3.ent
- updates for default httpd.conf
- fix omission of manual/style in httpd-manual

* Thu May 29 2003 Joe Orton <jorton@redhat.com> 2.0.46-2.ent
- fix libtool relink bug

* Thu May 29 2003 Joe Orton <jorton@redhat.com> 2.0.46-1.ent
- update to 2.0.46 for RHEL; use bundled apr/apr-util again
- drop experimental modules

* Mon May 19 2003 Joe Orton <jorton@redhat.com> 2.0.45-6
- don't load /usr/sbin/envvars from apxs
- add fix for mod_dav_fs namespace handling
- add fix for mod_dav If header etag comparison
- remove irrelevant warning from mod_proxy
- don't conflict with thttpd (#91422)

* Sun May 18 2003 Joe Orton <jorton@redhat.com> 2.0.45-5
- don't package any XML sources in httpd-manual
- fix examples in default httpd.conf for enabling caching

* Sun May 18 2003 Joe Orton <jorton@redhat.com> 2.0.45-4
- change default charset to UTF-8 (#88964)

* Thu May 15 2003 Joe Orton <jorton@redhat.com> 2.0.45-3
- update httpd.conf for changes from default in 2.0.45
- include conf.d/*.conf after loading standard modules
- include LDAP and cache modules (#75370, #88277)
- run buildconf in %%build not %%prep

* Tue May 13 2003 Joe Orton <jorton@redhat.com> 2.0.45-2
- have apxs always use /usr/bin/libtool

* Mon May 5 2003 Joe Orton <jorton@redhat.com> 2.0.45-1
- update to 2.0.45 (#82227)
- use separate apr, apr-util packages (#74951)
- mark logrotate file as noreplace (#85654)
- mark all of /var/www/error as %%config-not-noreplace
- remove dates from error pages (#86474)
- don't enable mod_cgid for worker MPM (#88819)

* Wed Apr 30 2003 Elliot Lee <sopwith@redhat.com> 2.0.40-22
- headusage patch to fix build on ppc64 etc.

* Tue Apr  1 2003 Joe Orton <jorton@redhat.com> 2.0.40-21.1
- add security fixes for CAN-2003-0020, CAN-2003-0132, CAN-2003-0083
- add security fix for file descriptor leaks, #82142
- add bug fix for #82587

* Mon Feb 24 2003 Joe Orton <jorton@redhat.com> 2.0.40-21
- add security fix for CAN-2003-0020; replace non-printable characters
  with '!' when printing to error log.
- disable debuginfo on IA64.

* Tue Feb 11 2003 Joe Orton <jorton@redhat.com> 2.0.40-20
- disable POSIX semaphores to support 2.4.18 kernel (#83324)

* Wed Jan 29 2003 Joe Orton <jorton@redhat.com> 2.0.40-19
- require xmlto 0.0.11 or later
- fix apr_strerror on glibc2.3

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 2.0.40-18
- rebuilt

* Thu Jan 16 2003 Joe Orton <jorton@redhat.com> 2.0.40-17
- add mod_cgid and httpd binary built with worker MPM (#75496)
- allow choice of httpd binary in init script
- pick appropriate CGI module based on loaded MPM in httpd.conf
- source /etc/sysconfig/httpd in apachectl to get httpd choice
- make "apachectl status" fail gracefully when links isn't found (#78159)

* Mon Jan 13 2003 Joe Orton <jorton@redhat.com> 2.0.40-16
- rebuild for OpenSSL 0.9.7

* Fri Jan  3 2003 Joe Orton <jorton@redhat.com> 2.0.40-15
- fix possible infinite recursion in config dir processing (#77206)
- fix memory leaks in request body processing (#79282)

* Thu Dec 12 2002 Joe Orton <jorton@redhat.com> 2.0.40-14
- remove unstable shmht session cache from mod_ssl
- get SSL libs from pkg-config if available (Nalin Dahyabhai)
- stop "apxs -a -i" from inserting AddModule into httpd.conf (#78676)

* Wed Nov  6 2002 Joe Orton <jorton@redhat.com> 2.0.40-13
- fix location of installbuilddir in apxs when libdir!=/usr/lib

* Wed Nov  6 2002 Joe Orton <jorton@redhat.com> 2.0.40-12
- pass libdir to configure; clean up config_vars.mk
- package instdso.sh, fixing apxs -i (#73428)
- prevent build if upstream MMN differs from mmn macro
- remove installed but unpackaged files

* Wed Oct  9 2002 Joe Orton <jorton@redhat.com> 2.0.40-11
- correct SERVER_NAME encoding in i18n error pages (thanks to Andre Malo)

* Wed Oct  9 2002 Joe Orton <jorton@redhat.com> 2.0.40-10
- fix patch for CAN-2002-0840 to also cover i18n error pages

* Wed Oct  2 2002 Joe Orton <jorton@redhat.com> 2.0.40-9
- security fixes for CAN-2002-0840 and CAN-2002-0843
- fix for possible mod_dav segfault for certain requests

* Tue Sep 24 2002 Gary Benson <gbenson@redhat.com>
- updates to the migration guide

* Wed Sep  4 2002 Nalin Dahyabhai <nalin@redhat.com> 2.0.40-8
- link httpd with libssl to avoid library loading/unloading weirdness

* Tue Sep  3 2002 Joe Orton <jorton@redhat.com> 2.0.40-7
- add LoadModule lines for proxy modules in httpd.conf (#73349)
- fix permissions of conf/ssl.*/ directories; add Makefiles for
  certificate management (#73352)

* Mon Sep  2 2002 Joe Orton <jorton@redhat.com> 2.0.40-6
- provide "httpd-mmn" to manage module ABI compatibility

* Sun Sep  1 2002 Joe Orton <jorton@redhat.com> 2.0.40-5
- fix SSL session cache (#69699)
- revert addition of LDAP support to apr-util

* Mon Aug 26 2002 Joe Orton <jorton@redhat.com> 2.0.40-4
- set SIGXFSZ disposition to "ignored" (#69520)
- make dummy connections to the first listener in config (#72692)

* Mon Aug 26 2002 Joe Orton <jorton@redhat.com> 2.0.40-3
- allow "apachectl configtest" on a 1.3 httpd.conf
- add mod_deflate
- enable LDAP support in apr-util
- don't package everything in /var/www/error as config(noreplace)

* Wed Aug 21 2002 Bill Nottingham <notting@redhat.com> 2.0.40-2
- add trigger (#68657)

* Mon Aug 12 2002 Joe Orton <jorton@redhat.com> 2.0.40-1
- update to 2.0.40

* Wed Jul 24 2002 Joe Orton <jorton@redhat.com> 2.0.36-8
- improve comment on use of UserDir in default config (#66886)

* Wed Jul 10 2002 Joe Orton <jorton@redhat.com> 2.0.36-7
- use /sbin/nologin as shell for apache user (#68371)
- add patch from CVS to fix possible infinite loop when processing
  internal redirects

* Wed Jun 26 2002 Gary Benson <gbenson@redhat.com> 2.0.36-6
- modify init script to detect 1.3.x httpd.conf's and direct users
  to the migration guide

* Tue Jun 25 2002 Gary Benson <gbenson@redhat.com> 2.0.36-5
- patch apachectl to detect 1.3.x httpd.conf's and direct users
  to the migration guide
- ship the migration guide

* Fri Jun 21 2002 Joe Orton <jorton@redhat.com>
- move /etc/httpd2 back to /etc/httpd
- add noindex.html page and poweredby logo; tweak default config
  to load noindex.html if no default "/" page is present.
- add patch to prevent mutex errors on graceful restart

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 2.0.36-4
- automated rebuild

* Wed Jun 12 2002 Joe Orton <jorton@redhat.com> 2.0.36-3
- add patch to fix SSL mutex handling

* Wed Jun 12 2002 Joe Orton <jorton@redhat.com> 2.0.36-2
- improved config directory patch

* Mon May 20 2002 Joe Orton <jorton@redhat.com>
- initial build; based heavily on apache.spec and mod_ssl.spec
- fixes: #65214, #58490, #57376, #61265, #65518, #58177, #57245
