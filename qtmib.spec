Summary:	Qt4 SNMP MIB Browser
Name:		qtmib
Version:	1.1.1
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://downloads.sourceforge.net/qtmib/%{name}-%{version}.tar.bz2
# Source0-md5:	1715ae9c88e1f0d355f9a93b3248455e
URL:		http://qtmib.sourceforge.net/
BuildRequires:	QtGui-devel
BuildRequires:	net-snmp-utils
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	sed >= 4.0
BuildRequires:	which
Requires:	net-snmp-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy-to-use SNMP MIB Browser based on QT4 library. It is build as a
front-end for net-snmp tools, and it allows the user to query
SNMP-enabled devices. It implements SNMPv1 and SNMPv2c.

%prep
%setup -q
%{__sed} -e 's/which qmake/which qmake-qt4/' -i configure

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README RELNOTES
%attr(755,root,root) %{_bindir}/qtmib
%attr(755,root,root) %{_bindir}/qtmib-discover
%attr(755,root,root) %{_bindir}/qtmib-report
%attr(755,root,root) %{_bindir}/qtmib-translate
%{_mandir}/man1/qtmib-discover.1*
%{_mandir}/man1/qtmib-report.1*
%{_mandir}/man1/qtmib-translate.1*
%{_mandir}/man1/qtmib.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
