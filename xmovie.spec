Summary:	Viewer for various movie formats
Summary(pl):	Odtwarzacz film�w w r�nych formatach
Summary(pt_BR):	Reprodutor de filmes QuickTime e MPEG-2
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
Introducing a movie player for MPEG-2, DVD, and Quicktime movies with
stereo sound. It won't play any movies you download from the internet.
What XMovie is used for is playing long, high resolution movies you
capture or composite yourself with stereo sound. The other Quicktime
players, well, the other player is not convenient for movies over 50
minutes and it doesn't support aspect ratios or stereo sound.

XMovie plays MPEG-1/MPEG-2 system streams, MP2/MP3/AC3 audio, MPEG-1/2
video, Quicktime video (Motion JPEG A, Uncompressed RGB, Component
video, Progressive JPEG, PNG, YUV 4:2:0, DV), Quicktime audio: Twos
complement, IMA4, ulaw).


%description -l pl
Odtwarzacz film�w w r�nych formatach - QuickTime i MPEG1/2.

%description -l pt_BR
Aqui est� um reprodutor de filmes em MPEG-2, DVD e Quicktime com som
est�reo. Ele n�o reproduzir� todos os filmes que voc� obter na
Internet. O XMovie deve ser usado para reproduzir filmes longos e de
alta resolu��o que voc� capture ou componha com som est�reo.

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
