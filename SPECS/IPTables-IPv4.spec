#
#   - IPTables::IPv4 -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   The following arguments were used:
#       IPTables::IPv4
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define pkgname IPTables-IPv4
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}
%define maketest 1

name:      perl-IPTables-IPv4
summary:   IPTables-IPv4 - Perl module for manipulating iptables rules for the IPv4 protocol
version:   0.98
release:   1
vendor:    Derrik Pates <dpates@dsdk12.net>
packager:  Arix International <cpan2rpm@arix.com>
license:   Artistic
group:     Applications/CPAN
url:       http://www.cpan.org
buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
buildarch: i386
prefix:    %(echo %{_prefix})
source:    http://search.cpan.org//CPAN/authors/id/D/DP/DPATES/IPTables-IPv4-0.98.tar.gz

%description
This package provides a nice interface to the IP Tables control API that fairly
closely parallels the C API exported in libiptc for manipulating firewalling
and forwarding rules for IPv4 packets. Also, a tied multilayer data structure
has been built, allowing the tables, chains, rules and fields to be
manipulated in a more natural fashion.

Wrappers have been implemented for all methods except one
("iptc_check_packet()"), and according to Harald Welte and Rusty Russell,
the unimplemented call will likely remain so. Protocol-specific match
modules have been implemented for TCP, UDP and ICMP. Several target and
non-protocol match modules have been implemented.

The module will be built with a default library path built into it. That
can be overridden using the IPT_IPV4_MODPATH environment variable. If your
script is being called suid root, you may want to do
"delete $ENV{IPT_IPV4_MODPATH};" to ensure that someone isn't subverting
your script. Make sure you do this before you "use IPTables::IPv4;" to
ensure that it never loads from an unapproved path.

#
# This package was generated automatically with the cpan2rpm
# utility.  To get this software or for more information
# please visit: http://perl.arix.com/
#

%prep
%setup -q -n %{pkgname}-%{version} 
chmod -R u+w %{_builddir}/%{pkgname}-%{version}

%build
grep -rsl '^#!.*perl' . |
grep -v '.bak$' |xargs --no-run-if-empty \
%__perl -MExtUtils::MakeMaker -e 'MY->fixin(@ARGV)'
CFLAGS="$RPM_OPT_FLAGS"
%{__perl} Makefile.PL `%{__perl} -MExtUtils::MakeMaker -e ' print qq|PREFIX=%{buildroot}%{_prefix}| if \$ExtUtils::MakeMaker::VERSION =~ /5\.9[1-6]|6\.0[0-5]/ '`
%{__make} 
%if %maketest
%{__make} test
%endif

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{makeinstall} `%{__perl} -MExtUtils::MakeMaker -e ' print \$ExtUtils::MakeMaker::VERSION <= 6.05 ? qq|PREFIX=%{buildroot}%{_prefix}| : qq|DESTDIR=%{buildroot}| '`

cmd=/usr/share/spec-helper/compress_files
[ -x $cmd ] || cmd=/usr/lib/rpm/brp-compress
[ -x $cmd ] && $cmd

# SuSE Linux
if [ -e /etc/SuSE-release -o -e /etc/UnitedLinux-release ]
then
    %{__mkdir_p} %{buildroot}/var/adm/perl-modules
    %{__cat} `find %{buildroot} -name "perllocal.pod"`  \
        | %{__sed} -e s+%{buildroot}++g                 \
        > %{buildroot}/var/adm/perl-modules/%{name}
fi

# remove special files
find %{buildroot} -name "perllocal.pod" \
    -o -name ".packlist"                \
    -o -name "*.bs"                     \
    |xargs -i rm -f {}

# no empty directories
find %{buildroot}%{_prefix}             \
    -type d -depth                      \
    -exec rmdir {} \; 2>/dev/null

%{__perl} -MFile::Find -le '
    find({ wanted => \&wanted, no_chdir => 1}, "%{buildroot}");
    print "%doc  modules IPv4 include Todo Changes libiptc README";
    for my $x (sort @dirs, @files) {
        push @ret, $x unless indirs($x);
        }
    print join "\n", sort @ret;

    sub wanted {
        return if /auto$/;

        local $_ = $File::Find::name;
        my $f = $_; s|^\Q%{buildroot}\E||;
        return unless length;
        return $files[@files] = $_ if -f $f;

        $d = $_;
        /\Q$d\E/ && return for reverse sort @INC;
        $d =~ /\Q$_\E/ && return
            for qw|/etc %_prefix/man %_prefix/bin %_prefix/share|;

        $dirs[@dirs] = $_;
        }

    sub indirs {
        my $x = shift;
        $x =~ /^\Q$_\E\// && $x ne $_ && return 1 for @dirs;
        }
    ' > %filelist

[ -z %filelist ] && {
    echo "ERROR: empty %files listing"
    exit -1
    }

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %filelist
%defattr(-,root,root)

%changelog
* Mon Dec 12 2005 root@tuxpri.c-note.dk
- Initial build.
