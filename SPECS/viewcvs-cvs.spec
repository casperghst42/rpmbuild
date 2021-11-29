Summary:	A CGI program for browsing CVS repositories.
Name:		viewcvs
Version:	1.0
Release:	0.%(date "+%Y%m%d%H")%{?distro_release:.%{distro_release}}
Epoch:		0
License:	BSD
Group:		System/Servers
Source0:	%{name}-cvs.tar.bz2
URL:		http://viewcvs.sf.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	rcs
Requires:	enscript
Requires:	webserver
# Need cgi.py
Requires:       python
BuildArch:	noarch

%description
ViewCVS is a visual (www) interface to explore a cvs repository. This is a
rewrite of cvsweb by Greg Stein.

%prep
%setup -q -n %{name}
# cvs update
(cd $RPM_BUILD_DIR; tar -cjf %{SOURCE0} %{name})

%build

%install
%__rm -rf $RPM_BUILD_ROOT

for i in `find . -name "*.cgi" -o -name "*.py"`; do
  %__perl -p -i \
        -e 's|LIBRARY_DIR = .*|LIBRARY_DIR = \"%{_datadir}/%{name}/lib\"|g;' \
        -e 's|CONF_PATHNAME = .*|CONF_PATHNAME = \"%{_sysconfdir}/cvs/%{name}.conf\"|g;' \
        -e 's|g_install_dir = .*|g_install_dir = \"%{_datadir}/%{name}\"|g;' $i
done

%__perl -p -i -e 's|<VIEWCVS_INSTALL_DIRECTORY>|%{_datadir}/%{name}|g;' viewcvs.conf.dist
%__perl -p -i -e 's|cvsgraph_conf =.*|cvsgraph_conf = %{_datadir}/%{name}/cvsgraph.conf|g;' viewcvs.conf.dist

find . -name "*.py" -o -name "*.ezt" -exec %__perl -p -i -e 's|.gif|.png|g;' {} \;

%__install -d -m 755 $RPM_BUILD_ROOT%{_var}/www/cgi-bin
%__install -m 755 www/cgi/*.cgi $RPM_BUILD_ROOT%{_var}/www/cgi-bin

%__install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/cvs
%__install -m 644 viewcvs.conf.dist $RPM_BUILD_ROOT%{_sysconfdir}/cvs/%{name}.conf

%__install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a lib $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a templates $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a tools/* $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a website $RPM_BUILD_ROOT%{_datadir}/%{name}/doc
%__install -m 644 cvsgraph.conf.dist $RPM_BUILD_ROOT%{_datadir}/%{name}/cvsgraph.conf

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README INSTALL TODO
%{_datadir}/%{name}
%{_var}/www/cgi-bin/*.cgi
%config(noreplace) %{_sysconfdir}/cvs/viewcvs.conf

%changelog
* Sat Sep 04 2004 Aleksey Nogin <rpm@nogin.org> 1.0-0.20040904
- Red Hat version

* Tue Jun 08 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0-0.20040223.4mdk
- Requires python itself (cgi.py)

* Tue Feb 24 2004 David Walluck <walluck@linux-mandrake.com> 0:1.0-0.20040223.3mdk
- use existing perl regex instead of patch

* Tue Feb 24 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0-0.20040223.2mdk
- %%patch0: uses png icons since http2 don't have gif

* Mon Feb 23 2004 David Walluck <walluck@linux-mandrake.com> 0:1.0-0.20040223.1mdk
- 1.0-dev (CVS-20040223) - svn 1.0 is out now, so why not update this as well
- update my email address in %%changelog

* Sun Feb 01 2004 David Walluck <walluck@linux-mandrake.com> 0:1.0-0.20040201.1mdk
- 1.0-dev (CVS-20040201) with fix for enabling of cvsgraph when not using cvs
- fix path of custom cvsgraph config

* Sun Oct 19 2003 David Walluck <walluck@linux-mandrake.com> 0:1.0-0.20031104.1mdk
- 1.0-dev (CVS-20031104) with svn support

* Thu May 29 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 0.9.2-5mdk
- fixed documentation and icons installation
- fhs patch
- cvsgraph patch
- noarch
- spec cleanup

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9.2-4mdk
- rebuild

* Tue Feb 12 2002 Alexander Skwar <ASkwar@DigitalProjects.com> 0.9.2-3mdk
- Modify the viewcvs.cgi "binary" to include the Library Dir by default
- Modify the Python viewcvs.py, query.py and cvsdb.py to
  include the CONF_PATHNAME
- Make setup be quiet
- Don't compile the python sources, because else references to the
  buildroot will be in the compiled files!

* Tue Feb 12 2002 Alexander Skwar <ASkwar@DigitalProjects.com> 0.9.2-2mdk
- Move cgi files from /var/www/html/cgi-bin to /var/www/cgi-bin
- Change URL
- Include the "template" configuration files as documentation
- Add %clean section to make rpmlint happy
- This needs a webserver - Added Requires: webserver

* Wed Jan 16 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.2-1mdk
- switch to python-2.2
- new release

* Mon Dec 31 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-1mdk
- 0.9.1

* Thu Sep 06 2001 Etienne Faure <etienne@mandrakesoft.com> 0.7-1mdk
- version 0.7

* Thu Mar 01 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.5-3mdk
- fix build

* Tue Sep 19 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.5-2mdk
- macros & clean spec

* Mon Jul 10 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.5-1mdk
- first Mandrake version.    
