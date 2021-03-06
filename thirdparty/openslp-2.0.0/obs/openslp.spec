#
# spec file for package OpenSLP (Version 2.0.0)
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via openslp-devel@lists.sourceforge.net
#

# norootforbuild

Name:           openslp
BuildRequires:  bison flex openssl-devel doxygen
Summary:        An Implementation of Service Location Protocol V2
Version:        2.0.0
Release:        1
License:        BSD 3-Clause
Group:          System/Daemons
URL:            http://www.openslp.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %name-%version.tar.gz

#Source1:        slpd.init
#Source2:        README.SuSE
#Source3:        openslp.desktop
#Source4:        openslp-devel.desktop
#Source5:        openslp.logrotate
#Source6:        slpd.xml
#Patch1:         openslp.diff
#Patch2:         openslp.audit.diff
#Patch3:         extensions.diff
#Patch4:         slptool-timeout.diff
#Patch5:         hppa.diff
#Patch6:         v1dadiscovery.diff
#Patch7:         openslp.poll.diff
#Patch8:         openslp.v1sladdr.diff
#Patch9:         openslp.tcpclearovr.diff
#Patch10:        openslp.checkovr.diff
#Patch11:        openslp.truncate.diff
#Patch12:        openslp.emptyanswer.diff
#Patch13:        openslp.doubleequal.diff
#Patch14:        openslp.dereg.diff

%description
Service Location Protocol is an IETF standards track protocol that
provides a framework that allows networking applications to discover
the existence, location, and configuration of networked services in
enterprise networks.

OpenSLP is an open source implementation of the SLPv2 protocol as
defined by RFC 2608 and RFC 2614.  This package includes the slptool
and runtime libraries.



Authors:
--------
    Matthew Peterson <mpeterson@calderasystems.com>
    John Calcote <john.calcote@gmail.com>
    Ganesan Rajagopal <rganesan@myrealbox.com>
    David McCormack <david.mccormack@ottawa.com>
    Evan Hughes <hughes@lab43.org>
    Matthieu Desmons <mdes@ocegr.fr>
    Praveen Kumar Amritaluru <praveen@india.hp.com>

%package server
Group:          System/Daemons
Summary:        The OpenSLP Implementation of the  Service Location Protocol V2

%description server
Service Location Protocol is an IETF standards track protocol that
provides a framework that allows networking applications to discover
the existence, location, and configuration of networked services in
enterprise networks.

This package contains the SLP server. Every system, which provides any
services that should be used via an SLP client must run this server and
register the service.



Authors:
--------
    Matthew Peterson <mpeterson@calderasystems.com>
    John Calcote <john.calcote@gmail.com>
    Ganesan Rajagopal <rganesan@myrealbox.com>
    David McCormack <david.mccormack@ottawa.com>
    Evan Hughes <hughes@lab43.org>
    Matthieu Desmons <mdes@ocegr.fr>
    Praveen Kumar Amritaluru <praveen@india.hp.com>

%package devel
Requires:       openssl-devel openslp = %version
Group:          System/Daemons
Summary:        OpenSLP Development SDK

%description devel
Service Location Protocol is an IETF standards track protocol that
provides a framework that allows networking applications to discover
the existence, location, and configuration of networked services in
enterprise networks.

This package contains header and library files to compile applications
with SLP support. It also contains developer documentation to develop
such applications.



Authors:
--------
    Matthew Peterson <mpeterson@calderasystems.com>
    John Calcote <john.calcote@gmail.com>
    Ganesan Rajagopal <rganesan@myrealbox.com>
    David McCormack <david.mccormack@ottawa.com>
    Evan Hughes <hughes@lab43.org>
    Matthieu Desmons <mdes@ocegr.fr>
    Praveen Kumar Amritaluru <praveen@india.hp.com>

%prep
%setup -q
#%patch1

%build
export CFLAGS="$RPM_OPT_FLAGS"
./configure \
  --prefix=/usr \
  --libdir=%_libdir \
  --sysconfdir=%_sysconfdir \
  --enable-async-api \
  --enable-slpv2-security
make

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install
mkdir -p ${RPM_BUILD_ROOT}/etc/slp.reg.d
mkdir -p ${RPM_BUILD_ROOT}/etc/init.d/
install -m 0755 etc/slpd.suse_init ${RPM_BUILD_ROOT}/etc/init.d/slpd
ln -sf ../../etc/init.d/slpd ${RPM_BUILD_ROOT}/usr/sbin/rcslpd

%post
%run_ldconfig

%postun
%run_ldconfig

%post server
%{fillup_and_insserv slpd}

%postun server
%restart_on_update slpd
%insserv_cleanup

%preun server
%stop_on_removal slpd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc doc/doc/*
%_libdir/libslp.so.*
/usr/bin/slptool
%config(noreplace) /etc/slp.conf
%config(noreplace) /etc/slp.spi

%files server
%defattr(-,root,root)
%dir /etc/slp.reg.d/
/usr/sbin/rcslpd
/usr/sbin/slpd
/etc/init.d/slpd
%config(noreplace) /etc/slp.reg

%files devel
%defattr(-,root,root)
/usr/include/slp.h
%_libdir/libslp.a
%_libdir/libslp.la
%_libdir/libslp.so

%changelog
* Tue Mar 26 2008 - jcalcote@users.sourceforge.net
- ported from openslp 1.2 spec file in opensuse factory
