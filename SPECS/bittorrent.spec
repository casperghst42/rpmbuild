Summary: BitTorrent is a tool for copying files from one machine to another
Name: bittorrent
Version: 3.4.2
Release: 1.fdr
Source0: http://bitconjurer.org/BitTorrent/BitTorrent-%{version}.tar.gz
License: MIT
Group: Networking/File transfer
URL: http://bitconjurer.org/BitTorrent/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: python
BuildArchitectures: noarch
Prefix: %{_prefix}

%description
BitTorrent is a tool for copying files from one machine to
another. FTP punishes sites for being popular. Since all uploading is
done from one place, a popular site needs big iron and big
bandwidth. With BitTorrent, clients automatically mirror files they
download, making the publisher's burden almost nothing.

%package gui
Summary: GUI versions of the BitTorrent file transfer tools
Group: Networking/File transfer
Requires: wxPythonGTK
Requires: %name = %version-%release

%description gui
BitTorrent is a tool for copying files from one machine to
another. FTP punishes sites for being popular. Since all uploading is
done from one place, a popular site needs big iron and big
bandwidth. With BitTorrent, clients automatically mirror files they
download, making the publisher's burden almost nothing.

This package contains the graphical versions of the BitTorrent tools.

%prep
%setup -q -n BitTorrent-%version

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install --prefix=$RPM_BUILD_ROOT/usr
perl -p -i -e 's/env python2/env python/' $RPM_BUILD_ROOT%_bindir/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt credits.txt INSTALL.unix.txt LICENSE.txt 
%_bindir/btcompletedir.py
%_bindir/btdownloadcurses.py
%_bindir/btdownloadheadless.py
%_bindir/btdownloadlibrary.py
%_bindir/btlaunchmany.py
%_bindir/btlaunchmanycurses.py
%_bindir/btmakemetafile.py
%_bindir/btreannounce.py
%_bindir/btrename.py
%_bindir/btshowmetainfo.py
%_bindir/bttest.py
%_bindir/bttrack.py
%_libdir/python*/site-packages/BitTorrent

%files gui
%defattr(-,root,root)
%doc README.txt
%_bindir/btcompletedirgui.py
%_bindir/btdownloadgui.py

%changelog
* Mon Nov 8 2004 Casper Pedersen <cpedersen@c-note.dk>
- 3.4.2

* Mon Oct 13 2003 Seth Vidal <skvidal@phy.duke.edu>
- 3.3

* Wed Jul 16 2003 Seth Vidal <skvidal@phy.duke.edu>
- rebuilt on rhl 9 - testing

* Fri May 30 2003 Peter Hanecak <hanecak@megaloman.sk> 3.2.1b-1
- adapted to Doors Linux

* Sun Mar 30 2003 Götz Waschk <waschk@linux-mandrake.com> 3.2.1b-1mdk
- split out gui tools to remove wxPythonGTK dep from the main package 
- new version

* Fri Mar 28 2003 Frederic Lepied <flepied@mandrakesoft.com> 3.2-1mdk
- 3.2

* Wed Mar 26 2003 Frederic Lepied <flepied@mandrakesoft.com> 3.1-1mdk
- initial packaging

# end of file
