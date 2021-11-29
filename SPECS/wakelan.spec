Summary: wakelan - send a wake-on-lan packet
Name: wakelan
Version: 1.1
Release: 1
License: GPL
Group: Networking/Utilities
Source: ftp://sunsite.unc.edu/pub/Linux/system/Network/misc/wakelan-1.1.tar.gz
Buildroot: %{_tmppath}/%{name}-root

%description
WakeLan sends a properly formatted UDP packet across the network which will
cause a wake-on-lan enabled computer to power on.

%changelog
%prep
%setup

%build
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=$RPM_BUILD_ROOT/usr --mandir=$RPM_BUILD_ROOT
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install wakelan $RPM_BUILD_ROOT%{_bindir}
install wakelan.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Tue Oct 28 2009 Casper Pedersen <cpedersen@c-note.dk> 1.1-1
Updating SPEC file

* Sat Aug 29 1998 Christopher Chan-Nui <channui+wakelan@freeware.tiny.org>
- Initial SPEC file
