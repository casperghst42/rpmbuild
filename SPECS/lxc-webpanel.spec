Name:	   lxc-webpanel 
Version:   0.2
Release:   1
Epoch:     1
Summary:   The most awesome web panel for LXC
Packager:  Casper Pedersen <cpedersen[at]c-note.dk>

Group:     Applications/System
License:   MIT
URL:       https://lxc-webpanel.github.io/index.html
Source0:   https://github.com/lxc-webpanel/LXC-Web-Panel/archive/%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  python-flask

%description
The most awesome web panel for LXC (https://github.com/lxc-webpanel/LXC-Web-Panel/archive/0.2.zip)

%prep
unzip %{SOURCE0}

%build
# Ugly hack to get around that we do not have a tar.gz

%install


%clean
#rm -rf $RPM_BUILD_ROOT

%post

%preun

%postun

%files 
%defattr(-,root,root,-)
%{_sbindir}/*
%{_defaultdocdir}/%{name}/*

%changelog
* Wed Oct 25 2017 Casper Pedersen <cpedersen[AT]c-note.dk> 
- Initial RPM release.
