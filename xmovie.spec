Summary:	Viewer for various movie formats
Summary(pl):	Odtwarzacz filmów w ró¿nych formatach
Name:		xmovie
Version:	1.6
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
URL:		http://heroine.linuxave.net/xmovie.html
Source0:	http://heroines.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-system-libs.patch
BuildRequires:	glib-devel
BuildRequires:	libmpeg3-devel
BuildRequires:	quicktime4linux-devel >= 1.3
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
mv -f quicktime/colormodels.[ch] guicast
mv -f quicktime/cmodel*.[ch] guicast
rm -rf libmpeg3 quicktime libsndfile

%build
./configure
%{__make} COPTS="%{rpmcflags} -fno-rtti"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install xmovie/xmovie $RPM_BUILD_ROOT%{_bindir}

gzip -9nf docs/index.html README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.gz README.gz
%attr(755,root,root) %{_bindir}/*
