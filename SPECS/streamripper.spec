%if %{_build_vendor} == "redhat"
 %define _rel fdr
%else
 %define _rel %{_build_vendor}
%endif

Name:           streamripper
Version:        1.61.4

Release:        1.%{_rel}
Epoch:          2
Summary:        Rip Shoutcast streams

Group:          Applications/Multimedia
License:        GPL2
URL:            http://streamripper.sourceforge.net/index.php
Source0:        ftp://ftp.sourceforge.net/pub/sourceforge/s/st/streamripper/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc, glibc-devel 
Requires:      glibc

Obsoletes:	streamripper-1.61.4-1

%description
With the emergence of file sharing protocols such as Napster, Gnutella, and now Mojonation and Freenet, the average Internet user can download nearly any mp3 he wants in a matter of no time, but many times people don't know what they want. Streamripper allows you to download an entire station of music. Many of these mp3 radio stations only play certain genres, so you can now download an entire collection of goa/trance music, an entire collection of jazz, punk rock, whatever you want.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
cp %{name}.1 $RPM_BUILD_ROOT/%{_mandir}/man1


%clean
rm -rf $RPM_BUILD_ROOT


%post

%preun

%postun

%files 
%defattr(-,root,root,-)
%doc CHANGES COPYING README THANKS
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sun Mar 06 2005 Casper Pedersen <cpedersen[AT]c-note.dk> - 1:1.61.4-1
- Fixed License 

* Sat Mar 05 2005 Casper Pedersen <cpedersen[AT]c-note.dk> - 1:1.61.4-1
- Initial RPM release.
