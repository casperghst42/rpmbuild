%define initdir  %{_initrddir}
%define menudir  %{_datadir}/applications
%define pixmaps  %{_datadir}/pixmaps/novelclient

Summary		: Novell Client for Linux 	
Name		: novelclient
Version		: 0.86
Release		: 3
Group		: Applications/Communications
License		: GPL 	
Vendor		: Ken Conrad
URL  		: http://novelclient.sourceforge.net
Packager	: Casper Pedersen <cpedersen@c-note.dk>
Source0		: novelclient-0.86.i386.tar.gz
Source1		: multicast.init
Source2		: multicast.conf
BuildRoot	: %{_tmppath}/%{name}-buildroot
Requires	: glibc >= 2.3.2
Requires	: ncpfs >= 2.2.3
Requires	: compat-libstdc++ >= 7.3-2
AutoReqProv     : no
# Disables generating dependencies automatically

%description 
Novell Client for Linux

The Novel Client for Linux is a GUI front-end for the ncpfs utilities making it easy to transfer data to and from a Novell Netware fileserver. Connections can be made using IP or IPX, Bindery or NDS to Netware server versions from 3.x through 6.x. Novel Client runs on Linux in X Windows. It is written in Object-Pascal using Kylix from Borland.

%prep
rm -rf %buildroot
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/kylix2
mkdir -p %{buildroot}%{menudir}
mkdir -p %{buildroot}%{pixmaps}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{initdir}

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
%setup -n novelclient -q

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
cp -a graphics/NovelClient_*.png %{buildroot}%{pixmaps}
cp -a usr/local/lib/kylix2/* %{buildroot}%{_libdir}/kylix2
cp -a Novel %{buildroot}%{_bindir}
cp -a dhcp %{buildroot}%{_bindir}
cp -a ncplist %{buildroot}%{_bindir}
cp -a ncpwhoami %{buildroot}%{_bindir}
cp -a slpquery %{buildroot}%{_bindir}

cp -a %{SOURCE1} %{buildroot}%{initdir}/multicast
cp -a %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/multicast

ln -sf %{_libdir}/kylix2/libqtintf-6.5.0-qt2.3.so %{buildroot}%{_libdir}/kylix2/libqtintf-6.5-qt2.3.so 
ln -sf %{_libdir}/kylix2/libqt.so.2.3.0 %{buildroot}%{_libdir}/kylix2/libqt.so.2 

#
# Generate the shell script to start the client
#
cat << EOF > %{buildroot}%{_bindir}/novelclient
#!/bin/sh
# Change this path to match where you installed the kylix libraries
export LD_LIBRARY_PATH=%{_libdir}/kylix2
# Change this to match where you stored the binary
%{_bindir}/Novel
EOF

#
# Generate the .desktop file
#
cat << EOF > %{buildroot}%{menudir}/NovelClient.desktop
[Desktop Entry]
Name=NovelClient
Comment=Novel Login
Exec=novelclient
Icon=%{pixmaps}/NovelClient_48.png
Terminal=0
Type=Application
Categories=Communication
EOF

%clean
rm -rf %buildroot
        
%post
/sbin/chkconfig --add multicast 2>&1 > /dev/null
/sbin/chkconfig multicast on 2>&1 > /dev/null
%{initdir}/multicast start

chown root:root %{_bindir}/novelclient
chmod 555 %{_bindir}/novelclient

/bin/chmod +s `/usr/bin/which ncpmount`
/bin/chmod +s `/usr/bin/which ncpumount`
/bin/chmod +s `/usr/bin/which slist`

%preun
%{initdir}/multicast stop

%postun
/bin/chmod -s `/usr/bin/which ncpmount`
/bin/chmod -s `/usr/bin/which ncpumount`
/bin/chmod -s `/usr/bin/which slist`


%files
#####################################################
# %defattr sets the default attributes for all files
#####################################################
%defattr(755,root,root)
%doc LICENSE INSTALL CHANGELOG README
%{_sysconfdir}
%{_bindir}
%{_libdir}
%{menudir}
%{pixmaps}

%changelog
* Wed Mar 5 2004 Casper Pedersen <cpedersen@c-note.dk> 0.86-3
- new version of Novelclient 
- modified to use rpmbuild macros for portability.
- removed fc1 from packagename

* Wed Feb 11 2004 Casper Pedersen <cpedersen@c-note.dk> 0.85a-2.fc1
- multicast have been added as a service script

* Thu Jan 9 2004 Casper Pedersen <cpedersen@c-note.dk> 0.85a-1.fc1
- First try

