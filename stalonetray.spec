Summary:	A stand-alone system tray
Summary(pl):	Samodzielna tacka systemowa
Name:		stalonetray
Version:	0.6.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/stalonetray/%{name}-%{version}.tar.bz2
# Source0-md5:	4367ca16e43fb1c9551512adc6ed8202
URL:		http://stalonetray.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The stalonetray is a STAnd-aLONE system tray. It runs under virtually
any window manager.

%description -l pl
stalonetray jest samodzieln± tack± systemow±. Dzia³a on w³a¶ciwie z
ka¿dym zarz±dc± okien.

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
