Summary:	Viewer for various movie formats
Summary(pl):	Odtwarzacz filmów w ró¿nych formatach
Name:		xmovie
Version:	1.9.6
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
URL:		http://heroine.linuxave.net/xmovie.html
Source0:	http://heroines.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-system-libs.patch
BuildRequires:	XFree86-devel
#BuildRequires:	avifile-devel
BuildRequires:	glib-devel
BuildRequires:	libmpeg3-devel
BuildRequires:	libpng-devel
BuildRequires:	libsndfile-devel
BuildRequires:	quicktime4linux-devel >= 1.5
BuildRequires:	zlib-devel
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
rm -rf libmpeg3 quicktime libsndfile avifile

%build
# -DUSE_AVI for avifile support - but doesn't build then
%{__make} OPTFLAGS="%{rpmcflags} -fno-rtti"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install xmovie/*/xmovie $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/index.html
%attr(755,root,root) %{_bindir}/*
