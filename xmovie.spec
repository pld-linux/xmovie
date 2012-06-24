Summary:	Viewer for various movie formats
Summary(pl):	Odtwarzacz film�w w r�nych formatach
Summary(pt_BR):	Reprodutor de filmes QuickTime e MPEG-2
Name:		xmovie
Version:	1.9.12
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/heroines/%{name}-%{version}-src.tar.bz2
# Source0-md5:	117714618963543573400c0809478555
Patch0:		%{name}-system-libs.patch
Patch1:		%{name}-alpha.patch
URL:		http://heroinewarrior.com/xmovie.php3
BuildRequires:	XFree86-devel
#BuildRequires:	avifile-devel
BuildRequires:	glib-devel
BuildRequires:	libmpeg3-devel
BuildRequires:	libpng-devel
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	quicktime4linux-devel >= 2.0.1
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

%description -l pl
XMovie to odtwarzacz film�w w formatach MPEG-2, DVD i QuickTime z
d�wi�kiem stereo. Nie odtwarza film�w �ci�ganych z Internetu - s�u�y
natomiast do odtwarzania d�ugich film�w w wysokiej rozdzielczo�ci
z d�wi�kiem stereo zgrywanych lub montowanych samemu. Inne odtwarzacze
Quicktime mog� nie by� zbyt wygodne dla film�w powy�ej 50 minut albo
nie obs�ugiwa� r�nych proporcji lub d�wi�ku stereo.

XMovie odtwarza strumienie MPEG-1/MPEG-2, d�wi�k MP2/MP3/AC3, obraz
MPEG-1/2, obraz Quicktime (w formatach Motion JPEG A,
nieskompresowanym RGB, Component video, Progressive JPEG, PNG, YUV
4:2:0, DV), d�wi�k Quicktime (w formatach ze znakiem, IMA4, uLaw).

%description -l pt_BR
Aqui est� um reprodutor de filmes em MPEG-2, DVD e Quicktime com som
est�reo. Ele n�o reproduzir� todos os filmes que voc� obter na
Internet. O XMovie deve ser usado para reproduzir filmes longos e de
alta resolu��o que voc� capture ou componha com som est�reo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
