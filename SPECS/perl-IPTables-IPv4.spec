%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPTables-IPv4


Name:           perl-IPTables-IPv4
Version:        0.98
Release:        1
Summary:        Perl module for manipulating iptables rules for the IPv4 protocol
License:        Distributable, see COPYING
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IPTables-IPv4/
Source0:        http://www.cpan.org/modules/by-module/IPTables/IPTables-IPv4-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This package provides a nice interface to the IP Tables control API that
fairly closely parallels the C API exported in libiptc for manipulating
firewalling and forwarding rules for IPv4 packets. Also, a tied multilayer
data structure has been built, allowing the tables, chains, rules and
fields to be manipulated in a more natural fashion.

%prep
%setup -n %{real_name}-%{version}

%build
mv modules/Makefile modules/Makefile-orig
cat modules/Makefile-orig | sed '/^CFLAGS/s/$/ -fPIC/' > modules/Makefile
mv libiptc/Makefile libiptc/Makefile-orig
cat libiptc/Makefile-orig | sed '/^CFLAGS/s/$/ -fPIC/' > libiptc/Makefile



CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" SITEPREFIX="%{buildroot}%{_prefix}"  PREFIX="%{buildroot}%{_prefix}"

TD=`echo $RPM_BUILD_ROOT%_prefix | sed s,/,\\\\\\\\\\/,g`
mv Makefile Makefile-orig
cat Makefile-orig | sed "/INSTALL_DIR/s/=/=$TD/" > Makefile

%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install

find %{buildroot} -name .packlist -exec %{__rm} {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST README Todo
%doc %{_mandir}/man3/IPTables::IPv4.3pm*
%doc %{_mandir}/man3/IPTables::IPv6.3pm*
%dir %{perl_vendorarch}/IPTables/
%{perl_vendorarch}/IPTables/IPv4.pm
%{perl_vendorarch}/IPTables/IPv4/
%{perl_vendorarch}/IPTables/IPv6.pm
#%{perl_vendorarch}/IPTables/IPv6/
%dir %{perl_vendorarch}/auto/IPTables/
%{perl_vendorarch}/auto/IPTables/IPv4/
%{perl_vendorarch}/auto/IPTables/IPv6/


%changelog
* Fri Apr 03 2009 cpedersen 0.98-1
- Specfile autogenerated by cpanspec 1.77.