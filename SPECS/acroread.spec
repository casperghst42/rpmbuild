Name		: acroread
Version		: 5.0.10
Release		: 1

License		: Commercial 	
Summary		: Adobe Acrobat Reader with Mozilla Plugin	
Group		: Applications/Internet

URL  		: http://www.adobe.com/
Vendor		: Adobe Systems Incorporated
Packager	: Thomas Chung <tchung@fedoranews.org>

BuildRoot	: %{_tmppath}/%{name}-%{version}-buildroot
Source0		: linux-5010.tar.gz
Source1         : acroread.desktop
Source2         : acroread.png
Patch0		: acroread.patch

AutoReq		: No
AutoProv	: No

%description
Adobe Acrobat Reader is the free viewing companion to Adobe Acrobat 5.0.
Acrobat Reader lets you view, navigate and print Portable Document Format (PDF)
files. Adobe Acrobat 5.0 is a complete solution for creating, enhancing,
reviewing, editing, and sharing information in PDF.

%prep
rm -rf %{buildroot}

%setup -q -n installers
#######################################################################
# setup macro
# -a num  : Only unpack source number after changing to the directory
# -b num  : Only unpack source number before changing to the directory
# -c      : Create directory before unpacking.
# -D      : Do not delete the directory before unpacking
# -n name : Name the directory as name
# -q      : Run quiety with minimum output
# -T      : Disable the automatic unpacking of the archives.
#######################################################################
tar xpf COMMON.TAR
tar xpf LINUXRDR.TAR
rm *.TAR
%patch0

%install
#########################################################
# Common Red Hat RPM macros (rpm --showrc for more info)
# {_sourcedir}  : /usr/src/redhat/SOURCES
# {_builddir}   : /usr/src/redhat/BUILD
# {_tmppath}    : /var/tmp
# {_libdir}     : /usr/lib
# {_bindir}     : /usr/bin
# {_datadir}    : /usr/share/
# {_mandir}     : /usr/share/man
# {_docdir}     : /usr/share/doc
# {_sysconfdir} : /etc
# {buildroot}
# {name}
# {version}
# {release}
##########################################################
%{__install} -d %{buildroot}%{_libdir}/acroread
%{__cp} -a Reader Resource %{buildroot}%{_libdir}/acroread
%{__install} -D -m 755 Browsers/intellinux/nppdf.so %{buildroot}%{_libdir}/mozilla/plugins/nppdf.so
%{__install} -D -m 755 Browsers/intellinux/nppdf.so %{buildroot}%{_libdir}/firefox/plugins/nppdf.so
%{__install} -D -m 755 bin/acroread.sh %{buildroot}%{_bindir}/acroread
%{__install} -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/acroread.desktop
%{__install} -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/acroread.png

%clean
rm -rf %{buildroot}
                                                                                                                        
%files
#####################################################
# defattr sets the default attributes for all files
#####################################################
%defattr(-,root,root)
%doc LICREAD.TXT README
%{_libdir}/acroread
%{_libdir}/mozilla/plugins/nppdf.so
%{_libdir}/firefox/plugins/nppdf.so
%{_bindir}/acroread
%{_datadir}/applications/acroread.desktop
%{_datadir}/pixmaps/acroread.png

%changelog
* Sat Dec 18 2004 Thomas Chung <tchung@fedoranews.org> 5.0.10-1
- Extract COMMON.TAR and LINUXRDR.TAR in the setup directive 
- Use gendiff script to create the patch
- Use patch directive to apply the patch

* Fri Dec 17 2004 Thomas Chung <tchung@fedoranews.org> 5.0.10-0
- Rebuild RPM for version 5.0.10
- Support for firefox
- New for Acrobat Reader 5.0.10
  A security patch was applied that solves a problem reported
  with malformed mail containing pdf attachments.

* Sun Jul 04 2004 Thomas Chung <tchung@fedoranews.org> 5.0.9-0
- Rebuild RPM for version 5.0.9
- New for Acrobat Reader 5.0.9
  A security patch was applied that solves a couple of problems
  reported with malformed uuencoded pdf files.

* Tue Jan 06 2004 Thomas Chung <tchung@fedoranews.org> 5.0.8-0
- Rebuild RPM for version 5.0.8
- Support for Gnome Menu
- Patch LANG, install_dir in acroread.sh
- New for Acrobat Reader 5.0.8
  A security patch was applied that solves a problem reported
  with long URLs in weblinks which can cause a buffer overrun.

