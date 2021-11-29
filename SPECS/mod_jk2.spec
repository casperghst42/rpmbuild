Name:           mod_jk2
Version:        2.0.2
Release:        1.fc1
Summary:        JK2 is a refactoring of JK and is much more powerfull.

Group:          System Enviroment/Libraries
License:        The Apache Software License, Version 1.1
URL:            http://jakarta.apache.org/tomcat/tomcat-4.1-doc/jk2/
Source0:        jakarta-tomcat-connectors-jk2-2.0.4-src.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gcc
BuildRequires:  httpd-devel 
BuildRequires:  apr
BuildRequires:  apr-devel
BuildRequires:  apr-util
BuildRequires:  apr-util-devel
Requires:       httpd >= 2.0.47
Requires:	jakarta-tomcat

%description
Even if it works with Apache 1.3, JK2 has been developed with Apache 2.0 in mind, and is better suited for multi-threaded servers like IIS, NES/iPlanet. It can also be embeded in other applications and used from java.

%prep
if [ -z $JAVA_HOME ]; then
  echo "\"JAVA_HOME\" is not set - exiting"
  exit 255;
fi
if [ -z $TOMCAT_HOME ]; then
  echo "\"TOMCAT_HOME\" is not set - exiting"
  exit 255;
fi
if [ ! -x /etc/httpd/build/libtool ]; then
  echo "\"/etc/httpd/build/libtool\" is missing!!"
  echo "as root do: ln -s /usr/bin/libtool /etc/httpd/build/libtool"
  exit 255;
fi

mkdir -p %{buildroot}/etc/httpd/conf
mkdir -p %{buildroot}/etc/httpd/conf.d
mkdir -p %{buildroot}/usr/lib/httpd/modules
mkdir -p %{buildroot}/usr/share/doc/%{name}-%{version}
mkdir -p %{buildroot}/usr/share/doc/%{name}-%{version}/conf
mkdir -p %{buildroot}/usr/share/doc/%{name}-%{version}/docs

%setup -n jakarta-tomcat-connectors-jk2-2.0.4-src

%build
cd jk/native2
sh buildconf.sh
%configure --with-apxs2=/usr/sbin/apxs --with-java-home=${JAVA_HOME} --with-apr-include=/usr/include/apr-0 
make %{?_smp_mflags}
cd ../..

%install
strip jk/build/jk2/apache2/mod_jk2.so
strip jk/build/jk2/apache2/jkjni.so
cp -a jk/build/jk2/apache2/mod_jk2.so %{buildroot}/usr/lib/httpd/modules
cp -a jk/build/jk2/apache2/jkjni.so %{buildroot}/usr/lib/httpd/modules
cp -a KEYS %{buildroot}/usr/share/doc/%{name}-%{version}
cp -a LICENSE %{buildroot}/usr/share/doc/%{name}-%{version}
cp -a jk/README.txt %{buildroot}/usr/share/doc/%{name}-%{version}
cp -ar jk/conf/* %{buildroot}/usr/share/doc/%{name}-%{version}/conf
cp -ar jk/build/docs/* %{buildroot}/usr/share/doc/%{name}-%{version}/docs
cp -a jk/conf/workers2.properties %{buildroot}/etc/httpd/conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/libtool --finish /usr/lib/httpd/modules 2>&1 > /dev/null
if [ -z $TOMCAT_HOME ]; then
  TOMCAT_HOME="<modify>"
  echo "Modify /etc/httpd/conf.d/mod_jk2.conf!!"
  echo "Replace \"<modify>\" with a correct path to your Jakarta Tomcat installation"
fi
cat << EOF > /etc/httpd/conf.d/mod_jk2.conf
# Load jk2_module
LoadModule jk2_module modules/mod_jk2.so
#                                                                               
# Give access to /examples context
Alias /examples ${TOMCAT_HOME}/webapps/examples
<Directory ${TOMCAT_HOME}/webapps/examples>
        Order allow,deny
        Allow from all
</Directory>
EOF

%preun

%postun

%files 
%defattr(-,root,root,-)
/usr/lib
/usr/share
/etc

%changelog
* Fri Jan 16 2004 Casper Pedersen <casper[AT]fedoranews.org> 2.0.2-1
- Initial RPM release.
