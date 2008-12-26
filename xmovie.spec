Summary:	Viewer for various movie formats
Summary(pl.UTF-8):	Odtwarzacz filmów w różnych formatach
Summary(pt_BR.UTF-8):	Reprodutor de filmes QuickTime e MPEG-2
Name:		xmovie
Version:	1.9.13
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/heroines/%{name}-%{version}-src.tar.bz2
# Source0-md5:	94608574eea5c6749528eedb08ee3139
Patch0:		%{name}-system-libs.patch
Patch1:		%{name}-alpha.patch
Patch2:		%{name}-sh.patch
Patch3:		%{name}-c++.patch
URL:		http://heroinewarrior.com/xmovie.php3
BuildRequires:	gcc-c++
BuildRequires:	glib-devel
BuildRequires:	libmpeg3-devel
BuildRequires:	libpng-devel
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	quicktime4linux-devel >= 2.0.1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86vidmodeproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	zlib-devel
Requires:	quicktime4linux >= 2.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Introducing a movie player for MPEG-2, DVD, and Quicktime movies with
stereo sound. It won't play any movies you download from the Internet.
What XMovie is used for is playing long, high resolution movies you
capture or composite yourself with stereo sound. The other Quicktime
players are not necessarily convenient for movies over 50 minutes or
may not support aspect ratios or stereo sound.

XMovie plays MPEG-1/MPEG-2 system streams, MP2/MP3/AC3 audio, MPEG-1/2
video, Quicktime video (Motion JPEG A, Uncompressed RGB, Component
video, Progressive JPEG, PNG, YUV 4:2:0, DV), Quicktime audio (Twos
complement, IMA4, uLaw).

%description -l pl.UTF-8
XMovie to odtwarzacz filmów w formatach MPEG-2, DVD i QuickTime z
dźwiękiem stereo. Nie odtwarza filmów ściąganych z Internetu - służy
natomiast do odtwarzania długich filmów w wysokiej rozdzielczości
z dźwiękiem stereo zgrywanych lub montowanych samemu. Inne odtwarzacze
Quicktime mogą nie być zbyt wygodne dla filmów powyżej 50 minut albo
nie obsługiwać różnych proporcji lub dźwięku stereo.

XMovie odtwarza strumienie MPEG-1/MPEG-2, dźwięk MP2/MP3/AC3, obraz
MPEG-1/2, obraz Quicktime (w formatach Motion JPEG A,
nieskompresowanym RGB, Component video, Progressive JPEG, PNG, YUV
4:2:0, DV), dźwięk Quicktime (w formatach ze znakiem, IMA4, uLaw).

%description -l pt_BR.UTF-8
Aqui está um reprodutor de filmes em MPEG-2, DVD e Quicktime com som
estéreo. Ele não reproduzirá todos os filmes que você obter na
Internet. O XMovie deve ser usado para reproduzir filmes longos e de
alta resolução que você capture ou componha com som estéreo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Just in case...
rm -rf libmpeg3 quicktime libsndfile* avifile

%build
# -DUSE_AVI for avifile support - but doesn't build then
CFLAGS="%{rpmcflags} -fno-rtti"; export CFLAGS
%{__make} \
	LFLAGS="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install xmovie/*/xmovie $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
