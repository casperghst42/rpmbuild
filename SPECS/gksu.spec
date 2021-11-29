Name:           gksu
Version:        1.2.2
Release:        2.fdr
Epoch:          1
Summary:        GKSu is a library that provides a Gtk+ frontend to su and sudo.

Group:          Applications/System
License:        GPL
URL:            http://www.nongnu.org/gksu/
Packager:	Casper Pedersen <cpedersen[at]c-note.dk>
Source0:        http://people.debian.org/~kov/gksu/gksu-1.2.2.tar.gz
#Source99:       <for original Red Hat or upstream spec as *.spec.upstream>
# Patch0:         gnome-terminal.patch
#Patch1:         
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtk2-devel
BuildRequires:	atk-devel
BuildRequires:	pango-devel
BuildRequires:  desktop-file-utils
BuildRequires:	glib2-devel
BuildRequires:	glibc-devel

Requires:       gtk2
Requires:	atk
Requires:	pango
Requires:	glib2
Requires:	glibc

#Requires(pre):  
#Requires(post): 
#Conflicts:      
#Obsoletes:      
#BuildConflicts: 

%description
GKSu is a library that provides a Gtk+ frontend to su and sudo. It supports login shells and preserving environment when acting as a su frontend. It is useful to menu items or other graphical programs that need to ask a user's password to run another program as another user.

%package        devel
Summary:        GKSu is a library that provides a Gtk+ frontend to su and sudo.
Group:          Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    devel
GKSu is a library that provides a Gtk+ frontend to su and sudo. It supports login shells and preserving environment when acting as a su frontend. It is useful to menu items or other graphical programs that need to ask a user's password to run another program as another user.

%prep
%setup -q

# %patch0 -p1 -b .ignome-terminal

%build
# For QT apps: [ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
# For GConf apps: prevent schemas from being installed at this stage
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

#desktop-file-install --vendor fedora                     \
#   --add-category X-Fedora                               \
#   --add-category SystemTools                            \
#   --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
#   gksu.desktop

#desktop-file-install --vendor fedora                     \
#   --add-category X-Fedora                               \
#   --add-category SystemTools                            \
#   --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
#   gksuexec.desktop

# Note: the find_lang macro requires gettext
%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%check || :
#make test
#make check


%clean
rm -rf $RPM_BUILD_ROOT


# ldconfig's for packages that install %{_libdir}/*.so.*
# -> Don't forget Requires(post) and Requires(postun): /sbin/ldconfig
# ...and install-info's for ones that install %{_infodir}/*.info*
# -> Don't forget Requires(post) and Requires(preun): /sbin/install-info

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :
# For GConf apps: install schemas as system default
#export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
#gconftool-2 --makefile-install-rule \
#  %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null

/usr/bin/update-desktop-database -q

%preun
if [ $1 -eq 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info \
    %{_infodir}/dir 2>/dev/null || :
fi
# For GConf apps: uninstall app's system default schemas
#export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
#gconftool-2 --makefile-uninstall-rule \
#  %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :

%postun -p /sbin/ldconfig
/usr/bin/update-desktop-database -q

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_libdir}/libgksu.so.*
#%{_libdir}/*.a
%{_libdir}/%{name}/*
%{_datadir}/gtk-doc/html/%{name}/
%{_datadir}/pixmaps/%{name}*
%{_datadir}/applications/%{name}*.desktop
%{_mandir}/man[^3]/*

%files devel
%defattr(-,root,root,-)
#%doc HACKING
%{_includedir}/%{name}/
%{_libdir}/*.a
%{_libdir}/*.so.*
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Feb 10 2005 Casper Pedersen <cpedersen[AT]c-note.dk> - 1:1.2.2-1
- New version 1.2.2

* Wed Jan 19 2005 Casper Pedersen <cpedersen[AT]c-note.dk> - 2:1.0.7-1
- Issue with gksu.desktop - using gnome-terminal

* Tue Jan 18 2005 Casper Pedersen <cpedersen[AT]c-note.dk> - 1:1.0.7-1
- Initial RPM release.

