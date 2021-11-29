Name:           amavis-new
Version:        20030616
Release:        p9.1
Epoch:          0
Summary:        amavisd-new is a high-performance interface between mailer (MTA) and content checkers: virus scanners, and/or SpamAssassin

Group:          System Environment/Daemons
Packager:	Casper Pedersen 
License:        GPL
URL:            http://www.ijs.si/software/amavisd/
Source0:        http://www.ijs.si/software/amavisd/amavisd-new-20030616-p9.tar.gz
Source1:	amavisd_init_milter.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  sendmail-devel
Requires:	sendmail
Requires:       perl-Archive-Tar
Requires:	perl-Archive-Zip
Requires:	perl-Compress-Zlib
Requires:	perl-Convert-TNEF
Requires:	perl-Convert-UUlib
Requires:	perl-MailTools
Requires:	perl-MIME-Tools
Requires:	perl-MIME-Base64
Requires:	perl-Net-Server
Requires:	perl-Time-HiRes
Requires:	perl-Unix-SysLog
Requires:	perl-libnet
Requires:	perl-IO-stringy
Requires:	perl-Digest-MD5

%description
amavisd-new is a high-performance interface between mailer (MTA) and content checkers: virus scanners, and/or SpamAssassin. It is written in Perl for maintainability, without paying a significant price for speed. It talks to MTA via (E)SMTP or LMTP, or by using helper programs. Best with Postfix, fine with dual-sendmail setup and Exim v4, works with sendmail/milter, or with any MTA as a SMTP relay.

%prep
mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/README_FILES
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/helper-progs
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/test-messages

%setup -n amavisd-new-20030616

%build
cd helper-progs
%configure
make %{?_smp_mflags}
make install DESTDIR=$RPM_BUILD_ROOT%{_sbindir}
cd ..

%install
## Enable if Courie IMAP/POP3 daemon is used.
## patch -p0 < amavisd-new-courier.patch

cp -a amavisd %{buildroot}%{_sbindir}
cp -a amavisd.conf %{buildroot}%{_sysconfdir}
cp -a amavisd_init.sh %{buildroot}%{_initrddir}
cp -a %{SOURCE1} %{buildroot}%{_initrddir}
cp -ar INSTALL AAAREADME.first LDAP.schema LICENSE MANIFEST RELEASE_NOTES %{buildroot}%{_docdir}/%{name}-%{version}
cp -ar README_FILES/* %{buildroot}%{_docdir}/%{name}-%{version}/README_FILES
cp -ar helper-progs/README %{buildroot}%{_docdir}/%{name}-%{version}/helper-progs
cp -ar test-messages/* %{buildroot}%{_docdir}/%{name}-%{version}/test-messages


%clean
# rm -rf $RPM_BUILD_ROOT

%post
if [ `getent group amavis 2> /dev/null | wc -l | xargs printf "%d"` -eq 0 ] ; then
  groupadd -r amavis 2>&1 /dev/null
fi

if [ `getent passwd amavis 2> /dev/null | wc -l | xargs printf "%d"` -eq 0 ] ; then
  useradd -r -g amavis -d /var/amavis amavis
  mkdir -p /var/amavis
  chown amavis.amavis /var/amavis
fi


%preun

%postun
if [ `getent passwd amavis 2> /dev/null | wc -l | xargs printf "%d"` -ne 0 ] ; then
  userdel amavis
fi

if [ `getent group amavis 2> /dev/null | wc -l | xargs printf "%d"` -ne 0 ] ; then
  groupdel amavis
fi

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}/*
%{_sbindir}/*
%{_sysconfdir}/*

%changelog
* Fri May 09 2004 Casper Pedersen <cpedersen[AT]c-note.dk> - 1:20030616.p9-1
- Initial RPM release.
