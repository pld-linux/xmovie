Summary:	Viewer for various movie formats
Summary(pl):	Odtwarzacz filmów w ró¿nych formatach
Name:		xmovie
Version:	1.5.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
URL:		http://heroine.linuxave.net/xmovie.html
Source0:	http://heroines.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-system-libs.patch
BuildRequires:	glib-devel
BuildRequires:	libmpeg3-devel
BuildRequires:	quicktime4linux-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Viewer for various movie formats, including QuickTime and MPEG1/2.

%description -l pl
Odtwarzacz filmów w ró¿nych formatach - QuickTime i MPEG1/2.

%prep
%setup -q
%patch0 -p1
# Just in case...
rm -f guicast/colormodels.[ch]
mv quicktime/colormodels.[ch] guicast
rm -rf libmpeg3 quicktime

%build
./configure
%{__make} COPTS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -s xmovie/xmovie $RPM_BUILD_ROOT%{_bindir}

gzip -9nf docs/index.html README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.gz README.gz
%attr(755,root,root) %{_bindir}/*
