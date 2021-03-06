Name:           exiv2
Version:        0.6.1
Release:        1.fdr
Epoch:          1
Summary:        Exiv2 comprises of a C++ library and a command line utility to access image metadata. Exiv2 is free software
Packager:	Casper Pedersen <cpedersen[at]c-note.dk>
Group:          Applications/Multimedia
License:        GPL
URL:            http://home.arcor.de/ahuggel/exiv2/index.html
Source0:        http://home.arcor.de/ahuggel/exiv2/exiv2-0.6.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description     
Exiv2 comprises of a C++ library and a command line utility to access image metadata. Exiv2 is free software

# Requires:       <requirements>
#Conflicts:      
#Obsoletes:      
#BuildConflicts: 
#Requires(pre,post): 

%prep

%setup -q


%build
# For QT apps: [ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
##%configure --prefix=$RPM_BUILD_ROOT
./configure --prefix=$RPM_BUILD_ROOT/usr
make %{?_smp_mflags}

#make test
#make check

%package        devel
Group:          Development/Libraries
Summary:        Exiv2 comprises of a C++ library and a command line utility to access image metadata. Exiv2 is free software
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    devel
Exiv2 comprises of a C++ library and a command line utility to access image metadata. Exiv2 is free software

%install
## rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
## %find_lang %{name}

mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}/doc
cp -a  README.make $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}/
cp -ar doc/* $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}/doc/

mkdir -p $RPM_BUILD_ROOT%{_

## rm -f $RPM_BUILD_ROOT%{_infodir}/dir
## find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%clean
# rm -rf $RPM_BUILD_ROOT


# ldconfig's for packages that install %{_libdir}/*.so.*
# -> Don't forget Requires(post,postun): /sbin/ldconfig
# ...and install-info's for ones that install %{_infodir}/*.info*
# -> Don't forget Requires(post,preun): /sbin/install-info

%post
/sbin/ldconfig
# /sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :

%preun
# if [ $1 = 0 ]; then
#   /sbin/install-info --delete %{_infodir}/%{name}.info \
#     %{_infodir}/dir 2>/dev/null || :
# fi

%postun
/sbin/ldconfig


%files 
%defattr(-,root,root,-)
# %doc README.make
%{_bindir}/*
%{_libdir}/*.so*
%{_defaultdocdir}/%{name}-%{version}/*
# %{_datadir}/%{name}
# %{_mandir}/man[^3]/*

%changelog
* Sat Feb 12 2005 Casper Pedersen <cpedersen[AT]c-note.dk> - 1:0.6.1-1
- Initial RPM release.
