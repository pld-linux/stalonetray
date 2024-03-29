Summary:	A stand-alone system tray
Summary(pl.UTF-8):	Samodzielna tacka systemowa
Name:		stalonetray
Version:	0.8.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/stalonetray/%{name}-%{version}.tar.bz2
# Source0-md5:	3bf4c7e5e3c077f26242b37a8e008774
Patch0:		%{name}-link.patch
URL:		http://stalonetray.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The stalonetray is a STAnd-aLONE system tray. It runs under virtually
any window manager.

%description -l pl.UTF-8
stalonetray jest samodzielną tacką systemową. Działa on właściwie z
każdym zarządcą okien.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO stalonetrayrc.sample
%attr(755,root,root) %{_bindir}/stalonetray
%{_mandir}/man1/stalonetray.1*
