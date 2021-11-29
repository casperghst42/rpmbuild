Name:    coretemp
Version: 1.1
Release: 2.el5
Group:   System Environment/Kernel
License: GPL v2
Summary: CentOS-5 coretemp module
URL:     http://www.kernel.org/

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-build-%(%{__id_u} -n)
ExclusiveArch: i686 x86_64

# Sources.
Source0:  %{name}-%{version}.tar.bz2
Source10: kmodtool-%{name}
Patch0: coretemp-msr.patch
Patch1: coretemp-compat-2.6.18.patch

# If kversion isn't defined on the rpmbuild line, build for the current kernel.
%{!?kversion: %define kversion %(uname -r)}

# Define the variants for each architecture.
%define basevar ""
%ifarch i686
%define paevar PAE
%endif
%ifarch i686 x86_64
%define xenvar xen
%endif

# If kvariants isn't defined on the rpmbuild line, build all variants for this architecture.
%{!?kvariants: %define kvariants %{?basevar} %{?xenvar} %{?paevar}}

# Magic hidden here.
%define kmodtool sh %{SOURCE10}
%{expand:%(%{kmodtool} rpmtemplate_kmp %{name} %{kversion} %{kvariants} 2>/dev/null)}

%description
This package provides the kernel module for monitoring the
temperature of the Intel Core 2 Duo and Quad processors.
It is built to depend upon the specific ABI provided by a range of releases
of the same variant of the CentOS kernel and not on any one specific build.

%prep
%setup -q -c -T -a 0
%patch0 -p1
%patch1 -p1
for kvariant in %{kvariants} ; do
    cp -a %{name}-%{version} _kmod_build_$kvariant
done

%build
for kvariant in %{kvariants} ; do
    ksrc=%{_usrsrc}/kernels/%{kversion}${kvariant:+-$kvariant}-%{_target_cpu}
    pushd _kmod_build_$kvariant
    make -C "${ksrc}" modules M=$PWD
    popd
done

%install
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=extra/%{name}
for kvariant in %{kvariants} ; do
    ksrc=%{_usrsrc}/kernels/%{kversion}${kvariant:+-$kvariant}-%{_target_cpu}
    pushd _kmod_build_$kvariant
    make -C "${ksrc}" modules_install M=$PWD
    install -d ${INSTALL_MOD_PATH}/usr/lib/debug
    popd
done

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Dec 19 2008 Philip J Perry <ned@unixmail.co.uk>
- Rebased to kernel-2.6.27.10 driver. 1.1-2.el5
- Added MSR patch <coretemp-msr.patch>
- Added 2.6.18 build compatibility patch <coretemp-compat-2.6.18.patch>

* Sat Dec 06 2008 Philip J Perry <ned@unixmail.co.uk>
- Rebased to kernel-2.6.27.8 driver. 1.1-1.el5

* Mon Oct 27 2008 Alan J Bartlett <ajb.stxsl@gmail.com>
- Total revision of the spec file. 1.1-1

* Tue Jul 15 2008 Alan J Bartlett <ajb.stxsl@gmail.com>
- Fixed bugs in spec file. 1.0-4.92.1.6.el5

* Sat Jul 12 2008 Philip J Perry <ned@unixmail.co.uk>
- Fixed dependencies. 1.0-3.92.1.6.el5

* Tue Jul 08 2008 Philip J Perry <ned@unixmail.co.uk>
- Fixed bug in spec file. 1.0-2.92.1.6.el5

* Tue Jul 08 2008 Philip J Perry <ned@unixmail.co.uk>
- Initial RPM build. 1.0-1.92.1.6.el5
