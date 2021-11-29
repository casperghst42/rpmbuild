Summary		: MySQL Control Center	
Name		: mysqlcc
Version		: 0.9.4
Release		: 4.fdr
Group		: Applications/Databases
License		: GPL 	
Vendor		: MySQL AB
URL  		: http://www.mysql.com/downloads/mysqlcc.html
Packager	: Casper Pedersen <cpedersen@c-note.dk>
Source0		: mysqlcc-0.9.4-linux-glibc23.tar.gz
Source1		: mysqlcc.xpm
Source2		: mysqlcc.desktop
BuildRoot	: %{_tmppath}/%{name}-buildroot
Requires	: glibc >= 2.3.2
AutoReqProv     : no
# Disables generating dependencies automatically

%description 
MySQL Control Center

%prep
rm -rf %buildroot
mkdir -p %buildroot/usr/local
mkdir -p %buildroot/usr/share/applications
mkdir -p %buildroot/usr/share/pixmaps

#######################################################################
# %setup macro
# -a num  : Only unpack source number after changing to the directory
# -b num  : Only unpack source number before changing to the directory
# -c      : Create directory before unpacking.
# -D      : Do not delete the directory before unpacking
# -n name : Name the directory as name
# -q      : Run quiety with minimum output
# -T      : Disable the automatic unpacking of the archives.
#######################################################################
%setup -q -n mysqlcc-0.9.4-linux-glibc23

############################################
# %{_sourcedir} : /usr/src/redhat/SOURCES
# %{_builddir}  : /usr/src/redhat/BUILD
# %{_tmppath}   : /var/tmp
# %{_libdir}    : /usr/lib
# %{_bindir}    : /usr/bin
# %{_datadir}   : /usr/share
# %{_mandir}    : /usr/man
# %{buildroot}
# %{name}
# %{version}
# %{release}
# rpm --showrc for more info
###########################################3
%install
cd %{buildroot}/usr/local
tar zxf %{SOURCE0}
cp -a %{SOURCE1}  %buildroot/usr/share/pixmaps
cp -a %{SOURCE2}  %buildroot/usr/share/applications

%clean
rm -rf %buildroot
        
%post
ln -sf /usr/local/%{name}-%{version}-linux-glibc23 /usr/local/mysqlcc

%postun
rm -rf /usr/local/mysqlcc                                                                                                                
%files
#####################################################
# %defattr sets the default attributes for all files
#####################################################
%defattr(-,root,root)
%doc LICENSE.txt INSTALL.txt Changelog.txt README.txt TODO.txt
/usr/local/%{name}-%{version}-linux-glibc23
/usr/share/applications/mysqlcc.desktop 
/usr/share/pixmaps

%changelog
* Sat Dec 11 2004 Casper Pedersen <cpedersen@c-note.dk> 0.9.4-4.fdr
- Renamed to 'fdr' package

* Sat Jan 3 2004 Casper Pedersen <cpedersen@c-note.dk> 0.9.4-3.fc1
- Group set to Applications/Databases
- Fixed installation point to follow instructions from developer

* Fri Jan 2 2004 Casper Pedersen <cpedersen@c-note.dk> 0.9.4-2.fc1
- Changed License to GPL

* Wed Dec 30 2003 Casper Pedersen <cpedersen@c-note.dk> 0.9.4-1.fc1
- First try

