Summary:	A stand-alone system tray
Summary(pl):	Samodzielny tray systemowy
Name:		stalonetray
Version:	0.6
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/stalonetray/%{name}-%{version}.tar.bz2
# Source0-md5:	2ecf17ebb22a4fb7430bc17197a86206
URL:		http://stalonetray.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The stalonetray is a STAnd-aLONE system tray. It runs under virtually
any window manager.

%description -l pl
stalonetray jest samodzielnym trayem systemowym. Dzia�a on w�a�ciwie z
ka�dym mened�erem okien.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
