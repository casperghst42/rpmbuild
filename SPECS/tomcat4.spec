%define PkgName		tomcat4
%define Destination	/opt/tomcat4
%define WebAppDir	/var/www

Name:           jakarta-tomcat
Version:        4.1.29
Release:        3.fc1
Summary:        Jakarta is a project of The Apache Software Foundation(ASF)

Group:          System Environment/Daemons
License:        The Apache Software License, Version 1.1
URL:            http://jakarta.apache.org/
Source0:        jakarta-tomcat-4.1.29.tar.gz 
Source1:	tomcat4
Source2:        dtomcat4
Source3:	tomcat4.conf	
Source4:	tomcat4-logrotate
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       mod_jk2 >= 2.0.2
Requires:	httpd >= 2.0.47

%description
Tomcat is the servlet container that is used in the official Reference Implementation for the Java Servlet and JavaServer Pages technologies. The Java Servlet and JavaServer Pages specifications are developed by Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and released under the Apache Software License. Tomcat is intended to be a collaboration of the best-of-breed developers from around the world. We invite you to participate in this open development project. 

%prep
rm -rf %{_builddir}/%{name}-%{version}
%setup -q -n %{name}-%{version}
mkdir -p %{buildroot}%{Destination}
mkdir -p %{buildroot}%{Destination}/conf
mkdir -p %{buildroot}%{_datadir}/doc/%{name}-%{version}
mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_sysconfdir}/%{PkgName}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_var}/log/tomcat
mkdir -p %{buildroot}%{_var}/spool/tomcat/work
mkdir -p %{buildroot}%{WebAppDir}

%build

%install
cp -ar bin                  %{buildroot}%{Destination}
cp -ar common               %{buildroot}%{Destination}
cp -ar conf                 %{buildroot}%{Destination}
cp -ar server               %{buildroot}%{Destination}
cp -ar shared               %{buildroot}%{Destination}
cp -ar temp                 %{buildroot}%{Destination}
cp -ar webapps              %{buildroot}%{WebAppDir}
cp -a LICENSE               %{buildroot}%{_datadir}/doc/%{name}-%{version}
cp -a README.txt            %{buildroot}%{_datadir}/doc/%{name}-%{version}
cp -a RELEASE-NOTES-4.1.txt %{buildroot}%{_datadir}/doc/%{name}-%{version}
cp -a RELEASE-PLAN-4.1.txt  %{buildroot}%{_datadir}/doc/%{name}-%{version}
cp -a RUNNING.txt           %{buildroot}%{_datadir}/doc/%{name}-%{version}

## Custom files
cp -a  %{SOURCE1} %{buildroot}%{_initrddir}
cp -a  %{SOURCE2} %{buildroot}%{Destination}/bin
cp -a  %{SOURCE3} %{buildroot}%{_sysconfdir}/%{PkgName}
cp -a  %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/tomcat4

%clean
rm -rf $RPM_BUILD_ROOT

%pre
# We don't want tomcat to run at root:root, with this
# tomcat will run as tomcat4:tomcat4
isgrp=`getent group %{PkgName} 2> /dev/null | wc -l | xargs printf "%d"`
if [ $isgrp -eq 0 ] ; then
  /usr/sbin/groupadd -r -g 91  %{PkgName} 
fi

isusr=`getent passwd %{PkgName} 2> /dev/null | wc -l | xargs printf "%d"`
if [ $isusr -eq 0 ] ; then
 /usr/sbin/useradd -c "Tomcat user" -s /bin/bash \
    -r -d %{Destination} -g 91 -u 91 %{PkgName} 
fi

%post
echo "CATALINA_HOME=%{Destination}" >> %{_sysconfdir}/%{PkgName}/%{PkgName}.conf
echo "JASPER_HOME=%{Destination}" >> %{_sysconfdir}/%{PkgName}/%{PkgName}.conf
echo "CATALINA_TMPDIR=%{Destination}/temp" >> %{_sysconfdir}/%{PkgName}/%{PkgName}.conf

# Logfiles should be in /var/log
ln -sf %{_var}/log/tomcat %{Destination}/logs

# Temp work files should be in /var/spool/tomcat
ln -sf %{_var}/spool/tomcat/work %{Destination}/work

# WebApps should be in /var/www/webapps
ln -sf %{WebAppDir}/webapps %{Destination}/webapps

chown root:root %{_initrddir}/%{PkgName} 2>&1 /dev/null
chmod 744 %{_initrddir}/%{PkgName} 2>&1 > /dev/null

/sbin/chkconfig --add %{PkgName}

%preun
rm -f %{Destination}/logs
rm -f %{Destination}/work
rm -f %{Destination}/webapps

/sbin/chkconfig %{PkgName} off
/sbin/chkconfig --del %{PkgName}

%postun
isusr=`getent passwd %{PkgName} 2> /dev/null | wc -l | xargs printf "%d"`
if [ $isusr -ne 0 ] ; then
  /usr/sbin/userdel %{PkgName} 
fi

isgrp=`getent group %{PkgName} 2> /dev/null | wc -l | xargs printf "%d"`
if [ $isgrp -ne 0 ] ; then
  /usr/sbin/groupdel %{PkgName} 
fi

%files 
%defattr(-,tomcat4,tomcat4,-)
%{Destination}
%{_datadir}/doc/%{name}-%{version}
%{_var}/log/tomcat
%{_var}/spool/tomcat
%{_sysconfdir}
%{WebAppDir}

%changelog
* Tue Mar 09  2004 Casper Pedersen <casper[AT]fedoranew.org>  - 4.1.29-3
- Using more macros
- Moved contents of webapps to /var/www/webapps
- using getent instead of grep for user/group (Thanks to Jeff Carlson)

* Fri Feb 06  2004 Casper Pedersen <casper[AT]fedoranews.org> - 4.1.29-2
- Added more stable scripts to start tomcat, provided by: 
  Gomez Henri <hgomez@users.sourceforge.net>
  Keith Irwin <keith_irwin@non.hp.com>
  Nicolas Mailhot <nicolas.mailhot@one2team.com>
  Novell eNterprise Services for Linux - src rpm's are available from forge.novell.com)

* Fri Jan 18  2004 Casper Pedersen <casper[AT]fedoranews.org> - 4.1.29-1
- Initial RPM release.
