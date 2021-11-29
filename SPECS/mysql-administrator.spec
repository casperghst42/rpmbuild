%define version		1.0.16
%define release		1

Summary: A MySQL server management, configuration and monitoring tool.
Name: mysql-administrator
Version: %{version}
Release: %{release}.%{targos}
Group: Applications/Databases
Vendor: MySQL AB
License: GPL
URL: http://www.mysql.com/products/administrator
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: pcre-devel >= 3.9
%if "%{targos}" == "suse91"
BuildRequires: libglade2-devel >= 2.0.0, gtkmm2-devel >= 2.2.0
%else if "%{targos}" == "rh9"
BuildRequires: libglade2-devel >= 2.0.0, gtkmm2-devel >= 2.2.0
%else
BuildRequires: libglade2-devel >= 2.0.0, gtkmm2-devel >= 2.2.0
%endif

%description
MySQL Administrator is a powerful visual administration console that 
enables you to easily administer your MySQL environment and gain 
significantly better visibility into how your databases are operating. 
MySQL Administrator now integrates database management and maintenance 
into a single, seamless environment, with a clear and intuitive graphical 
user interface.

It's part of the MySQL Administration Suite.

%prep
%setup -q -n %{name}-%{version}/mysql-gui-common
%setup -q -n %{name}-%{version}/%{name}

%build

# first we have to build the common libs
cd ../mysql-gui-common
%configure --with-commondirname=administrator
make %{?_smp_mflags}

# then the app itself
cd ../%{name}
%configure --with-commondirname=administrator
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
cd ../mysql-gui-common
make DESTDIR=%{buildroot} install

cd ../%{name}
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}%{_datadir}/mysql-gui/doc/administrator/
cp -a doc/* %{buildroot}%{_datadir}/mysql-gui/doc/administrator/
 
%clean
rm -rf %{buildroot}

%files
%defattr(0644, root, root, 0755)
%doc ChangeLog COPYING res/FAQ
%attr(0755,root,root) %{_bindir}/mysql-administrator
%attr(0755,root,root) %{_bindir}/mysql-administrator-bin
%{_datadir}/applications/*.desktop
%{_datadir}/mysql-gui/*.png
%dir %{_datadir}/mysql-gui/administrator
%{_datadir}/mysql-gui/administrator/*
%dir %{_datadir}/mysql-gui/doc/administrator
%{_datadir}/mysql-gui/doc/administrator/*

%changelog
* Sat Apr  3 2004 Alfredo Kojima <alfredo@mysql.com> 1.0.3_alpha-1
- initial RPM packaging

